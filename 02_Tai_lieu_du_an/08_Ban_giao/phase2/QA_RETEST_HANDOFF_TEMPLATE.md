# Phase 2 R1 → Independent QC/QA Retest Handoff

> Codex must fill this file after execution. Do not pre-mark PASS.

## Candidate identity

- Package: `<fill>`
- SHA-256: `<fill>`
- Git/revision: `<fill>`
- Date: `<fill>`
- Architecture baseline: V3.2.0 unchanged
- Phase 2 gate: NOT PASSED pending independent QC/QA

## Codex execution summary

- Static verifier: `<PASS/FAIL>`
- Node syntax: `<PASS/FAIL>`
- Browser regression: `<counts/evidence>`
- QA cases: `<PASS / FAIL / BLOCKED / NOT RUN>` of 94
- Open defects: `<P0/P1/P2/P3 counts>`
- Accessibility environment: `<browser/OS/screen reader or limitation>`

## Mandatory evidence

- `03_Kiem_thu/QA_QC/phase2/evidence/codex/rework_r1_static_checks.*`
- browser screenshots/logs for D001–D005, D013 and QA-OFF-007
- first-use, Grammar, Listening and Staff publishing flow evidence
- accessibility tree/focus/zoom evidence
- updated QA control workbook
- updated defect retest results

## Independent QA instructions

1. Verify package hash/manifest.
2. Do not trust Codex PASS labels without reproducing P0 cases.
3. Execute all P0 first.
4. Re-test all P2-D001..P2-D016.
5. Run full 94-case suite or record exact environment blockers.
6. Gate requires 100% P0 PASS, zero open P0/P1, ≥95% executed PASS, mandatory accessibility PASS, Tech Lead acceptance and Product/Owner signoff.
7. Only independent QC/QA may recommend Phase 2 DONE; Product/Owner records final signoff.
