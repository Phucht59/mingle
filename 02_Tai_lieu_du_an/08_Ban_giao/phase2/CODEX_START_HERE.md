# Codex Start Here — Phase 2 Rework R1

Use this package as the only Phase 2 working candidate. Do not reopen V3.2 or Phase 1.

1. Use `CODEX_SUPER_PROMPT.md` as the execution prompt, then read `CODEX_EXECUTION_HANDOFF.md` completely.
2. Run from repository root:
   - `python 04_Van_hanh/Scripts/verify_phase2_rework.py`
   - `node --check 02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/prototype/app.js`
3. Execute the browser/accessibility regression described in the handoff against a clean browser profile.
4. Update `03_Kiem_thu/QA_QC/phase2/Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx` and evidence files from actual runs.
5. Do not mark Phase 2 DONE.
6. Create a QA-retest package using `QA_RETEST_HANDOFF_TEMPLATE.md` and hand it to independent QC/QA.

If a test fails, fix the Phase 2 prototype/spec/handoff only unless the evidence proves a frozen V3.2 conflict. Never weaken a test just to make it pass.
