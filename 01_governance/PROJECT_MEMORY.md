# Project Memory — canonical handoff

Updated **2026-09-26**. This file summarizes durable project context; current operational truth is also reflected in `PROJECT_STATE.md` and `PHASE_STATUS.yaml`.

## Owner instructions and accepted decisions

- Phase 0 architecture/contract baseline is V3.2 and remains the implementation source of truth.
- Research Q1–Q18 and the Phase 1 product/scientific specifications are DONE; do not repeat that work by default.
- Authority precedence: explicit owner instruction → exact approved V3.2 → approved Change Request/latest approved decision → scientific resolution → current snapshot/register → older context.
- Do not silently amend V3.2. A concrete implementation defect/conflict becomes an Implementation Issue; a foundational change requires an approved Change Request.
- Audio replay telemetry cannot prove physical listens or become canonical scoring evidence. II-03 remains pending exact source mapping.
- Separate learning evidence, engagement evidence, UX evidence and product hypotheses. “Mingo” remains a working product name, not a frozen naming decision.

## Frozen implementation baseline

- Flutter learner: Android-first; preserve iOS capability for later public release.
- Flutter Web: staff/admin.
- FastAPI/Python backend, PostgreSQL, Object Storage.
- Modular monolith; API and durable worker are separate processes from the same codebase.
- Server authoritative for scoring, progress and permission.
- Commands are separate from telemetry.
- Offline client uses durable command and telemetry queues.
- Published content is immutable/versioned; enrollment/attempt pins exact revisions.
- Analytics preserves event time, knowledge/availability time and source capture.
- Mastery != Risk; Risk is optional input to recommendation.
- Prediction / Recommendation Decision / Exposure / Execution / Outcome remain distinct layers.
- Product must function with ML/recommendation disabled.
- Do not add Kafka, Kubernetes, microservices, warehouse or external feature store without demonstrated requirement/load.

## Current implementation and verified status

Canonical runtime code is under `05_code/`.

- Backend API/foundation, worker source, infrastructure-only PostgreSQL migrations, local immutable object adapter and test harness exist.
- Existing evidence records **10 backend unit/security/storage tests PASS**.
- Windows rerun on Python 3.14.7 installed the locked dependencies, passed Ruff and 9 backend tests; six PostgreSQL tests were skipped without a DB URL, and symlink escape was skipped on Windows error 1314. A real Uvicorn subprocess returned liveness 200 and readiness 503. II-09 records the Windows storage path/fsync fix.
- Existing HTTP smoke records liveness=200 and readiness=503 without DB.
- Six PostgreSQL integration/concurrency tests exist but are **NOT RUN** against a real PostgreSQL runtime.
- Worker success against PostgreSQL is not yet evidenced.
- Flutter learner/staff shell source and tests exist but have not yet produced accepted analyze/test/build/actual-boot evidence.
- Exact original V3.2 source and the original **115 contract + 22 SQL** check sources remain absent from the active repository.
- Hosted CI has not yet produced a recorded run.
- Git metadata was restored on branch `main` from the supplied canonical bundle; no hosted `origin` remote is configured.
- Phase 1 is **ACTIVE; GATE NOT PASSED**. Phase 2 remains DEFERRED.

## Canonical repository organization

`01_governance/` decisions/status; `02_product/` active product specs; `03_research/` scientific rationale; `04_architecture/` V3.2/boundaries; `05_code/` runtime source; `06_quality/` gates/standards/evidence; `07_operations/` run/verify scripts; `08_handoff/` provenance; `99_archive/` history only.

## Next work

Run DB/worker and Flutter verification on supported hosts, import exact V3.2 originals with provenance, wire the original 115+22 suite, run hosted CI and whole-stack clean reproduction, then rerun the Phase 1 gate. Do not begin formal Phase 2 implementation before that gate passes.
