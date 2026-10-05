# Phase 2 R1 → Independent QC/QA Retest Handoff

> **QA RETEST CANDIDATE.** Codex execution complete. Independent approval pending; Phase 2 ACTIVE / GATE NOT PASSED, Phase 3 DEFERRED.

## Candidate identity

- Package: `Mingo_Phase2_UXUI_QA_Retest_R1_20260927_codex-r1.zip`
- SHA-256: exact value in the adjacent `.zip.sha256` and `.manifest.json` release sidecars. The ZIP cannot contain its own final checksum.
- Git/revision: `codex-r1`; exact Git commit in the external `.manifest.json`.
- Date: 2026-09-27
- Input ZIP SHA-256: `2645679376da1d5f4bf01cdf5a94c04c4bc1cc6326197902f8c502afda08dd48`
- Architecture baseline: V3.2.0 unchanged
- Phase 2 gate: NOT PASSED pending independent QC/QA

## Codex execution summary

- Static verifier: PASS
- Node syntax: PASS
- Browser regression: 74 cases PASS plus 30 supplemental checks PASS. Twenty further canonical cases are artifact reviews.
- QA cases: **94 PASS / 0 FAIL / 0 BLOCKED / 0 NOT RUN**; **44/44 P0 PASS**. Final execution runs P0 before P1.
- Open defects pending independent closure: **4 P0 / 14 P1 / 2 P2 / 0 P3**. All 20 findings have Codex retest PASS; none independently CLOSED.
- Accessibility: Windows / real headless Chromium; native AX names, keyboard/focus, modal containment/restore, live-region targeting, reduced motion and text/reflow checks PASS. **Interactive screen-reader/TalkBack speech session BLOCKED**, outside the canonical 94-case count and still mandatory for the gate.
- Production `01_San_pham/` and original V3.2 unchanged. No Phase 3 implementation or architecture change.
- Tech Lead handoff acceptance and Product/Owner UAT/signoff: PENDING.

## Mandatory evidence

- `03_Kiem_thu/QA_QC/phase2/evidence/codex/rework_r1_static_checks.*`
- browser screenshots/logs for D001–D005, D013 and QA-OFF-007
- first-use, Grammar, Listening and Staff publishing flow evidence
- accessibility tree/focus/zoom evidence
- updated QA control workbook
- updated defect retest results

Paths: `03_Kiem_thu/QA_QC/phase2/DEFECT_RETEST_RESULTS.csv`, `CODEX_EXECUTION_DEFECTS.md`, `PHASE_2_VERIFICATION_REPORT.md`, and `evidence/codex/README.md`. The workbook retains all Expected values and pending signoffs. The original independent audit is immutable.

`MANIFEST_SHA256.txt` covers every package file except itself. The external manifest records exact commit, ZIP hash and completed release integrity checks; it completes workbook CX-14 after packaging without embedding a circular checksum.

## Independent QA instructions

1. Verify package hash/manifest.
2. Do not trust Codex PASS labels without reproducing P0 cases.
3. Execute all P0 first.
4. Re-test P2-D001..P2-D020, including draft persistence, modal Escape/Tab, missing-media Skip and 320px/200% clipping.
5. Run full 94-case suite or record exact environment blockers.
6. Gate requires 100% P0 PASS, zero open P0/P1, ≥95% executed PASS, mandatory accessibility PASS, Tech Lead acceptance and Product/Owner signoff.
7. Only independent QC/QA may recommend Phase 2 DONE; Product/Owner records final signoff.

Verify the manifest immediately after fresh extraction, before runners rewrite evidence. Use `QA_QC_RETEST_PROMPT.md` and the evidence README for execution commands. Screen/state mapping does not prove every one of the 166 variants was runtime exercised. Complete interactive assistive-technology review separately.

## Delivery status

This exact package is prepared for the user to transfer to independent QC/QA. No named external QA account/chat or delivery endpoint was supplied; no external receipt or independent acceptance is claimed.
