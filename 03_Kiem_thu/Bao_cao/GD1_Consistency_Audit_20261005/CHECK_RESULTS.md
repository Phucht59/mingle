# Executed verification — 05/10/2026

Windows/PowerShell; V3.2 và backend Python3.12.10; Node24.19.0; Flutter3.32.8/Dart3.8.1. Bundled Python chỉ dùng đọc workbook/evidence. Repo main/HEADa112f762..., dirty candidate. Baseline checks chạy trước corrections, không sửa test hoặc original files.

| Check | Command | Expected | Actual | Result |
|---|---|---|---|---|
| Original V3.2 | `.local/v32-venv/Scripts/python.exe -X utf8 04_Van_hanh/Scripts/check_original_contracts.py` | 115 contract +22 SQL, hashes intact | 115/0failed,22/0failed,102hashes; npm/contract/sql exits0 | PASS — SQL PGlite |
| Dependencies | `.local/v32-venv/Scripts/python.exe -m pip check` | Không broken requirements | Không broken requirements | PASS |
| Adapter guards | `.local/v32-venv/Scripts/python.exe -m unittest discover -s 04_Van_hanh/tests -v` | 9 additive guards | 9passed,0failed,0skip | PASS; không cộng vào115/22 |
| Backend | `.venv/Scripts/python.exe -m pytest 01_San_pham/backend/tests -q --junitxml=03_Kiem_thu/Bang_chung/gd1_consistency_20261005/backend.xml` | Environment-supported cases | 9passed,7skipped,0failed | PARTIAL EXECUTION |
| Flutter shared package | `flutter test test/fixture_test.dart test/independent_test.dart test/presentation_test.dart --reporter json` | 3 unchanged test files | 232passed,0failed,0skipped; exit0 | PASS presentation/widget/golden |
| Legacy static | `MINGO_QA_OUTPUT=<audit>/legacy_static`; `python -X utf8 04_Van_hanh/Scripts/verify_phase2_artifacts.py` | Inherited spec metadata | 57screens,18components,16PRD,94QA,0errors | PASS at legacy spec scope |
| Current evidence verifier | `python -X utf8 <audit>/run_current_verifier.py` | Existing conditions, preserve historical report | 19checksPASS,0errors | PASS integrity of recorded evidence |
| Fresh structural extraction | Bundled Python `-X utf8 <audit>/collect_evidence.py` | Exact ID/set consistency | 16PRD/61screens/175states; zero dangling/missing/duplicate | PASS structure |
| Native PostgreSQL | NOT EXECUTED with --run-postgres | Disposable native DB cases | 6 foundation PG cases skipped | NOT EXECUTED |
| Mobile/domain fault scenarios, real auth/offline/deletion/restore | NOT EXECUTED | Runtime acceptance | Handlers/queues not implemented in current source | NOT EXECUTED |
| Physical device/TalkBack/human studies | NOT EXECUTED | Device/human evidence | No run in this audit | NOT EXECUTED |
| Hosted CI for dirty candidate | NOT EXECUTED | Exact candidate CI | Workflow inspected, no dispatch/push | NOT EXECUTED |
| Actual BA workbook checks | NOT EXECUTED | Full P0/P1/RTM/WBS semantics | NOT FOUND | BLOCKED |

Backend7skip gồm6 PostgreSQL và1 Windows symlink privilege. XML/log giữ reasons. Historical foundation6/6 không thay fresh native evidence. Selected Flutter232 khác prior full275 do test subset; không phải drift115/22. Legacy57 và current61 là hai source boundaries, không ép số khớp.

Original run: `03_Kiem_thu/Bang_chung/v3_2/20261004T181105665514Z/`, package3.2.0. ManifestSHA `617245605096b3b9cc5f141dda352abc180d97f11738297949c3195711cc0e6d`. UTC04/10 18:11:05 tương ứng05/10 Asia/Saigon.

Current verifier wrapper không đổi conditions/input; chỉ redirect sole report write sang audit evidence. Các số50/274/275 trong output được đọc từ runs20261003, không chạy lại ở audit này. Prior report nguyên byte. `docs/12_ACCEPTANCE_TESTS_V3.md` là acceptance plan, không phải toàn bộ scenarios executed.

Logs/XML/JSON, source hash ledger và post-fix validation nằm trong `03_Kiem_thu/Bang_chung/gd1_consistency_20261005/`. Post-fix checks không rerun runtime suites vì corrections chỉ ở documentation, nhưng kiểm chứng originals/protected source, expected edits, navigation links và report counts.
