# Báo cáo tái cấu trúc repository Mingo — 2026-10-01

**Kết quả tổ chức repository: hoàn tất; an toàn để tiếp tục Human Review Phase 0–2. Phase 3 HOLD / DEFERRED.** Không đóng Phase 2, không implement Auth, không thay đổi architecture hoặc business rules. Historical release verification còn FAIL đã có trước migration; không coi đây là release/signoff mới.

## Cấu trúc cũ → mới

Trước: `01_governance`, `02_product`, `03_research`, `04_architecture`, `05_code`, `06_quality`, `07_operations`, `08_handoff`, `99_archive`, workbook và `outputs` ở root.

```text
C:/Mingo/
  01_San_pham/        backend/, apps/learner/, apps/staff/, postgres/, compose.yaml
  02_Tai_lieu_du_an/  01_Tong_quan_du_an/, 02_Ke_hoach_phat_trien/, 03_Nghien_cuu/
                     04_Thiet_ke_san_pham/, 05_Kien_truc_he_thong/, 06_Quyet_dinh_da_chot/
                     07_Tien_do_du_an/, 08_Ban_giao/
  03_Kiem_thu/        Tu_dong/, QA_QC/, Bao_cao/, Bang_chung/, Gate/
  04_Van_hanh/        Trien_khai/, Cau_hinh/, Scripts/, Runbook/, tests/
  99_Luu_tru/        historical deliveries, superseded dated snapshot/original rules
  .github/          CI vẫn ở root
  README.md, START_HERE.md, PROJECT_MAP.md, REPO_RULES.md
```

