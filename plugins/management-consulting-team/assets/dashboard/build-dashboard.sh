#!/usr/bin/env bash
# Build the MC Dashboard from project data.
# Usage: bash assets/dashboard/build-dashboard.sh [project-data-dir]
set -euo pipefail

PROJECT_DATA="${1:-./project-data}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT="${PROJECT_DATA}/dashboard.html"

if [ ! -d "$PROJECT_DATA" ]; then
    echo "Error: project-data directory not found at $PROJECT_DATA" >&2
    exit 1
fi

python3 "${SCRIPT_DIR}/assemble.py" \
    "$PROJECT_DATA" \
    "${SCRIPT_DIR}/template.html" \
    "$OUTPUT"
