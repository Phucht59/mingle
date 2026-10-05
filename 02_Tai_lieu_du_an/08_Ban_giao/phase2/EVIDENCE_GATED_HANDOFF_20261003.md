# Bàn giao QA —Phase1/Phase2, candidate ngày2026-10-03

**Phase2 đang HUMAN/DEVICE GATE PENDING; Phase3 HOLD.** Bản này dùng dữ liệu mẫu. QA kiểm tra giao diện/luồng/ranh giới và các kết quả kỹ thuật, không ghi nhận nó là auth/scoring/offline/ML thật.

Đọc [báo cáo A–S](../../04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PHASE2_FINAL_GATE_REPORT.md), [trạng thái hiện hành](../../07_Tien_do_du_an/PROJECT_STATE.md), [protocol kiểm tra độc lập](../../04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/INDEPENDENT_VERIFICATION_PROTOCOL.md), [checklist accessibility người thật](../../04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/ACCESSIBILITY_MANUAL_CHECKLIST.md), rồi mở [gallery205ảnh](../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/SCREENSHOT_GALLERY.html).

Gói hiện hành: [Mingo_QA_Phase1_Phase2_EvidenceGate_2026-10-03.zip](../../../03_Kiem_thu/QA_QC/QA_Handoff_Phase1_2_20261003/Mingo_QA_Phase1_Phase2_EvidenceGate_2026-10-03.zip). README_QA.md bên trong mô tả source, APK/AAB/Web và cách đọc raw evidence; manifest kiểm tra từng file. ZIP cũ ngày02/10 giữ nguyên để đối chiếu lịch sử.

- Phase1:9unitPASS/7skip;6nativePGPASS;Ruff,migration,worker/heartbeat,API200/200,storagePASS. V3.2original115contracts+22SQLPASS;102sourcefileshash0mismatch.
- Phase2:275sharedtestsPASS,205goldencomparisons,3840responsiveobservations;5IVchallengePASS; mỗiapp1widgettest;7Webruntime;2Androidboot/audioinit. Tất cả là kiểm tra thực đã chạy, không phải chữ ký QA độc lập.
- Đã sửa composition learner, guard xác nhận mẫu staff và transient decode kích thước0. Đã chuẩn bị mô hình học, nghiên cứu/metrics/telemetry-purpose/discovery/pilot/readback,performancebudget/harness.
- Performance đã đo11window vànormalprofile/release5cold+5warm. EmulatorSwiftShader60Hz vượt framebudget;90/120Hz/physicaltiers/TalkBack/battery/thermal vẫnchưađo. Hero/mascotencodedassets vượt mục tiêu riêng,uniqueposes chưa đủ; không ghiPASS các mục này.
- PO cần duyệt visual/coreloop/readback;contentreviewer đánhgiácontent/license;humanQA xácnhậncriticalcases;tester chạyhardware/TalkBack. D021Linux/D022workbookvisual độc lập vẫnPENDING.

QA ghi tester/ngày/buildSHA/device/OS,case/expected/actual,evidence,severity vàretetst. Ưu tiên coreloop→firstresponse/assistance/Check→nextstep;staffsource/review/confirmation;recommendationoutage;AndroidBack;200%/dark;offline/errorfixtures. Source snapshot trước rework và sealed ZIP cũ hỗ trợ rollback chọn lọc trong checkout cô lập; không reset/xóa workingtree của user. Không bắt đầu Phase3.
