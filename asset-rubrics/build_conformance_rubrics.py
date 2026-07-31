import os
import re
import sys
import yaml

# Custom representer to preserve literal block style for long or multiline strings (expressions)
def str_presenter(dumper, data):
    if len(data.splitlines()) > 1 or len(data) > 80:
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)

def load_globals(filepath, _visited=None):
    """Load variables and expressions from a globals file, recursively following include: lists."""
    if _visited is None:
        _visited = set()
    filepath = os.path.abspath(filepath)
    if filepath in _visited:
        return {'variables': {}, 'expressions': {}}
    _visited.add(filepath)

    with open(filepath, 'r') as f:
        doc = yaml.safe_load(f)

    result = {
        'variables':   dict(doc.get('variables',   {}) or {}),
        'expressions': dict(doc.get('expressions', {}) or {}),
    }

    base_dir = os.path.dirname(filepath)
    for name in (doc.get('include') or []):
        included = load_globals(os.path.join(base_dir, name), _visited)
        # Included file provides the base; current file's keys win on conflict.
        result['variables']   = {**included['variables'],   **result['variables']}
        result['expressions'] = {**included['expressions'], **result['expressions']}

    return result

def filter_used_globals(statements, all_globals):
    """
    Scan statement expressions and return only the variables/expressions
    that are actually referenced, following transitive expression dependencies.
    """
    used_vars = set()
    used_exprs = set()
    for stmt in statements:
        if not isinstance(stmt, dict):
            continue
        expr = stmt.get('expression', '')
        if not isinstance(expr, str):
            continue
        used_vars.update(re.findall(r'\$[A-Za-z_]\w*', expr))
        used_exprs.update(re.findall(r'_[A-Za-z_]\w*(?=\()', expr))

    # Transitively include expressions called by already-included expressions.
    frontier = set(used_exprs)
    while frontier:
        next_frontier = set()
        for name in frontier:
            body = all_globals['expressions'].get(name, '')
            if not isinstance(body, str):
                continue
            used_vars.update(re.findall(r'\$[A-Za-z_]\w*', body))
            for dep in re.findall(r'_[A-Za-z_]\w*(?=\()', body):
                if dep not in used_exprs:
                    next_frontier.add(dep)
            used_exprs.update(re.findall(r'_[A-Za-z_]\w*(?=\()', body))
        frontier = next_frontier

    variables   = {k: v for k, v in all_globals['variables'].items()   if k in used_vars}
    expressions = {k: v for k, v in all_globals['expressions'].items() if k in used_exprs}
    return variables, expressions

def load_component_file(filename):
    print(f"  Loading {filename} ...")
    filepath = os.path.join('composables', filename)
    with open(filepath, 'r') as f:
        docs = list(yaml.safe_load_all(f))
        statements = []
        for d in docs:
            if isinstance(d, list):
                statements.extend(d)
            elif isinstance(d, dict) and "id" in d:
                statements.append(d)
        return statements

def assemble_rubric(target_filename, name, version, files, all_globals, spec):
    print(f"Generating Rubric: {target_filename}")

    statements_map = {}
    for f in files:
        statements = load_component_file(f)
        for s in statements:
            if isinstance(s, dict) and "id" in s:
                # Later files override earlier files (deduplication by ID).
                statements_map[s["id"]] = s

    all_statements = list(statements_map.values())

    # Deep-copy globals and dynamically map version-specific variables to standard generic names
    import copy
    recipe_globals = copy.deepcopy(all_globals)
    spec_key = spec.replace(".", "") # "2.2" -> "22", "2.4" -> "24"
    vars_map = recipe_globals["variables"]
    
    # Dynamic Injection Map
    vars_map["$allowed_assertions"] = vars_map[f"$allowed_assertions_v{spec_key}"]
    vars_map["$allowed_actions"] = vars_map[f"$allowed_actions_v{spec_key}"]
    vars_map["$deprecated_assertion_labels"] = vars_map[f"$deprecated_assertion_labels_v{spec_key}"]
    vars_map["$deprecated_action_labels"] = vars_map[f"$deprecated_action_labels_v{spec_key}"]
    vars_map["$standard_parameters"] = vars_map[f"$standard_parameters_v{spec_key}"]

    variables, expressions = filter_used_globals(all_statements, recipe_globals)

    metadata = {
        "rubric_metadata": {
            "name": name,
            "issuer": "C2PA Conformance Task Force",
            "date": "2026-03-31T05:00:00Z",
            "version": version,
            "language": "en"
        }
    }
    if variables:
        metadata["variables"] = variables
    if expressions:
        metadata["expressions"] = expressions

    try:
        with open(target_filename, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, sort_keys=False, width=1000, allow_unicode=True)
            f.write("\n---\n\n")
            yaml.dump(all_statements, f, sort_keys=False, width=1000, allow_unicode=True)

        print(f"  SUCCESS: Wrote {target_filename}\n")
    except Exception as e:
        print(f"Error writing rubric {target_filename}: {e}", file=sys.stderr)

def main():
    all_globals = load_globals(os.path.join('composables', 'globals.yml'))

    # Recipe definitions
    recipes = [
        {
            "target": "asset-rubric-conformance0.1-spec2.2.yml",
            "name": "C2PA Asset Conformance 0.1 Spec 2.2 Rubric",
            "version": "0.1.0",
            "spec": "2.2",
            "files": ["conformance-program-0.1.yml", "integrity-structural.yml", "conformance-spec-2.2.yml"]
        },
        {
            "target": "asset-rubric-conformance0.2-spec2.2.yml",
            "name": "C2PA Asset Conformance 0.2 Spec 2.2 Rubric",
            "version": "0.2.0",
            "spec": "2.2",
            "files": ["conformance-program-0.1.yml", "conformance-program-0.2.yml", "integrity-structural.yml", "conformance-spec-2.2.yml"]
        },
        {
            "target": "asset-rubric-conformance0.2-spec2.4.yml",
            "name": "C2PA Asset Conformance 0.2 Spec 2.4 Rubric",
            "version": "0.2.0",
            "spec": "2.4",
            "files": ["conformance-program-0.1.yml", "conformance-program-0.2.yml", "integrity-structural.yml", "conformance-spec-2.2.yml", "conformance-spec-2.4.yml"]
        }
    ]

    for r in recipes:
        assemble_rubric(r["target"], r["name"], r["version"], r["files"], all_globals, r["spec"])

    print("All rubrics built successfully! 🎉")

if __name__ == "__main__":
    main()
