import re
import yaml
import json
import sys
from json_formula import JsonFormula
from json_formula.data_types import TYPE_ANY


def get_sort_priority(val):
    if val == "true" or val is True:
        return 0
    if val == "warn":
        return 1
    return 2  # "false", False, or None


def _infer_arities(expressions):
    """Infer the arity of each named expression from call sites and from $args body references.

    Two complementary passes:
    1. Call-site scanning: scans every expression body for calls like `name(a, b)` and
       records the maximum argument count seen.
    2. Body reference scanning: if an expression body uses $args[N], it must accept at least
       N+1 args ($args[0]=arg0, $args[1]=arg1, ..., $args[N]=argN).  Handles expressions that
       are only called from statement expressions outside the expressions dict.
    """
    arities = {name: 0 for name in expressions}

    for func_name in expressions:
        escaped = re.escape(func_name)
        call_pattern = re.compile(r'\b' + escaped + r'\s*\(')
        for expr_val in expressions.values():
            expr_str = str(expr_val) if expr_val is not None else ''
            for match in call_pattern.finditer(expr_str):
                rest = expr_str[match.end():]
                if rest.startswith(')'):
                    count = 0
                else:
                    depth = 1
                    count = 1
                    for c in rest:
                        if c == '(':
                            depth += 1
                        elif c == ')':
                            depth -= 1
                            if depth == 0:
                                break
                        elif c == ',' and depth == 1:
                            count += 1
                arities[func_name] = max(arities[func_name], count)

    for name, expr_val in expressions.items():
        expr_str = str(expr_val) if expr_val is not None else ''
        # $args[0] is the first positional arg, $args[1] the second, etc.
        # So if the body references $args[N], the expression needs at least N+1 args
        # (arg 0 becomes @; arg 1 → $args[0]; … arg N+1 → $args[N]).
        max_idx = max((int(i) for i in re.findall(r'\$args\[(\d+)\]', expr_str)), default=-1)
        if max_idx >= 0:
            arities[name] = max(arities[name], max_idx + 1)
        elif re.search(r'\$args\b', expr_str):
            arities[name] = max(arities[name], 1)

    return arities


def create_json_formula_engine(metadata, debug=False):
    """Create a JsonFormula engine with variables and named expressions from rubric metadata.

    Named expressions (_exprName) are registered as custom functions using the following
    argument-passing convention:

      - All positional args → injected as a single array global `$args` before evaluation,
        so $args[0] is the first arg, $args[1] is the second arg, etc.
      - `@` (data context) inside the body is the call-site's ambient data — unchanged.

    Zero-argument expressions evaluate with the call-site's `@` unchanged.

    Arity is inferred automatically via two passes (see _infer_arities):
      1. Call-site scanning across all expression bodies — finds calls like `_foo(a, b)`.
      2. Body scanning — if an expression body references `$args[N]`, it needs at least N+1 args.

    The `$args` array global is the correct way to pass values into an expression.
    `$args` is a global and is NOT shadowed by filter projections `[?...]`, so
    `$args[0]`, `$args[1]`, etc. remain readable at any nesting depth.  Inside
    `[?condition]`, `@` is rebound to the current array element; use `$args[N]` to
    reference call arguments.  See `_startsWithAny` and `_manifest_createdWithDst`
    for examples.
    """
    variables = dict(metadata.get('variables') or {})
    expressions = dict(metadata.get('expressions') or {})

    debug_list = []

    # Infer arity of each expression from call sites in all other expression bodies.
    expr_arities = _infer_arities(expressions)

    # Automatically detect all global variables (any identifier starting with '$') across expression bodies
    dollar_vars = set(variables.keys())
    for expr_val in expressions.values():
        if expr_val is not None:
            dollar_vars.update(re.findall(r'\$[a-zA-Z0-9_]+', str(expr_val)))

    # Compile all expression ASTs (parsing only — no runtime needed at this stage).
    compile_helper = JsonFormula(debug=[])
    allowed_names = list(dollar_vars) + list(expressions.keys())


    compiled_asts = {}
    for name, expr_val in expressions.items():
        expr_str = str(expr_val).strip() if expr_val is not None else ''
        try:
            compiled_asts[name] = compile_helper.compile(expr_str, allowed_names)
        except Exception as e:
            if debug:
                print(f"Warning: Failed to compile expression '{name}': {e}", file=sys.stderr)
            compiled_asts[name] = None

    def make_expr_fn(ast, name, arity):
        if arity == 0:
            def fn(args, data, interpreter):
                if ast is None:
                    raise Exception(f"Expression '{name}' failed to compile")
                return interpreter.search(ast, data)
            return fn
        else:
            # All args become $args array; @ (data context) is the call-site ambient data.
            def fn(args, data, interpreter):
                if ast is None:
                    raise Exception(f"Expression '{name}' failed to compile")
                ctx = data
                extra = list(args)
                saved = interpreter.globals.get('$args')
                interpreter.globals['$args'] = extra
                try:
                    return interpreter.search(ast, ctx)
                finally:
                    if saved is None:
                        interpreter.globals.pop('$args', None)
                    else:
                        interpreter.globals['$args'] = saved
            return fn

    def make_signature(arity):
        if arity == 0:
            return []
        return [{'types': [TYPE_ANY]} for _ in range(arity)]

    custom_functions = {
        name: {
            'func': make_expr_fn(compiled_asts[name], name, expr_arities[name]),
            'signature': make_signature(expr_arities[name]),
        }
        for name in compiled_asts
    }

    engine = JsonFormula(debug=debug_list, custom_functions=custom_functions)
    return engine, variables


