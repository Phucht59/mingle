# Review lần 2 — Baseline V2 / manifest v2.1

Ngày: 15/09/2026. Đầu vào: `ADAPTIVE_LANGUAGE_LEARNING_SYSTEM_BASELINE_V2_FINAL_REVIEW(1).zip`.

Đã kiểm tra toàn bộ 50 entry. Bản review nguồn bên trong giống từng byte với báo cáo review lần 1. Đây là review tài liệu và hợp đồng dữ liệu, không phải kiểm thử ứng dụng đã triển khai. Các sửa đổi dưới đây là đề xuất cụ thể cho vòng hoàn thiện tiếp theo; gói V2 đầu vào chưa bị sửa.

## A. Verdict

**8/10 — GO WITH CONDITIONS. Có thể bắt đầu triển khai vertical slice: YES, theo điều kiện dưới đây.**

V2 đã tiến bộ thực chất: chọn scope kỹ thuật hẹp, tách command/telemetry, bổ sung transaction/outbox, quyền cấp đối tượng, content pinning, availability time và recommendation không bắt buộc có risk. Giữ Flutter + FastAPI + PostgreSQL + object storage và modular monolith.

Nhưng chưa đồng ý với `00_SUPERVISOR_FIX_MATRIX.md` rằng cả B1–B7 đã “CLOSED AT SPEC LEVEL”, hoặc trạng thái `spec-complete` trong manifest. Những câu như “if product rules allow”, “if appropriate”, “according to explicit ordering” vẫn để trống quyết định có ảnh hưởng trực tiếp đến dữ liệu. Một số schema còn không biểu diễn được trường mà chính tài liệu bắt buộc.

**Cách hiểu YES:** có thể mở repo, migration, client cache và xây slice theo từng bước. Đóng C1–C3 dưới đây trong PR hợp đồng đầu tiên, trước khi cố định migration/API nộp bài và đồng bộ. Chưa cho phép coi slice dùng dữ liệu thật là sẵn sàng nghiệm thu. C4–C5 được đóng ở cổng analytics/ML tương ứng, không bắt hoàn thành model trước khi làm nền tảng.

Điểm số đánh giá chất lượng đặc tả, không phải phần trăm hoàn thành hoặc cam kết hệ thống chạy đúng.

## B. Trạng thái B1–B7

| Vấn đề cũ | Trạng thái review lần 2 | Phần còn thiếu | Phải sửa trước phần lõi vertical slice? |
|---|---|---|---|
| B1 — command, transaction, ownership | PARTIALLY CLOSED | Ownership và transaction boundary đã rõ; thiếu completion/scoring invariants, concurrent retry, same attempt/new command, receipt semantics | Có — C1/C2 |
| B2 — offline | PARTIALLY CLOSED | Có queue và scope; thiếu download grant contract, thời hạn nhận lệnh/retry, trạng thái nội dung và đường lấy canonical result | Có — C2/C3 |
| B3 — trust/object authorization | CLOSED AT SPEC LEVEL | Token identity, backend writes, role + assignment đã rõ. Còn phải triển khai/test và biểu diễn trong OpenAPI | Không mở lại kiến trúc; kiểm thử trước real data |
| B4 — content versioning | PARTIALLY CLOSED | Nguyên tắc pinning/rescore đã rõ; manifest chưa biểu diễn đầy đủ release, grant và content graph; thiếu cách xử lý completion khi revoke | Có với schema content/download — C1/C3 |
| B5 — late data/replay | PARTIALLY CLOSED | Đã phân biệt thời gian; source manifest/watermark còn tùy chọn, availability/ordering chưa có cơ chế cụ thể | Trước source metadata/summary; ML replay chi tiết trước analytics — C4 |
| B6 — risk optional/recommendation lifecycle | CLOSED AT SPEC LEVEL đối với lỗi coupling ban đầu | Pipeline không cần risk và tách decision/exposure/execution/outcome đã rõ. Audit schema còn thiếu nhưng không phủ nhận việc sửa coupling | Không chặn slice lõi; sửa trước recommendation release |
| B7 — feature/model contract | PARTIALLY CLOSED | Prose khá đủ; schema thiếu conditional required, range/window/preprocess fields, unique order, rollout validation và ví dụ liên kết nhất quán | Không chặn slice lõi; có trước inference — C5 |

