#!/bin/bash

# ############################################################################
#
# Build script for C2PA asset rubric YAML files.
#
# Runs all three rubric builders in order to produce:
#   asset-rubric-integrity.yml
#   asset-rubric-conformance0.1-spec2.2.yml
#   asset-rubric-conformance0.2-spec2.2.yml
#   asset-rubric-conformance0.2-spec2.4.yml
#   asset-rubric-signals-local.yml
#
# Must be run from the asset-rubrics/ directory, or will cd there automatically
# when invoked as ./asset-rubrics/build_rubrics.sh from the repo root.
#
# ############################################################################

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

PYTHON="${PYTHON:-python3}"

# Verify python is available
if ! command -v "$PYTHON" &> /dev/null; then
    echo "Error: '$PYTHON' not found. Set the PYTHON environment variable to override." >&2
    exit 1
fi

echo "Building rubrics in: $SCRIPT_DIR"
echo "Using Python: $($PYTHON --version)"
echo ""

echo "==> Integrity rubric"
"$PYTHON" build_integrity_rubric.py
echo ""

echo "==> Conformance rubrics"
"$PYTHON" build_conformance_rubrics.py
echo ""

echo "==> Signals rubric"
"$PYTHON" build_local_signals_rubric.py
echo ""

echo "All rubrics built successfully."
