#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
EVIDENCE="$REPO_ROOT/06_quality/evidence"
mkdir -p "$EVIDENCE"
python -m ruff check 05_code/backend
python -m pytest 05_code/backend --junitxml="$EVIDENCE/backend-unit.xml"
python 07_operations/scripts/smoke_api.py
if [[ "${RUN_POSTGRES:-0}" == 1 ]]; then
  : "${TEST_DATABASE_URL:?Disposable *_test database required}"
  python -m pytest 05_code/backend --run-postgres -m postgres --junitxml="$EVIDENCE/postgres.xml"
fi