Hai nhóm đã đóng lỗi gốc ở mức thiết kế; năm nhóm đóng một phần. Không có nhóm nào được xác nhận runtime-closed khi chưa có code và kết quả kiểm thử.

## C. Defects có thể gây sai dữ liệu hoặc làm hợp đồng nền tảng không tương thích

### C1 — Chưa định nghĩa đầy đủ completion và tính duy nhất dưới concurrency

**Nguồn:** `04` phần canonical progress; `05` mục 3–4; `06` mục 7; `20`; `contracts/scoring_contract_v1.json`; `schemas/submit_attempt_command.schema.json`.

**Mức độ:** High; chặn việc cố định schema và nghiệp vụ submit.

Scoring contract chỉ có đúng=1, sai=0. Chưa xác định activity có một hay nhiều câu, phải trả lời đủ hay không, điểm tổng/max, hoàn thành có cần đạt điểm hay chỉ cần nộp hợp lệ. README gọi activity là single-choice question nhưng submit example chứa hai question revisions. Không có định nghĩa mẫu số `eligible_activity_count` hoặc giới hạn completion credit.

Một lần làm lại có thể tạo attempt mới hợp lệ, nhưng không được tăng số activity hoàn thành lần thứ hai. Transaction nguyên tử không tự đảm bảo invariant này. Hai command khác nhau cùng `attempt_id`, hai request đồng thời cùng command, hoặc hai thiết bị đồng thời hoàn thành cùng activity đều chưa có kết quả được chốt. Câu “create/update attempt exactly once” không chỉ rõ finalized attempt có được thay đáp án không.

**Bản sửa đề xuất cho technical pilot, không phải quy tắc mastery:**

1. Activity có danh sách câu hỏi bất biến; mỗi câu đúng một option hợp lệ. Server đối chiếu tập question revision IDs, cấm trùng/ngoài activity, yêu cầu đủ câu trong pilot. Nếu muốn hỗ trợ unanswered phải định nghĩa riêng trước khi bật.
2. `raw_score=sum(points)`; `max_score=question_count`; activity có ít nhất một câu. `completion` nghĩa đã nộp hợp lệ và đã chấm xong; không đồng nghĩa mastery hoặc pass. Chọn nghĩa này như quy tắc thử nghiệm kỹ thuật, ghi thành `completion_policy_v1`.
3. `completed_activity_count` đếm activity được credit duy nhất theo enrollment + release activity; cùng activity làm nhiều lần chỉ credit một lần. Mẫu số là tập activity bắt buộc trong release được ghim; tài liệu cần có field để biểu diễn tập này. Trường hợp tập rỗng phải xác định hoặc cấm publish.
4. Finalized attempt bất biến. Same attempt ID + different command ID trả `ATTEMPT_ALREADY_FINALIZED`, không update answers. Muốn làm lại tạo attempt ID mới; rescore đi workflow riêng.
5. Quy định unique constraint cho `(learner_id, command_id)`, ownership/identity attempt và completion credit. Check-then-insert phải có unique conflict handling; serialize progress update bằng row lock hoặc CAS phù hợp. Không chỉ nêu “verify ID” trước insert.
6. Payload digest theo canonicalization có version; chốt cách xử lý null/omitted, thứ tự answers và trường bị loại khỏi digest. JSON khác whitespace/key order không được tự thành lệnh khác.

**Test đóng issue:** 20 request đồng thời cùng command → một result; hai command khác nhau cùng attempt → không overwrite; hai thiết bị cùng activity → hai attempts nhưng một completion credit; bài thiếu/trùng/sai option bị từ chối; repeat attempt không làm completion_fraction vượt 1.

