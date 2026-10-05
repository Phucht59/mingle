# Executed verification and evidence boundaries

All six applicable existing checks were executed. Original V3.2 adapter is executed through an output-only harness: exactly two output path expressions redirect evidence and work copy inside the dedicated audit evidence. ROOT, SOURCE, checksum inventory, adapter source bytes, validators, assertions and failure conditions remain unchanged. The canonical script is not edited. Exact transformation: v3_output_redirect.json; child commands include npm-ci, original validators/run_checks.py and original tests/check_sql.mjs. Flutter uses --no-pub to avoid dependency/lock updates; backend disables pytest cache provider and writes JUnit only here.

| Check | Result | Passed | Failed | Skipped | Execution/evidence limitation |
| --- | --- | --- | --- | --- | --- |
| v3_versions | PASS | N/A version query | 0 | 0 | Read-only environment/tool query; no gate result |
| node_version | PASS | N/A version query | 0 | 0 | Read-only environment/tool query; no gate result |
| original_contracts | PASS | 137 | 0 | 0 | 115 contract + 22 SQL; 102 original hashes; npm ci exit0 |
| pip_check | PASS | N/A dependency consistency | 0 | 0 | No broken requirements found |
| flutter_version | PASS | N/A version query | 0 | 0 | Read-only environment/tool query; no gate result |
| adapter_guards | PASS | 9 | 0 | 0 | 9 negative/positive adapter-integrity/report guards |
| backend_version | PASS | N/A version query | 0 | 0 | Read-only environment/tool query; no gate result |
| backend | PASS | 9 | 0 | 7 | API/worker foundation; native DB tests skipped when test DSN unavailable |
| flutter_selected | PASS | 232 | 0 | 0 | Unit/widget/presentation fixtures; three selected files; no auth/durable/native/customer claim |
| phase2_artifacts | PASS | N/A structural aggregate | 0 | 0 | 57 legacy screens, 18 components, 16 PRDs, 94 QA specs; not 94 executed QA cases |

## Commands, cwd, timing, artifacts

| Command | Working directory | Start UTC | End UTC | Exit | Output/artifacts |
| --- | --- | --- | --- | --- | --- |
| C:\Mingo\.local\v32-venv\Scripts\python.exe --version | C:\Mingo | 2026-10-05T03:11:59.815394+00:00 | 2026-10-05T03:11:59.880777+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_versions.log;  |
| "C:\Program Files\nodejs\node.EXE" --version | C:\Mingo | 2026-10-05T03:11:59.886068+00:00 | 2026-10-05T03:11:59.960339+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\node_version.log;  |
| C:\Mingo\.local\v32-venv\Scripts\python.exe -X utf8 C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\run_v3_redirect.py | C:\Mingo | 2026-10-05T03:11:59.962348+00:00 | 2026-10-05T03:12:20.462751+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\original_contracts.log; C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_2\20261005T031200415707Z\run.json, C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_child_commands.json, C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_output_redirect.json, C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_work |
| C:\Mingo\.local\v32-venv\Scripts\python.exe -m pip check | C:\Mingo | 2026-10-05T03:12:00.185589+00:00 | 2026-10-05T03:12:02.464505+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\pip_check.log;  |
| C:\Dev\flutter-3.32.8\bin\flutter.BAT --version | C:\Mingo | 2026-10-05T03:12:00.540636+00:00 | 2026-10-05T03:12:03.206005+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\flutter_version.log;  |
| C:\Mingo\.local\v32-venv\Scripts\python.exe -m unittest discover -s 04_Van_hanh/tests -v | C:\Mingo | 2026-10-05T03:12:02.464505+00:00 | 2026-10-05T03:12:02.855058+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\adapter_guards.log;  |
| C:\Mingo\.venv\Scripts\python.exe --version | C:\Mingo | 2026-10-05T03:12:02.856058+00:00 | 2026-10-05T03:12:02.901229+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\backend_version.log;  |
| C:\Mingo\.venv\Scripts\python.exe -m pytest 01_San_pham/backend/tests -q -p no:cacheprovider --junitxml=C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\backend.xml | C:\Mingo | 2026-10-05T03:12:02.902296+00:00 | 2026-10-05T03:12:08.964698+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\backend.log; C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\backend.xml, C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\backend_summary.json |
| C:\Dev\flutter-3.32.8\bin\flutter.BAT test test/fixture_test.dart test/independent_test.dart test/presentation_test.dart --reporter json --no-pub | C:\Mingo\01_San_pham\cong_cu_phat_trien\mingo_ui | 2026-10-05T03:12:03.207473+00:00 | 2026-10-05T03:13:52.633846+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\flutter_selected.log; C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\flutter_selected.log, C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\flutter_selected_summary.json |
| C:\Mingo\.local\v32-venv\Scripts\python.exe -X utf8 04_Van_hanh/Scripts/verify_phase2_artifacts.py | C:\Mingo | 2026-10-05T03:12:08.965698+00:00 | 2026-10-05T03:12:09.245017+00:00 | 0 | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\phase2_artifacts.log; C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\phase2_static\internal_static_checks.json |

