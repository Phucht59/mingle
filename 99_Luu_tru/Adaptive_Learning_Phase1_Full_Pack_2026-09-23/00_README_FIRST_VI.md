# Phase 1 — bộ tổng hợp từ đầu, 23/09/2026

**Đây là toàn bộ hồ sơ + source + bằng chứng hiện có. Phase 1 vẫn ACTIVE, gate NOT PASSED.**

## Đã làm

1. Giữ lại research Q1–Q18 và toàn bộ lịch sử handoff.
2. Giữ 5 product specs đã được owner review; không nghiên cứu lại, không đổi V3.2.
3. Tạo repo mới: FastAPI, worker durable, SQL migrations, local object adapter, Flutter learner/staff source, Docker/Compose, test harness và CI YAML.
4. Kiểm chứng backend: 10 tests pass; API boot bằng Uvicorn và HTTP thật; storage smoke; setup venv mới. 6 tests PostgreSQL chưa chạy, không tính pass.
5. Cập nhật PROJECT_MEMORY, PROJECT_STATE, snapshot, issues, backlog và gate theo bằng chứng.

## Cách đọc nhanh

- `source/docs/PROJECT_STATE.md`: trạng thái hiện tại.
- `source/evidence/VERIFICATION_REPORT.md`: từng check đã chạy/chưa chạy và giới hạn.
- `source/docs/PROJECT_MEMORY.md`: bộ nhớ để tiếp tục ở phiên khác.
- `source/README.md`: hướng dẫn source/setup.
- `history/continuous_handoff/03_PHASE1_SCIENTIFIC_RESEARCH_RESOLUTION.md`: research đã hoàn thành.
- `history/`: tài liệu và ZIP cũ để truy nguồn; trạng thái cũ không ghi đè trạng thái hiện tại.
- `01_FILE_INDEX.md`: danh mục đầy đủ.
- `MANIFEST_SHA256.json`: checksum của mọi file (trừ chính manifest).

## Chưa thể chốt DONE

Thiếu V3.2 gốc và bộ kiểm tra 115+22; PostgreSQL/worker chưa chạy thành công; Flutter bị auto-review chặn vì SDK liên hệ endpoint metadata cloud; CI chưa chạy trên runner; chưa có clean setup toàn stack. Không bypass chặn đó và không tạo CR khi chưa có conflict thật.

Flutter mới có Dart/pubspec/test và script sinh platform host từ SDK đã pin; chưa có Android/Web build, pub lock hoặc device boot. Local storage smoke không phải bằng chứng S3 production. Backend fresh venv không phải toàn bộ môi trường production.

## Dùng repo

Có thể làm việc trực tiếp trong `source/`. Nếu cần repo Git đầy đủ với commit gốc:

```sh
git clone Adaptive_Learning_Phase1_Source.bundle adaptive-learning
```

Không kèm SDK, virtualenv, build cache hoặc secrets. Dependency lock Python được kèm; Flutter dependency resolution còn pending. Phase 2 chưa được formally enter.
