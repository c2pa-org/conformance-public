#!/usr/bin/env python3
"""
validate_rubric.py - Validate C2PA Asset Profile YAML files against the JSON Schema.

Usage:
    python validate_rubric.py <file.yml> [file2.yml ...]
    python validate_rubric.py --all          # validate all *.yml in same directory

Requires:
    pip install pyyaml jsonschema
"""

import argparse
import datetime
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Missing dependency: pip install pyyaml")

try:
    import jsonschema
    from jsonschema import Draft202012Validator, ValidationError
except ImportError:
    sys.exit("Missing dependency: pip install jsonschema")


SCHEMA_PATH = Path(__file__).parent.parent / "schemas" / "asset-rubrics" / "asset-rubrics.schema.json"


def normalize(obj):
    """
    Recursively convert types that PyYAML auto-converts (datetime, date) back
    to ISO 8601 strings so they validate correctly against the JSON Schema.
    """
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    if isinstance(obj, datetime.date):
        return obj.isoformat()
    if isinstance(obj, dict):
        return {k: normalize(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [normalize(v) for v in obj]
    return obj


def load_schema() -> dict:
    with SCHEMA_PATH.open() as f:
        return json.load(f)


def parse_rubric(path: Path) -> dict:
    """
    Parse a multi-document YAML file into the shape the schema expects:
        {
            "information_block": <first YAML document>,
            "sections": [<second document>, <third document>, ...]
        }
    Returns None (and prints an error) if the file cannot be parsed.
    """
    with path.open() as f:
        docs = list(yaml.safe_load_all(f))

    # Filter out None documents (e.g. empty documents between --- separators)
    docs = [d for d in docs if d is not None]

    if not docs:
        raise ValueError("File contains no YAML documents")

    assembled = {"information_block": normalize(docs[0])}
    if len(docs) > 1:
        assembled["sections"] = [normalize(d) for d in docs[1:]]

    return assembled


def validate_rubric(path: Path, schema: dict) -> list[str]:
    """
    Validate a single profile file.
    Returns a list of error message strings (empty list = valid).
    """
    try:
        profile = parse_rubric(path)
    except yaml.YAMLError as exc:
        return [f"YAML parse error: {exc}"]
    except ValueError as exc:
        return [str(exc)]

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(profile), key=lambda e: list(e.absolute_path))

    messages = []
    for err in errors:
        path_str = " -> ".join(str(p) for p in err.absolute_path) or "(root)"
        messages.append(f"  [{path_str}] {err.message}")
    return messages


def check_duplicate_ids(path: Path) -> list[str]:
    """
    Additional check not expressible in JSON Schema: statement ids must be
    unique across the entire profile.
    """
    try:
        with path.open() as f:
            docs = [d for d in yaml.safe_load_all(f) if d is not None]
    except yaml.YAMLError:
        return []  # Already reported by validate_profile

    seen: dict[str, int] = {}
    duplicates: list[str] = []

    for doc_idx, doc in enumerate(docs[1:], start=1):
        if not isinstance(doc, list):
            continue
        for item in doc:
            if not isinstance(item, dict):
                continue
            stmt_id = item.get("id")
            if stmt_id is None:
                continue
            if stmt_id in seen:
                duplicates.append(
                    f"  Duplicate id '{stmt_id}' (first in section {seen[stmt_id]}, repeated in section {doc_idx})"
                )
            else:
                seen[stmt_id] = doc_idx

    return duplicates


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate C2PA Asset Profile YAML files against the JSON Schema."
    )
    parser.add_argument(
        "files",
        nargs="*",
        metavar="FILE",
        help="One or more .yml profile files to validate.",
    )
    parser.add_argument(
        "--all",
        "-a",
        action="store_true",
        help="Validate all *.yml files in the same directory as this script.",
    )
    args = parser.parse_args()

    paths: list[Path] = []
    if args.all:
        paths = sorted(Path(__file__).parent.glob("*.yml"))
        if not paths:
            print("No *.yml files found.", file=sys.stderr)
            return 1
    elif args.files:
        paths = [Path(f) for f in args.files]
    else:
        parser.print_help()
        return 0

    schema = load_schema()

    total = 0
    failed = 0

    for profile_path in paths:
        total += 1
        print(f"\n{'='*60}")
        print(f"Validating: {profile_path.name}")
        print(f"{'='*60}")

        if not profile_path.exists():
            print(f"  ERROR: File not found: {profile_path}")
            failed += 1
            continue

        schema_errors = validate_rubric(profile_path, schema)
        id_errors = check_duplicate_ids(profile_path)
        all_errors = schema_errors + id_errors

        if all_errors:
            print(f"  FAIL ({len(all_errors)} error(s)):")
            for msg in all_errors:
                print(msg)
            failed += 1
        else:
            print("  PASS")

    print(f"\n{'='*60}")
    print(f"Results: {total - failed}/{total} valid")
    print(f"{'='*60}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