### Nested unchanged V3.2 commands

| Command | CWD | Start UTC | End UTC | Exit |
| --- | --- | --- | --- | --- |
| "C:\Program Files\nodejs\npm.cmd" ci --ignore-scripts --no-audit --no-fund | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_work\20261005T031200415707Z | 2026-10-05T03:12:00.815789+00:00 | 2026-10-05T03:12:15.168997+00:00 | 0 |
| C:\Mingo\.local\v32-venv\Scripts\python.exe -X utf8 validators/run_checks.py | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_work\20261005T031200415707Z | 2026-10-05T03:12:15.168997+00:00 | 2026-10-05T03:12:17.420905+00:00 | 0 |
| "C:\Program Files\nodejs\node.EXE" tests/check_sql.mjs | C:\Mingo\03_Kiem_thu\Bang_chung\gd1_targeted_closure_20261005\v3_work\20261005T031200415707Z | 2026-10-05T03:12:17.422350+00:00 | 2026-10-05T03:12:20.373316+00:00 | 0 |

## Material versions

Python V3.2: 3.12.10 (tags/v3.12.10:0cc8128, Apr  8 2025, 12:21:36) [MSC v.1943 64 bit (AMD64)]; Node v24.19.0; original package 3.2.0. Flutter version output: CWD: C:\Mingo
Command: C:\Dev\flutter-3.32.8\bin\flutter.BAT --version
Flutter 3.32.8 • channel [user-branch] • unknown source
Framework • revision edada7c56e (1 year, 2 months ago) • 2025-07-25 14:08:03 +0000
Engine • revision ef0cd00091 (1 year, 2 months ago) • 1970-01-01 07:00:00.000
Tools • Dart 3.8.1 • DevTools 2.45.1
. Backend dependency versions and loaded-source equivalence: backend_loaded_source_boundary.json. Loaded installed package matches 11 current source files: True.

## Backend skip reasons

| Test | Reason |
| --- | --- |
| test_migration_idempotent_and_readiness | Use --run-postgres with TEST_DATABASE_URL; NOT verified |
| test_migration_checksum_and_atomic_failure | Use --run-postgres with TEST_DATABASE_URL; NOT verified |
| test_concurrent_idempotent_enqueue_and_claim | Use --run-postgres with TEST_DATABASE_URL; NOT verified |
| test_crash_recovery_and_stale_worker_fencing | Use --run-postgres with TEST_DATABASE_URL; NOT verified |
| test_retry_exhaustion_and_no_partial_effect | Use --run-postgres with TEST_DATABASE_URL; NOT verified |
| test_worker_health_expires | Use --run-postgres with TEST_DATABASE_URL; NOT verified |
| test_storage_rejects_symlink_escape | Windows symlink creation requires an unavailable privilege |

## Evidence type separation

| Layer | Current result | Meaning / limit |
| --- | --- | --- |
| ARTIFACT PRESENT | Repo source/specs present; actual BA workbook NOT FOUND | Presence alone is not semantic approval |
| STRUCTURAL VALIDATION | Current16/61/175 zero dangling; legacy verifier57/94 PASS | Current Flutter catalog and inherited Phase2 artifacts are different inventories |
| SEMANTIC VALIDATION | PARTIAL; actual priority/BR/Trigger/UC/WF unknown | Candidate PO/source trace is reviewable but cannot certify absent workbook |
| EXECUTABLE CHECK | 115+22, 9 guards, backend9/7, Flutter232 passed | Original PGlite and fixtures/foundation, not full auth/offline runtime |
| RUNTIME VALIDATION | NOT EXECUTED for full product/native DB concurrency/auth/offline/device recovery | Skipped DB-dependent tests are not PASS |
| HUMAN VALIDATION | NOT EXECUTED in this audit; separate Phase2 gate pending | Widget/golden/structural checks do not sign human acceptance |
| CUSTOMER VALIDATION | VALIDATION DEBT; NOT EXECUTED | No market/PMF/learning/ML efficacy claim |
