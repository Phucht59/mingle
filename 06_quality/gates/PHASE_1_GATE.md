# Phase 1 Gate — 2026-09-26

**Overall gate: NOT PASSED. Phase 1 ACTIVE; Phase 2 NOT ELIGIBLE.**

The repository was reorganized on 2026-09-24 for maintainability. That reorganization does **not** count as new runtime verification and does not change the gate result.

Windows rerun evidence collected 2026-09-26 is in `06_quality/evidence/PHASE1_RERUN_20260926.md`. It resolves II-09 and proves a focused backend run only; it does not close any PostgreSQL, worker, Flutter, hosted-CI, original-contract or full clean-reproduction gate.

## Observed evidence carried forward

| Check | Result | Evidence / limit |
|---|---|---|
| Python package install | PASS | `06_quality/evidence/install-backend.log`, `reinstall-final-source.log`; dependencies pinned in `05_code/backend/requirements.lock` |
| Windows locked backend install / package health | PASS | Fresh Python 3.14.7 venv; `06_quality/evidence/backend-install-20260926.log`; `pip check` clean. Repository target remains Python >=3.12; Python 3.12 runtime itself is not installed here |
| Windows backend Ruff + unit/security/storage | PASS, 9 passed / 7 skipped | `backend-lint-20260926T071502Z.log`, `backend-unit-20260926T071502Z.log`, `backend-unit-20260926T071502Z.xml`; six DB tests skipped, symlink test skipped for Windows error 1314 |
| Ruff static check | PASS | `06_quality/evidence/lint.log`, `backend-final-verification.log` |
| Backend unit/security/local-storage tests | PASS: 10 | `06_quality/evidence/backend-unit.xml`; path traversal, symlink escape, concurrent immutable publication, health failure semantics, config validation |
| PostgreSQL integration/concurrency suite | **NOT RUN: 6 skipped** | Requires real disposable `*_test` PostgreSQL; no mock/SQLite substitution |
| API process boot and HTTP | PASS with degraded dependency | Real Uvicorn subprocess; live=200, ready=503 because DB unavailable |
| Windows API process boot / liveness | PASS, HTTP 200 | `api-process-20260926T071508Z.log`, `api-http-smoke-20260926T071508Z.json`; readiness is 503 pending DB access |
| Local object storage smoke | PASS | Immutable local adapter only; not S3/cloud evidence |
| Fresh Python venv setup | PASS, backend-only | Not a whole-stack clean-machine claim |
| Worker successful boot against DB | **BLOCKED** | Source exists, but durable execution against real PostgreSQL is not proven |
| PostgreSQL server/migrations | **BLOCKED** | SQL authored; real runtime/migration evidence absent |
| Flutter Android/Web shells | **SOURCE + TESTS AUTHORED, NOT RUN** | `05_code/apps/{learner,staff}`; no successful analyze/test/build/actual boot evidence |
| Hosted CI | **NOT RUN** | `.github/workflows/foundation.yaml` supplied; no remote-run evidence |
| Exact original 115 contract + 22 SQL checks | **BLOCKED** | Exact sources absent. `07_operations/scripts/check_original_contracts.py` fails closed. New tests do not replace originals |
| Authentication/permissions and offline sync | CONTRACT-DEPENDENT / NOT IMPLEMENTED | Foundation has boundaries only; no invented domain protocol/auth proof |
| Full clean environment reproduction | **NOT VERIFIED** | Backend-only clean evidence exists; DB/worker/Flutter/hosted CI incomplete |

## Phase 1 implementation foundation currently present

- FastAPI factory/lifecycle, structured logging and correlation IDs.
- PostgreSQL migration source and durable worker source in one backend codebase.
- Local immutable object-storage adapter.
- Separate command and telemetry foundation ports.
- Separate learner/staff Flutter shells.
- Dockerfile/Compose, dependency pins, verification scripts and hosted-CI definition.
- Canonical repository organization with research/product/architecture/code/quality separation and historical provenance preserved.

## Mandatory closure sequence

1. Import exact V3.2 originals and genuine original 115 contract + 22 SQL check sources with checksums/provenance.
2. Run PostgreSQL migrations plus the six real DB integration/concurrency tests; boot worker and API together and obtain readiness=200.
3. Run pinned Flutter on a supported host: bootstrap platform files, resolve/lock, analyze, unit/widget tests, Android build, Web build, **actual Android boot and actual Web boot**.
4. Push/clone the canonical repository through hosted CI; run original V3.2 checks plus foundation checks.
5. Perform full clean-environment reproduction and capture new evidence.
6. Re-run this gate. Only then may Phase 1 become DONE and Phase 2 become eligible.

No architecture review is reopened by this gate. A concrete blocking implementation defect is required before proposing a foundational Change Request.
