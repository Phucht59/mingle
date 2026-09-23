#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python -m ruff check backend
python -m pytest backend --junitxml=evidence/backend-unit.xml
python scripts/smoke_api.py
if [[ "${RUN_POSTGRES:-0}" == 1 ]]; then
  : "${TEST_DATABASE_URL:?Disposable *_test database required}"
  python -m pytest backend --run-postgres -m postgres --junitxml=evidence/postgres.xml
fi