| Old Path | New Path |
|---|---|
| `05_code` | `01_San_pham` |
| `02_product` | `02_Tai_lieu_du_an/04_Thiet_ke_san_pham` |
| `03_research` | `02_Tai_lieu_du_an/03_Nghien_cuu` |
| `04_architecture` | `02_Tai_lieu_du_an/05_Kien_truc_he_thong` |
| `08_handoff` | `02_Tai_lieu_du_an/08_Ban_giao` |
| `99_archive` | `99_Luu_tru` |
| `06_quality/evidence` | `03_Kiem_thu/Bang_chung` |
| `06_quality/gates` | `03_Kiem_thu/Gate` |
| `06_quality/standards` | `03_Kiem_thu/QA_QC/standards` |
| `06_quality/phase2` | `03_Kiem_thu/QA_QC/phase2` |
| `06_quality/README.md` | `03_Kiem_thu/README.md` |
| `07_operations/scripts` | `04_Van_hanh/Scripts` |
| `07_operations/tests` | `04_Van_hanh/tests` |
| `07_operations/requirements-v3_2.lock` | `04_Van_hanh/requirements-v3_2.lock` |
| `07_operations/README.md` | `04_Van_hanh/README.md` |
| `outputs` | `03_Kiem_thu/Bang_chung/outputs` |
| `Manage Project.xlsx` | `02_Tai_lieu_du_an/07_Tien_do_du_an/Quan_ly_du_an_Mingo.xlsx` |
| `01_governance/README.md` | `02_Tai_lieu_du_an/01_Tong_quan_du_an/README.md` |
| `01_governance/BACKLOG.md` | `02_Tai_lieu_du_an/02_Ke_hoach_phat_trien/BACKLOG.md` |
| `01_governance/IMPLEMENTATION_ROADMAP.md` | `02_Tai_lieu_du_an/02_Ke_hoach_phat_trien/IMPLEMENTATION_ROADMAP.md` |
| `01_governance/ROADMAP_PHASE_0_TO_17.md` | `02_Tai_lieu_du_an/02_Ke_hoach_phat_trien/ROADMAP_PHASE_0_TO_17.md` |
| `01_governance/CHANGE_REQUESTS.md` | `02_Tai_lieu_du_an/06_Quyet_dinh_da_chot/CHANGE_REQUESTS.md` |
| `01_governance/DECISION_REGISTER.md` | `02_Tai_lieu_du_an/06_Quyet_dinh_da_chot/DECISION_REGISTER.md` |
| `01_governance/IMPLEMENTATION_ISSUES.md` | `02_Tai_lieu_du_an/06_Quyet_dinh_da_chot/IMPLEMENTATION_ISSUES.md` |
| `01_governance/PHASE_STATUS.yaml` | `02_Tai_lieu_du_an/07_Tien_do_du_an/PHASE_STATUS.yaml` |
| `01_governance/PROJECT_MEMORY.md` | `02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_MEMORY.md` |
| `01_governance/PROJECT_PROGRESS_SNAPSHOT.md` | `02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_PROGRESS_SNAPSHOT.md` |
| `01_governance/PROJECT_STATE.md` | `02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_STATE.md` |
| `01_governance/PROJECT_PROGRESS_SNAPSHOT_PHASE2_CANDIDATE_20260927.md` | `99_Luu_tru/governance/PROJECT_PROGRESS_SNAPSHOT_PHASE2_CANDIDATE_20260927.md` |
| `01_governance/WORKING_RULES_ORIGINAL.md` | `99_Luu_tru/governance/WORKING_RULES_ORIGINAL.md` |
| `07_operations/docs/CI_CD.md` | `04_Van_hanh/Trien_khai/CI_CD.md` |
| `07_operations/docs/CONFIG_AND_SECRETS.md` | `04_Van_hanh/Cau_hinh/CONFIG_AND_SECRETS.md` |
| `07_operations/docs/DATABASE_BOOTSTRAP_AND_MIGRATIONS.md` | `04_Van_hanh/Runbook/DATABASE_BOOTSTRAP_AND_MIGRATIONS.md` |
| `07_operations/docs/ENVIRONMENTS.md` | `04_Van_hanh/Cau_hinh/ENVIRONMENTS.md` |
| `07_operations/docs/LOCAL_RUNTIME.md` | `04_Van_hanh/Runbook/LOCAL_RUNTIME.md` |
| `07_operations/docs/V3_2_VERIFICATION.md` | `04_Van_hanh/Runbook/V3_2_VERIFICATION.md` |
| `07_operations/docs/WINDOWS_FLUTTER.md` | `04_Van_hanh/Runbook/WINDOWS_FLUTTER.md` |

Git tracked count trước/sau: **780**. Initial draft counter 781 đã sửa vì một empty NUL sentinel của git ls-files; per-file inventory và hashes không đổi.

Mapping từng artifact (10.096 file, gồm các copied snapshots/exports chưa tracked) có trong [RESTRUCTURE_BASELINE.json](RESTRUCTURE_BASELINE.json); reasons/risks/decisions trong [plan](REPOSITORY_RESTRUCTURE_PLAN.md). Tracked paths di chuyển bằng `git mv`; workbook/outputs chưa tracked dùng native PowerShell `Move-Item`. Không copy-delete để migration. Safety copies tách riêng trong ignored `.local/restructure-20261001/before/` để bảo toàn working tree ban đầu.

## Giữ nguyên và bảo toàn

