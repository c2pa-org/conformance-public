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

def build_rubric():
    composables_dir = 'composables'
    try:
        files = os.listdir(composables_dir)
    except Exception as e:
        print(f"Error listing directory {composables_dir}: {e}", file=sys.stderr)
        return

    all_globals = load_globals(os.path.join(composables_dir, 'globals-signals.yml'))

    # Look for -local.yml files
    trait_files = [f for f in files if (f.startswith('signal-inception-') or f.startswith('signal-transformations-')) and f.endswith('-local.yml')]

    trait_files.sort()  # alphabetical sort for determinism

    inceptions = [f for f in trait_files if f.startswith('signal-inception-')]
    transformations = [f for f in trait_files if f.startswith('signal-transformations-')]
    ordered_files = inceptions + transformations

    if not ordered_files:
        print("No individual signal-*-local.yml files found!", file=sys.stderr)
        return

    monolithic_path = 'asset-rubric-signals-local.yml'
    print(f"Generating Monolithic Rubric: {monolithic_path}")

    all_statements = []

    for tf in ordered_files:
        print(f"  Processing {tf} ...")
        try:
            filepath = os.path.join(composables_dir, tf)
            with open(filepath, 'r') as f:
                docs = list(yaml.safe_load_all(f))

            statements = []
            for d in docs:
                if isinstance(d, list):
                    statements.extend(d)
                elif isinstance(d, dict) and "statements" in d:
                    statements.extend(d["statements"])
                elif isinstance(d, dict) and "id" in d:
                    statements.append(d)

            # Strip -local.yml as well as .yml
            trait_name = tf.replace('signal-inception-', '').replace('signal-transformations-', '').replace('-local.yml', '').replace('.yml', '')
            category = 'inception' if tf.startswith('signal-inception-') else 'transformation'

            for s in statements:
                if isinstance(s, dict):
                    s["id"] = f"{category}:signal_{trait_name}"
                    all_statements.append(s)

        except Exception as e:
            print(f"Error processing {tf}: {e}", file=sys.stderr)
            return

    variables, expressions = filter_used_globals(all_statements, all_globals)

    metadata = {
        "rubric_metadata": {
            "name": "C2PA Asset Signals Rubric (Local)",
            "issuer": "C2PA Conformance Task Force",
            "date": "2026-03-31T05:00:00Z",
            "version": "1.0.0",
            "language": "en"
        }
    }
    if variables:
        metadata["variables"] = variables
    if expressions:
        metadata["expressions"] = expressions

    try:
        with open(monolithic_path, 'w') as f:
            yaml.dump(metadata, f, sort_keys=False, width=1000, allow_unicode=True)
            f.write("\n---\n\n")
            yaml.dump(all_statements, f, sort_keys=False, width=1000, allow_unicode=True)
    except Exception as e:
        print(f"Error writing monolithic rubric: {e}", file=sys.stderr)
        return

    print("\nSUCCESS: All rubrics built successfully! 🎉")

if __name__ == "__main__":
    build_rubric()
