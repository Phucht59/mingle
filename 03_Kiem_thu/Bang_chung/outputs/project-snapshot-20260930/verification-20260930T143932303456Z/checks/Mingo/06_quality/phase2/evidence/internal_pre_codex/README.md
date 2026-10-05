# Internal pre-Codex evidence — non-gating

These files were generated while building Rework R1 to catch obvious regressions before handing the package to Codex. They are **not independent QA evidence and do not close Phase 2 defects**.

- `learner_browser_pre_codex.json` — PASS for learner learning-integrity/offline/preview representative checks.
- `placement_listening_pre_codex.json` — PASS for placement/listening representative checks.
- `staff_browser_pre_codex.json` — PASS for staff publishing/accessibility representative checks.
- `browser_regression_pre_codex.json` — an earlier combined harness run. Product checks passed but the harness timed out when switching to Staff; this was superseded by the split Staff suite above, which passed. Preserve it for transparency; do not treat the harness timeout as a Phase 2 product PASS or FAIL.

Codex must re-execute the mandatory regressions in a fresh environment according to `08_handoff/phase2/CODEX_EXECUTION_HANDOFF.md`. Independent QC/QA must then reproduce gate-critical cases.
