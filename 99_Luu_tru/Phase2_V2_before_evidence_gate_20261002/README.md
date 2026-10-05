# Mingo — Adaptive Language Learning & Early Intervention Platform

Nền tảng học ngôn ngữ thích ứng và hỗ trợ can thiệp sớm, phát triển từ KLTN của Trần Hoàng Phúc thành sản phẩm thực tế.

**Bắt đầu tại [START_HERE.md](START_HERE.md).** Source code nằm ngay trong [01_San_pham](01_San_pham/); tài liệu, nghiên cứu và UX/UI nằm trong [02_Tai_lieu_du_an](02_Tai_lieu_du_an/).

```text
01_San_pham/         backend, Flutter learner/staff, local stack
02_Tai_lieu_du_an/   tổng quan, kế hoạch, research, UX/UI, kiến trúc, tiến độ, bàn giao
03_Kiem_thu/         QA/QC, gate, bằng chứng và chỉ dẫn chạy test
04_Van_hanh/         cấu hình, runbook, scripts, triển khai
99_Luu_tru/          lịch sử, snapshot và tài liệu đã thay thế
```

Stack freeze: Flutter Android-first learner, Flutter Web staff/admin, FastAPI/Python, PostgreSQL và Object Storage. API và durable worker dùng chung modular monolith; server quyết định scoring, progress và permission. [V3.2](02_Tai_lieu_du_an/05_Kien_truc_he_thong/V3.2/) là architecture/contract authority.

Phase0 và Phase1 DONE; Phase1 regression PASS. Phase2 V2 **TECHNICALLY COMPLETE / HUMAN GATE PENDING**, gate chưa PASSED. **Phase3 HOLD**. Xem [trạng thái hiện hành](02_Tai_lieu_du_an/07_Tien_do_du_an/PROJECT_STATE.md) và [báo cáo final gate V2](02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PHASE2_FINAL_GATE_REPORT.md). Flutter hiện dùng dữ liệu mẫu để review; domain/auth/offline/ML implementation thuộc phase sau.

- [Chạy backend, database và Flutter](04_Van_hanh/Runbook/PHASE1_FOUNDATION.md)
- [Chạy API/worker và client](04_Van_hanh/Runbook/LOCAL_RUNTIME.md)
- [Kiểm tra bộ V3.2 gốc](04_Van_hanh/Runbook/V3_2_VERIFICATION.md)
- [Sơ đồ repository](PROJECT_MAP.md) · [Quy tắc làm việc](REPO_RULES.md)
- [Hồ sơ tái cấu trúc và verification](02_Tai_lieu_du_an/07_Tien_do_du_an/Tai_cau_truc_20261001/)
