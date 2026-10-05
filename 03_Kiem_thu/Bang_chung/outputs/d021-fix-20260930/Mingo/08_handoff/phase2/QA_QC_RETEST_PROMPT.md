# Independent QC/QA Retest Prompt — Phase 2 Rework R1

You are the independent QC/QA gate owner. Codex has executed a Phase 2 R1 candidate and supplied fresh evidence.

Do not trust source-level “fixed” labels or Codex PASS labels without reproducing gate-critical cases.

## Required basis

- exact R1 retest ZIP + SHA-256/manifest;
- `06_quality/phase2/Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx` updated by Codex;
- original independent audit under `06_quality/phase2/audits/2026-09-27_independent/`;
- `PHASE2_REWORK_R1_FIX_REGISTER.md`;
- 94-case `QA_TEST_CASES.csv`;
- `SCREEN_STATE_QA_TRACEABILITY.csv`;
- fresh Codex evidence.

## Retest order

1. Integrity/provenance and V3.2/05_code immutability.
2. All P0 cases first, especially D001-D003 and QA-OFF-007.
3. All P1 defect regressions D004-D013 and D016.
4. Accessibility D010/D014/D015 with keyboard, accessibility tree/screen reader where available, 200% text scaling and required viewports.
5. Full 94-case suite.
6. Developer handoff completeness and Screen→State→Rule→QA→Evidence coverage.
7. Tech Lead + Product/Owner signoff only after objective gate criteria are met.

## Codex execution addendum — 2026-09-27

The retest candidate includes four additional findings D017–D020. Retest all 20 findings using `DEFECT_RETEST_RESULTS.csv`. Execution reports 94/94 canonical PASS and 30 supplemental PASS, but an interactive screen-reader/TalkBack speech session remains BLOCKED. AX tree and keyboard results are not a substitute for that gate condition. Package hash and exact Git revision are recorded in the external release sidecars.

## Gate

Phase 2 may PASS only when:
- 100% P0 PASS;
- zero open P0/P1 defects;
- at least 95% of executed cases PASS with remaining P2/P3 explicitly accepted/deferred;
- mandatory accessibility PASS;
- developer handoff accepted;
- Product/Owner + Tech Lead signoff recorded.

NOT RUN/BLOCKED is never PASS. Phase 3 stays deferred until this gate passes.
