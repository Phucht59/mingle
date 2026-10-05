# START HERE — developer/agent onboarding

## 1. Current truth

- Phase 0: **DONE**.
- Phase 1: **DONE; GATE PASSED**.
- Phase 2: **ACTIVE — REWORK R1 CODEX EXECUTED / READY FOR INDEPENDENT QA RETEST; GATE NOT PASSED**.
- Phase 3: **DEFERRED** until Phase 2 signoff.
- Local Python 3.12 backend, PostgreSQL, API, worker, Flutter Android build/boot, and
  Flutter Web build/boot have current evidence.
- Hosted CI, full runtime clean reproduction and exact original 115+22 verification
  PASS. The original source package and byte-level provenance are now in the repository.

Read `01_governance/PROJECT_STATE.md`, then `08_handoff/phase2/CODEX_START_HERE.md`, `02_product/ux_ui/phase2/README.md`, and `06_quality/phase2/PHASE_2_GATE.md`. The first Phase 2 candidate failed independent QC/QA; do not use old PASS assumptions.

## 2. Authority order

1. Explicit owner instruction.
2. Exact approved V3.2 baseline/contract in `04_architecture/contracts/v3_2/source/`.
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
   Use `07_operations/docs/V3_2_VERIFICATION.md` for the unchanged original suites.
5. Read new output in the matching `06_quality/evidence/` subdirectory; do not rewrite
   old evidence.

## 4. Work map

| Task | Read first | Work mainly in |
|---|---|---|
| Product behavior / MVP | `02_product/` | product specs + governance when behavior changes |
| Phase 2 Rework R1 | `08_handoff/phase2/CODEX_START_HERE.md` | R1 specs/prototype + Codex execution, then independent QA retest in `06_quality/phase2/` |
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

Source existence or a visually complete prototype alone does not close a phase gate. Phase 2 closes only after QC/QA exit criteria and Product/Tech signoff are recorded.

## Codex execution update — 2026-09-27

Phase 2 remains ACTIVE / GATE NOT PASSED. Canonical suite: 94/94 Codex PASS (44/44 P0); 30 supplemental browser checks PASS. Interactive screen-reader/TalkBack review is BLOCKED. All 20 findings await independent closure; Tech Lead and Product/Owner signoffs remain pending. Phase 3 is DEFERRED. See `08_handoff/phase2/QA_RETEST_HANDOFF.md` and `06_quality/phase2/PHASE_2_VERIFICATION_REPORT.md`.