def build_provenance_dag(data):
    dag = {}
    if "manifests" not in data:
        return dag

    for manifest in data["manifests"]:
        label = manifest.get("label")
        if not label:
            continue

        dag[label] = {
            "edges": [],
            "signals": []
        }

        assertions = manifest.get("assertions", {})
        for key, value in assertions.items():
            if key.startswith("c2pa.ingredient"):
                active_manifest = value.get("activeManifest", {})
                url = active_manifest.get("url")
                relationship = value.get("relationship")

                if url:
                    parent_urn = url
                    if "urn:c2pa:" in url:
                        idx = url.find("urn:c2pa:")
                        parent_urn = url[idx:]
                        if "/" in parent_urn:
                            parent_urn = parent_urn.split("/")[0]

                    dag[label]["edges"].append({
                        "parent": parent_urn,
                        "relationship": relationship
                    })
    return dag


def evaluate_asset_against_rubric(rubric_path, json_path=None, data_dict=None, debug=False, spec_version=None):
    # Load rubric
    with open(rubric_path, 'r') as f:
        try:
            docs = list(yaml.safe_load_all(f))
        except yaml.YAMLError as exc:
            print(f"Error parsing rubric {rubric_path}: {exc}", file=sys.stderr)
            return None

    # Extract metadata if available
    metadata = docs[0] if len(docs) > 0 and isinstance(docs[0], dict) else {}
    rubric_name = metadata.get("rubric_metadata", {}).get("name", "Unknown")
    rubric_version = metadata.get("rubric_metadata", {}).get("version", "Unknown")

    if not docs:
        print("Empty rubric file!", file=sys.stderr)
        return None

    # Create json-formula engine with variables/expressions from metadata
    engine, variables = create_json_formula_engine(metadata, debug=debug)

    # Dynamically determine expected spec version
    if spec_version is None:
        match = re.search(r'spec(\d+\.\d+)', rubric_path)
        if match:
            spec_version = match.group(1)

    if spec_version is not None:
        variables["$expected_spec_version"] = spec_version

    # Doc 2+: Statements (lists of checks)
    statements = []
    for doc in docs[1:]:
        if isinstance(doc, list):
            statements.extend(doc)
        elif isinstance(doc, dict):
            if "block" in doc:
                continue
            statements.append(doc)

    if not statements:
        print("No statements found in rubric!", file=sys.stderr)
        return None

    # Load data
    if data_dict is not None:
        data = data_dict
    elif json_path is not None:
        with open(json_path, 'r') as f:
            data = json.load(f)
    else:
        print("Error: Either json_path or data_dict must be provided", file=sys.stderr)
        return None

    dag = build_provenance_dag(data)

    def evaluate_list(stmt_list):
        results = []
        for stmt in stmt_list:
            if not isinstance(stmt, dict):
                continue

            stmt_id = stmt.get("id") or "unnamed_trait"
            expr = stmt.get("expression")
            report_text_dict = stmt.get("reportText", {})
            fail_if_matched = stmt.get("failIfMatched", False)
            warn_if_matched = stmt.get("warnIfMatched", False)

            trait_name = stmt_id
            if stmt_id == 'c2pa:signal_compliance':
                true_text = report_text_dict.get("true", {}).get("en", "")
                if true_text:
                    if true_text.startswith("Contains "):
                        trait_name = true_text[9:]
                    else:
                        trait_name = true_text

            category = "general"
            display_name = trait_name
            if ":" in trait_name:
                category, display_name = trait_name.split(":", 1)

            if not expr:
                continue

            print(f"Evaluating: {display_name} ... ", file=sys.stderr)

            try:
                val = engine.search(expr.strip(), data, globals=variables)

                state = "false"
                matches = []

                if fail_if_matched:
                    if isinstance(val, list) and len(val) > 0:
                        state = "false"
                        matches = val
                    else:
                        state = "true"
                elif warn_if_matched:
                    if isinstance(val, list) and len(val) > 0:
                        state = "warn"
                        matches = val
                    else:
                        state = "true"
                else:
                    if isinstance(val, list):
                        if len(val) > 0 and isinstance(val[0], dict) and ("label" in val[0] or "signature" in val[0]):
                            matches = val
                            state = "true"
                        else:
                            state = "true" if len(val) > 0 else "false"
                    else:
                        if isinstance(val, bool):
                            state = "true" if val else "false"
                        elif isinstance(val, (int, float)):
                            state = "true" if val > 0 else "false"
                        elif val is not None:
                            state = "true"
                        else:
                            state = "false"

                txt_val = state
                if txt_val == "warn" and "warn" not in report_text_dict:
                    txt_val = "false"

                report_text = ""
                if txt_val in report_text_dict:
                    val_obj = report_text_dict[txt_val]
                    if isinstance(val_obj, dict):
                        report_text = val_obj.get("en", "")
                    else:
                        report_text = str(val_obj)
                elif "default" in report_text_dict:
                    val_obj = report_text_dict["default"]
                    if isinstance(val_obj, dict):
                        report_text = val_obj.get("en", "")
                    else:
                        report_text = str(val_obj)

                if matches and isinstance(matches, list) and len(matches) > 0 and isinstance(matches[0], str):
                    report_text = report_text.replace("{{matches}}", ", ".join(str(m) for m in matches))

                if matches and not fail_if_matched and not warn_if_matched:
                    for manifest in matches:
                        subject = manifest.get("signature", {}).get("certificateInfo", {}).get("subject", {})
                        cn = subject.get("CN", "Unknown CN")
                        o = subject.get("O", "Unknown O")
                        ou = subject.get("OU")

                        asserted_by = {"CN": cn, "O": o}
                        if ou:
                            asserted_by["OU"] = ou

                        results.append({
                            "trait": display_name,
                            "category": category,
                            "value": "true",
                            "reportText": report_text,
                            "asserted_by": asserted_by,
                            "manifest_urn": manifest.get("label")
                        })
                else:
                    results.append({
                        "trait": display_name,
                        "category": category,
                        "value": state,
                        "reportText": report_text,
                    })

            except Exception as e:
                if debug:
                    import traceback
                    traceback.print_exc()
                results.append({
                    "trait": display_name,
                    "category": category,
                    "value": None,
                    "reportText": f"Error: {e}",
                })

        results.sort(key=lambda x: (get_sort_priority(x.get("value")), x.get("trait") or ""))
        return results

    # Evaluate all statements
    results = evaluate_list(statements)

    # Pruning Logic
    cut_off_traits = []
    cut_off_manifests = set()

    for r in results:
        if r.get("trait") in cut_off_traits and r.get("manifest_urn"):
            cut_off_manifests.add(r.get("manifest_urn"))

    urns_to_prune = set()

    def get_all_ancestors(urn, memo=None):
        if memo is None:
            memo = set()
        if urn in memo:
            return memo
        memo.add(urn)
        if urn in dag:
            for edge in dag[urn]["edges"]:
                get_all_ancestors(edge["parent"], memo)
        return memo

    def is_pure_capture_chain(start_urn):
        current_urn = start_urn
        while current_urn:
            is_capture = False
            for r in results:
                if r.get("manifest_urn") == current_urn and r.get("trait") == "signal_capturedMedia":
                    is_capture = True
                    break
            if is_capture:
                return True
            for r in results:
                if r.get("manifest_urn") == current_urn and r.get("trait") in ["signal_perceptibleGenAI", "signal_perceptibleNonGenAI", "signal_perceptiblePossiblyGenAI"]:
                    return False
            if current_urn not in dag:
                return False
            edges = dag[current_urn]["edges"]
            if not edges:
                return False
            if len(edges) > 1:
                return False
            edge = edges[0]
            if edge["relationship"] != "parentOf":
                return False
            current_urn = edge["parent"]
        return False
 
    all_urns_to_prune = set()
 
    for r in results:
        if r.get("trait") in cut_off_traits and r.get("manifest_urn"):
            urn = r.get("manifest_urn")
            if urn in dag:
                for edge in dag[urn]["edges"]:
                    if edge["relationship"] == "inputTo":
                        branch_urns = set()
                        get_all_ancestors(edge["parent"], branch_urns)
 
                        branch_signals = [res.get("trait") for res in results if res.get("manifest_urn") in branch_urns]
                        print(f"Manifest {urn} branch signals: {branch_signals}", file=sys.stderr)
 
                        new_trait = None
                        if is_pure_capture_chain(edge["parent"]):
                            new_trait = "signal_fullyGenAIMediaInspiredByCapturedMedia"
                        else:
                            has_capture = "signal_capturedMedia" in branch_signals
                            has_genai = any(s in branch_signals for s in ["signal_fullyGenAIMedia", "signal_perceptibleGenAI"])
                            if has_capture and has_genai:
                                new_trait = "signal_fullyGenAIMediaInspiredByMix"
                            elif has_genai and not has_capture:
                                new_trait = "signal_fullyGenAIMediaInspiredByGenerativeMedia"

                        if new_trait:
                            r["trait"] = new_trait
                            text_mapping = {
                                "signal_fullyGenAIMediaInspiredByCapturedMedia": "Contains Fully GenAI Media inspired by Captured Media",
                                "signal_fullyGenAIMediaInspiredByGenerativeMedia": "Contains Fully GenAI Media inspired by GenAI Media",
                                "signal_fullyGenAIMediaInspiredByMix": "Contains Fully GenAI Media inspired by a mix of Captured and GenAI Media"
                            }
                            if new_trait in text_mapping:
                                r["reportText"] = text_mapping[new_trait]

                        all_urns_to_prune.update(branch_urns)

    if all_urns_to_prune:
        print(f"Pruning signals from manifests: {all_urns_to_prune}", file=sys.stderr)
        results = [r for r in results if not r.get("manifest_urn") or r.get("manifest_urn") not in all_urns_to_prune]

    category_mapping = {
        "inception": "inceptions",
        "transformation": "transformations"
    }

    unique_categories = set()
    for stmt in statements:
        if isinstance(stmt, dict) and "id" in stmt:
            stmt_id = stmt["id"]
            if ":" in stmt_id:
                cat = stmt_id.split(":", 1)[0]
                mapped_cat = category_mapping.get(cat, cat)
                unique_categories.add(mapped_cat)
            else:
                unique_categories.add("general")

    if not unique_categories:
        unique_categories.add("general")

    sorted_categories = sorted(list(unique_categories))

    output = {
        "rubricName": rubric_name,
        "rubricVersion": rubric_version,
        "true": {cat: [] for cat in sorted_categories},
        "false": {cat: [] for cat in sorted_categories},
        "warning": {cat: [] for cat in sorted_categories}
    }

    for v in results:
        raw_cat = v.pop("category", "general")
        cat = category_mapping.get(raw_cat, raw_cat)
        val = v.pop("value")
        if val == "warn":
            outcome = "warning"
        elif val == "true" or val is True:
            outcome = "true"
        else:
            outcome = "false"
        v.pop("manifest_urn", None)

        if cat not in output[outcome]:
            output[outcome][cat] = []
        output[outcome][cat].append(v)

    print(json.dumps(output, indent=2, ensure_ascii=False))
    return output


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Evaluate a C2PA asset against a conformance rubric')
    parser.add_argument('rubric', help='Path to the rubric YAML file')
    parser.add_argument('asset', help='Path to the asset JSON file')
    parser.add_argument('--debug', action='store_true', help='Enable debug output')
    parser.add_argument('--spec-version', help='Expected specification version (e.g., 2.2, 2.4)')
    args = parser.parse_args()

    evaluate_asset_against_rubric(args.rubric, args.asset, debug=args.debug, spec_version=args.spec_version)
