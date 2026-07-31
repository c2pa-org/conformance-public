#!/usr/bin/env python3
"""
eval_composable.py — Debug evaluator for composable rubric/signal YAML files.

Unlike the production evaluators which require fully-built rubrics, this script
accepts a raw composable file (e.g. composables/signal-inception-capturedMedia-local.yml),
automatically loads variables and expressions from the referenced globals file(s),
and evaluates every statement against the supplied crJSON — printing rich debug output.

Evaluation context is auto-detected from the composable's `include:` list:
  - includes globals-signals.yml  → signal context (root = each manifest object)
  - includes globals.yml          → conformance context (root = full crJSON)
  - no include / both             → conformance context (explicit --context flag overrides)

Usage:
  python3 eval_composable.py <composable.yml> <data.json> [--context {conformance,signal}] [--no-debug]
"""

import argparse
import json
import os
import sys
import traceback

import yaml
from c2pa_conformance_rubric_evaluator import create_json_formula_engine


GLOBALS_SIGNALS = "globals-signals.yml"
GLOBALS_CONFORMANCE = "globals.yml"


# ---------------------------------------------------------------------------
# Globals loading
# ---------------------------------------------------------------------------

def load_globals_file(path, _visited=None):
    """Load variables and expressions from a globals file, recursively following include: lists."""
    if _visited is None:
        _visited = set()
    path = os.path.abspath(path)
    if path in _visited:
        return {"variables": {}, "expressions": {}}
    _visited.add(path)

    with open(path, "r") as f:
        doc = yaml.safe_load(f)

    result = {
        "variables":   dict(doc.get("variables",   {}) or {}),
        "expressions": dict(doc.get("expressions", {}) or {}),
    }

    base_dir = os.path.dirname(path)
    for name in (doc.get("include") or []):
        candidate = os.path.join(base_dir, name)
        if not os.path.exists(candidate):
            print(f"  [warn] globals file not found: {candidate}", file=sys.stderr)
            continue
        print(f"  Loading globals (transitive): {candidate}", file=sys.stderr)
        included = load_globals_file(candidate, _visited)
        # Included file provides the base; current file's keys win on conflict.
        result["variables"]   = {**included["variables"],   **result["variables"]}
        result["expressions"] = {**included["expressions"], **result["expressions"]}

    return result


def merge_globals(base, override):
    """Merge two globals dicts; override wins on key conflicts."""
    merged = {
        "variables":   {**base.get("variables", {}),   **override.get("variables", {})},
        "expressions": {**base.get("expressions", {}), **override.get("expressions", {})},
    }
    return merged


def resolve_globals(composable_path, include_list):
    """
    Load and merge all globals files listed in `include:`.
    Looks for globals files in the same directory as the composable.
    Each globals file may itself declare further includes, which are resolved recursively.
    """
    composable_dir = os.path.dirname(os.path.abspath(composable_path))
    merged = {"variables": {}, "expressions": {}}
    for name in include_list:
        candidate = os.path.join(composable_dir, name)
        if not os.path.exists(candidate):
            print(f"  [warn] globals file not found: {candidate}", file=sys.stderr)
            continue
        print(f"  Loading globals: {candidate}", file=sys.stderr)
        merged = merge_globals(merged, load_globals_file(candidate))
    return merged


# ---------------------------------------------------------------------------
# Context detection
# ---------------------------------------------------------------------------

def detect_context(include_list):
    """Return 'signal' or 'conformance' based on which globals are included."""
    names = [os.path.basename(n) for n in include_list]
    if GLOBALS_SIGNALS in names and GLOBALS_CONFORMANCE not in names:
        return "signal"
    return "conformance"


