# Phase1 foundation regression — RERUN NOW

Executed 2026-10-02, using existing Python 3.12.10 backend environment. Source/backend/V3.2 boundaries stayed frozen during concurrent presentation work. Fresh evidence lives only in `phase1_final/`; previous runs remain intact. `FINAL_FOUNDATION_COUNTS.json` derives counts from the newly generated XML and records individual command exit codes/log hashes.

| Check | Actual result | Fresh evidence |
|---|---|---|
| Ruff | PASS, exit0 | backend-lint.log |
| Focused backend/security/storage | 9 passed, 7 skipped, 0 failed | backend-unit.log/.xml |
| Native PostgreSQL integration/concurrency | 6 passed, 0 skipped, 0 failed | postgres.log/.xml |
| Migration repeat | PASS; `applied: []` | postgres-migrate.log |
| Durable probe enqueue and worker completion | PASS; job.completed observed | worker-enqueue.log; worker-once.log |
| Worker heartbeat healthcheck | PASS, exit0 | worker-healthcheck.log |
| API health/readiness | live200; ready200 | api-ready-smoke.log |
| Immutable local object storage smoke | PASS | storage-smoke.log |
| Original V3.2 unchanged suites | 115 contracts +22 SQL passed, 0 failed | original_suites_after/ |
| Source inventory/hash | expected102; actual102; missing0; extra0; mismatch0 | original_suites_after/run.json |
| Protected/archived/old packages | protected141 mismatch0; archived96 mismatch0; sealed packages mismatch0 | after_protected_integrity.json |

Six PostgreSQL cases were intentionally excluded from the focused test invocation and then **all six reran separately** against the disposable `_test` database: migration idempotency/readiness, migration checksum/atomic failure, concurrent idempotent enqueue/claim, crash recovery/stale-worker fencing, retry exhaustion/no partial effect, and heartbeat expiry. The remaining Windows symlink escape case could not create a symlink with available privilege and remains **SKIPPED**, not PASS.

All nine fresh foundation commands exited0. No business migration or source edit was made. A durable runtime probe is test instrumentation for the existing foundation; it is not a product learning command. Current hosted CI and other OS runs are **NOT RUN**. Flutter analysis/tests/builds are separately owned by the main execution and performance agent and are not certified by this foundation-only report.

The retained Starlette/httpx deprecation warning is non-failing technical debt. No dependency was upgraded to suppress it. Original SQL remains the PGlite/PostgreSQL WASM suite; six native PostgreSQL checks prove the foundation behavior, not later production domain scoring/progress/offline submission. Manual accessibility, human product/content/independent QA and physical performance gates remain pending. Phase3 HOLD.
