# Project Memory — canonical handoff

Updated **2026-09-26**. This file summarizes durable project context; current operational truth is also reflected in `PROJECT_STATE.md` and `PHASE_STATUS.yaml`.

## Owner instructions and accepted decisions

- Phase 0 architecture/contract baseline is V3.2 and remains the implementation source of truth.
- Research Q1–Q18 and the Phase 1 product/scientific specifications are DONE; do not repeat that work by default.
- Authority precedence: explicit owner instruction → exact approved V3.2 → approved Change Request/latest approved decision → scientific resolution → current snapshot/register → older context.
- Do not silently amend V3.2. A concrete implementation defect/conflict becomes an Implementation Issue; a foundational change requires an approved Change Request.
- Audio replay telemetry cannot prove physical listens or become canonical scoring evidence. II-03 authority mapping is resolved against exact event/scoring/security sources; new condition metadata belongs to later versioned contracts.
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
- Canonical Python 3.12.10 locked install, Ruff and storage smoke pass. Windows passes 9 focused tests; Linux hosted CI passes all 10, including symlink escape.
- PostgreSQL role `mingo_app`, application DB `mingo`, disposable test DB `mingo_test`; no phase-specific databases. All 6 integration/concurrency tests pass locally and on CI.
- Real API liveness/readiness are 200/200. Worker durable completion and heartbeat pass. A fresh isolated cluster also verifies simultaneous API/worker execution and exactly one persisted probe effect.
- Flutter 3.32.8 learner/staff analyze/test/build pass locally and on CI. Actual Android emulator and Chrome boot are evidenced locally.
- Owner-supplied V3.2 source and original **115 contract + 22 SQL** suites are preserved unchanged with complete hashes/provenance. Local, fresh-clone and hosted reruns pass.
- Hosted run `36252349822` at `d4165e8` passes every job, including the original suites and nine independent adapter guard tests.
- Branch `main` is hosted at `https://github.com/Phucht59/mingo.git`; application source remains unchanged from fully reproduced runtime revision `4cdecb4`.
- Phase 1 is **DONE; GATE PASSED**. Phase 2 is **ELIGIBLE TO START**, not started.

## Canonical repository organization

`01_governance/` decisions/status; `02_product/` active product specs; `03_research/` scientific rationale; `04_architecture/` V3.2/boundaries; `05_code/` runtime source; `06_quality/` gates/standards/evidence; `07_operations/` run/verify scripts; `08_handoff/` provenance; `99_archive/` history only.

## Next work

No mandatory Phase 1 work remains. Keep originals immutable and the verification
adapter fail-closed. Phase 2 can be started only through the project workflow; it has
not been automatically started. Later domain/auth/offline/ML and production gates
remain in the roadmap. Current closure state is in `PROJECT_STATE.md`.
