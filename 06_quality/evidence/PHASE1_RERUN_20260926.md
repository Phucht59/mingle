# Phase 1 verification rerun — 2026-09-26

**Result: Phase 1 remains ACTIVE / GATE NOT PASSED.** This rerun records checks completed from the Windows workspace after restoring Git metadata from the supplied canonical bundle.

## Run context

- OS: Windows 11, PowerShell 7.6.5.
- Python: 3.14.7 (the repository requires Python >=3.12; Python 3.12 was not installed).
- Git branch/base revision: `main` / `fc6e40e93f547bc0cc34a9b2c10c33432209eb95`.
- PostgreSQL: local PostgreSQL 18 service running on `localhost:5432`; DB authentication not attempted because the role password was not available from environment or pgpass.
- Flutter SDK, Android SDK/device/emulator, Docker and an `origin` Git remote were not available in this environment.
- Commands below ran from `C:\Mingo`; no password or token was written to evidence.

## Results

| Check | Result | Evidence / limits |
|---|---|---|
| Locked backend dependency installation and package install | PASS | `backend-install-20260926.log`; fresh `.venv` with Python 3.14.7, locked requirements installed, package reinstalled from current source, and `pip check` clean |
| Ruff | PASS | `backend-lint-20260926.log`; `python -m ruff check 05_code/backend` |
| Backend unit/security/storage | PASS, 9 passed | `backend-unit-20260926.log`, `backend-unit-20260926.xml`; 6 PostgreSQL tests skipped because no test DB URL, 1 symlink test skipped because Windows returned privilege error 1314 |
| API process / liveness | PASS, HTTP 200 | `api-process-20260926T071148Z.log`, `api-http-smoke-20260926T071148Z.json`; real Uvicorn subprocess |
| API readiness | BLOCKED, HTTP 503 | Same API evidence; database unavailable to this probe |
| PostgreSQL migrations/integration/concurrency | BLOCKED | Service is running, but password and disposable `*_test` database access are not established; no migration attempted |
| Durable worker against PostgreSQL | BLOCKED | Depends on a migrated, accessible PostgreSQL database |
| Flutter learner/staff checks and device/web boot | BLOCKED | Flutter and Android tooling are absent |
| Exact V3.2 original 115 + 22 checks | BLOCKED | Searched active source, archive, canonical bundle and historical handoff; exact originals are not present. The fail-closed adapter remains unchanged |
| Hosted CI / full clean reproduction | BLOCKED | No hosted Git remote; runtime prerequisites and original suite are incomplete |

## Commands and exit status

- `py -3.14 --version` — 0.
- `py -3.14 -m venv .venv` — 0.
- `.venv\Scripts\python.exe -m pip install --upgrade pip` — 0.
- `.venv\Scripts\python.exe -m pip install -r 05_code/backend/requirements.lock` — 0.
- `.venv\Scripts\python.exe -m pip install --no-deps --force-reinstall .\05_code\backend` — 0.
- `.venv\Scripts\python.exe -m pip check` — 0.
- `.venv\Scripts\python.exe -m ruff check 05_code/backend 07_operations/scripts/smoke_api.py` — 0.
- `.venv\Scripts\python.exe -m pytest 05_code/backend --junitxml=06_quality/evidence/backend-unit-20260926.xml` — 0 (9 passed, 7 skipped).
- `.venv\Scripts\python.exe 07_operations/scripts/smoke_api.py` — 0 (liveness 200, readiness 503).
- `python 07_operations/scripts/check_original_contracts.py` — BLOCKED by design; exact source absent, exit 1. Output: `original-contract-gate-20260926.log`.
- `.\07_operations\scripts\verify_backend.ps1 -Python .\.venv\Scripts\python.exe` — 0; Windows wrapper rerun produced `backend-lint-20260926T071502Z.log`, `backend-unit-20260926T071502Z.log`, `backend-unit-20260926T071502Z.xml`, `api-smoke-20260926T071502Z.log`, `api-process-20260926T071508Z.log` and `api-http-smoke-20260926T071508Z.json`.

## Implementation fixes from this rerun

- `LocalObjectStore` now handles Windows extended-length resolved paths when enforcing root containment, avoids POSIX-only directory fsync flags on Windows, and creates temporary publication files beside their target. The concurrent immutable-publication test now passes on Windows.
- The symlink escape test reports a skip only for Windows error 1314 (the current account lacks symlink-creation privilege); other errors still fail. Hosted/Linux execution remains needed to exercise that security test.
- API smoke runs now write timestamped evidence, preserving earlier run files.
