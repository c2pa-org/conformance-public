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

def get_version():
    version_file = os.path.join(os.path.dirname(__file__), 'VERSION')
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            return f.read().strip()
    return "0.1.1"

def main():
    print("Generating Rubric: asset-rubric-integrity.yml")

    all_globals = load_globals(os.path.join('composables', 'globals.yml'))

    source_files = [
        os.path.join('composables', 'integrity-structural.yml'),
        os.path.join('composables', 'integrity-trust.yml')
    ]
    target_file = 'asset-rubric-integrity.yml'

    try:
        statements = []
        for sf in source_files:
            with open(sf, 'r') as f:
                docs = list(yaml.safe_load_all(f))
            for doc in docs:
                if isinstance(doc, list):
                    statements.extend(doc)
                elif isinstance(doc, dict) and "id" in doc:
                    statements.append(doc)

        variables, expressions = filter_used_globals(statements, all_globals)

        metadata = {
            "rubric_metadata": {
                "name": "C2PA Asset Integrity Rubric",
                "issuer": "C2PA Conformance Task Force",
                "date": "2026-08-06T00:00:00Z",
                "version": get_version(),
                "language": "en"
            }
        }
        if variables:
            metadata["variables"] = variables
        if expressions:
            metadata["expressions"] = expressions

        with open(target_file, 'w', encoding='utf-8') as f:
            yaml.dump(metadata, f, sort_keys=False, width=1000, allow_unicode=True)
            f.write("\n---\n\n")
            yaml.dump(statements, f, sort_keys=False, width=1000, allow_unicode=True)

        print(f"  SUCCESS: Wrote {target_file}")
    except Exception as e:
        print(f"Error building integrity rubric: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
