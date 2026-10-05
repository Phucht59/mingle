# Phase 0–2 regression — V2, 2026-10-02

Machine evidence is local Windows execution on the uncommitted candidate, HEAD a112f762ab08f6fa688cc4857b21d95d1055ab5c. Previous failed attempts remain separate files. No hosted run, independent QA acceptance or human study is claimed.

| Check actually run | Result | Evidence under 03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001 |
|---|---|---|
| Original V3.2 contracts / SQL | 115/115 + 22/22 PASS | v3_2_after.log |
| Protected V3/backend/foundation hashes | 141 checked, 0 mismatch | v2_verification.json |
| Before-migration artifact presence | 10096 present, 0 missing | v2_verification.json |
| Historical/evidence preservation | 9607 checked, 0 mismatch | v2_verification.json |
| Backend Ruff / unit harness | PASS; 9 passed, 7 skipped in non-PostgreSQL run | phase1_revalidation_pwsh.log |
| Native PostgreSQL integration/concurrency | 6/6 PASS; separate execution | phase1_revalidation_pwsh.log |
| API live/ready; worker durable probe; storage | 200/200; completion; smoke PASS | phase1_revalidation_pwsh.log |
| Shared Flutter analyze | No issues | shared_sealed_analyze.log |
| Shared Flutter final tests | 227/227 PASS, 0 skipped | flutter_sealed_final.jsonl |
| Presentation matrix | 3,500 screen/state/size/scale checks + 96 domain checks + 4 at320px/200% | presentation_test.dart and final JSON events |
| Repeat golden comparison | 195/195 captures compared, PASS | screenshot_manifest.json; screenshots/ |
| Learner/staff analyze and widget tests | No issues; 1/1 each PASS | flutter_sealed_apps.log |
| Learner Android debug APK / staff Web build | PASS | flutter_sealed_apps.log |
| Fresh learner/staff Web with final audio adapter | PASS | learner_sealed_web.log; flutter_sealed_apps.log |
| Actual Android emulator integration | 2/2 PASS: boot and licensed sample playback initialization/budget | android_review_final.log |
| Compiled Chrome runtime navigation | 7/7 PASS; learner360/412/430, staff600/1280/1440/1920 | web_runtime_sealed_final/run.json |
| Original adapter guard suite | 9/9 PASS retained in this rebaseline | adapter_final_verified.log |
| R1 browser / supplemental | 74/74 + 30/30 PASS | r1_final/browser/; r1_final/supplemental/ |
| R1 review suite | 19/20 PASS; QC-002 FAIL | r1_final/review/: sealed old Flutter shell hashes intentionally reject authorized V2 UI |
| Original organization hash verifier after UI rework | FAIL under its historical organization-only scope | historical_organization_scope_after_ui.json; seal not weakened |
| D022 original/corrected workbook hashes | 2/2 PASS; no edits | d022_preservation.json |

The two historical verifier failures remain failures. They seal the former Flutter shell/current documentation, which the owner's subsequent instruction explicitly authorizes replacing. The scoped V2 verifier protects unchanged backend/V3, every original screen/state, all original artifacts and historical bytes. It does not change the old assertions or manufacture a 94/94 rerun.

NOT RUN / PENDING: current hosted GitHub Actions; Linux/iOS/macOS execution; physical-device audio; actual TalkBack/VoiceOver speech and focus; complete human keyboard/accessibility review; participant usability study; diary pilot; independent QA/content/tech/Product Owner acceptance. Windows symlink-escape case skips because WinError1314 requires symlink privileges; it remains required on the Linux suite. Emulator was launched with -no-audio: successful playback requests are not proof of audible listening.

Nonblocking observed toolchain warnings: Android template NDK26 versus plugin-declared NDK27, SDK XML tool versions, Material typography's optional Cupertino icon-family lookup, deprecated Starlette/httpx TestClient path. Builds/tests pass; Tech Lead should disposition these before a production integration/build toolchain decision. No business dependency upgrade was made to suppress warnings.

Final scope additions: unavailable/submitting lesson states cannot answer or advance; locked objectives permit preview/recovery; eligible sample challenge contains one unaided Check without granting unlock. At320px/200%, a full-width selected-tab label and four labeled64dp icons prevent fragmented words; the test also navigates Learn→Profile. Final source state tests and all195 comparisons pass.

Current navigation/path audit:20 Python/YAML/JSON/JavaScript syntax checks PASS;3 PowerShell scripts parse with0 errors;105 current local Markdown links resolve;0 critical old-root path hits. Historical captured paths and intentional migration adapters remain. Pure-Python YAML audit dependency was installed only under ignored.local, preserving the user virtual environment. A grammar-only accidental path substitution in the retained R1 contract's ordinary word “outputs” was corrected; no V3 original changed.

Keyboard verification: the staff publication test dismisses the confirmation with Escape, checks it did not publish, then reopens and confirms. The same Escape/reopen path passes on compiled Web at1280/1440/1920. This is targeted keyboard evidence; complete keyboard/screen-reader focus and speech review remains manual/PENDING. Informational notices use neutral blue info icons rather than achievement checkmarks; missing evidence or permission is not presented as success.

Final navigation corrections: a reproduced system-Back failure is retained in system_back_reproduction.log. Learner PopScope now uses the presentation history; each entry retains its lesson family. Regression cases invoke platform pop, preserve first-response/feedback and return to the original Grammar summary after visiting Vocabulary. Android boot integration invokes platform pop back to Home. A separate reproduced staff drawer failure is retained in staff_drawer_reproduction.log; narrow navigation now uses a context below Scaffold, closes after selecting content and exposes the Vietnamese menu label. The new widget test and actual compiled Web at600px validate that recovery. Final227 tests,195 comparisons, Chrome7/7 and actual Android2/2 pass; earlier failures remain failures. No server/business/V3 rule changed.

Normal Android review: the final debug APK was installed after the integration-test entry point; cold launch returned Status: ok, and android_normal_review.png was captured and visually inspected. APK/screenshot hashes are recorded in android_normal_review_metadata.json. The build stays in its ignored source build directory; no production deployment is claimed.
