# Phase 2 R1 — Codex execution report — 2026-09-27

Status: **QA RETEST CANDIDATE. Phase 2 ACTIVE / GATE NOT PASSED.**

## Actual results

| Evidence | Result |
|---|---|
| Canonical suite | 94 PASS / 0 FAIL / 0 BLOCKED / 0 NOT RUN |
| P0 | 44/44 PASS |
| Real browser cases | 74 PASS, fresh Chromium context per case |
| Artifact review cases | 20 PASS; document/source checks, not runtime coverage |
| Supplemental browser checks | 30 PASS, including 200% text at learner 320/360/412/480 and staff 1024/1440 |
| Static verifier / Node syntax | PASS |
| Screen-reader/TalkBack speech session | BLOCKED; outside the 94-case count, still a mandatory gate condition |
| D001–D016 and new D017–D020 | Codex retest PASS; independent closure PENDING |
| Open pending independent closure | P0: 4, P1: 14, P2: 2, P3: 0 |

The 94-case count does not establish that all 166 mapped screen/state variants are runtime implemented or exercised. Artifact review verifies contracts and mappings. Tech Lead acceptance remains pending. An accessibility tree is not proof of screen-reader speech output.

## Concrete execution fixes

- D004: all responses/skips queue local work, including online. A later online answer cannot erase pending work. Explicit mock acknowledgement/canonical refresh is required for Synced.
- D009: draft fields survive Save, Preview, Review and publication. Published values are a separate snapshot; New Draft copies its lineage. Prompt/answer validation is visible; changing source invalidates license verification; draft text is HTML-escaped.
- D013/D014: option selection preserves focus. Escape/Cancel restores the modal trigger; Tab/Shift+Tab remain contained.
- D017: Profile goal edit/clear/save changes intent only.
- D018: demo scenarios expose unavailable recommendation, usable eligible cycles and honest nothing-eligible copy.
- D019: missing-media practice Skip renders recorded state and Continue. Check stays blocked without media.
- D020: 200% text no longer clips Start or bottom navigation inside the learner frame. Narrow cards stack, grids wrap and the demo toolbar does not obscure content.

## Evidence and limits

See `evidence/codex/README.md`, per-case JSON/PNG, `ordered_execution_commands.json`, `environment.json`, `DEFECT_RETEST_RESULTS.csv` and the updated workbook. Initial failing observations are retained separately.

Workbook Expected values, sheet order, historical audit values, validation/conditional-format/merge counts and pending signoffs were preserved. Artifact Tool recalculation found no formula errors. Its renderer did not finish on two bounded attempts; saved OOXML layout previews were inspected with a fallback reader. No native Excel interaction is claimed.

Production `01_San_pham/` and original V3.2 source are unchanged, checked by Git and raw working-copy hashes. Nine supplied runtime files use LF versus existing CRLF checkout bytes; content is identical. Git packaging uses canonical blobs. No architecture change or Phase 3 implementation was made.

Independent QC/QA must reproduce critical cases, close/reject findings, complete an interactive screen-reader/TalkBack-equivalent session, and obtain Tech Lead and Product/Owner acceptance. Codex grants none of these approvals. Phase 3 remains DEFERRED.

See:
- `PHASE2_REWORK_R1_FIX_REGISTER.md`
- `audits/2026-09-27_independent`
- `../../../02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/SCREEN_STATE_QA_TRACEABILITY.csv`
- `../../../02_Tai_lieu_du_an/08_Ban_giao/phase2/CODEX_EXECUTION_HANDOFF.md`
