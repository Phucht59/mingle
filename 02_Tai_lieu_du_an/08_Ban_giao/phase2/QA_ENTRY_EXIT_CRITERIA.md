# Phase 2 Rework R1 — QA Entry / Exit Criteria

## Entry to independent QA retest

- Exact R1 retest package identity, SHA-256 and manifest recorded.
- Codex static verifier and JS syntax PASS.
- Codex has actually executed the mandatory browser P0 regressions and provided evidence.
- R1 QA workbook identifies executed/not-run/blocked cases truthfully.
- 16 original defects have a concrete R1 fix reference and Codex retest result or an explicit blocker.
- V3.2 original and Phase 1 production source remain unchanged by Phase 2 rework.

If these are not met, reject the handoff before broad QA.

## Exit / Phase 2 gate

- 100% P0 cases PASS.
- Zero open P0/P1 defects.
- ≥95% of executed Phase 2 cases PASS; any remaining P2/P3 defect explicitly accepted/deferred.
- Mandatory accessibility checks PASS.
- Screen→State→Rule→QA→Evidence traceability accepted.
- Tech Lead developer-handoff acceptance.
- Product/Owner UX/UAT signoff.
- Final verification report and progress snapshot updated.

Only then Phase 2 = DONE / GATE PASSED and Phase 3 = ELIGIBLE TO START.