### C2 — Receipt, duplicate và batch reconciliation chưa có cùng semantics

**Nguồn:** `05` mục 4–5, `06` mục 5, `13` mục 4, schemas `command_receipt` và `sync_batch_response`.

**Mức độ:** High; chặn API contract giữa Flutter và backend.

- Tài liệu vừa yêu cầu trả receipt nguyên gốc, vừa đổi status từ accepted sang duplicate. Chưa tách trạng thái nghiệp vụ đã lưu và kết quả vận chuyển lần retry.
- Receipt bắt buộc `committed_at` cho cả `retryable`, dù failure trước commit không có authoritative commit. `if appropriate` chưa xác định validation failure nào lưu terminal receipt.
- Batch item accepted/duplicate không bắt buộc có receipt hoặc result. Chỉ `canonical_state_version` không đủ lấy điểm/attempt/progress; chưa có receipt lookup endpoint bù lại.
- Receipt nguyên gốc có thể chứa progress revision 5 trong khi thiết bị đã có revision 7. Chưa có quy tắc client không được rollback về 5 khi nhận duplicate cũ.
- Unknown commit outcome không đồng nghĩa transaction chắc chắn rollback. Mô tả 503 “before authoritative commit” không bao phủ mất kết nối DB đúng lúc commit.

**Bản sửa đề xuất:**

- Receipt persisted có terminal outcome `accepted|rejected`, ID, command digest, version và typed canonical result. Transport item có `accepted|duplicate|rejected|retryable|conflict` và nhúng receipt khi đã có terminal outcome. Duplicate không sửa receipt cũ.
- Retryable/conflict không bị bắt buộc có successful commit time. Tên timestamp và ý nghĩa phải đúng với cách thu thập; thời điểm ghi trong transaction không tự là thời điểm commit chính xác.
- Terminal rejected chỉ áp dụng validation nghiệp vụ xác định sau xác thực; auth failure/temporary dependency error không khóa command thành permanent failure. Chốt reason-code catalog và cách retry khi sửa payload: command mới, không đổi payload trên command ID cũ.
- Accepted/duplicate bắt buộc có typed receipt, hoặc bắt buộc receipt ID cùng endpoint lookup đã xác định. Per-item transaction độc lập; lỗi một item không rollback item đã commit.
- Flutter chỉ áp dụng canonical progress nếu revision mới hơn local canonical revision; duplicate cũ vẫn được dùng để đóng queue item.
- Mất xác nhận commit → retry cùng command ID. Không hứa chắc “chưa có tác động” khi outcome chưa biết.
- Xác thực account và quyền đọc receipt trước; với lệnh đã commit, trả lịch sử hợp lệ của chính account trước khi áp điều kiện content mới cho một lệnh mới. Hard revoke không biến command đã accepted thành chưa từng tồn tại.

**Test đóng issue:** response accepted có canonical result; retry sau revoke/expiry của command đã commit vẫn reconcile được theo quyền hiện tại; duplicate revision cũ không rollback UI; unknown commit outcome không tạo command mới; temporary failure không bị cache vĩnh viễn.

### C3 — Offline authorization chưa có contract; release manifest trộn dữ liệu bất biến với trạng thái thay đổi

**Nguồn:** `03`, `06` mục 1/8, `08`, `13` content flow, `schemas/course_release_manifest.schema.json`, submit schema.

**Mức độ:** High; chặn offline download và submit acceptance.

Tài liệu có hạn offline 7 ngày “from package issue”, nhưng schema release chỉ có `published_at`, không có package ID, issued/expiry hay account grant. Submit command cũng không tham chiếu grant. Chưa có bản ghi/hợp đồng nào cho server phân biệt người thật sự tải package được phép và người tự khai occurred_at cũ.