- Backend vẫn là một codebase FastAPI + durable worker + storage + migrations; không tách worker/database thành service mới. Flutter learner/staff và executable unit/integration tests giữ nguyên layout bên trong source tree.
- 31 backend/app files byte-identical với working tree đầu task. Trong 35 file tracked của cây runtime cũ, 34 giữ nguyên byte; chỉ README của source thay đường dẫn navigation. Compose, environment template và SQL bootstrap không đổi nội dung.
- UX prototype `app.js`, `index.html`, `styles.css` giữ nguyên byte so với đầu task. CSS đã dirty trước migration được bảo toàn, không tính là UX change của migration.
- 9.607 captured historical/evidence files byte-identical. Original intake/logs/audits/workbooks/package manifests/provenance không được regenerate. Các markdown packet final gate có path adaptation để dùng được sau move; captured JSON/log/input workbooks vẫn giữ nguyên byte.
- `Manage Project.xlsx` chuyển thành `Quan_ly_du_an_Mingo.xlsx`, byte-identical; không chỉnh worksheet, formula hay project status.
- `.git`, `.github`, `.idea`, `.local`, `.venv`, `.ruff_cache` giữ tại root. IDE/env/cache đã ignored. Không xóa môi trường, cache, runtime objects, snapshot hay evidence. Flutter build/.dart_tool caches có absolute paths cũ được giữ dưới `.local/restructure-20261001/flutter_generated_cache_before_fresh_build/` và tái tạo tại source mới. Containers cũ rỗng được giữ trong `.local/restructure-20261001/empty_original_directories/`, không xóa.
- `outputs` đã inspect: UX/report derivatives, diagnostics và copied snapshots. Chuyển nguyên byte vào `03_Kiem_thu/Bang_chung/outputs`, phân loại GENERATED / EVIDENCE; không promote derivative thành CURRENT.

Git local `core.longpaths=true` đã bật để đọc được copied snapshots sâu sau khi đổi parent folder trên Windows. Không thay đổi global Git config. Lần integrity check cuối đầu tiên phát hiện generated `05_code` rỗng do stale Flutter build metadata; thư mục rỗng được giữ local, cache được bảo toàn và rebuild từ paths mới. Không có project artifact bị kẹt không move được. Các local environment/IDE/Git directories giữ nguyên có chủ đích. Không tạo worker/database/Monitoring folders rỗng hoặc duplicate code để khớp proposal.

## V3.2

102 canonical original files + 3 provenance files: **SHA256 mismatch = 0**. Original manifest SHA256: `617245605096b3b9cc5f141dda352abc180d97f11738297949c3195711cc0e6d`.

Originals: `02_Tai_lieu_du_an/05_Kien_truc_he_thong/contracts/v3_2/source/`; index cho con người: `02_Tai_lieu_du_an/05_Kien_truc_he_thong/V3.2/`; provenance: `02_Tai_lieu_du_an/08_Ban_giao/provenance/v3_2/`. `.gitattributes -text` đã chuyển tới boundary mới trước move; `git check-attr text` xác nhận unset. Xem [V3_2_HASH_CHECK.json](V3_2_HASH_CHECK.json).

## References và verifier adaptation

[PATH_ADAPTATIONS.json](PATH_ADAPTATIONS.json) ghi before/after hashes và lý do cho 82 file sửa nội dung: đường dẫn, relative links, navigation và required verifier I/O/config. Không format hàng loạt source.

CI workflow, root ignore/attributes, PowerShell/shell/Python/JS entry points và docs links đã cập nhật. Adapter guard import dùng đúng `Scripts/` để hoạt động trên filesystem phân biệt hoa/thường. Split Python path components được điều chỉnh tới QA_QC/Bang_chung đúng chỗ.

`repository_paths.py` đọc captured old paths bằng migration mapping và chỉ chấp nhận captured digest khi current bytes trùng ledger đã ghi nhận. QC protected-file checks vẫn từ chối unrecorded content changes và mới tracked runtime files. Historical manifest dùng captured-path resolver, giữ nguyên checksum package cũ. Phase 2 verifiers có output directory/run mới để không ghi đè evidence cũ; ordered runner vẫn chạy P0 trước P1. Các thay đổi này chỉ phục vụ migration/provenance, không đổi assertion về UX/business.

Scan hiện hành: **0 legacy path dependency; 0 broken Markdown link** sau hoàn tất report. Captured originals/provenance/evidence/archive và audit before/mapping vẫn có old path có chủ đích. `verify_restructure.py` giữ danh sách tên cũ để phát hiện folder cũ tái xuất hiện; đây là migration assertion. Local-only scratch scripts/IDE/cache có thể chứa paths chụp trước move; không phải supported current entry point và không tự sửa dữ liệu local của owner.