# ---------------------------------------------------------------------------
# Pretty debug printing
# ---------------------------------------------------------------------------

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[32m"
RED    = "\033[31m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
DIM    = "\033[2m"


def _c(code, text):
    return f"{code}{text}{RESET}" if sys.stderr.isatty() else text


def print_separator(char="─", width=72):
    print(_c(DIM, char * width), file=sys.stderr)


def print_statement_result(stmt_id, expr, raw_val, bool_val, error=None, manifest_label=None):
    label_prefix = f"[{manifest_label}] " if manifest_label else ""
    header = f"{label_prefix}{stmt_id}"
    print(f"\n{_c(BOLD, header)}", file=sys.stderr)
    print(f"  expr : {_c(CYAN, expr)}", file=sys.stderr)
    if error:
        print(f"  error: {_c(RED, str(error))}", file=sys.stderr)
    else:
        raw_display = json.dumps(raw_val, default=str) if not isinstance(raw_val, str) else repr(raw_val)
        print(f"  raw  : {_c(DIM, raw_display)}", file=sys.stderr)
        result_color = GREEN if bool_val else RED
        print(f"  bool : {_c(result_color, str(bool_val))}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Evaluation helpers
# ---------------------------------------------------------------------------

def to_bool(val):
    if isinstance(val, bool):
        return val
    if isinstance(val, (int, float)):
        return val > 0
    if isinstance(val, list):
        return len(val) > 0
    return val is not None


def evaluate_statements(engine, variables, statements, data, context_label=None, debug=True):
    results = []
    for stmt in statements:
        if not isinstance(stmt, dict):
            continue
        stmt_id = stmt.get("id", "<unnamed>")
        expr = stmt.get("expression", "")
        if not expr:
            continue

        try:
            raw_val = engine.search(expr.strip(), data, globals=variables)
            bool_val = to_bool(raw_val)
            error = None
        except Exception as e:
            raw_val = None
            bool_val = None
            error = e
            if debug:
                traceback.print_exc(file=sys.stderr)

        if debug:
            print_statement_result(stmt_id, expr, raw_val, bool_val,
                                   error=error, manifest_label=context_label)

        results.append({
            "id":       stmt_id,
            "expr":     expr,
            "raw":      raw_val,
            "result":   bool_val,
            "error":    str(error) if error else None,
            "context":  context_label,
        })
    return results


# ---------------------------------------------------------------------------
# Main evaluation entry points
# ---------------------------------------------------------------------------

def run_conformance(engine, variables, statements, data, debug):
    print(f"\n{_c(BOLD, '=== Conformance context (root = full crJSON) ===')}", file=sys.stderr)
    return evaluate_statements(engine, variables, statements, data, debug=debug)


def run_signal(engine, variables, statements, data, debug):
    all_results = []
    manifests = data.get("manifests", [])
    if not manifests:
        print("  [warn] No manifests found in JSON data.", file=sys.stderr)
        return []

    print(f"\n{_c(BOLD, f'=== Signal context ({len(manifests)} manifest(s), root = manifest object) ===')}", file=sys.stderr)
    for manifest in manifests:
        label = manifest.get("label", "<no-label>")
        results = evaluate_statements(engine, variables, statements, manifest,
                                      context_label=label, debug=debug)
        all_results.extend(results)
    return all_results


# ---------------------------------------------------------------------------
# Summary output
# ---------------------------------------------------------------------------

def print_summary(results):
    print_separator("═")
    print(_c(BOLD, "SUMMARY"), file=sys.stderr)
    print_separator()

    true_ids  = [r for r in results if r["result"] is True]
    false_ids = [r for r in results if r["result"] is False]
    error_ids = [r for r in results if r["error"]]

    def _row(r):
        ctx = f"  [{r['context']}]" if r["context"] else ""
        return f"  {r['id']}{ctx}"

    if true_ids:
        print(_c(GREEN, f"PASS ({len(true_ids)}):"), file=sys.stderr)
        for r in true_ids:
            print(_c(GREEN, _row(r)), file=sys.stderr)

    if false_ids:
        print(_c(RED, f"FAIL ({len(false_ids)}):"), file=sys.stderr)
        for r in false_ids:
            print(_c(RED, _row(r)), file=sys.stderr)

    if error_ids:
        print(_c(YELLOW, f"ERROR ({len(error_ids)}):"), file=sys.stderr)
        for r in error_ids:
            print(_c(YELLOW, f"{_row(r)} — {r['error']}"), file=sys.stderr)

    print_separator()

    # JSON summary to stdout (machine-readable)
    out = []
    for r in results:
        entry = {"id": r["id"], "result": r["result"]}
        if r["context"]:
            entry["manifest"] = r["context"]
        if r["error"]:
            entry["error"] = r["error"]
        out.append(entry)
    print(json.dumps(out, indent=2))


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Evaluate a composable rubric/signal YAML file against a crJSON, "
                    "auto-loading globals and running in debug mode."
    )
    parser.add_argument("composable", help="Path to the composable .yml file")
    parser.add_argument("data",       help="Path to the crJSON .json file")
    parser.add_argument(
        "--context", choices=["conformance", "signal"],
        help="Force evaluation context (default: auto-detect from include: list)"
    )
    parser.add_argument(
        "--no-debug", action="store_true",
        help="Suppress per-expression debug output (only show summary)"
    )
    args = parser.parse_args()

    debug = not args.no_debug

    # ---- Load composable ----
    print(f"\n{_c(BOLD, 'Loading composable:')} {args.composable}", file=sys.stderr)
    with open(args.composable, "r") as f:
        try:
            docs = list(yaml.safe_load_all(f))
        except yaml.YAMLError as e:
            print(f"YAML parse error: {e}", file=sys.stderr)
            sys.exit(1)

    # First doc may be an info block with include/metadata
    info_block = {}
    statements = []
    for doc in docs:
        if isinstance(doc, dict) and ("include" in doc or "rubric_metadata" in doc or "variables" in doc or "expressions" in doc):
            info_block = doc
        elif isinstance(doc, list):
            statements.extend(doc)
        elif isinstance(doc, dict):
            statements.append(doc)

    include_list = info_block.get("include", [])
    print(f"  include: {include_list or '(none)'}", file=sys.stderr)
    print(f"  statements found: {len(statements)}", file=sys.stderr)

    if not statements:
        print("No statements found in composable — nothing to evaluate.", file=sys.stderr)
        sys.exit(1)

    # ---- Load globals ----
    globals_data = resolve_globals(args.composable, include_list)

    # Merge any inline variables/expressions from the composable itself
    inline_vars  = dict(info_block.get("variables",   {}) or {})
    inline_exprs = dict(info_block.get("expressions", {}) or {})
    globals_data["variables"].update(inline_vars)
    globals_data["expressions"].update(inline_exprs)

    print(f"  variables loaded : {len(globals_data['variables'])}", file=sys.stderr)
    print(f"  expressions loaded: {len(globals_data['expressions'])}", file=sys.stderr)

    # ---- Detect context ----
    context = args.context or detect_context(include_list)
    print(f"  evaluation context: {_c(BOLD, context)}", file=sys.stderr)

    # ---- Load JSON data ----
    print(f"\n{_c(BOLD, 'Loading data:')} {args.data}", file=sys.stderr)
    with open(args.data, "r") as f:
        data = json.load(f)

    # ---- Build engine ----
    # create_json_formula_engine expects a dict with 'variables' and 'expressions' keys
    engine, variables = create_json_formula_engine(globals_data, debug=debug)

    # ---- Evaluate ----
    if context == "signal":
        results = run_signal(engine, variables, statements, data, debug=debug)
    else:
        results = run_conformance(engine, variables, statements, data, debug=debug)

    # ---- Summary ----
    print_summary(results)


if __name__ == "__main__":
    main()
