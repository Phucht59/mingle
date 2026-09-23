#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
if [[ -e .venv ]]; then
  echo 'Use a fresh checkout/extraction without .venv for clean reproduction.' >&2
  exit 1
fi
python3 -m venv .venv
.venv/bin/python -m pip install -r backend/requirements.lock
.venv/bin/python -m pip install --no-deps ./backend
PATH="$PWD/.venv/bin:$PATH" bash scripts/verify_backend.sh
