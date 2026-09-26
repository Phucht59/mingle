# START HERE — developer/agent onboarding

## 1. Current truth

- Phase 0: **DONE**.
- Phase 1: **ACTIVE; GATE NOT PASSED**.
- Phase 2+: **DEFERRED**.
- Local Python 3.12 backend, PostgreSQL, API, worker, Flutter Android build/boot, and
  Flutter Web build/boot have current evidence.
- Hosted foundation jobs and full runtime clean reproduction PASS. Exact V3.2
  executable originals remain the external artifact blocker; their CI job fails closed.

Read `01_governance/PROJECT_STATE.md`, then `06_quality/gates/PHASE_1_GATE.md`.

## 2. Authority order

1. Explicit owner instruction.
2. Exact approved V3.2 baseline/contract once available.
3. Approved Change Request and latest approved decision.
4. Approved Phase 1 scientific resolution.
5. Current project state/snapshot/decision register.
6. Older handoff/history.

Do not silently change a frozen business rule. Log an Implementation Issue and use a
Change Request only when a concrete contract conflict requires a semantic change.

## 3. First local run

1. Install/use Python 3.12 and Flutter 3.32.8.
2. Provision PostgreSQL role `mingo_app`, application DB `mingo`, and disposable test DB
   `mingo_test`. Never create a database per development phase.
3. Copy `05_code/.env.example` to ignored `05_code/.env` and replace placeholders.
4. Follow the backend and Flutter commands in `README.md`.
5. Read new output in the matching `06_quality/evidence/` subdirectory; do not rewrite
   old evidence.

## 4. Work map

| Task | Read first | Work mainly in |
|---|---|---|
| Product behavior / MVP | `02_product/` | product specs + governance when behavior changes |
| Scientific rationale | `03_research/phase1/06_SCIENTIFIC_RESEARCH_RESOLUTION.md` | research docs |
| Backend/API/worker | `04_architecture/`, Phase 1 gate | `05_code/backend/` |
| Learner Android | product specs + boundaries | `05_code/apps/learner/` |
| Staff Web | product specs + permission boundaries | `05_code/apps/staff/` |
| Database/migrations | V3.2 material + ops docs | backend migrations / Compose init |
| Verification | `06_quality/standards/`, gate | tests + matching evidence subfolder |
| Setup/CI | `07_operations/` | scripts and `.github/workflows/` |
| Historical audit | `99_archive/` | inspect only; do not implement from it |

## 5. Invariants

- Flutter Android-first learner and Flutter Web staff/admin.
- FastAPI/Python, PostgreSQL, Object Storage, modular monolith.
- API and durable worker share one codebase.
- Server authority for scoring, progress, and permission.
- Commands and telemetry stay separate; offline queues are durable.
- Published content is immutable/versioned; attempts pin exact revisions.
- Event time, knowledge/availability time, and source capture remain distinct.
- Mastery is distinct from Risk; prediction, decision, exposure, execution, and outcome
  remain distinct.
- The product has a deterministic path with intelligence/recommendation disabled.
- No Kafka, Kubernetes, microservices, warehouse, or external feature store without a
  demonstrated requirement.

Source existence, a successful schema compile, or a build artifact alone does not close a
runtime gate. Phase 1 closes only when every mandatory item has observed evidence.
