# Kết quả kiểm tra và hoàn thiện trực tiếp V3 → V3.2

Ngày 15/09/2026. Đầu vào: `ADAPTIVE_LANGUAGE_LEARNING_SYSTEM_BASELINE_V3_FINAL_REVIEW(1).zip`.

**Điểm sau sửa: 9/10 cho baseline kiến trúc/hợp đồng. Quyết định: GO để triển khai phần lõi.** Không chấm 10/10 hoặc gọi production-ready khi chưa có ứng dụng, dữ liệu/model và kiểm thử vận hành. Điểm số là nhận định chuyên môn; bằng chứng chính là các thay đổi và kết quả kiểm tra bên dưới.

## V3 có “PASS” đáng tin đến đâu?

Đã đối chiếu 66 entry đầu vào, xác minh SHA-256/kích thước của 65 file trong manifest. Gói không bị hỏng. Nhưng báo cáo 41 PASS chỉ bao phủ tập kiểm tra hẹp, không chứng minh hết những điều README/fix matrix tuyên bố.

Tái hiện trực tiếp trên validator V3:

| Thay đổi đầu vào | Validator cũ | Sau sửa |
|---|---|---|
| p=0.73, threshold=0.6 nhưng label=false | Cho qua | Từ chối |
| Thay model_bundle_sha256 bằng 64 số 0 | Cho qua | Từ chối |
| Đẩy candidate sang production với runtime `2.x-pinned-at-build` | Cho qua | Từ chối |
| Feature array bị đảo thứ tự nhưng tập position vẫn liên tục | Chưa kiểm tra array order | Từ chối |
| So sánh deadline theo chuỗi thay vì instant múi giờ | Có thể so sánh sai | Parse timezone và so sánh instant |
| Hash JSON bằng sort_keys thay vì JCS thật | Không đồng nhất RFC8785 cho mọi dữ liệu | Dùng rfc8785 và test số/Unicode |

Những kết quả này chứng minh validator bỏ lọt lỗi. Không có bằng chứng để kết luận AI trước cố ý gian lận. Cách xử lý là sửa điều kiện kiểm tra và chạy phản ví dụ, không tin nhãn PASS tự viết.

## Những thay đổi đã thực hiện

### 1. Submit, scoring và tiến độ

- Cấm dùng expected_state_version khác null cho submit độc lập; CAS nằm phía server.
- Có nội dung MCQ mẫu thật và đáp án server-only; validate đủ câu, đúng option, đúng scoring revision.
- Làm rõ activity không bắt buộc không tạo required credit. SQL chặn cấp nhầm credit và chặn counter lệch khỏi credit rows.
- Bổ sung FK nhiều cột giữa learner/enrollment/release/activity/attempt/answers/scoring; chặn gắn bài làm vào sai scope.
- Deferred constraints kiểm tra accepted receipt phải có attempt, đủ answers, score đúng, required credit và outbox trước COMMIT. Có test rollback khi thiếu từng phần.
- Có trigger chống UPDATE lịch sử attempt, answer, score, receipt và credit; rescore phải tạo revision mới. Xóa tài khoản vẫn là workflow đặc quyền có audit, không bị tuyên bố “không thể xóa”.

### 2. Receipt và đồng bộ

- Tách receipt terminal khỏi delivery. Duplicate của một rejected receipt không bị ép thành thành công hoặc ép có progress.
- Accepted receipt phải có canonical result typed; tiến độ mang enrollment/release identity để compare revisions đúng scope.
- Bổ sung per-item denied không tạo business receipt, batch shape/unique IDs/limits và response-loss semantics.
- Typed response cho submit lỗi, telemetry batch, receipt lookup; có state refetch và content/package/resource endpoints.
- Viết thuật toán transaction rõ ràng ở `docs/14`: per-learner serialization, current auth/object checks, idempotency trước deadline cho command đã commit, deferred receipt FK và unknown commit retry.

### 3. Offline và nội dung

- Command offline bind grant, package, installation; grant account/session được kiểm tra phía server.
- Chốt thứ tự hard revoke → grant revoke → upload expiry, ranh giới thời gian và soft revoke không còn câu “tùy policy khác”.
- Grant issuance có request ID idempotent để mất response không tự gia hạn học.
- Có package schema, content-resource reference, resource hash/size, nội dung render và đúng bộ fixtures liên kết nhau.
- Không gửi answer key trong package learner; kết quả offline là pending đến khi server chấm.

### 4. Dữ liệu lịch sử và ML

