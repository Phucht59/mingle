#!/usr/bin/env bash
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$REPO_ROOT"
if [[ -e .venv ]]; then
  echo 'Use a fresh checkout/extraction without .venv for clean reproduction.' >&2
  exit 1
fi
python3.12 -m venv .venv
.venv/bin/python -m pip install -r 05_code/backend/requirements.lock
.venv/bin/python -m pip install --no-deps ./05_code/backend
PATH="$PWD/.venv/bin:$PATH" bash 07_operations/scripts/verify_backend.sh
