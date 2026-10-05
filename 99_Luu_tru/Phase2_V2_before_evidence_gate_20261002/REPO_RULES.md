# Repository rules

1. **Do not code from `99_Luu_tru`.** Use active folders; archive is provenance only.
2. **Do not change frozen rules silently.** Log an Implementation Issue. Use a Change Request for foundational/business-rule changes.
3. **Do not call Phase 1 DONE without gate evidence.** Use `03_Kiem_thu/Gate/PHASE_1_GATE.md`.
4. **Do not replace the original V3.2 115+22 suite with new tests.** New tests are additive.
5. **Keep domain authority on the server.** Client telemetry is not authoritative scoring/progress/permission state.
6. **Keep commands and telemetry separate.** Offline support must preserve this boundary.
7. **Keep published content immutable/versioned.** Pin exact revisions where specified.
8. **Avoid premature distributed infrastructure.** Modular monolith + durable worker is the current baseline.
9. **Every new important decision updates governance.** At minimum: decision register/issue/CR as applicable and progress snapshot at major milestones.
10. **Evidence is append-only in spirit.** Never rewrite a failed/blocked historical run into a pass; record a new run.
11. **Use one Mingo database topology.** Application role `mingo_app`, application database `mingo`, disposable automated-test database `mingo_test`; never split databases by development phase.
12. **Keep secrets local.** Commit only placeholders; `.env`, passwords, tokens and private connection strings stay ignored and out of logs/evidence.
13. **Put new evidence with its runtime boundary.** Use `backend/`, `postgres/`, `api/`, `worker/`, `flutter/{learner,staff}/`, `v3_2/`, `ci/`, or `clean_reproduction/`.
14. **Package tracked source.** Final handoffs use `git archive` or an equivalent tracked-source export and exclude `.git`, virtual environments, caches and builds.

15. **Phase 3 remains HOLD / DEFERRED.** Repository organization never authorizes Identity/Auth/Authorization implementation or phase closure.
16. **Classify artifact authority.** CURRENT is scoped; HISTORICAL, GENERATED, EVIDENCE and LOCAL ONLY do not override approved contracts. Different dated status snapshots require reconciliation by the owner; never silently choose a new project state.
17. **Keep executable tests with their projects.** QA controls and evidence belong under `03_Kiem_thu`; research/product/architecture documents belong under `02_Tai_lieu_du_an`. Runtime code belongs under `01_San_pham`.
18. **Preserve provenance bytes.** V3.2 originals, SHA256SUMS, captured intake/logs and historical package manifests must not be regenerated to fit a current tree. Resolve captured paths through migration metadata where necessary.
19. **Keep local environments local.** `.local`, `.venv`, `.idea`, caches and Flutter generated host/build files are ignored; never remove user runtime data to tidy the repository.

20. **Current owner-authorized V2 scope:** the2026-10-01 instruction permits Flutter presentation/design and current governance reconciliation after actual verification. Keep backend/V3/business invariants protected. Phase2 technical completion does not sign a human gate; Phase3 remains HOLD. Preserve historical seals and report their old-shell scope rejections; do not weaken assertions to fit new UI. Capture source/package provenance for the full uncommitted candidate, including new shared source and review assets.
