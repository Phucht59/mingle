# Mingo — bàn giao Phase 1 và Phase 2 cho QA

Ngày đóng gói: 2026-10-02. Đây là gói review của working tree tại commit `a112f762ab08f6fa688cc4857b21d95d1055ab5c` trên nhánh `main`; chưa có commit, push hoặc triển khai sản xuất cho V2. Đọc [báo cáo gate](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PHASE2_FINAL_GATE_REPORT.md), [kết quả regression](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/REGRESSION_REPORT.md) và [checklist QA](01_CHECKLIST_QA.md) trước khi chạy thử.

## Tôi đã làm

1. Tổ chức repository thành năm khu vực dễ tìm: sản phẩm, tài liệu, kiểm thử, vận hành và lưu trữ. Giữ backend API/worker/migrations trong một modular monolith; cập nhật link, CI và scripts. Các file local, lịch sử và evidence được giữ nguyên.
2. Revalidate Phase 1: kiểm tra backend FastAPI, worker, PostgreSQL, storage, Flutter foundation và V3.2. Backend business logic, schema và V3.2 không được thay đổi.
3. Làm lại presentation Phase 2 theo hướng Mingo “Quiet Exploration”: Flutter learner/staff, 61 màn hình/175 trạng thái, Vocabulary–Grammar–Listening, hành trình Review → Learn → Retrieve → Transfer → Check → Summary, onboarding tùy chọn, tiến độ dựa trên bằng chứng và staff workflow theo nhiệm vụ. UI ghi rõ **“Bản xem trước · dữ liệu mẫu”**. Mascot capybara, Inter, sample audio có provenance; các protocol usability/diary mới là kế hoạch.
4. Thêm unit/widget/navigation/responsive/semantics/golden tests, kiểm tra trên Android emulator và compiled Chrome; sửa system Back của learner và drawer staff 600px. Cập nhật traceability, báo cáo, status và bộ ảnh. [Mở gallery 195 ảnh](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/SCREENSHOT_GALLERY.html).

## Trạng thái và số liệu đã chạy

| Phạm vi | Kết quả | Bằng chứng |
|---|---|---|
| Phase 1 | DONE; regression PASS | [Báo cáo](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PHASE1_REVALIDATION_REPORT.md), [log](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/phase1_revalidation_pwsh.log) |
| Backend | Ruff PASS; 9 unit PASS/7 skip trong lượt không PostgreSQL; 6 native PostgreSQL PASS; API/worker/storage PASS | [Log Phase 1](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/phase1_revalidation_pwsh.log) |
| V3.2 | 115/115 contracts, 22/22 SQL PASS; 105 file gốc/provenance byte-identical | [Báo cáo](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/V3_2_INTEGRITY_REPORT.md), [log](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/v3_2_after.log) |
| Flutter V2 | 227/227 PASS, 195/195 captures PASS, 3.600 kiểm tra ma trận | [Machine log](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/flutter_sealed_final.jsonl), [traceability](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/SCREEN_STATE_TRACEABILITY.csv) |
| Build/runtime | Hai app analyze/widget/build PASS; Android 2/2; compiled Chrome 7/7 | [App log](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/flutter_sealed_apps.log), [Android](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/android_review_final.log), [Chrome](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/web_runtime_sealed_final/run.json) |
| Preservation | 141 protected, 9.607 historical/evidence: mismatch 0; 10.096 artifact trước migration còn đủ | [Verifier](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/v2_verification.json) |
| Phase 2 gate | **TECHNICALLY COMPLETE / HUMAN GATE PENDING / NOT PASSED** | [Gate](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PHASE2_FINAL_GATE_REPORT.md) |
| Phase 3 | **HOLD; chưa bắt đầu** | [Gate](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PHASE2_FINAL_GATE_REPORT.md) |

## QA cần kiểm tra tiếp

- Review thật trên [APK Android](03_BUILD/learner_debug.apk) và hai Web build trong `03_BUILD/`; kiểm tra luồng, nội dung, 320px/200%, focus và TalkBack. Build là debug/preview với dữ liệu mẫu, không phải bản sản xuất.
- D021: V2 có bốn ca 320px/200% PASS, nhưng finding Linux R1 cần independent disposition. D022: hai workbook giữ nguyên hash; cần kiểm tra hiển thị workbook và xác nhận độc lập. Xem [D021/D022](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/D021_D022_RECONCILIATION.md).
- R1 browser 74/74 và supplemental 30/30 PASS; R1 review **19/20**, QC-002 FAIL do seal hash của Flutter cũ; verifier organization-only cũng FAIL phạm vi cũ. Hai lỗi lịch sử này được giữ nguyên, không được tính là V2 PASS. Xem [báo cáo regression](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/REGRESSION_REPORT.md).
- Hosted CI của V2, Linux/iOS/macOS, âm thanh trên thiết bị vật lý, actual TalkBack/screen-reader, usability study và diary pilot **NOT RUN**. Product Owner, Tech Lead, content reviewer và independent QA chưa ký. QA ghi kết quả mới, không sửa log cũ hoặc tự đóng gate.

## Cấu trúc gói

`01_CHECKLIST_QA.md` là danh sách test thủ công; `03_BUILD/` có APK và Web builds; `04_SOURCE/` là lát cắt source/docs/evidence theo đúng cấu trúc repository, gồm 195 ảnh và các log; `MANIFEST_SHA256.txt` liệt kê mọi file kèm hash. `04_SOURCE` không chứa `.git`, môi trường local, secrets, cache hay toàn bộ kho lịch sử. Verifier tổng 10.096 artifact cần chạy trong repository đầy đủ.

Để mở Web build đã giải nén, chạy `python -m http.server 8765 --directory 03_BUILD/learner_web` và lệnh tương tự trên cổng 8766 cho `03_BUILD/staff_web`. Trên máy có Flutter 3.32.8, source và dependencies, chạy `flutter pub get`, `flutter analyze`, `flutter test` trong `04_SOURCE/01_San_pham/cong_cu_phat_trien/mingo_ui`. Xem [developer handoff](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/DEVELOPER_HANDOFF_V2.md) cho các giới hạn của fixture. Ghi tester, OS/device, SHA của build, bước tái hiện, expected/actual, ảnh/log và quyết định PASS/FAIL/PENDING cho từng ca.