Manifest release bất biến lại có `status` published/retired/revoked có thể đổi. Hash nằm trong chính object nhưng chưa xác định bytes/fields được hash. Activities chỉ có ID/revision/scoring và mảng media checksums không gắn asset ID; thiếu lesson/question references và nội dung render hoặc đường resolve có version. Chỉ thêm expiry vào release manifest cũng không đúng vì mỗi lượt download có thời gian cấp riêng.

**Bản sửa đề xuất:**

1. Tách **ContentReleaseManifest** bất biến, **ReleaseAccessStatus** có version thay đổi được và **OfflineDownloadGrant** theo account/enrollment/package.
2. Grant gồm package ID, learner/enrollment owner server-side, release hash, issued_at, learn_until, upload_until và policy version; server giữ record đối chiếu. Submit offline có grant reference. Online submit có mode/contract riêng để không giả vờ đã tải package.
3. Định nghĩa thời hạn học và hạn server nhận submission tách nhau. Nếu giữ learn_until 7 ngày, có thể đề xuất grace upload 48 giờ, nhưng phải đánh dấu đây là cấu hình đề xuất, chưa được chủ dự án chốt. Retry command đã được ghi receipt đi theo idempotency policy, không bị mất vì hết hạn upload.
4. occurred_at từ client không phải bằng chứng chống giả mạo thời gian. Pilot practice có thể chấp nhận clock uncertainty trong giới hạn grant + server upload deadline, gắn quality; không sử dụng như bằng chứng kỳ thi có thời hạn nghiêm ngặt.
5. Bảng quyết định rõ published/retired/soft/hard × grant hợp lệ/hết hạn × command mới/đã commit. Bỏ chữ “may accept” nếu hai implementation cần cùng hành vi. Chốt tiến độ xử lý activity bị hard revoke: giữ lịch sử, ngừng nộp mới, migration/supersession theo policy; không tự đổi mẫu số ngầm.
6. Hard revoke có hiệu lực server khi biết trạng thái; thiết bị đang offline không thể nhận revoke tức thì. Chặn khi reconnect/cập nhật status và ở thời hạn grant. Không mô tả như có thể thu hồi nội dung trên thiết bị mất mạng ngay lập tức.
7. Hash trên canonical manifest content, loại trường digest ra khỏi dữ liệu được hash; access status/grant nằm ngoài content hash. Media entry có asset ID, revision/hash, size và quyền resolve/download. Có full typed content hoặc resolvable immutable references cho unit/lesson/activity/questions/options.

**Test đóng issue:** cùng release hai account có grant riêng; đổi status không đổi content hash; hard revoke chặn command mới nhưng không xóa receipt cũ; submit ngoài grant không được cấp credit mới; package corruption/thiếu assets bị phát hiện; sync đến muộn có kết quả xác định.

### C4 — Availability và source snapshot vẫn chưa đủ tái hiện serving

**Nguồn:** `09` mục 1/3, `10` mục 8, `11` mục 3, `21` mục 5, `schemas/feature_snapshot_manifest.schema.json`.

**Mức độ:** High đối với ML validity; không chặn giao diện bài học. Cần chuẩn bị source revisions ngay lúc xây dữ liệu.

Schema cho phép `replayability_status=replayable` nhưng không có source manifest hoặc watermark. Watermark chỉ là string chưa định nghĩa; latest ordering liệt kê ba trường nhưng chưa xác định ưu tiên/cách so sánh computation versions hoặc nhánh serving/research. Timestamp đơn lẻ không biểu diễn được chính xác tập dữ liệu đã nhìn thấy.

