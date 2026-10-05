#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
EVIDENCE="$REPO_ROOT/03_Kiem_thu/Bang_chung"
BACKEND_EVIDENCE="$EVIDENCE/backend"
POSTGRES_EVIDENCE="$EVIDENCE/postgres"
WORKER_EVIDENCE="$EVIDENCE/worker"
RUN_ID="$(date -u +%Y%m%dT%H%M%SZ)"
COMMIT="$(git rev-parse HEAD)"
mkdir -p "$BACKEND_EVIDENCE" "$POSTGRES_EVIDENCE" "$WORKER_EVIDENCE"
printf 'Commit: %s\nPython: %s\n' "$COMMIT" "$(python --version 2>&1)" > "$BACKEND_EVIDENCE/run-$RUN_ID.txt"
if [[ -f "$REPO_ROOT/01_San_pham/.env" ]]; then
  set -a
  # shellcheck disable=SC1091
  source "$REPO_ROOT/01_San_pham/.env"
  set +a
fi
python -m ruff check 01_San_pham/backend
python -m pytest 01_San_pham/backend --junitxml="$BACKEND_EVIDENCE/backend-unit.xml"
if [[ "${RUN_POSTGRES:-0}" == 1 ]]; then
  : "${TEST_DATABASE_URL:?Disposable *_test database required}"
  python -m pytest 01_San_pham/backend --run-postgres -m postgres --junitxml="$POSTGRES_EVIDENCE/postgres.xml"
  python -m all_foundation.cli migrate | tee "$POSTGRES_EVIDENCE/postgres-migrate-$RUN_ID.log"
  python -m all_foundation.cli enqueue-probe --key "verify-$RUN_ID" | tee "$WORKER_EVIDENCE/worker-enqueue-$RUN_ID.log"
  python -m all_foundation.worker --once 2>&1 | tee "$WORKER_EVIDENCE/worker-once-$RUN_ID.log"
  python -m all_foundation.worker --healthcheck 2>&1 | tee "$WORKER_EVIDENCE/worker-healthcheck-$RUN_ID.log"
  python 04_Van_hanh/Scripts/smoke_api.py --expect-ready
else
  python 04_Van_hanh/Scripts/smoke_api.py
fi
# Storage never connects to this fallback URI; Settings requires a valid URI.
DATABASE_URL="${DATABASE_URL:-postgresql://unused:unused@127.0.0.1:1/mingo}" \
  python -m all_foundation.cli storage-smoke | tee "$BACKEND_EVIDENCE/storage-smoke-$RUN_ID.log"
