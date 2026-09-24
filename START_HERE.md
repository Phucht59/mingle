# START HERE — developer/agent onboarding

This is the shortest safe path into the project.

## 1. Know the authority order

When two documents appear to disagree, use this order:

1. Explicit owner instruction.
2. Exact approved V3.2 baseline/contract once available.
3. Approved Change Request and latest approved decision.
4. Approved Phase 1 scientific resolution.
5. Current project state/snapshot/decision register.
6. Older handoff/history.

Do **not** silently change a frozen business rule. Raise an Implementation Issue; if the foundation must change, use a Change Request.

## 2. Know the current phase

- Phase 0 — Architecture & Contract Baseline: **DONE**.
- Phase 1 — Implementation Foundation / Product Build Kickoff: **ACTIVE**.
- Phase 1 mandatory gate: **NOT PASSED**.
- Phase 2 onward: **DEFERRED** until Phase 1 closes.

Current blockers are documented in `06_quality/gates/PHASE_1_GATE.md` and `01_governance/IMPLEMENTATION_ISSUES.md`.

## 3. Read only what your task needs

| Task | Read first | Work mainly in |
|---|---|---|
| Product behavior / MVP | `02_product/` | specs + issue/CR if behavior changes |
| Scientific/learning rationale | `03_research/phase1/06_SCIENTIFIC_RESEARCH_RESOLUTION.md` | research docs; do not rewrite frozen product rules automatically |
| Backend/API/worker | `04_architecture/`, Phase 1 gate | `05_code/backend/` |
| Flutter learner | product specs + architecture boundaries | `05_code/apps/learner/` |
| Flutter staff/admin | product specs + auth/permission boundaries | `05_code/apps/staff/` |
| Database/migrations | V3.2 + DB ops doc | `05_code/backend/.../migrations/` |
| Tests/gate verification | `06_quality/standards/`, gate | tests + `06_quality/evidence/` |
| CI/local setup | `07_operations/` | scripts/workflows |
| Historical audit only | `99_archive/` | do not implement directly from archive |

## 4. Rules that must survive implementation

- Flutter Android-first learner; Flutter Web for staff/admin; iOS-compatible, public release later.
- FastAPI/Python + PostgreSQL + Object Storage.
- Modular monolith; API process and durable worker process share the codebase.
- Server authoritative for scoring, progress and permission.
- Commands are separate from telemetry.
- Offline client uses durable command and telemetry queues.
- Published content is immutable/versioned; enrollment/attempt pins exact revisions.
- Analytics distinguishes event time, knowledge/availability time and source capture.
- Mastery is not Risk; Risk is optional input to recommendation.
- Prediction, Recommendation Decision, Exposure, Execution and Outcome remain separate layers.
- Product must work with ML/recommendation disabled.
- Do not introduce Kafka, Kubernetes, microservices, warehouse or external feature store without a real requirement/load justification.

## 5. Definition of safe progress

A schema compiling is not a runtime pass. A source file existing is not a gate pass. Phase 1 closes only with the required integration/concurrency/security/runtime evidence and the exact V3.2 original verification suite integrated with provenance.
