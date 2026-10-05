# Path dependency analysis

Pre-migration rg scan covers Markdown, YAML/CI, JSON/manifests, Python, shell/PowerShell, Dart, JavaScript and all nonignored text. Exact matches: 2845. Full matches in path_matches_before.txt.

Critical: .github/workflows/foundation.yaml; .gitignore/.gitattributes; operation scripts using repo-root paths; adapter import in operations/tests; provenance SHA256SUMS; Phase 2 release manifest; QC protected-file intake; Python editable installation; Flutter generated absolute paths.

Frozen V3.2 source, historical manifests, captured logs and evidence must remain byte-identical. Relocation metadata will map their captured old paths; current navigation/scripts will use new paths. Historical release verifier is package-scoped and cannot assert the dirty working tree matches an older release.

| File | Matches | Treatment |
|---|---:|---|
| `.\.gitattributes` | 1 | Update current path references / relative links |
| `.\.github\workflows\foundation.yaml` | 11 | Update current path references / relative links |
| `.\.gitignore` | 6 | Update current path references / relative links |
| `.\01_governance\DECISION_REGISTER.md` | 1 | Update current path references / relative links |
| `.\01_governance\IMPLEMENTATION_ROADMAP.md` | 1 | Update current path references / relative links |
| `.\01_governance\PROJECT_MEMORY.md` | 5 | Update current path references / relative links |
| `.\01_governance\PROJECT_PROGRESS_SNAPSHOT.md` | 2 | Update current path references / relative links |
| `.\01_governance\PROJECT_STATE.md` | 3 | Update current path references / relative links |
| `.\02_product\MVP_PRD.md` | 1 | Update current path references / relative links |
| `.\02_product\learning_design\LEARNER_EVIDENCE_MODEL.md` | 1 | Update current path references / relative links |
| `.\02_product\ux_ui\phase2\01_PHASE_2_CONTRACT.md` | 1 | Update current path references / relative links |
| `.\02_product\ux_ui\phase2\13_DEVELOPER_HANDOFF.md` | 2 | Update current path references / relative links |
| `.\02_product\ux_ui\phase2\README.md` | 1 | Update current path references / relative links |
| `.\02_product\ux_ui\phase2\SCREEN_STATE_QA_TRACEABILITY.csv` | 166 | Update current path references / relative links |
| `.\04_architecture\README.md` | 1 | Update current path references / relative links |
| `.\04_architecture\REPO_STRUCTURE.md` | 13 | Update current path references / relative links |
| `.\04_architecture\V3_2_COMPATIBILITY_MATRIX.md` | 1 | Update current path references / relative links |
| `.\04_architecture\baseline\V3_2_BASELINE_SUMMARY.md` | 3 | Update current path references / relative links |
| `.\04_architecture\contracts\v3_2\README.md` | 2 | Update current path references / relative links |
| `.\04_architecture\contracts\v3_2\original_verification\README.md` | 1 | Update current path references / relative links |
| `.\05_code\.env.example` | 1 | Update current path references / relative links |
| `.\05_code\README.md` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\PHASE1_RERUN_20260926.md` | 8 | Update current path references / relative links |
| `.\06_quality\evidence\VERIFICATION_REPORT.md` | 3 | Update current path references / relative links |
| `.\06_quality\evidence\api-smoke-20260926T071502Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend-install-20260926.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend-lint-20260926T071502Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend-unit-20260926.log` | 4 | Update current path references / relative links |
| `.\06_quality\evidence\backend-unit-20260926.xml` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend-unit-20260926T071502Z.log` | 5 | Update current path references / relative links |
| `.\06_quality\evidence\backend-unit-20260926T071502Z.xml` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend\api-ready-smoke-20260926T100322Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend\backend-lint-20260926T100322Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\backend\backend-unit-20260926T100322Z.log` | 5 | Update current path references / relative links |
| `.\06_quality\evidence\backend\backend-unit-20260926T100322Z.xml` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36250667211\108427966672.log` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36250667211\108427966747.log` | 56 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36250667211\108427966750.log` | 39 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36250667211\108427966792.log` | 56 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36250667211\run.json` | 6 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36252349822\108432611678.log` | 39 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36252349822\108432611844.log` | 29 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36252349822\108432611896.log` | 56 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36252349822\108432612475.log` | 56 | Update current path references / relative links |
| `.\06_quality\evidence\ci\36252349822\run.json` | 8 | Update current path references / relative links |
| `.\06_quality\evidence\ci\PHASE1_PASS_20260926.md` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\ci\diagnostics\backend-container-before-fix.log` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\clean-repro-api-smoke-20260926T071803Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean-repro-backend-lint-20260926T071803Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean-repro-backend-unit-20260926T071803Z.log` | 5 | Update current path references / relative links |
| `.\06_quality\evidence\clean-repro-backend-unit-20260926T071803Z.xml` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean-repro-install-20260926.log` | 26 | Update current path references / relative links |
| `.\06_quality\evidence\clean-repro-package-20260926.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\README.md` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\api-degraded-smoke-20260926T150704Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\api-ready-smoke-20260926T150728Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\backend-lint-20260926T150704Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\backend-lint-20260926T150728Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\backend-unit-20260926T150704Z.log` | 5 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\backend-unit-20260926T150704Z.xml` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\backend-unit-20260926T150728Z.log` | 5 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\backend\backend-unit-20260926T150728Z.xml` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\android-install.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\android-screenshot.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\android-ui-pull.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\backend-postgres.log` | 8 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\backend-without-env.log` | 5 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\chrome-render.log` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\flutter-bootstrap.log` | 55 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\flutter-verify.log` | 3 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\locked-install.log` | 27 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\original-v3-2.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\commands\package-install.log` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\flutter\learner\test-20260926T150621Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\flutter\staff\test-20260926T150621Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\harness\client_boot.py` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\harness\reproduce.py` | 10 | Update current path references / relative links |
| `.\06_quality\evidence\clean_reproduction\run-4cdecb4\postgres\postgres-20260926T150728Z.log` | 4 | Update current path references / relative links |
| `.\06_quality\evidence\flutter\diagnostics\analyze-20260926T093040Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\flutter\learner\test-20260926T100348Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\flutter\staff\test-20260926T100348Z.log` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\postgres\postgres-20260926T100322Z.log` | 4 | Update current path references / relative links |
| `.\06_quality\evidence\v3_2\INTAKE_AND_VERIFICATION_20260926.md` | 2 | Update current path references / relative links |
| `.\06_quality\evidence\v3_2\SEARCH_20260926.md` | 1 | Update current path references / relative links |
| `.\06_quality\evidence\v3_2\clean-d4165e8\locked-install.log` | 22 | Update current path references / relative links |
| `.\06_quality\evidence\v3_2\original-contract-gate-20260926.log` | 1 | Update current path references / relative links |
| `.\06_quality\gates\PHASE_1_GATE.md` | 2 | Update current path references / relative links |
| `.\06_quality\phase2\DEFECT_RETEST_RESULTS.csv` | 20 | Update current path references / relative links |
| `.\06_quality\phase2\PHASE_2_VERIFICATION_REPORT.md` | 3 | Update current path references / relative links |
| `.\06_quality\phase2\QA_TEST_CASES.csv` | 94 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\builder_preflight\README.md` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\README.md` | 4 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\browser-first-run.json` | 74 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\browser\run-P0.json` | 29 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\browser\run-P1.json` | 45 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\browser\run.json` | 74 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\defect_retest_results.json` | 20 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\environment.json` | 6 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\intake.json` | 275 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\node_syntax_final.json` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\ordered_execution_commands.json` | 5 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\review\QC-001.json` | 8 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\review\QC-009.json` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\review\run-P0.json` | 24 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\review\run-P1.json` | 5 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\review\run.json` | 29 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\codex\rework_r1_static_checks.log` | 2 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\internal_pre_codex\README.md` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\evidence\source_immutability_check.txt` | 2 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\FINAL_GATE_INTAKE.md` | 2 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\P2_D021_DECISION_PACKET.md` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\PHASE2_SCOPE_RECONCILIATION.md` | 2 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\TALKBACK_MANUAL_RUNBOOK.md` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\d021-fix\review-run.json` | 29 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\d021-fix\verification.json` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\diagnose-d021.cjs` | 1 | Update current path references / relative links |
| `.\06_quality\phase2\final_gate\2026-09-30\review_cases.json` | 29 | Update current path references / relative links |
| `.\06_quality\phase2\qa_cases.json` | 94 | Update current path references / relative links |
| `.\06_quality\standards\DEFINITION_OF_DONE.md` | 1 | Update current path references / relative links |
| `.\06_quality\standards\TEST_STRATEGY.md` | 1 | Update current path references / relative links |
| `.\07_operations\README.md` | 1 | Update current path references / relative links |
| `.\07_operations\docs\CI_CD.md` | 2 | Update current path references / relative links |
| `.\07_operations\docs\DATABASE_BOOTSTRAP_AND_MIGRATIONS.md` | 2 | Update current path references / relative links |
| `.\07_operations\docs\ENVIRONMENTS.md` | 1 | Update current path references / relative links |
| `.\07_operations\docs\LOCAL_RUNTIME.md` | 6 | Update current path references / relative links |
| `.\07_operations\docs\V3_2_VERIFICATION.md` | 5 | Update current path references / relative links |
| `.\07_operations\scripts\bootstrap_clients.ps1` | 2 | Update current path references / relative links |
| `.\07_operations\scripts\bootstrap_clients.sh` | 2 | Update current path references / relative links |
| `.\07_operations\scripts\check_original_contracts.py` | 3 | Update current path references / relative links |
| `.\07_operations\scripts\clean_setup.sh` | 3 | Update current path references / relative links |
| `.\07_operations\scripts\run_phase2_qa.py` | 3 | Update current path references / relative links |
| `.\07_operations\scripts\smoke_api.py` | 1 | Update current path references / relative links |
| `.\07_operations\scripts\verify_backend.ps1` | 7 | Update current path references / relative links |
| `.\07_operations\scripts\verify_backend.sh` | 8 | Update current path references / relative links |
| `.\07_operations\scripts\verify_flutter.ps1` | 3 | Update current path references / relative links |
| `.\07_operations\scripts\verify_phase2_artifacts.py` | 3 | Update current path references / relative links |
| `.\07_operations\scripts\verify_phase2_browser.cjs` | 3 | Update current path references / relative links |
| `.\07_operations\scripts\verify_phase2_package_manifest.py` | 1 | Update current path references / relative links |
| `.\07_operations\scripts\verify_phase2_review.py` | 6 | Update current path references / relative links |
| `.\07_operations\scripts\verify_phase2_rework.py` | 1 | Update current path references / relative links |
| `.\07_operations\scripts\verify_phase2_supplemental.cjs` | 1 | Update current path references / relative links |
| `.\08_handoff\PHASE1_CLOSURE_20260926.md` | 1 | Update current path references / relative links |
| `.\08_handoff\README.md` | 3 | Update current path references / relative links |
| `.\08_handoff\RELEASE_CHECK.md` | 2 | Update current path references / relative links |
| `.\08_handoff\RELEASE_CHECK_20260926.md` | 1 | Update current path references / relative links |
| `.\08_handoff\phase2\CODEX_EXECUTION_HANDOFF.md` | 12 | Update current path references / relative links |
| `.\08_handoff\phase2\CODEX_START_HERE.md` | 3 | Update current path references / relative links |
| `.\08_handoff\phase2\CODEX_SUPER_PROMPT.md` | 15 | Update current path references / relative links |
| `.\08_handoff\phase2\HANDOFF_INDEX.md` | 7 | Update current path references / relative links |
| `.\08_handoff\phase2\MANIFEST_SHA256.txt` | 772 | Preserve captured bytes / historical context |
| `.\08_handoff\phase2\PHASE2_QA_HANDOFF.md` | 1 | Update current path references / relative links |
| `.\08_handoff\phase2\QA_EXECUTION_PLAN.md` | 1 | Update current path references / relative links |
| `.\08_handoff\phase2\QA_QC_RETEST_PROMPT.md` | 3 | Update current path references / relative links |
| `.\08_handoff\phase2\QA_RETEST_HANDOFF.md` | 3 | Update current path references / relative links |
| `.\08_handoff\phase2\QA_RETEST_HANDOFF_TEMPLATE.md` | 1 | Update current path references / relative links |
| `.\08_handoff\phase2\REWORK_R1_PACKAGE_README.md` | 4 | Update current path references / relative links |
| `.\08_handoff\provenance\CANONICAL_MANIFEST_SHA256.json` | 164 | Preserve captured bytes / historical context |
| `.\08_handoff\provenance\ORIGINAL_FULL_PACK_MANIFEST_SHA256.json` | 4 | Preserve captured bytes / historical context |
| `.\08_handoff\provenance\REORGANIZATION_RECORD.md` | 9 | Update current path references / relative links |
| `.\08_handoff\provenance\v3_2\SOURCE.md` | 2 | Update current path references / relative links |
| `.\99_archive\Adaptive_Learning_Phase1_Full_Pack_2026-09-23\01_FILE_INDEX.md` | 4 | Preserve captured bytes / historical context |
| `.\99_archive\Adaptive_Learning_Phase1_Full_Pack_2026-09-23\MANIFEST_SHA256.json` | 4 | Preserve captured bytes / historical context |
| `.\99_archive\Adaptive_Learning_Phase1_Full_Pack_2026-09-23\history\project\adaptive_language_learning_project_handoff_2026-09-23\README.md` | 1 | Preserve captured bytes / historical context |
| `.\99_archive\README.md` | 1 | Preserve captured bytes / historical context |
| `.\PROJECT_MAP.md` | 10 | Update current path references / relative links |
| `.\README.md` | 31 | Update current path references / relative links |
| `.\REPO_RULES.md` | 2 | Update current path references / relative links |
| `.\START_HERE.md` | 15 | Update current path references / relative links |
