# Mingo Phase 2 Rework R1 — Codex Execution Package

## Status

- Phase 0: DONE — V3.2.0 canonical baseline.
- Phase 1: DONE / GATE PASSED.
- Phase 2: ACTIVE — Rework R1 source/spec fixes complete; **GATE NOT PASSED**.
- Phase 3: DEFERRED.

Independent Candidate-v1 audit found 16 defects (3 P0, 11 P1, 2 P2). R1 contains source/spec/handoff fixes for all 16, while preserving the original independent audit. Fixes are **READY FOR RETEST**, not CLOSED by declaration.

## Codex entry

1. Open `CODEX_SUPER_PROMPT.md`.
2. Follow `CODEX_EXECUTION_HANDOFF.md` exactly.
3. Use `03_Kiem_thu/QA_QC/phase2/Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx` and the 94-case `QA_TEST_CASES.csv`.
4. Write actual evidence to `03_Kiem_thu/QA_QC/phase2/evidence/codex/`.
5. Fill `QA_RETEST_HANDOFF.md` only after execution.
6. Build the exact QA retest ZIP + hash + manifest and hand it with `QA_QC_RETEST_PROMPT.md` to independent QC/QA.

## Authority and boundaries

Do not modify V3.2 or Phase 1 production source to force UX tests green. `01_San_pham/` and `02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source/` are byte-identical to the Phase 1 DONE package at handoff creation. Phase 2 is prototype/spec/handoff work only.

## Builder preflight

The package builder ran static/syntax checks and internal non-gating browser smoke/regressions. Those results are under `03_Kiem_thu/QA_QC/phase2/evidence/`. They are not substitutes for Codex execution or independent QC/QA.