## Verification thực sự đã chạy

| Command/group | Result | Evidence / scope |
|---|---|---|
| adapter_guards | PASS (exit 0) | 9 adapter guard tests PASS. |
| phase2_artifacts | PASS (exit 0) |  |
| phase2_rework | PASS (exit 0) |  |
| phase2_review | PASS (exit 0) |  |
| javascript_syntax | PASS (exit 0) |  |
| v3_2_original_suites | PASS (exit 0) | 115 original contract + 22 original PGlite SQL checks PASS on disposable copy; originals rechecked. |
| backend_verifier_postgres | PASS (exit 0) | ruff PASS; 9 unit tests PASS, 7 skipped in default run; 6 native PostgreSQL tests PASS separately; migration, worker enqueue/execute/health, HTTP live/ready 200, storage smoke PASS. Remaining skipped symlink case requires Windows privilege. |
| historical_release_manifest | FAIL (exit 1) | PRE-EXISTING FAIL: old Git-package manifest applied to dirty/non-package working tree. Before 145 checksum mismatches; after 144, no new checksum mismatch and no missing captured entry. Manifest bytes unchanged. Local Git/env/build/new evidence remain outside the old release scope. |
| flutter_verifier | PASS (exit 0) | Flutter 3.32.8: learner + staff pub get/analyze/widget test PASS; Android debug APK and staff Web builds PASS. |
| Fresh Flutter build after cache relocation | PASS | Learner pub get + Android debug APK, staff pub get + Web build PASS; generated old root không tái xuất hiện. Raw fresh_flutter_builds.json và logs trong evidence. |
| Ordered Phase 2 QA | PASS | 20 artifact review + 74 browser = 94 canonical cases; 30 supplemental checks; P0 trước P1; fresh contexts. |
| File preservation + organization manifest | PASS | 10.096 baseline artifacts đủ; current migration inventory hashes đúng; 105 V3.2/provenance hashes đúng; no protected changes. |
| Path / Markdown scan | PASS | 0 current old-path dependency, 0 broken current Markdown link; historical exceptions rõ phạm vi. |
| Python / JavaScript syntax | PASS | Current Python AST parse; node --check cho prototype + 2 browser tools. |
| PowerShell / shell syntax | PASS | 3 PowerShell parsers không lỗi; bash -n cho 3 shell scripts. |
| YAML parse | PASS | 7 YAML configs, gồm CI workflow/Compose/Flutter/PHASE_STATUS; PyYAML trong V3.2 verification environment. |
| Git diff checks | PASS | git diff --check và --cached --check không whitespace error; runtime/hash comparison không business logic change. |

Raw logs và fresh result files: [restructure evidence](../../../03_Kiem_thu/Bang_chung/restructure_20261001/). [verification_before.json](verification_before.json), [verification_after.json](verification_after.json), [browser_validation.json](browser_validation.json) lưu exit codes/commands; không gọi test chưa chạy là PASS.

### BLOCKED / NOT RUN

- Symlink escape unit case SKIPPED: Windows user thiếu symlink creation privilege (winerror 1314). 6 PostgreSQL cases skipped trong default unit run đã chạy riêng và PASS; symlink case là skip còn lại.
- Flutter device/browser integration boot tests không chạy lại; verifier đã analyze/test/build cả hai apps nhưng không chứng minh real-device boot. Không thay đổi trước/ sau về runtime acceptance cũ.
- GitHub-hosted Actions không dispatch/rerun trong task local này. CI paths/YAML/shell syntax đã kiểm tra; chưa claim hosted PASS cho migration.
- Docker Compose execution NOT RUN: không có Docker CLI trong environment. Compose YAML parse PASS; PostgreSQL/API/worker native verifier PASS.
- Interactive TalkBack/staff screen-reader speech, Linux-specific D021 retest, independent QA closure, Tech Lead và Product Owner acceptance NOT RUN trong organization task. Những pending gate requirements giữ nguyên; browser automation không thay human review.
- Historical release manifest FAIL trước và sau; không regenerate hoặc đổi business status để ép PASS. Organization manifest là checksum riêng cho preservation/migration inventory, không thay thế manifest release cũ và không phải Phase 2 acceptance.

