# Bản đồ repository Mingo

| Khu vực | Nội dung | Phân loại |
|---|---|---|
| [01_San_pham](01_San_pham/) | Source chạy được, local stack và tests cùng source | CURRENT |
| [02_Tai_lieu_du_an](02_Tai_lieu_du_an/) | Tài liệu con người cần đọc | CURRENT / nguồn nghiên cứu có ngữ cảnh lịch sử |
| [03_Kiem_thu](03_Kiem_thu/) | QA controls, gate, báo cáo và bằng chứng | CURRENT / EVIDENCE |
| [04_Van_hanh](04_Van_hanh/) | Runbook, cấu hình, scripts và triển khai | CURRENT |
| [99_Luu_tru](99_Luu_tru/) | Package cũ, snapshot và tài liệu đã thay thế | HISTORICAL |

```text
01_San_pham/
  backend/src/all_foundation/   API, worker, storage, migrations/
  backend/tests/               Python unit/integration tests
  apps/learner/                Flutter learner, test/, integration_test/
  apps/staff/                  Flutter staff web, test/, integration_test/
  postgres/init/               local PostgreSQL test-database bootstrap
  compose.yaml, .env.example   local stack và template cấu hình

02_Tai_lieu_du_an/
  01_Tong_quan_du_an/          giới thiệu và hướng dẫn đọc
  02_Ke_hoach_phat_trien/      backlog và roadmap
  03_Nghien_cuu/              research Phase 1 và legacy KLTN
  04_Thiet_ke_san_pham/        charter, PRD, learning design, ux_ui/phase2/
  05_Kien_truc_he_thong/       V3.2/ index, contracts/v3_2/source/ nguyên bản
  06_Quyet_dinh_da_chot/       decision register, CR và implementation issues
  07_Tien_do_du_an/           state, memory, phase status, workbook quản lý
  08_Ban_giao/                handoff hiện hành và provenance có ngày/revision

03_Kiem_thu/
  Tu_dong/                    chỉ dẫn chạy tests/verifiers, không nhân bản tests
  QA_QC/standards/            tiêu chuẩn QA và Definition of Done
  QA_QC/phase2/               suite, QA control, reports, audits, evidence, final_gate
  Bao_cao/                   index báo cáo theo phase/run
  Bang_chung/                 Phase 1 runtime/CI evidence và outputs/ đã chụp
  Gate/                      gate nền tảng Phase 1

04_Van_hanh/
  Trien_khai/                CI/CD
  Cau_hinh/                 môi trường và secrets guidance
  Scripts/                  bootstrap và verification tools
  tests/                    adapter guard tests gắn với scripts
  Runbook/                  local runtime, database, Flutter, V3.2
```

Worker và migrations ở chung backend; việc tổ chức thư mục không tách service hoặc đổi code architecture. Baseline DDL là contract trong V3.2; runtime migrations nằm tại `01_San_pham/backend/src/all_foundation/migrations/`.

`CURRENT` chỉ authority trong phạm vi của tài liệu. `HISTORICAL` và `EVIDENCE` giữ nguyên ngày/revision đã chụp. `Bang_chung/outputs/` chứa derivative/generated exports và bản copy để review, không phải source hiện hành. Manifest bàn giao cũ giữ checksum của package cũ. Baseline và mapping migration nằm trong [hồ sơ tái cấu trúc](02_Tai_lieu_du_an/07_Tien_do_du_an/Tai_cau_truc_20261001/).

Root giữ `.github`, `.git`, `.gitignore`, `.gitattributes` và bốn entry docs. `.idea`, `.local`, `.venv` là LOCAL ONLY; `.ruff_cache` là GENERATED. Các môi trường/cache này vẫn ở nguyên chỗ và được Git ignore.

Current Phase2 UI: `01_San_pham/cong_cu_phat_trien/mingo_ui/` shares tokens/components/fixtures/assets/tests for both Flutter apps. Current UX/research/handoff: [V2](02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/README.md); current machine evidence: `03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/`. R1 pre-rework authored source and governance snapshots: `99_Luu_tru/Phase2_R1_before_rebaseline_20261001/`. Historical QA packets retain their dates and hashes.
