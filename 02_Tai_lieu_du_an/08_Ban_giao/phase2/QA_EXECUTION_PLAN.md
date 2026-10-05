# Phase 2 Rework R1 — Execution and QC/QA Plan

## Stage A — Codex execution (not gate ownership)

1. Verify R1 package/static invariants and JS syntax.
2. Run clean-browser P0 learning-integrity regressions.
3. Run offline authority/recovery flows.
4. Run first-use, Grammar, Listening and Staff publishing flows.
5. Run accessibility/viewport checks that the environment supports.
6. Execute/update the 94-case control with evidence. Never convert unexecuted cases to PASS.
7. Fix only proven Phase 2 defects; rerun surrounding cases.
8. Package exact QA retest candidate + SHA-256 + manifest + filled retest handoff.

## Stage B — Independent QC

Verify package provenance, V3.2 and `01_San_pham/` immutability, artifact completeness, IDs/tokens, traceability and no false DONE status.

## Stage C — Independent QA

Execute all P0 first, then full 94-case suite. Reproduce P2-D001..P2-D016. Run responsive/accessibility matrix and record environment limitations truthfully.

## Stage D — Signoff

Only after objective exit criteria: Tech Lead accepts developer handoff; Product/Owner accepts UX/UAT; QC/QA recommends gate PASS. Governance can then mark Phase 2 DONE and Phase 3 ELIGIBLE.