## NEEDS_REVIEW / issue cần owner

1. **Status recency inconsistent:** PROJECT_MEMORY ngày 27/09 vẫn ghi READY FOR CODEX EXECUTION; PROJECT_STATE/snapshot và PHASE_STATUS cùng ngày ghi CODEX EXECUTED / READY FOR INDEPENDENT QA RETEST. Packet 30/09 ghi TECHNICAL RETEST PASS / GATE HOLD, D021 và D022 confirmation/retest pending. Handoff index còn câu “NOT EXECUTED” trong khi appended execution reports đã có. Không sửa semantic status; owner/role reviewers cần reconcile sau human review.
2. **Authority wording:** PROJECT_MEMORY dùng “canonical handoff”, PROJECT_STATE dùng current state, dated snapshot/package docs có stage khác nhau. Navigation mới ghi rõ ngày/phạm vi; không tự chọn một business state mới. Không tìm thấy file current riêng tên PACKAGE_STATUS; package wording nằm trong dated handoff docs.
3. **Release manifest scope:** manifest cũ nhận Git package bytes tại thời điểm bàn giao; working tree có newline conventions, prior edits và local/generated files. Khi owner thực sự authorizes release mới, cần tạo release-specific manifest riêng sau review; không phải task này.
4. **Generated outputs retained:** owner có thể quyết định snapshot/export nào còn cần dùng. Chưa chọn/xóa/archive thêm file không rõ authority; toàn bộ retained derivatives ở khu vực evidence, không CURRENT.

Không có quyết định Product Owner nào cần để hoàn tất việc tổ chức thư mục. Các quyết định trên thuộc status reconciliation/release hoặc Phase 2 gate; **Phase 3 vẫn HOLD**.

## Git và rollback guidance

Branch `main`, HEAD `a112f762ab08f6fa688cc4857b21d95d1055ab5c` giữ nguyên; chưa commit/push. `git mv` tạo staged renames; path/navigation edits và new indexes/evidence có thể còn unstaged/untracked. Existing user-dirty CSS và untracked final gate/workbook/outputs đã được ghi trước move và bảo toàn. Xem Git status/diff evidence trước khi commit, không stage toàn bộ local-generated outputs một cách mù quáng.

Rollback có chọn lọc:

1. Giữ bản sao các thay đổi mới sau migration trước khi rollback; so với baseline và ledger để tách thay đổi của owner.
2. Dùng đầy đủ inventory old→new trong baseline để inverse `git mv` tracked paths và native Move-Item untracked paths. Xử lý governance/archive rules theo từng file, tránh move container vào destination đang tồn tại.
3. Với path-adapted/navigation files, phục hồi byte từ `.local/restructure-20261001/before/<old path>` sau khi đã xem diff. Safety copy chứa cả CSS dirty tại thời điểm bắt đầu; Git HEAD không chứa bản này.
4. Cập nhật lại .gitattributes/.gitignore bằng safety bytes tương ứng và chạy lại original hashes/tests. Local `.venv`, `.local` và IDE folders chưa bị move nên không cần khôi phục.
5. Không dùng reset --hard/clean hoặc xóa historical/new evidence để rollback; chúng có thể mất thay đổi uncommitted của owner. Các artifacts migration có thể giữ lại làm lịch sử audit.

**Tiếp tục Human Review Phase 0–2: an toàn về organization, source paths và protected baseline. Phase 2 acceptance vẫn cần các reviewer/evidence đã quy định; không mở Phase 3.**
