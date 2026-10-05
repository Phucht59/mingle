# Phase 1 runtime verification — carried forward to canonical repo 2026-09-24

**Overall gate: NOT PASSED. Phase 1 ACTIVE; Phase 2 NOT ELIGIBLE.**

This folder contains observed evidence generated before the 2026-09-24 repository reorganization. File relocation does not create a new pass. New verification runs should generate new/updated evidence from the canonical scripts while preserving the truth of prior failures/blocks.

## Observed evidence

| Check | Result | Evidence and limit |
|---|---|---|
| Python package install | PASS | `install-backend.log`, `reinstall-final-source.log`; dependencies were pinned in the source now at `05_code/backend/requirements.lock` |
| Ruff static check | PASS | `lint.log`, `backend-final-verification.log` |
| Backend unit/security/local-storage tests | PASS: 10 | `backend-unit.xml` |
| PostgreSQL integration/concurrency suite | NOT RUN: 6 skipped | Real disposable PostgreSQL required |
| API process boot and HTTP | PASS, degraded dependencies | `api-process.log`, `api-http-smoke.json`; live=200, ready=503 without DB |
| Local object storage smoke | PASS | `storage-smoke.log`; local adapter only |
| Fresh Python venv setup | PASS, backend-only | `clean-backend-setup.log`; not whole-stack proof |
| Worker successful boot | BLOCKED | `worker-boot-attempt.log`; no durable DB execution claimed |
| PostgreSQL server/migrations | BLOCKED | SQL source exists, runtime evidence absent |
| Flutter toolchain/runtime | BLOCKED / NOT VERIFIED | `flutter-toolchain.log`; no successful analyze/test/build/boot claim |
| Flutter Android/Web shells | SOURCE + TESTS AUTHORED, NOT RUN | Source now under `05_code/apps/{learner,staff}` |
| Hosted CI | NOT RUN | Workflow authored; no remote execution evidence |
| Exact original 115 contract / 22 SQL checks | BLOCKED | Original sources absent; fail-closed script now at `07_operations/scripts/check_original_contracts.py` |
| Full clean environment reproduction | NOT VERIFIED | Backend-only clean setup was observed; remaining stack incomplete |

## Interpretation rule

Existing evidence proves only the checks explicitly recorded above. It must not be generalized into PostgreSQL/worker, Flutter, hosted-CI, exact V3.2 or full-stack passes.
