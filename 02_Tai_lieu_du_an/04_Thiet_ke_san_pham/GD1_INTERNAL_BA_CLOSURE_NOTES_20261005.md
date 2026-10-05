# GĐ1 — Ghi chú chốt nghĩa nghiệp vụ và ranh giới bàn giao

Ngày 05/10/2026, Asia/Saigon. Phạm vi: tổng hợp nguyên tắc đã có trong V3.2, PRD và chỉ đạo PO ngày 04/10/2026. Đây là bổ sung an toàn về thuật ngữ/role intent/NFR/governance, không thay thế BA workbook đang **NOT FOUND**, không thêm API hoặc cấp quyền thực tế. GĐ1 internal gate chưa đạt. Customer validation remains **VALIDATION DEBT**.

GĐ1 trong yêu cầu là **Internal BA Baseline**. Engineering Phase1 trong repo là **Implementation Foundation**, đã có gate lịch sử riêng. Roadmap GĐ1–GĐ8 và Phase0–17 chưa có mapping được cung cấp; không đồng nhất hai hệ đánh số.

## Actor và role intent

Nguồn: V3.2 `docs/07_SECURITY_PERMISSION_V3.md`, PRD-14, J-S01/J-S02/J-S03/J-S06. RACI quản trị dự án không cấp quyền cho người dùng sản phẩm.

| Actor/role | Ranh giới nghiệp vụ đã có | Trạng thái/phạm vi |
|---|---|---|
| Learner | Học, xem dữ liệu enrollment/attempt/receipt/grant của chính mình; server xác thực ownership | ĐÃ CHỐT; learner core IN MVP, triển khai ở phase sau |
| Content Author | Tạo/sửa draft, chuẩn bị nguồn/giấy phép, preview, gửi review; không sửa bản published | ĐÃ CHỐT role intent; content operations IN MVP planned |
| Reviewer | Review draft, trả lại với lý do hoặc approve; lỗi nội dung/giấy phép chặn publication | ĐÃ CHỐT role intent; không mặc định có quyền xuất bản |
| Publisher/Operator | Xác nhận/publish nội dung đã đủ điều kiện; thay đổi published phải tạo revision mới | ĐÃ CHỐT role intent; không cấp quyền dữ liệu học viên/risk mặc định |
| Staff | Nhóm người dùng nội bộ; quyền cụ thể đến từ role và object scope, không từ nhãn Staff | ĐÃ CHỐT nguyên tắc; không phải quyền toàn hệ thống |
| Instructor/Advisor | Chỉ learner được phân công khi use case tương ứng được đưa vào scope | ĐÃ CHỐT object boundary; inclusion hiện tại ĐỂ GIAI ĐOẠN SAU/CHƯA QUYẾT ĐỊNH cho MVP |
| Admin | Thao tác đặc quyền có kiểm soát và audit theo V3.2; không lấy việc thấy UI làm authorization | ĐÃ CHỐT ranh giới; màn admin hiện FUTURE placeholder |
| Guardian | Không nằm trong adult learner baseline; cần child domain/privacy/safety review riêng | ĐỂ GIAI ĐOẠN SAU / FUTURE |
| Worker | System actor, least privilege theo job class; không phải project team role | ĐÃ CHỐT technical boundary |

V3.2 dùng nhóm `content admin`; các tên Author/Reviewer/Publisher diễn tả trách nhiệm trong flow, không tự tạo enum permission hoặc tách service. Một người có thể giữ bao nhiêu role, ai được tự review/publish và cách cấp/thu hồi role là **CHƯA QUYẾT ĐỊNH**. Không áp đặt separation-of-duties mới từ suy đoán.

## Glossary nghiệp vụ

| Thuật ngữ | Nghĩa dùng khi bàn giao |
|---|---|
| Lesson | Đơn vị nội dung có revision; có thể chứa nhiều activity. Không mặc định bằng một cycle hay attempt |
| Cycle | Vòng học hữu hạn có mục tiêu, feedback, điểm kết thúc và next step. Thời lượng là hypothesis |
| Session | Một lần tương tác có thể chứa/pause/resume cycle. Không đồng nhất session ID với attempt ID |
| Attempt | Một lần trả lời theo pinned activity revision. V3.2 finalized attempt bất biến; retry sau finalize dùng attempt ID mới |
| Check | Cơ hội độc lập có điều kiện rõ; trước trả lời không có hint. Không phải chứng nhận CEFR/mastery |
| First response | Câu trả lời đầu tiên giữ nguyên cùng assistance context. Không mặc định unaided |
| Assisted / unaided | Có hỗ trợ / không có hỗ trợ theo điều kiện quan sát; unknown context phải giữ unknown |
| Evidence | Quan sát có nguồn, điều kiện, revision và thời điểm khả dụng; exposure/click không tự thành learning evidence |
| Mastery | Khái niệm năng lực theo evidence; công thức/model cuối cùng deferred; không tự hiển thị % chính xác |
| Risk | Dự đoán cần hỗ trợ trong lớp intelligence khác mastery; là optional recommendation input |
| Recommendation | Decision có reason/policy/candidates/evidence; không đồng nhất Prediction/Exposure/Execution/Outcome |
| Revision | Phiên bản bất biến khi published. Attempt/enrollment pin đúng revision/release theo contract |
| Command | Đường duy nhất thay authoritative score/progress; receipt/state/outbox atomic, replay idempotent |
| Telemetry | Quan sát có thể thiếu/trễ/client-reported; không cấp completion, permission hay score |
| Sync | Reconciliation với receipt/canonical state. Network restored không đồng nghĩa synced |
| Progress | State server theo required completion credits của pinned release; completion != mastery |
| Event / knowledge / processing time | Occurrence, khả dụng trong capture/read view và xử lý là ba nghĩa khác nhau; timestamp đơn lẻ không thay exact source capture |

