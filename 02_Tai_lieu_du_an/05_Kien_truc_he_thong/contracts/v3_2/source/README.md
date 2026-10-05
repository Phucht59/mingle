# Adaptive Language Learning — Baseline V3.2 hoàn thiện

**Kết luận: 9/10 ở mức kiến trúc và hợp đồng; GO để triển khai vertical slice.**
Đây là bản sửa trực tiếp từ V3 do người dùng gửi. Không cần chuyển đi thêm một vòng review kiến trúc chung. Gói này chứa đặc tả, schema/API, SQL lõi tham chiếu, validators và fixtures có thể kiểm tra; chưa phải ứng dụng Flutter/FastAPI hoàn chỉnh hoặc model đã huấn luyện.

**Đã chạy: 115 kiểm tra hợp đồng + 22 kiểm tra SQL, tất cả PASS.**
Xem `FINALIZATION_REPORT_VI.md`, `VALIDATION_REPORT.txt`, `validation_results.json` và `SQL_VALIDATION_REPORT.json`. SQL được chạy bằng PGlite/PostgreSQL WebAssembly: kiểm chứng constraints/triggers/rollback, không chứng minh native multi-connection concurrency.

## Bắt đầu đọc

1. `FINALIZATION_REPORT_VI.md` — lỗi đã xác minh, sửa đổi, điểm số và giới hạn kiểm chứng.
2. `docs/01_MASTER_BASELINE_V3.md` — kiến trúc và ownership.
3. `docs/14_SUBMIT_ALGORITHM.md` — thuật toán submit nguyên tử, retry, scope và completion.
4. `docs/02_MVP_INVARIANTS.md` đến `docs/10_RETENTION_DELETE_RESTORE_V3.md` — các hợp đồng chi tiết.
5. `contracts/openapi_vertical_slice_v1.yaml`, `schemas/`, `contracts/core_ddl_postgresql.sql` — căn cứ triển khai.
6. `docs/15_OPERATIONS_AND_DELIVERY.md` — vận hành, retention, tải, khôi phục, thứ tự triển khai.
7. `IMPLEMENTATION_HANDOFF_PROMPT.md` — prompt bàn giao làm code, không phải prompt review tiếp.

## Phạm vi đã chốt

- Flutter Android cho learner pilot; Flutter Web cho staff/admin; FastAPI; PostgreSQL; object storage; modular monolith với API và durable worker cùng codebase.
- Nội dung thử nghiệm English A1; `mcq_single_v1` và `listening_mcq_v1`; bài có 1–100 câu, mỗi câu chọn một option và phải trả lời đủ.
- Chấm điểm deterministic ở server. Completion = nộp hợp lệ và được chấm đủ, không phải mastery/pass.
- Một credit cho một activity bắt buộc trong enrollment; làm lại dùng attempt ID mới. Activity không bắt buộc không tăng tiến độ bắt buộc.
- Nội dung/revision bất biến; release status và download grant tách riêng. Offline mặc định học 7 ngày, nhận submission thêm 48 giờ, theo grant/account/package; đây là cấu hình pilot.
- Receipt lịch sử và delivery status tách biệt; duplicate của rejected cũng được xử lý đúng. Tiến độ có scope enrollment/release, không rollback từ revision cũ.
- SourceCapture ghi tập dữ liệu thật sự nhìn thấy trong read view; replay dùng tập đã ghi, không giả tạo lịch sử bằng lọc timestamp hiện tại.
- Risk tắt trong slice đầu; curriculum/mastery/risk label và thuật toán ML tiếp tục ở giai đoạn Learning Intelligence.

## Chạy lại kiểm tra trên Windows PowerShell

Yêu cầu Python 3.12 và Node.js/npm. Các dependency dưới đây phục vụ kiểm tra gói, không phải stack runtime cuối của ứng dụng.

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe validators\run_checks.py
npm.cmd ci
npm.cmd run test:sql
```

Không cần activate PowerShell script. `npm.cmd` tránh lỗi chặn `npm.ps1`. Lệnh kiểm tra ghi lại báo cáo và trả exit code khác 0 nếu có lỗi. Chạy từ thư mục chứa README này.

Linux/macOS tương đương:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python validators/run_checks.py
npm ci
npm run test:sql
```

## Những file mẫu cần hiểu đúng

- `artifacts/activity_content.json` là bài mẫu có nội dung render được.
- `artifacts/server_only/scoring_key.json` là đáp án chỉ phía server; không đưa vào package người học.
- Descriptor package/release và resource hashes tính từ dữ liệu/file thật trong gói.
- Model, preprocessing, target/horizon và validation dưới `artifacts/` là fixtures được ghi rõ `fixture_only`. Chúng không phải weights/nhãn nghiên cứu đã được chốt; gate chặn đưa chúng vào shadow/production.
- `review/SECOND_SUPERVISOR_REVIEW_SOURCE.md` là lịch sử review V2, không phải đặc tả hiện hành.

## Cổng còn phải thực hiện khi có ứng dụng

Native PostgreSQL concurrency; auth/JWT/RLS; Flutter offline trên thiết bị; mất mạng/unknown commit; worker/deletion race tích hợp; benchmark và backup/restore. Phần ML cần dữ liệu/nhãn/evaluation và quyền phê duyệt registry thực. Đây là công việc triển khai và nghiệm thu phần mềm, không phải lý do để viết lại baseline hoặc tiếp tục chấm điểm tài liệu vòng quanh.