`available_at` được mô tả “normally transaction commit time” nhưng chưa có cách thu thập. Trong PostgreSQL `CURRENT_TIMESTAMP`/`now()` là thời điểm bắt đầu transaction; `clock_timestamp()` là thời điểm gọi hàm, không tự biến thành commit timestamp. Vì vậy không gán `DEFAULT now()` rồi tuyên bố đã giải quyết point-in-time. [PostgreSQL date/time functions](https://www.postgresql.org/docs/current/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT).

**Bản sửa tối thiểu:** feature builder đọc một consistent DB snapshot, lưu tập source evidence IDs/revisions hoặc manifest tham chiếu chính xác tập đó và immutable payload/hash; source capture identity bắt buộc khi claim replayable. Mutable profile/progress cũng cần snapshot/revision tương ứng. Định nghĩa `available_at` thực tế, chấp nhận là logical analytical publication time nếu dùng cơ chế publish batch được ghi bền vững; không ngụy tạo commit time. Với nhiều truy vấn nguồn, chọn isolation hoặc source capture bảo đảm cùng view; PostgreSQL Repeatable Read cho các SELECT trong transaction nhìn cùng snapshot. [PostgreSQL transaction isolation](https://www.postgresql.org/docs/current/transaction-iso.html).

Latest pointer đề xuất phân scope `(learner/enrollment, summary_kind, computation_version, serving_mode)`; trong scope dùng numeric revision được cấp theo quy tắc publish có concurrency control. Active computation version đổi bằng config/rollout riêng, không so sánh chuỗi `v2` với `v10`. Chốt liệu hai source manifests có thể so sánh thứ tự hay phải cùng scope/watermark semantics.

**Test bổ sung:** transaction bắt đầu 09:59 nhưng commit 10:01 không xuất hiện trong replay 10:00; builder đọc nhiều query trong lúc có commit mới vẫn nhất quán; snapshot tự nhận replayable mà thiếu source lineage bị từ chối; research restatement không ghi đè latest serving; version v10 không bị xếp trước v2 bằng string sort.

### C5 — ML/schema contract chưa ràng buộc những trạng thái đã cam kết

**Nguồn:** `11`, feature/model/prediction schemas và examples.

**Mức độ:** High ở cổng ML; không chặn slice chưa bật risk.

Kiểm thử trực tiếp cho thấy schema nhận prediction `available` thiếu toàn bộ probability/model/threshold; nhận `model_unavailable` nhưng probability=0. Nó cũng nhận model production với runtime rỗng và target placeholder. Feature schema nhận trùng name/position, đồng thời từ chối field `valid_range` mà prose yêu cầu. Feature còn thiếu nơi biểu diễn time window/preprocessing reference; prediction không có model hash/bundle reference bất biến đủ rõ.

**Sửa:** conditional schemas cho available/nonavailable; available phải có đủ tham chiếu và numeric outputs, nonavailable không được mang fake prediction. Model deployment gate resolve mọi registry reference thành artifact immutable, xác minh hashes/runtime, target/horizon đã hoàn chỉnh và validation record; không bắt placeholder example đạt production gate. Feature definition bổ sung range/window/preprocess metadata hoặc reference đến typed immutable contract. Service validator kiểm tra names/positions duy nhất, contiguous/order, dimension/mask/missingness, label/margin/entropy và compatibility; JSON Schema không thay thế kiểm tra cross-record.

Hai example dùng cùng `model_version=hybrid_candidate_v1` nhưng model bundle có target/horizon TBD, prediction có example_target/example_horizon khác. Nếu là hai ví dụ độc lập phải dùng model identity khác hoặc ghi rõ fixture độc lập; nếu là ví dụ end-to-end thì sửa để khớp. Threshold/margin/entropy đã được sửa đúng so với lần 1.

**Test đóng issue:** available thiếu p bị từ chối; unavailable có p=0 bị từ chối; model production chưa resolve target/runtime/artifact bị chặn; feature names/positions trùng bị từ chối; prediction/bundle khác target/horizon bị từ chối.

## D. High-priority nhưng không chặn bắt đầu slice lõi

1. **Worker fencing và outbox relay:** unique key cho `(outbox_message_id, handler_version/type)` hoặc semantics tương đương; lease token/generation và conditional completion để worker hết lease không hoàn tất job của worker mới. Test crash giữa tạo job/đánh dấu outbox, lease hết hạn khi worker cũ vẫn chạy. “Handler idempotent” cần chỉ ra effect key cho từng handler, nhất là delete/export.
2. **Deletion chống race/restore:** tombstone bền vững ngoài điểm backup có thể restore lùi hoặc có nguồn replay độc lập. Chỉ lưu tombstone trong DB rồi restore về trước lúc xóa có thể làm mất tombstone. Job đang chạy phải recheck deletion generation trước khi publish; export được tạo sau purge cũng phải bị ngăn và cleanup.
3. **Recommendation audit:** `12` yêu cầu evidence refs nhưng schema không cho field này; candidate-set reference tùy chọn. Thêm evidence/candidate lineage trước recommendation release. Một exposure có thể đi cả `/exposures` và telemetry; quy định chung exposure ID/dedup để không đếm đôi. Outcome nên gắn decision dù chưa có execution, và schema metric/window/cutoff/eligibility phải đủ đánh giá.
4. **Pilot SLO:** đã có targets và load envelope, không còn claim DB “đã tối ưu”. Cần xác định test duration, mix read/submit/event, DB volume tương ứng retention và percentile scope. RPO 15 phút phải có backup/PITR capability và restore drill thực tế; “nếu provider hỗ trợ” chưa chứng minh đạt mục tiêu.
5. **Queue deletion UX:** rejected/conflict có thể terminal về vận chuyển nhưng bài chưa được cứu. Giữ local result/tombstone đến khi người dùng đã được báo và có recovery path; không xóa bài chỉ vì status terminal.
6. **Telemetry context:** envelope + payload catalog đã tốt hơn. Cần event-specific context validation và ownership/revision binding cho media, hint, exposure; payload schema đơn lẻ không thể chứng minh media thuộc lesson được quyền dùng.

## E. Over-engineering / under-design

Không cần thêm service, Kafka, Redis, warehouse, feature store hay Kubernetes. API và durable worker cùng codebase hợp lý với scope hiện tại. Có thể chưa xây staff dashboard hoàn chỉnh, recommendation hoặc registry UI trong slice đầu.

Thiếu chủ yếu là invariant và protocol, không phải công nghệ. Không nên tăng số file chỉ để ghi lại “must be idempotent” hoặc “explicit ordering”; cần một định nghĩa authoritative, có schema/test tham chiếu được. Published content nên giữ kiến trúc đơn giản, không xây cả nền tảng CMS tổng quát trước pilot.

Scope Android, English A1, hai activity types và synchronous scoring đủ hẹp để thực hiện. English A1 là cấu hình nội dung thử nghiệm; chưa là chứng nhận chuẩn CEFR hoặc chốt thuật toán sư phạm. Giữ việc phân tích curriculum/mastery/risk label ở giai đoạn riêng như đã thống nhất.

## F. Contract consistency audit và bằng chứng kiểm tra

### F1. Validation đã thực hiện

| Kiểm tra | Kết quả |
|---|---|
| ZIP CRC | PASS, 50 entries |
| Manifest bytes + SHA-256 | PASS, 49/49 file được liệt kê; manifest không tự hash |
| JSON parse | PASS, 23 JSON |
| JSON Schema Draft 2020-12 meta-validation | PASS, 16/16 schemas |
| 4 examples đối chiếu schema tương ứng, bật FormatChecker | PASS, 4/4 |
| Semantic/adversarial probes | 12 trường hợp bên dưới cho thấy contract gaps |
| YAML parse/OpenAPI inspection | Parse được; chỉ là excerpt chưa đủ binding cho implementation |
| Source ứng dụng/SQL/load/security runtime | Chưa có để kiểm thử |

Validator: Python `jsonschema 4.26.0`, `Draft202012Validator` + `FormatChecker`; YAML đọc bằng PyYAML. Khác lần review 1, lần này đã chạy schema validator thành công.

PASS meta-validation chỉ có nghĩa schema hợp lệ theo meta-schema. PASS example chỉ chứng minh example thỏa schema hiện tại. Không suy ra dữ liệu nghiệp vụ hợp lệ. Các probe sau kiểm tra ranh giới schema; không khẳng định backend chưa tồn tại sẽ chấp nhận chúng.

| Probe | Schema hiện tại | Ý nghĩa |
|---|---|---|
| Prediction available thiếu probability | ACCEPTED | Thiếu conditional required |
| Model unavailable nhưng p=0 | ACCEPTED | Thiếu ràng buộc nonavailable |
| Accepted receipt thiếu attempt/score/progress | ACCEPTED | Không đủ canonical result |
| Accepted batch item thiếu receipt | ACCEPTED | Có thể không reconcile được |
| Trùng question ID, answer object/null cho MCQ | ACCEPTED | Cần typed scoring + business validator |
| Production bundle runtime rỗng/target TBD | ACCEPTED | Cần release validator ngoài shape check |
| Replayable snapshot thiếu manifest/watermark | ACCEPTED | Thiếu lineage requirement |
| Recommendation thêm `evidence_refs` | REJECTED | Prose yêu cầu nhưng schema cấm field |
| Feature list trùng tên/vị trí | ACCEPTED | Cần semantic validator |
| Feature thêm `valid_range` | REJECTED | Prose yêu cầu nhưng schema cấm field |
| Course release activities rỗng | ACCEPTED | Publish validator/rule chưa chốt |
| Manifest thêm issued_at/expires_at | REJECTED | Không có schema download grant riêng |

**Mẫu tái hiện tối thiểu:** object dưới đây qua `prediction_snapshot.schema.json`, dù không có xác suất hoặc model.

```json
{
  "prediction_id": "p",
  "status": "available",
  "feature_snapshot_id": "f",
  "generated_at": "2026-09-15T10:00:00Z",
  "as_of_at": "2026-09-15T10:00:00Z"
}
```

### F2. Những chỗ khác cần thống nhất

| Vị trí | Mâu thuẫn/thiếu | Sửa |
|---|---|---|
| `05`, receipt schema | Stored receipt nguyên gốc nhưng duplicate status thay đổi; retryable bắt có committed_at | Tách receipt và transport outcome — C2 |
| `08`, manifest schema | Immutable content nhưng mutable status trong object hash | Tách content/status/grant — C3 |
| `11`, feature schema | Prose có range/window/preprocess; schema cấm thêm | Bổ sung typed fields/reference |
| `12`, recommendation schema | Evidence refs required theo prose nhưng field không tồn tại | Thêm field và validation |
| `04` ERD vs outcome schema | ERD buộc prediction cho decision và execution cho outcome; schema cho null/không execution | Sửa cardinality, nối decision→outcome |
| `04` ERD | `RELEASE_ACTIVITY` không nối `ACTIVITY_REVISION`, USER→ENROLLMENT lặp, unit/lesson chưa biểu diễn | Hoàn thiện logical relations trước physical schema |
| `21` | Latest ordering liệt kê trường nhưng không định nghĩa thứ tự/version scope | Chốt ordering/publish CAS — C4 |
| `20` vs `05` | SUBMITTED→REJECTED không rõ persisted attempt hay command rejected trước khi tạo attempt | Phân biệt transaction nội bộ và trạng thái đã commit |
| `00`/MANIFEST | Tất cả closed/spec-complete | Đổi theo bảng B; không đồng nhất schema validation với closure |

`contracts/openapi_contract_excerpt.yaml` thiếu requestBody/schema bindings, auth scheme, response bodies và response definitions cho hai batch operations. File đã tự gọi là excerpt, nên không coi thiếu phần đó là bằng chứng API thực tế không có auth hay tự kết luận file invalid. Nhưng chưa thể dùng nó làm hợp đồng generate client/backend tương thích. Hoàn thiện các operation thuộc slice, không cần toàn bộ sản phẩm. [OpenAPI 3.1.0 — Operation Object](https://spec.openapis.org/oas/v3.1.0.html#operation-object).

Phân tách 401/403/404 theo chính sách auth và privacy; 422 cho payload/content validation. Hiện excerpt gộp unauthorized enrollment vào 422 chưa phản ánh permission matrix. Xác định malformed whole batch, item-level validation, 429/backoff, 503/unknown commit và lookup result.

## G. Freeze recommendation

| LOCK | CONFIGURE có version | DEFER |
|---|---|---|
| Flutter/FastAPI/PostgreSQL/object storage; modular monolith | Offline horizon + upload grace sau khi semantics C3 đã chốt | Full curriculum, taxonomy, mastery/adaptive path |
| Android pilot, deterministic MCQ/listening MCQ | Media quota, batch limits, retry/lease durations | Speaking/writing scoring |
| Server identity, object authorization, backend business writes | Retention, SLO, connection pools và provider | Risk target/label đến trước dataset/training |
| Command tách telemetry, atomic state/receipt/outbox | Completion/scoring policy revision sau baseline kỹ thuật đầu | Hybrid/ranker production đến sau đánh giá |
| Immutable content/attempt history, explicit rescore | Active model/threshold/calibration/policy | Causal personalization và hạ tầng scale chưa cần |
| Mastery tách risk; risk optional | Active computation version, freshness | iOS public pilot và multi-institution |

Chưa freeze tên/shape hiện tại của receipt, grant/manifest, prediction và feature schemas. Sau patch contract có thể freeze v1 public protocol; thay đổi semantics sau đó dùng version mới. Chưa cần freeze provider Supabase khi đang là candidate, nhưng cần chọn auth/DB capabilities trước tích hợp và restore gate.

## H. Implementation start checklist và patch order

### PR 1 — Hợp đồng đủ đóng cho phần lõi

- [ ] Chốt C1: question set, scoring total/max, completion meaning, denominator, repeat attempts và invariants.
- [ ] Chốt C2: canonicalization, uniqueness/concurrency, typed receipt, transport status, unknown commit, anti-rollback client.
- [ ] Chốt C3: immutable content manifest, mutable access status, account download grant và hạn sync/retry.
- [ ] OpenAPI cho release/grant, submit, command batch, telemetry batch và canonical result lookup nếu dùng.
- [ ] ERD/DDL cùng thể hiện ownership, FK/revision constraints, completion credit và command identity.
- [ ] Sửa fix matrix về trạng thái thật; xác định schema vs semantic validator chịu trách nhiệm mỗi invariant.

### PR 2 — Vertical slice triển khai và kiểm tra

- [ ] Download → local durable command → offline submit → server score/progress → receipt → queue reconciliation.
- [ ] Thử response loss và concurrent submissions; command cũ không bị recreate sau retry.
- [ ] Thử cross-account/instructor scope; grant owner và revision membership được kiểm tra.
- [ ] Thử published/retired/soft/hard revoke, expiry/grace và command đã commit.
- [ ] Outbox/worker có unique effect và lease ownership; summary source revision đủ audit.
- [ ] Không dùng passed schema validation thay cho các integration tests này.

### Trước analytics/ML/recommendation/pilot

- [ ] C4 source capture/availability/latest ordering; long transaction và multi-query snapshot tests.
- [ ] C5 feature/model/prediction validators; examples end-to-end nhất quán.
- [ ] Recommendation audit/exposure/outcome schema; no risk và model outage vẫn hoạt động.
- [ ] Delete/restore race, RPO/RTO, retention và mixed load tests đạt mục tiêu hoặc có correction trước release.
- [ ] Target/horizon/cohort/censoring/split được chốt đúng cổng, không ép làm sớm trong slice đầu.

**Phạm vi vòng sửa tiếp theo:** tập trung C1–C3, hoàn thiện machine-readable contracts và bổ sung các test phản ví dụ. Giữ roadmap sư phạm/ML theo cổng hiện có. Không cần viết lại toàn bộ kiến trúc hoặc bổ sung công nghệ mới để xử lý những khoảng trống này.
