# P2-D022 — Independent QA workbook Dashboard reconciliation

Opened: 2026-09-30. Status: **FIX IMPLEMENTED / DATA AND PRESERVATION RETEST PASS; VISUAL AND INDEPENDENT CONFIRMATION PENDING**. Severity: **P2 Minor**, based on QA_DEFECT_SEVERITY.md: non-core inconsistency with a usable source-detail workaround. Engineering classification only; no owner acceptance/defer decision recorded.

Scope: `Mingo_Phase2_R1_Independent_QA_Control_2026-09-29.xlsx`, sheet `00_Dashboard`. This supplied report is outside the sealed R1 ZIP. No R1 package/hash mismatch is implied.

| Cell | Label | Actual | Expected from detail |
|---|---|---|---|
| E5 | Total cases (D5) | 0 | 94 |
| E6 | P0 cases (D6) | 0 | 44 |
| E7 | PASS (D7) | 0 | 94 |
| E4 | Column header beside Live test metric | 94 | Header aligned with its column, count in E5 |
| B10 | Prepared QC/QA cases (A10) | V3.2.0 — unchanged | 94 |
| I8 | PRD traceability criterion | Interactive SR/TalkBack BLOCKED | PRD mapping result |
| I9 | Accessibility mandatory checks | Tech Lead PENDING | Interactive SR/TalkBack BLOCKED |
| I10 | Developer handoff | Product/Owner PENDING | Tech Lead PENDING |

Reproduction: open the Dashboard and compare the cells above against `04_QA_Test_Cases`, columns A/D/K. There are 94 unique case IDs, all PASS, of which 44 are P0. `08_Signoff` and `11_Independent_Retest_R1` report the correct technical totals and HOLD state. Dashboard A2 also retains the earlier statement that independent QA is pending; the retest sheet supersedes it.

Evidence: `workbook_sanity.json`, `input_workbook_structure.json`, and preserved original `inputs` workbook. Hash of supplied workbook: `6c3792d76628e894c46e814db933714a63b6669fd6bd936f1ac3b4d575438222`.

Impact: Dashboard is unreliable for release counts/criterion alignment. The detailed independent test results agree with the independent report and JSON. This does not reopen D001–D020, change learning behavior, or create a need to invent business rules.

Proposed narrow correction: create a clearly labeled derivative of the QA workbook, correct summary references/labels and stale subtitle, preserve all source result rows and original evidence. Recount 94/44/94, verify gate remains HOLD and names/dates/signoffs remain blank/PENDING, render affected Dashboard, compare all other sheets, then request independent confirmation. Do not overwrite the supplied independent workbook or sign for its author.

## Targeted correction produced

Derivative: `C:/Mingo/03_Kiem_thu/Bang_chung/outputs/phase2-completion-20260930/Mingo_Phase2_QA_Control_Dashboard_Corrected_2026-09-30.xlsx`.

SHA-256: `e4fefc2f813c3b549d4f7263d974b157b1a17c537828519403c64f4e1758ad31`.

19 Dashboard cells corrected: aligned count/criterion headers, 94 total / 44 P0 / 94 PASS, formula-driven counts, ACTIVE/HOLD state and pending AT/Tech/Owner results. Artifact Tool recalculation and error scan passed. Final OOXML preservation check confirmed only `xl/worksheets/sheet1.xml` changed; all other ZIP parts and 13 other sheets, including signoff and detailed QA/defects, are byte-identical to the supplied original. Cell styles are preserved throughout. Original input SHA-256 still matches the value above. No independent author signature was added.

Source Dashboard was viewed in native Excel Protected View. The final derivative visual check remains pending: two bounded Artifact Tool render attempts failed to complete, and native Excel foreground interaction later failed. Recalculated values and cached saved values were verified separately; this is not a claim of native Excel recalculation or final visual approval.

Owner: QA/report maintainer — unassigned. Independent closure: ______. Verification: `03_Kiem_thu/Bang_chung/outputs/phase2-completion-20260930/workbook-correction-verification.json`.
