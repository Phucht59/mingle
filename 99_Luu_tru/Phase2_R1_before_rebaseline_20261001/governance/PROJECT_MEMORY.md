# Project Memory — canonical handoff

Updated **2026-09-27**. This file summarizes durable project context; current operational truth is also reflected in `PROJECT_STATE.md` and `PHASE_STATUS.yaml`.

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

Canonical runtime code is under `01_San_pham/`.

- Backend API/foundation, worker source, infrastructure-only PostgreSQL migrations, local immutable object adapter and test harness exist.
- Canonical Python 3.12.10 locked install, Ruff and storage smoke pass. Windows passes 9 focused tests; Linux hosted CI passes all 10, including symlink escape.
- PostgreSQL role `mingo_app`, application DB `mingo`, disposable test DB `mingo_test`; no phase-specific databases. All 6 integration/concurrency tests pass locally and on CI.
- Real API liveness/readiness are 200/200. Worker durable completion and heartbeat pass. A fresh isolated cluster also verifies simultaneous API/worker execution and exactly one persisted probe effect.
- Flutter 3.32.8 learner/staff analyze/test/build pass locally and on CI. Actual Android emulator and Chrome boot are evidenced locally.
- Owner-supplied V3.2 source and original **115 contract + 22 SQL** suites are preserved unchanged with complete hashes/provenance. Local, fresh-clone and hosted reruns pass.
- Hosted run `36252349822` at `d4165e8` passes every job, including the original suites and nine independent adapter guard tests.
- Branch `main` is hosted at `https://github.com/Phucht59/mingo.git`; application source remains unchanged from fully reproduced runtime revision `4cdecb4`.
- Phase 1 is **DONE; GATE PASSED**. Phase 2 is **ACTIVE — Candidate v1 rejected by independent QC/QA; Rework R1 source/spec fixes complete and READY FOR CODEX EXECUTION + INDEPENDENT QA RETEST; gate NOT PASSED**. Phase 3 is DEFERRED.

## Canonical repository organization

`02_Tai_lieu_du_an/` decisions/status; `02_Tai_lieu_du_an/04_Thiet_ke_san_pham/` active product specs; `02_Tai_lieu_du_an/03_Nghien_cuu/` scientific rationale; `02_Tai_lieu_du_an/05_Kien_truc_he_thong/` V3.2/boundaries; `01_San_pham/` runtime source; `03_Kiem_thu/` gates/standards/evidence; `04_Van_hanh/` run/verify scripts; `02_Tai_lieu_du_an/08_Ban_giao/` provenance; `99_Luu_tru/` history only.

## Current Phase 2 Rework R1

The first UX/UI candidate was independently audited on 2026-09-27 and rejected with 16 findings: 3 P0, 11 P1 and 2 P2. Rework R1 fixes the source/spec/handoff defects without changing V3.2 or `01_San_pham/`. The canonical R1 still has 57 screen IDs and 18 shared component contracts, but now includes executable onboarding/placement, Grammar, Listening, authoritative sync states, full staff publishing, persistent assisted evidence, bounded retry, accessibility/focus fixes, complex-screen interaction contracts and explicit Screen→State→Rule→QA traceability. The canonical retest suite is **94 cases** (87 original + 7 independent-audit regression/coverage cases).

Source-level R1 fixes are **not QA closure**. All 16 defect records remain READY FOR RETEST until execution/review evidence closes them. The R1 QA control workbook is `03_Kiem_thu/QA_QC/phase2/Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx`.

## Next work

Codex must execute `02_Tai_lieu_du_an/08_Ban_giao/phase2/CODEX_EXECUTION_HANDOFF.md`, collect fresh browser/accessibility evidence, update the 94-case control truthfully, and create a QA retest package. Independent QC/QA then reproduces P0, retests all 16 findings and owns the gate recommendation. Do not mark Phase 2 DONE or start Phase 3 until 100% P0 PASS, zero open P0/P1, ≥95% executed PASS, mandatory accessibility PASS, developer handoff acceptance and Tech Lead + Product/Owner signoff. Keep V3.2 originals immutable; no architecture Change Request is open.