Nguồn chính: V3.2 docs/01–05, docs/09; Evidence Model; Learning Experience Model. Glossary này không sửa schema.

## Checklist NFR ở mức GĐ1

| Nhóm | Ràng buộc/bằng chứng phải bàn giao | Giới hạn verification hiện có |
|---|---|---|
| Reliability / failure recovery | Không mất command pending khi crash/retry; unknown commit outcome retry cùng ID/payload; có recovery state | Contract verified; durable mobile/domain runtime NOT EXECUTED |
| Offline / sync correctness | Queue command và telemetry tách; local/pending/syncing/ack/failure phân biệt; chống duplicate và rollback revision | V3.2 + UX states; fixture verification không chứng minh durability |
| Data integrity | Immutable published/attempt/receipt; pin exact revision; unique credit; transaction nguyên tử | Original SQL PGlite verified; native domain concurrency NOT EXECUTED |
| Performance | Đo trên environment/device/release scope thực; không gọi emulator là physical proof; không cắt câu trả lời bằng timer | Existing performance budget có phạm vi riêng; không đặt SLA mới trong audit |
| Accessibility | Semantic controls/focus/status, scalable text, reduced motion, audio availability/context; manual TalkBack riêng | Existing accessibility specs/tests; human/physical checks còn pending |
| Security | Server identity/role/object scope; không đưa secret/correct-key vào learner package; không coi visibility là permission | Contract verified; auth runtime Phase3 HOLD |
| Privacy | Purpose/minimization/access/TTL/deletion/export/audit; không thu dữ liệu tùy ý từ thiết bị | Register prepared; collection disabled; phê duyệt TTL/consent chưa hoàn tất |
| Auditability / observability | Reason/policy/evidence/revision/source boundary truy được; log tránh secrets; phân biệt receipt với availability | V3.2 lineage + foundation logs; domain observability implementation còn debt |
| Backup / restore | Replay independent deletion ledger trước mở dịch vụ; export/publish kiểm tra generation atomically | Contract có; production drill NOT EXECUTED, RPO/RTO CHƯA QUYẾT ĐỊNH |

Không tự đặt uptime/latency/retention SLA. Những tham số chưa có decision phải được track như điều kiện trước runtime/pilot/release tương ứng, không gọi implementation hoàn tất.

## Privacy/data governance intent

**EXTERNAL EVIDENCE:** Cổng văn bản Chính phủ ghi [Luật 91/2025/QH15](https://chinhphu.vn/?classid=1&docid=214590&pageid=27160) và [Nghị định 356/2025/NĐ-CP](https://vanban.chinhphu.vn/?docid=216387&pageid=27160&typegroupid=4), đều có hiệu lực **01/01/2026**. Đây là xác minh danh tính/ngày hiệu lực nguồn pháp lý được project record nêu, không chứng nhận tuân thủ hoặc tự suy ra legal TTL. Không dùng Nghị định13 làm current primary baseline; lịch sử nếu có phải ghi lịch sử.

| Purpose / nhóm dữ liệu | Collection | Access / use | Retention | Deletion/export / audit |
|---|---|---|---|---|
| Account/session/explicit preferences | Chỉ dữ liệu cần cho identity và preference đã phê duyệt; account lifecycle scope còn thiếu | Own learner + server scope; preference không là mastery evidence | Tham số CHƯA QUYẾT ĐỊNH trước collection/pilot | Scope CR-GD1-001; identity bảo vệ export/delete; request/status/failure phải được spec |
| Authoritative learning/attempt/progress | Command hợp lệ, pinned revisions và assistance context phù hợp versioned contract | Own learner; assigned advisor nếu approved; không mở raw risk cho content admin | Theo retention policy được owner/privacy review chốt; không giả định vô hạn | V3.2 generation gate, immutable history theo permitted period, ledger restore; audit source |
| Product telemetry | Chỉ purpose register; collection hiện DISABLED; không raw answer/audio/location/free text/advertising ID | Least privilege theo câu hỏi nghiên cứu; không thay score/progress | `RW` trong register là research window proposal, không legal TTL đã phê duyệt | Disable không chặn learner core; withdrawal/delete treatment và capture quality phải test trước thu |
| Content/license/provenance | Draft/source/creator/license/review/revision cần cho publication | Author/Reviewer/Publisher scope; published read-only | Chính sách lưu provenance/phiên bản chưa có số ngày, phải đủ trace trong phạm vi cho phép | Giữ revision liên quan attempts theo contract; access status độc lập hash; publication audit |
| Consented discovery/pilot records | Protocol chưa thực hiện; consent/contact tách mã participant và observation | Research organizer được phép; không đưa diary text vào telemetry | Trước recruitment phải phê duyệt retention/access/withdrawal | Không tự tạo transcript/participant; record withdrawal/redaction và giới hạn nghiên cứu |

Nguồn: V3.2 docs/07/docs/10, Learner Evidence Model §5, Telemetry Purpose Register, Initial Wedge Research Plan. Việc consolidation không hoàn tất account BA và không cho phép thu dữ liệu hoặc mở phase triển khai.

## Điểm còn thiếu để chốt BA

Actual BA workbook và snapshot04/10 chưa được cung cấp trong workspace. Account lifecycle MVP inclusion, state/trigger/acceptance và requirement priority vẫn **CHƯA QUYẾT ĐỊNH / UNKNOWN**. Các annex audit chỉ map nguồn đã có; không giả lập hàng BR/UC/RTM/WBS của workbook. Candidate CR cần owner disposition, không tự implement.