- Chỉ ra và sửa điểm còn thiếu của publication timestamp: transaction publication cũng có thể commit sau timestamp ghi trong nó.
- Serving SourceCapture gắn actual read view và exact membership; replay dùng capture gốc. Không dựng lại visibility cũ bằng việc query data hiện tại với cutoff cũ.
- Hash capture/evidence/payload/bundle được tính thật và cross-check; không còn các chuỗi aaaa/bbbb giả làm bằng chứng end-to-end.
- Model/target/horizon/preprocess vẫn là fixtures minh bạch. Gate kiểm tra registry được tin cậy, hash file thật, runtime exact, non-fixture target/horizon và validation cho đúng stage; sample model bị chặn triển khai.
- Bổ sung label/margin/entropy/version checks, feature array order, dtype/range/mask/length và snapshot-owner/hash consistency.

### 5. Worker, deletion và vận hành

- Fencing phải bảo vệ effect write và job completion trong cùng transaction; không chỉ bảo vệ dòng status cuối.
- Có effect key cho timer job không có outbox ID.
- Deletion và publish dùng chung subject gate lock; đọc generation hai lần mà không khóa chưa đủ.
- Khôi phục lại retention matrix, budget, SLO/RPO/RTO và runbook từ hướng baseline trước, ghi rõ là targets chưa đo.
- Thay prompt review tiếp bằng prompt triển khai; bỏ bytecode/cache khỏi deliverable.

## Bằng chứng đã chạy

| Nhóm | Kết quả | Phạm vi |
|---|---|---|
| Python contract suite | 115 PASS, 0 FAIL | Meta-schema, examples, semantic/cross-record, JCS, negative cases, OpenAPI references, SQL parse |
| SQL execution suite | 22 PASS, 0 FAIL | PostgreSQL 18.3 qua PGlite 0.5.8; FK/check/trigger/rollback/immutability/effect key/fencing condition |
| Artifact hashes | Tính từ JSON/file thật | JCS cho contract JSON, raw bytes cho content resources; fixture status rõ |
| Flutter/FastAPI runtime | Chưa triển khai | Không nằm trong ZIP đầu vào và không được giả nhận đã test |
| Native multi-connection concurrency/auth/load/restore | Chưa chạy | Cổng nghiệm thu bắt buộc lúc triển khai |
| Model khoa học | Chưa có | Không suy ra độ chính xác từ schema hoặc fixture |

Test SQL không hạ điều kiện khi gặp lỗi: hai fixture ban đầu đụng unique receipt trước khi tới FK mục tiêu đã được tách ID để thực sự kiểm tra FK; assertion vẫn đòi đúng lỗi khóa ngoại. Kết quả 22 PASS là lần chạy trên fixtures đã cô lập đúng invariant.

## Mức đóng C1–C5

| Nhóm | Sau hoàn thiện |
|---|---|
| C1 — scoring/completion/concurrency contract | Đã chốt hành vi, có SQL/validator và kiểm tra constraints; concurrency của handler thật phải nghiệm thu |
| C2 — receipt/sync | Đã đồng bộ schema/API/algorithm, gồm rejected duplicate và unknown commit |
| C3 — offline/content | Đã chốt grant/package/status/resource contracts và fixture liên kết; thiết bị thật phải nghiệm thu |
| C4 — source capture | Đã sửa semantics visibility/replay và kiểm tra hash/lineage; MVCC capture pipeline thật là cổng analytics |
| C5 — ML | Đã sửa các ràng buộc/negative cases/gate; không có production model trong gói |

Được freeze v1.1 protocol trước triển khai ban đầu; đây là thay đổi pre-release từ V3 candidate, chưa có installed client cần migration. Tên file `_v1` vẫn chỉ major version của contract family; release baseline là 3.2.0 và OpenAPI 1.1.0. Thay đổi semantics sau khi có client thực phải có compatibility policy/version mới.

## Việc triển khai kế tiếp

Làm một slice: **authorized release/grant → download → offline answers → submit/retry → canonical score/progress → outbox/worker → summary**. Dùng thuật toán và contracts trong gói; kiểm thử native PostgreSQL đồng thời và Flutter trên thiết bị. Chưa cần model, mastery hoặc giáo trình đầy đủ. Không cần thêm vòng review kiến trúc chung trước khi bắt đầu.

## Tài liệu kỹ thuật đối chiếu

JCS quy định biểu diễn số và thứ tự khóa ổn định, không tương đương đơn thuần sort_keys: [RFC 8785](https://www.rfc-editor.org/rfc/rfc8785).

PostgreSQL isolation quyết định read view nhìn thấy dữ liệu nào; replay cần bảo tồn capture gốc: [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html).

PGlite chạy PostgreSQL qua WebAssembly, phù hợp kiểm tra SQL cục bộ nhưng không thay môi trường server nhiều kết nối: [PGlite documentation](https://pglite.dev/docs/).
