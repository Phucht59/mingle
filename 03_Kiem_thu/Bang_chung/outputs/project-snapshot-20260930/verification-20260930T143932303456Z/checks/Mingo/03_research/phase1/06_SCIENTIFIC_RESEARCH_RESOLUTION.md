# Adaptive Language Learning — Phase 1 Scientific Resolution

**Bản đề xuất để owner duyệt · 23/09/2026 · Trạng thái: research complete, implementation chưa được phê duyệt**

## 1. Executive conclusion

**Methodology đề xuất:** curriculum có mục tiêu và điều kiện tiên quyết; mỗi chu kỳ hữu hạn khoảng 5 phút tạo cơ hội ôn giãn cách, tiếp nhận nội dung mới có hướng dẫn, tự truy hồi, dùng ở ngữ cảnh khác và kiểm tra; hệ thống lưu *đúng điều đã quan sát* từ từng lần thử, chọn nội dung tiếp theo bằng quy tắc minh bạch. Sau này mới hiệu chỉnh mô hình mastery/risk/path bằng dữ liệu sản phẩm và đánh giá độc lập. Bằng chứng tốt nhất hỗ trợ retrieval, spacing và feedback có thông tin, nhưng không chứng minh rằng tỷ lệ 5 vai trò hoặc độ dài 5 phút là tối ưu [S1–S3].

Các quyết định đã chấp nhận vẫn phù hợp: năm vai trò Review–Learn–Retrieve–Transfer–Check, phiên có điểm kết thúc, skip không phải mastery, giải thích gợi ý, learner control trong phạm vi prerequisite, fallback khi ML tắt. Cần chỉnh cách diễn đạt: flashcard dịch nghĩa và lời giải thích ngữ pháp *có chỗ đứng* cho người mới; không nên độc quyền đo kỹ năng; replay giúp luyện nghe nhưng số lần replay không trực tiếp đo năng lực; streak có thể tăng trở lại ứng dụng, không chứng minh tiến bộ tiếng Anh [S4–S9].

**Mức độ quyết định:** đóng băng *ràng buộc quan sát, phân tách khái niệm và hành vi an toàn*; triển khai các tham số 5 phút, mức hạn chế replay, ngưỡng nhắc ôn và reward như **MVP HYPOTHESIS** có version/config, thử trong pilot. Không đóng băng công thức mastery, ngưỡng CEFR, đường học hoặc trọng số recommendation trước Phase 9. Không tìm thấy xung đột được chứng minh với **bản tóm tắt** V3.2; bản spec/checks gốc vắng mặt, do đó phải chạy compatibility gate trước khi ghi các rule này vào code.

## 2. Evidence model

**Thứ bậc:** (a) meta-analysis/systematic review về học tập và SLA [S1–S6, S10, S11]; (b) nghiên cứu sơ cấp/đánh giá đo lường [S7, S12–S15]; (c) CEFR và testing guidance [S16–S18]; (d) thử nghiệm của sản phẩm khác về *engagement* [S9]; (e) báo cáo hành vi di động về *UX*, không về học [S19]. Nghiên cứu product có nguy cơ thiên lệch công bố; nhiều nghiên cứu giáo dục khác tuổi, ngôn ngữ mẹ đẻ, độ thành thạo và bối cảnh với người Việt trưởng thành học tiếng Anh. Mạnh ở nguyên lý retrieval/spacing/feedback, yếu ở tham số cụ thể và hiệu quả của tổ hợp feed này. “Evidence strength” dưới đây áp cho *cơ sở học/đo lường*, không nâng các ngưỡng thiết kế thành kết luận khoa học.

**Bốn nhãn không được trộn:** **Learning evidence** = kết quả truy hồi, chuyển ngữ cảnh, giữ lại sau trì hoãn; **engagement evidence** = số ngày trở lại, chu kỳ hoàn thành; **UX/consumer evidence** = ma sát, dễ hiểu, sở thích thời lượng; **product hypothesis** = chính sách cụ thể của Mingo cần kiểm nghiệm. CEFR là bộ mô tả năng lực, không tự động xác thực level từ vài câu hỏi; **A0 là nhãn nội bộ**, đối chiếu *Pre-A1* một cách có chú thích, không quảng bá là chứng chỉ CEFR [S16–S18].

## 3. Decisions Q1–Q18

### Q1. Error interpretation

- **Recommended MVP policy:** Ghi lỗi quan sát và objective/item/modalities; chỉ gắn nhãn nhầm lẫn nếu item đã được biên soạn với distractor ánh xạ khái niệm rõ và có mẫu lặp lại; còn lại `CAUSE_UNKNOWN`.
- **Why:** Một đáp án sai có thể do nhiều cơ chế và cả item kém; chẩn đoán tâm lý từ một click làm scheduler sai.
- **Evidence:** Testing Standards yêu cầu tính hợp lệ của diễn giải điểm; phản hồi phải chứa thông tin nhiệm vụ thay vì gắn nhãn người học [S3, S18].
- **Evidence strength:** **Moderate** cho guardrail đo lường; taxonomy và ngưỡng lặp là **product hypothesis**.
- **Implementation rule:** Sai lần đầu → feedback theo đáp án/micro-explanation; chỉ hiển thị “cần ôn mục tiêu X” khi có ≥2 lần sai ở **hai item khác nhau** cùng objective (ngưỡng thử nghiệm), không ghi “careless/listening deficit”.
- **Telemetry/evidence:** `item_revision`, `objective_id`, `modality`, `first_response`, `first_correct`, `distractor_tag` nếu có, thời điểm và lần thử sau trì hoãn.
- **What NOT to infer:** Một lỗi ≠ thiếu năng lực, mất tập trung hay thiếu động lực; distractor sai ≠ chẩn đoán chắc chắn.
- **Later-phase option:** Phân tích lỗi có kiểm định chất lượng item và đối chiếu đánh giá người dạy; ước lượng xác suất với uncertainty.

### Q2. Response time

- **Recommended MVP policy:** Lưu thời gian thao tác như tín hiệu phụ để phát hiện ma sát và rà soát item; **không cộng/trừ mastery theo tốc độ** trong MVP.
- **Why:** Thời gian chịu ảnh hưởng độ khó item, thiết bị, khả năng tiếp cận, ngắt ứng dụng và đánh đổi tốc độ–độ chính xác.
- **Evidence:** Các mô hình đo lường xử lý accuracy và response time như cấu trúc riêng; speeded test có thể đưa phương sai không liên quan vào điểm [S12, S13].
- **Evidence strength:** **Moderate** cho không đồng nhất speed với ability; **limited** cho cách chuẩn hóa ứng dụng cụ thể.
- **Implementation rule:** Lấy thời gian foreground từ item-render-ready đến submit; pause/background được loại; lưu `duration_ms` nullable và `measurement_quality`; không dùng trong scoring/scheduler, trừ cảnh báo QA về item lỗi.
- **Telemetry/evidence:** `active_duration_ms`, `interrupted`, `item_revision`, device class *nếu cần chẩn đoán kỹ thuật*; không lấy dấu vết touch.
- **What NOT to infer:** Nhanh ≠ giỏi; chậm ≠ kém; timeout thiết bị ≠ hành vi học.
- **Later-phase option:** Mô hình speed–accuracy theo item và modality đã hiệu chuẩn, sau kiểm tra fairness.

### Q3. Hints

- **Recommended MVP policy:** Cho hint theo bậc ở **Learn/Retrieve/Transfer**, có thể cho mở transcript/gloss sau khi thử nghe; **Check độc lập** không cho hint trước submit.
- **Why:** Scaffolding giúp vượt khó nhưng lời giải sau hint là bằng chứng được hỗ trợ, khác retrieval không trợ giúp.
- **Evidence:** Feedback có hiệu quả khác nhau tùy nội dung; gloss L2 có ích khi đọc; hướng dẫn rõ đặc biệt phù hợp người mới [S3, S5, S20].
- **Evidence strength:** **Moderate** cho hỗ trợ/feedback; **product hypothesis** cho thứ tự hint từng loại.
- **Implementation rule:** Vocabulary: gợi ý âm/nhóm nghĩa → ví dụ; grammar: nêu điểm cần chú ý → quy tắc ngắn; listening: nghe đoạn ngắn hơn → transcript sau đáp án. Mỗi hint bấm tường minh; `assisted_correct` lưu riêng và không thay `first_unassisted_correct`.
- **Telemetry/evidence:** `hint_id`, `hint_type`, `shown_at`, `before_first_submit`, kết quả trước/sau.
- **What NOT to infer:** Dùng hint ≠ không biết; đáp án đúng sau hint ≠ đã giữ lâu.
- **Later-phase option:** A/B mức scaffolding theo objective sau khi đủ dữ liệu.

### Q4. Retry policy

- **Recommended MVP policy:** Cho **một lần sửa có feedback** trong thực hành; nếu vẫn sai, hiện lời giải/đường ôn và chuyển tiếp; Check giữ nguyên kết quả lần đầu, sau đó có thể luyện lại ở item tương đương.
- **Why:** Sửa lỗi có giá trị học, nhưng cố bấm đến đúng không được xóa sai lần đầu.
- **Evidence:** Practice testing và feedback hỗ trợ lưu giữ; loại phản hồi và đặc điểm bài tập điều tiết kết quả [S1, S3].
- **Evidence strength:** **Strong** cho retrieval + feedback; số lần retry là **product hypothesis**.
- **Implementation rule:** Append-only first submit, feedback, retry; `eventual_correct` chỉ là outcome luyện tập; cùng item sau feedback không nâng trạng thái độc lập; một item khác sau trì hoãn mới tăng mức tin cậy.
- **Telemetry/evidence:** `attempt_id`, `try_index`, `response`, `correct`, `feedback_revision`, `first_try_at`, `submit_at`.
- **What NOT to infer:** Sửa đúng ngay ≠ mastery; sai sau feedback ≠ không thể học.
- **Later-phase option:** Điều chỉnh số lần thử theo mức item và độ mệt; đánh giá retention trễ.

### Q5. Skip policy

- **Recommended MVP policy:** Skip tường minh và dễ dùng, được ghi là **missing learning evidence** kèm vị trí; một skip không đổi mastery, skip lặp lại khiến scheduler đổi cách trình bày hoặc hỏi khó khăn.
- **Why:** Hành vi bỏ qua có nhiều nguyên nhân; cấm skip làm tăng bế tắc, xem skip là hoàn thành làm mất chuẩn đánh giá.
- **Evidence:** Nguyên tắc diễn giải đo lường phải gắn với dữ liệu đã thu; learner control là hỗ trợ quyền tự chủ, không thay phép đo [S18, S21].
- **Evidence strength:** **Moderate** cho không suy diễn; xử lý lặp lại là **product hypothesis**.
- **Implementation rule:** `SKIPPED` ≠ `COMPLETED`/`CORRECT`; sau 2 skip cùng objective qua các exposure khác nhau, đề nghị dạng dễ hơn/hint/đổi modality; vẫn giữ objective trong due pool, không ép lặp vô hạn trong cùng chu kỳ.
- **Telemetry/evidence:** `skip`, `item_revision`, `objective`, `selection_reason`, `exposure_id`, số lần có thể đã thấy.
- **What NOT to infer:** Skip ≠ mastery, lười hay rủi ro bỏ học.
- **Later-phase option:** Hỏi lý do tùy chọn và phân tích item/friction theo nhóm.

### Q6. Listening replay

- **Recommended MVP policy:** Ở hoạt động luyện nghe, cho nghe lại **không giới hạn cứng** và cho tua; ở Check/placement dùng chính sách cố định **tối đa hai lượt nghe**, nêu trước, có tùy chọn accessibility; lần nghe thêm chuyển hoạt động sang practice, không là Check độc lập.
- **Why:** Nghe lặp là scaffold hợp lý; nếu điều kiện nghe khác nhau thì kết quả Check không còn so sánh được.
- **Evidence:** Nghiên cứu lặp tác vụ nghe gợi ý thay đổi xử lý input nhưng bối cảnh video/bài giảng khác microclip; chuẩn đánh giá yêu cầu điều kiện diễn giải nhất quán [S14, S18].
- **Evidence strength:** **Limited** cho replay tối ưu; **moderate** cho nhất quán đo lường.
- **Implementation rule:** Audio ngắn có nút replay; Check ghi `allowed_plays=2`, không auto-submit khi hết lượt, có nhãn accessibility và mode khác; chuyển mode không xóa quan sát luyện tập.
- **Telemetry/evidence:** `play_count`, `mode`, `allowed_plays`, `accessibility_override`, `audio_revision`, `first_answer`.
- **What NOT to infer:** Nghe lại nhiều ≠ kỹ năng nghe thấp; một đáp án đúng sau 5 lượt ≠ tương đương một lượt.
- **Later-phase option:** Chuẩn hóa điều kiện nghe theo task và đánh giá độ tin cậy/khả năng tiếp cận.

### Q7. Vocabulary representation

- **Recommended MVP policy:** Đơn vị từ vựng gồm nghĩa ngắn (có thể dịch Việt), âm/phát âm, một câu dễ hiểu và nhiều kiểu truy hồi; flashcard hai chiều là *một* mode nhanh, không là toàn bộ chương trình.
- **Why:** Người mới cần liên kết form–meaning rõ; hiểu một cặp dịch chưa chứng minh nghe, sản xuất hay dùng trong ngữ cảnh.
- **Evidence:** Tổng quan word cards cho thấy lợi ích; meta-analysis gloss và nghiên cứu receptive/productive cho thấy các nhiệm vụ đo khía cạnh khác nhau [S5, S6, S15].
- **Evidence strength:** **Moderate** cho kết hợp direct learning và context; tỷ lệ từng mode **product hypothesis**.
- **Implementation rule:** Mỗi lexical objective có audio, gloss, ví dụ kiểm duyệt; bắt đầu recognition/meaning, sau đó recall và nghe/ứng dụng phù hợp mức; tag từng outcome theo `skill_dimension`.
- **Telemetry/evidence:** `lexeme_id`, `sense_id`, `item_revision`, `task_type` (recognition/recall/listening/context), unassisted result.
- **What NOT to infer:** Nhận ra bản dịch ≠ nói/viết/hiểu lời nói; một nghĩa ≠ mọi nghĩa của từ.
- **Later-phase option:** Collocations, tự tạo câu và đánh giá production có con người/rubric.

### Q8. Grammar teaching sequence

- **Recommended MVP policy:** **Hybrid theo prior evidence:** có ví dụ/pattern ngắn; nếu mục tiêu quen thuộc thì thử trước, nếu mới thì giải thích quy tắc cực ngắn trước; thực hành có feedback, cuối cùng ứng dụng ngữ cảnh khác.
- **Why:** Hướng dẫn explicit và focus-on-form giúp tránh mò mẫm cho người mất gốc, trong khi retrieval/transfer giúp kiểm tra hơn là chỉ đọc quy tắc.
- **Evidence:** Meta-analysis L2 cho thấy focused/explicit instruction thường có lợi, nhưng kết quả phụ thuộc feature và phép đo; retrieval/feedback hỗ trợ luyện tập [S1, S3, S4].
- **Evidence strength:** **Moderate** cho hybrid; **limited** cho nhánh exact theo prior.
- **Implementation rule:** `new/uncertain` → example + one-rule card + guided item; `seen` → attempt-first + feedback; Check là item mới không hint; không có đoạn lý thuyết dài.
- **Telemetry/evidence:** `objective`, `instruction_variant`, `prior_exposure`, `first_response`, `rule_seen`, delayed check.
- **What NOT to infer:** Thuộc quy tắc ≠ dùng được trong câu; một lỗi grammar ≠ thiếu toàn bộ nền tảng.
- **Later-phase option:** So sánh sequence theo feature và trình độ sau khi có đủ item/learners.

### Q9. Difficulty progression

- **Recommended MVP policy:** Tăng độ khó **trong cùng objective** theo recognition → cued recall → nghe/ngữ cảnh → ứng dụng, nhưng chỉ từng bước và quay về scaffold khi sai; không chờ ranh giới lesson.
- **Why:** Muốn biết khả năng chuyển giao phải kiểm tra khác task, nhưng nhảy khó nhiều bước gây quá tải.
- **Evidence:** Receptive/productive knowledge không đồng nhất; retrieval và feedback có lợi, song “desirable difficulty” phụ thuộc khả năng learner [S1, S3, S15, S20].
- **Evidence strength:** **Moderate** cho nhiều phép đo và hướng dẫn; bước/ngưỡng là **product hypothesis**.
- **Implementation rule:** Một thành công không hint → đưa *một item khác* cùng objective ở mức kế; sai → trợ giúp/ôn; cấm chuyển objective mới nếu prerequisite chưa đủ theo rule tạm thời, không gọi rule này final mastery.
- **Telemetry/evidence:** `objective`, `difficulty_band`, `task_type`, `item_revision`, `unassisted_result`, `policy_version`.
- **What NOT to infer:** Nhận diện đúng ≠ recall/transfer đã đạt; difficulty item gắn tay ≠ đã hiệu chuẩn.
- **Later-phase option:** Item calibration và mastery threshold có uncertainty ở Phase 9.

### Q10. User focus vs system need

- **Recommended MVP policy:** Tôn trọng focus trong tập item hợp lệ, nhưng bắt đầu bằng một nhiệm vụ ôn có hạn nếu quá hạn hoặc thiếu prerequisite liên quan; sau đó ưu tiên focus. Cho người học xem lý do và đổi focus.
- **Why:** Quyền chủ động hỗ trợ động lực, còn việc ôn và prerequisite bảo vệ giá trị học; không cần quyền phủ quyết mơ hồ của thuật toán.
- **Evidence:** Spacing L2 có lợi; tổng quan learner-controlled instruction cho thấy ảnh hưởng phụ thuộc bối cảnh; không có dữ liệu nào quyết định chính xác tỷ lệ [S2, S21].
- **Evidence strength:** **Moderate** cho hai nguyên tắc; phân bổ là **product hypothesis**.
- **Implementation rule:** Mỗi chu kỳ tối đa **một review/prerequisite item bắt buộc** trước nhóm ưu tiên focus; nếu learner chọn Listening, phần còn lại là Listening hợp lệ; nếu không có item phù hợp, giải thích và cho lựa chọn review hoặc học objective khả dụng.
- **Telemetry/evidence:** `chosen_focus`, `eligible_pool`, `selected_reason`, `override_presented`, `override_choice`.
- **What NOT to infer:** Chọn Listening ≠ yếu Listening; bỏ review ≠ từ chối học.
- **Later-phase option:** Personalize mức ưu tiên theo lựa chọn được lặp lại và retention, không theo click đơn lẻ.

### Q11. Placement scope

- **Recommended MVP policy:** Placement **ngắn, phân nhánh theo rule**, chạm cả Vocabulary, Grammar, Listening; ước lượng khởi điểm có uncertainty; phần nghe và mục tiêu khó được tiếp tục hiệu chỉnh trong các chu kỳ sau.
- **Why:** Một composite test dài tăng ma sát và chưa thể cho CEFR chính xác nếu item chưa được chuẩn hóa; bỏ Listening làm sai bức tranh kỹ năng.
- **Evidence:** CEFR khuyến khích profile theo kỹ năng; liên kết bài thi với CEFR cần quy trình xác thực; testing standards nhấn mạnh diễn giải hợp lệ [S16–S18].
- **Evidence strength:** **Moderate** cho đa chiều và uncertainty; độ dài/branching là **product hypothesis**.
- **Implementation rule:** Hỏi tự báo cáo và mục tiêu tùy chọn; 6–9 item ngắn qua ba lĩnh vực, khoảng 3–6 phút là *mục tiêu UX*, dừng/skip Listening khi không có tai nghe hay môi trường phù hợp; nhánh lên/xuống từng band, cap B2 nếu item coverage thiếu; trả `starting_band` + `provisional`/`needs_more_evidence`, không tuyên bố điểm CEFR/TOEIC.
- **Telemetry/evidence:** `placement_version`, item/revision, domain, first result, skip/accessibility, estimated band, uncertainty reason, later calibration.
- **What NOT to infer:** Tự báo cáo ≠ trình độ; 9 item ≠ chứng chỉ A0–B2; nghe trong nơi ồn ≠ kém nghe.
- **Later-phase option:** Calibrated adaptive testing với item bank, invariance/fairness và cut scores đã xác thực.

### Q12. User-facing learner model

- **Recommended MVP policy:** Hồ sơ định tính theo objective/skill: “đã thử”, “cần thêm bằng chứng”, “đang ôn”, “gần đây làm tốt”; có số lần quan sát và link tới ví dụ, không hiện % mastery.
- **Why:** Giải thích có thể giúp tự điều chỉnh, còn số lẻ chính xác giả khi item chưa hiệu chuẩn.
- **Evidence:** CEFR cho phép profile kỹ năng; dashboard research gợi ý giá trị của feedback có ngữ cảnh nhưng kết quả chuyển sang app này chưa chắc [S16, S22].
- **Evidence strength:** **Moderate** cho tránh false precision; UI cụ thể **product hypothesis**.
- **Implementation rule:** Chỉ nói “Bạn làm sai hai bài do/does gần đây; thử ôn?” nếu hai item hợp lệ; khi mẫu ít hiện “chưa đủ bằng chứng”; mọi insight có `evidence_refs` và ngày, có nút báo “không đúng”.
- **Telemetry/evidence:** `insight_type`, `supporting_attempt_ids`, `evidence_count`, `generated_at`, `shown_at`, feedback người học.
- **What NOT to infer:** Pattern ngắn ≠ chẩn đoán lâu dài; engagement ≠ mastery.
- **Later-phase option:** Uncertainty/calibration dashboard sau nghiên cứu hiểu nhầm của người dùng.

### Q13. Learning goals

- **Recommended MVP policy:** Hỏi **một câu mục tiêu có thể bỏ qua**: xây nền / dùng cho công việc / TOEIC / duy trì hằng ngày; cho sửa sau. Dùng để chọn ví dụ, từ vựng và mục tiêu gần, không vượt prerequisite.
- **Why:** Ý định cải thiện relevance và agency nhưng không là bằng chứng năng lực.
- **Evidence:** Lợi ích của self-regulation và learner choice có phụ thuộc thiết kế; chưa có bằng chứng về thứ tự curriculum tốt nhất cho mục tiêu của nhóm này [S21, S23].
- **Evidence strength:** **Limited** cho hiệu quả cụ thể; **product hypothesis**.
- **Implementation rule:** `goal_id` chỉ định trọng số nội dung *trong pool hợp lệ* và copy; TOEIC là mapping ngoại sinh, không ghi đè A0–B2; bắt đầu cả khi người dùng skip câu hỏi.
- **Telemetry/evidence:** `goal_id`, `goal_changed_at`, `goal_source`, acceptance/relevance feedback tùy chọn.
- **What NOT to infer:** Mục tiêu nghề/thi ≠ level hay động lực bền vững.
- **Later-phase option:** Goal-specific units sau khi nội dung và outcome ngoài app được xác thực.

### Q14. Daily target

- **Recommended MVP policy:** Default **một chu kỳ hữu hạn ~5 phút/ngày**; cho chọn 5/10/15+ phút tương ứng 1/2/3+ chu kỳ, không cắt ngang mục tiêu để đúng đồng hồ.
- **Why:** Mức bắt đầu thấp giảm ma sát theo giả thuyết UX; learning evidence vẫn là hoàn thành tác vụ và kiểm tra trễ, không là phút dùng.
- **Evidence:** Consumer mobile report chứng minh bối cảnh di động phổ biến nhưng không đo độ dài học tối ưu; thí nghiệm Duolingo về tách streak/target chỉ đo return/goal behavior [S9, S19].
- **Evidence strength:** **Product hypothesis** cho 5 phút/target; **limited** engagement transfer.
- **Implementation rule:** 1 cycle = objective có closure; `target_cycles` mặc định 1, user đổi bất kỳ lúc nào cho ngày sau; đạt target bằng cycle hợp lệ, không bằng idle time.
- **Telemetry/evidence:** `target_cycles`, `cycle_started/completed`, `active_duration`, abandon reason tùy chọn.
- **What NOT to infer:** 15 phút ≠ học gấp ba; daily target đạt ≠ retention.
- **Later-phase option:** Điều chỉnh target dựa trên preference/hoàn thành và wellbeing, không tối đa screen time.

### Q15. Streak rule

- **Recommended MVP policy:** Streak học tập tăng khi mỗi ngày có **một hoạt động truy hồi có chấm điểm hợp lệ và feedback**, kể cả review rất ngắn; mục tiêu nhiều chu kỳ theo dõi riêng.
- **Why:** Ngưỡng thấp giảm áp lực, nhưng mở app/skip/nghe thụ động không thành hành động học có ý nghĩa.
- **Evidence:** Duolingo A/B tách daily goal khỏi streak cải thiện retention và DAU, không đo proficiency; retrieval là cơ chế học phù hợp hơn click mở app [S1, S9].
- **Evidence strength:** **Moderate** cho retrieval; định nghĩa streak là **product hypothesis**.
- **Implementation rule:** Một `qualifying_activity_id` duy nhất/ngày theo timezone người học; một attempt đầu có nội dung học, nộp đáp án và xem feedback; đúng/sai đều đủ, skip không đủ; thay timezone có hiệu lực ngày tiếp theo; offline sync idempotent và điều chỉnh công bằng khi event đến muộn; không cộng hai lần.
- **Telemetry/evidence:** `qualifying_activity_id`, `local_day/timezone`, `event_time`, `received_at`, `streak_award_id`, `policy_version`.
- **What NOT to infer:** Streak ≠ proficiency, effort tuyệt đối hay bằng chứng đủ học.
- **Later-phase option:** “Grace day” có giới hạn và đánh giá stress/trust trong beta.

### Q16. Reward design

- **Recommended MVP policy:** Phản hồi tiến bộ gắn objective, milestone ôn trễ/transfer và badge hiếm; **không triển khai XP farm, leaderboard hoặc trả thưởng theo số câu bấm**.
- **Why:** Thưởng hướng vào tiến bộ và quyền tự chủ có thể nâng trải nghiệm; reward đếm click khuyến khích lạm dụng, nhiều cơ chế game có tác động khác nhau.
- **Evidence:** Meta-analysis gamification có hiệu ứng trung bình nhưng dị biệt mạnh; nghiên cứu reward cảnh báo tác động lên động lực nội tại trong một số điều kiện [S8, S10].
- **Evidence strength:** **Moderate** cho dè chừng và dùng feedback; cơ chế cụ thể **product hypothesis**.
- **Implementation rule:** Một badge/milestone từ server theo idempotency key, chỉ gắn với `first meaningful review`, `delayed check`, `unit completion`; reward không làm tăng mastery, không mở khóa prerequisite. Theme chỉ cosmetic nếu sau pilot có nhu cầu.
- **Telemetry/evidence:** `reward_rule_version`, `source_activity_id`, `awarded_at`, `badge_seen`, opt-out; không tracking chia sẻ xã hội.
- **What NOT to infer:** Badge/XP ≠ học tốt; retention ↑ ≠ vocabulary/grammar/listening ↑.
- **Later-phase option:** Thử reward tùy chọn so với progress-only với chỉ số học trễ và stress.

### Q17. Learner control over course map

- **Recommended MVP policy:** Cho xem bản đồ và học lại mọi phần đã mở; objective mới ngoài lộ trình hiện tại có thể **preview không chấm tiến độ**, còn prerequisite chưa đạt thì có nhãn hướng dẫn thay vì mở tự do dưới dạng học chính thức.
- **Why:** Đảm bảo agency và khám phá trong khi giữ tính hợp lệ của chuỗi nền tảng; khóa cứng mọi nội dung dễ gây bế tắc.
- **Evidence:** Learner control có hiệu ứng phụ thuộc đối tượng/bối cảnh; novice thường hưởng lợi từ guidance [S20, S21].
- **Evidence strength:** **Moderate** cho balance; kiểu preview là **product hypothesis**.
- **Implementation rule:** `OPEN`, `REVIEW`, `PREVIEW_ONLY`, `PREREQUISITE_NEEDED`; preview không ghi completion/mastery, có đường về prerequisite; manual level override chỉ thay điểm bắt đầu/độ khó hiển thị, không sửa lịch sử evidence.
- **Telemetry/evidence:** `map_opened`, `chosen_objective`, `eligibility_result`, `preview_started`, `manual_override`.
- **What NOT to infer:** Chọn B2 ≠ đạt B2; xem preview ≠ đã học.
- **Later-phase option:** Cho challenge để chứng minh prerequisite qua assessment độc lập đã hiệu chuẩn.

### Q18. Recommendation explanations

- **Recommended MVP policy:** Giải thích ngắn 1 lý do kiểm chứng được trên card hoặc trước chu kỳ; có “xem thêm” để thấy quan sát làm cơ sở, tránh kể suy đoán nguyên nhân.
- **Why:** Người học cần hiểu vì sao ôn; lời giải thích phải khớp decision thật và đủ dễ đọc trên di động.
- **Evidence:** Nghiên cứu XAI giáo dục cho thấy minh bạch có giá trị và giới hạn; hiệu quả giải thích trong chính app vẫn cần đo UX [S24].
- **Evidence strength:** **Limited** cho learning outcome; **product hypothesis** về UX/trust.
- **Implementation rule:** Render `DUE_REVIEW`→“Đến lúc ôn”, `RECENT_ERROR`→“Bạn vừa gặp khó ở mục này”, `PREREQUISITE_GAP`→“Ôn bước nền trước”, `CURRENT_OBJECTIVE`→“Tiếp tục mục tiêu”, `MODALITY_TRANSFER`→“Thử ở dạng khác”, `CHALLENGE`→“Thử nâng mức”; priority reason + supporting event IDs phải log; khi reason không xác minh được dùng “Tiếp tục lộ trình” chứ không bịa.
- **Telemetry/evidence:** `decision_id`, `policy_version`, `candidate_set_ref`, `selection_reason`, `supporting_evidence_ids`, `exposure_id`, accept/skip.
- **What NOT to infer:** Lý do do rule sinh ≠ giải thích nhân quả về não/trí thông minh; click chấp nhận ≠ học.
- **Later-phase option:** Explainable ML có fidelity test và user study riêng.

## 4. Synthesized Learner Evidence Model

| Lớp | Dữ liệu MVP | Quy tắc sử dụng |
|---|---|---|
| A. Raw observable | Item/objective/content revision, modality, context practice/Check/placement, first response và correctness do server chấm, retry, hint, replay, skip, active time chất lượng đo, event/received time, provenance. | Append-only theo attempt; không sửa lần đầu khi retry; chống trùng command; không gán nguyên nhân tâm lý. |
| B. Short-term derived | `DUE_REVIEW`, `RECENT_ERROR`, `ASSISTED_SUCCESS`, `REPEATED_ERROR`, `INSUFFICIENT_EVIDENCE`, `RECENT_UNASSISTED_SUCCESS`. | Chỉ là tín hiệu giải thích được, version theo rule và dựa vào bằng chứng có sẵn *tại thời điểm quyết định*. Một thành công chưa đủ chốt mastered. |
| C. Curriculum | Objective và skill dimension; content item và prerequisite đã biên soạn; trạng thái eligible/preview/review. | Quan hệ curriculum được kiểm duyệt; **bản đồ và ngưỡng hiện tại là provisional**, giữ ranh giới V3.2 và Phase 9. |
| D. User intent | Focus hiện chọn, mục tiêu tự khai, daily target, yêu cầu accessibility và override. | Dùng để cá nhân hóa trải nghiệm trong pool hợp lệ; không nhập vào chỉ số competence. |
| E. Engagement | Chu kỳ hoàn thành, streak, badge, việc quay lại. | Dashboard engagement riêng; không góp vào mastery, level hoặc risk mặc định. |
| F. Deferred intelligence | Mastery formula, knowledge tracing, production risk/labels, ranking weights, final adaptive paths/CEFR cut scores. | **Không freeze** trong Phase 1; Phase 9+ cần dữ liệu, calibration, kiểm tra leakage và fairness. |

Nguyên tắc **availability**: scheduler tại thời điểm `decision_at` chỉ đọc những observation có `known_at ≤ decision_at`. Event offline đến muộn cập nhật trạng thái hiện tại và có thể ghi lại projection lịch sử phục vụ phân tích, nhưng không viết lại lý do đã hiển thị ở một quyết định cũ. `attempt` là command có score canonical; `replay`, `hint_view`, `exposure` có thể là telemetry nhưng mọi điều kiện ảnh hưởng score, reward hay eligibility phải được xác nhận ở server hoặc mang provenance/quality và quy trình reconcile theo V3.2. `mastery` tách `risk`; decision, exposure, execution và outcome có ID riêng. Khi cả recommendation bị tắt, ứng dụng vẫn có đường học/review theo curriculum cơ bản.

## 5. Adaptive Learning Feed / Scheduler policy

**Policy sơ bộ, deterministic, versioned; không phải công thức mastery cuối.**

1. **Eligibility:** Lấy content *published* đúng revision phù hợp enrollment; objective trong band hiện hành hoặc review trước đó; item license/source hợp lệ, có đáp án/feedback, không vừa hiển thị trùng trong chu kỳ; đảm bảo medium hiện sẵn (audio/download). Nếu offline, dùng pool snapshot có version đã tải.
2. **Prerequisite:** Objective mới chỉ hợp lệ nếu prerequisite đạt điều kiện vận hành provisional dựa trên Check độc lập; không phụ thuộc streak/XP; objective đã học có thể review; mục tiêu khóa có preview riêng. Nếu chưa có dữ liệu, khởi điểm cơ bản an toàn và placement tiếp diễn.
3. **Priority có thứ tự, không điểm trọng số mờ:** (a) một item due hoặc gap cản objective hiện tại, (b) item đúng focus/mục tiêu của learner, (c) một item mới từ current objective, (d) transfer/challenge nếu có đủ success không hint. Khi nhiều candidate cùng ưu tiên, chọn item lâu chưa thấy nhất, tie-break ổn định theo `item_id`. Due review quá nhiều: giới hạn có cấu hình và carry-forward phần còn lại; **không tuyên bố lịch giãn cách tối ưu**. `RECENT_ERROR` chèn remedial item khác sau feedback, không lặp mãi cùng stem.
4. **Phân bổ mẫu một chu kỳ:** phải có đủ năm *chức năng* Review, Learn, Retrieve, Transfer, Check và feedback cho objective, dù không cần năm màn hình hay năm item riêng. Review kiểm tra kiến thức cũ nếu có; nếu người hoàn toàn mới, dùng câu gợi nhớ kiến thức nền hoặc entry cue có đáp án. Learn có thể là micro-explanation củng cố trong review-only cycle; Transfer thay ngữ cảnh hoặc cue/modalities, Check dùng item khác item vừa nhận feedback. Nếu không biên soạn đủ item hợp lệ cho các chức năng, không dựng một chu kỳ giả; báo content gap và dùng objective khác hoặc yêu cầu đồng bộ nội dung.
5. **Độ khó:** Nhích một bậc trong objective sau unassisted success ở item khác; lỗi chuyển về scaffold/remediation. Hướng từ dễ sang khó **không** là chứng minh đạt level mới; cập nhật provisional evidence.
6. **Focus:** Tuân Q10; người học có thể chọn focus và bỏ qua với hậu quả rõ ràng. Khi prerequisite quan trọng, giải thích lý do trước khi chèn một item.
7. **Closure:** Kết thúc sau khi microgoal có feedback và Check/next review plan, ước chừng 5 phút nhưng không hard-cut giữa câu; nếu dài, cho pause/resume theo objective; kết quả cycle có thể `COMPLETED`, `PAUSED`, `SKIPPED_OBJECTIVE`, `ABANDONED`, không cộng completion cho skip toàn bộ. Sau màn kết thúc chỉ thêm cycle khi người dùng bấm tiếp.
8. **Audit:** Mỗi quyết định lưu `decision_id`, pool/eligibility snapshot ref, rule version, priority reason chính, content revision, evidence IDs sẵn lúc đó; exposure ghi riêng, execution và outcome ghi khi thực sự xảy ra. Không đưa text explanation vào làm source of truth thay reason code.
9. **Fallback:** Khi ML tắt hoặc recommendation service lỗi: chọn due review theo hạn, tiếp current objective hợp lệ theo thứ tự curriculum ổn định, nếu không có due chọn bài mới đầu tiên; nếu content audio offline thiếu thì chọn item text hợp lệ cùng objective và log `FALLBACK_MEDIA_UNAVAILABLE`; nếu không còn candidate, hiển thị kết thúc/đồng bộ, không tự mở bài khóa.

**Lưu ý implementation:** Các số “một review”, “một lần nâng bậc” là tham số thử nghiệm được đặt trong policy config, không sửa hợp đồng chấm điểm V3.2. Decision path phải có unit/integration tests cho offline late event, item revision, disabled ML và no eligible item.

## 6. Placement policy

- **Khởi động:** optional goal/self-assessment và môi trường âm thanh; hỏi learner muốn bắt đầu ngay hay làm chẩn đoán 3–6 phút. Chưa chẩn đoán → A0/Pre-A1 provisional hoặc band tự chọn có nhãn *chưa xác nhận*, không gắn nhãn thấp như đánh giá con người.
- **Bao phủ:** 2–3 câu từ vựng, 2–3 grammar, 2–3 listening clip ngắn, trải A0/A1/A2/B1/B2 theo nội dung đã biên soạn. Nhánh rule lên/xuống sau item phân biệt đơn giản; không gọi là statistical CAT; loại câu đã thấy. Nếu thiếu item B2 kiểm duyệt, ghi `B2_UNRESOLVED`, không mặc nhiên xếp B2.
- **Điều kiện:** Check item không hint, listening tối đa hai lượt và điều kiện biết trước; audio không dùng được → skip domain, hồ sơ Listening “chưa đánh giá”, không thay bằng grammar. Accessibility mode được lưu và diễn giải riêng, không phạt người dùng.
- **Kết quả:** band gợi ý khởi điểm và biểu diễn từng domain `observed evidence / insufficient`, không hiện “CEFR certified” hay số % chính xác. Đưa ngay vào cycle đầu; dùng item mới trong các ngày tiếp để xác nhận/sửa band, cho user chuyển điểm bắt đầu có kiểm soát.
- **Hiệu chuẩn sau onboarding:** Nếu hai Check không hint ở item khác cùng domain/target hỗ trợ mức cao hơn/thấp hơn, đề xuất đổi nội dung tiếp theo; giữ lịch sử placement và giải thích “đang hiệu chỉnh”; ngưỡng là giả thuyết, không phải cut score CEFR. Một bài nghe ở môi trường ồn không hạ band chung.

## 7. Motivation / engagement policy

Streak kích hoạt bằng một hoạt động truy hồi có đáp án và feedback/ngày; đáp án sai vẫn tính nỗ lực. Daily target mặc định một cycle, user có thể chọn 2, 3 hoặc hơn; completion phải có closure, còn streak có thể giữ bằng một review ngắn có ý nghĩa khi không đủ thời gian. Streak và target là hai counter riêng. Reward MVP = phản hồi tiến bộ theo objective và milestone ôn trễ/transfer; không có điểm XP theo số lần chạm, leaderboard hay mở prerequisite bằng reward. Không thúc ép kéo dài phiên, không mặc định gửi notification ép học. Server reconcile ngày theo timezone và offline late arrival; idempotent reward/streak; chỉ hiển thị tiến độ sau sync với trạng thái tạm khi offline. Hiệu quả cần đo riêng: return days, cycle completion, friction/stress (engagement/UX) **và** delayed unassisted checks (learning). Thí nghiệm Duolingo chỉ hỗ trợ giả thuyết engagement cho Mingo [S9].

## 8. User-facing learner profile

Màn “Lộ trình của tôi” hiển thị: objective hiện tại; từ vựng/ngữ pháp/nghe với nhãn **chưa đủ bằng chứng / đang luyện / cần ôn / gần đây làm tốt**; một ví dụ quan sát và thời điểm; danh sách “Vì sao hôm nay ôn mục này?”; quyền đổi focus/mục tiêu và báo insight sai. Dùng ngôn ngữ tạm thời: “2 bài do/does gần đây chưa đúng ở lần đầu” thay vì “bạn yếu ngữ pháp”. Chỉ đưa insight khi có ít nhất hai item độc lập; nếu không thì nói rõ chưa đủ dữ liệu. Khả năng biết từ ở dạng nghe, nhận diện nghĩa và dùng ngữ cảnh được phân biệt. Bên trong giữ ID nguồn, uncertainty/missingness, rule revision; không hiện mastery %, risk score, tiên đoán bệnh lý hay xếp hạng xã hội. Profile phải tránh khiến người mới xấu hổ và vẫn khả dụng khi không có data/ML.

## 9. Minimal telemetry contract

| Trường / nhóm | Vì sao cần | Nguồn / lớp | Retention / privacy note |
|---|---|---|---|
| `user_pseudonymous_id`, `device_install_id` tùy trường hợp, `command_id`, `event_id` | Liên kết và idempotency offline | Server ID / raw | Tách identity, hạn chế quyền; không lưu advertising ID. |
| `event_time`, `known_at/received_at`, `source_capture`, `offline_flag`, `timezone_at_event` | Reconstruct và chống leakage, streak đúng ngày | Client + server / raw | Lưu provenance; timestamp client untrusted, đối chiếu server. |
| `content_id`, `content_revision`, `item_revision`, `objective_id`, `skill_dimension`, `modality`, `task_mode` | Giải nghĩa historical attempt và đo theo domain | Content catalog + command / raw | Published content immutable, pin revision. |
| `attempt_id`, `try_index`, `response_code`, `server_correct`, `feedback_revision`, `hint_type`, `replay_count`, `skip` | Phân biệt unassisted/assisted/skip, score canonical | Command authoritative + limited telemetry / raw | Tránh lưu free-text thô nếu không cần; không lưu full audio microphone. |
| `active_duration_ms`, `interrupted`, `measurement_quality` | QA item/UX, không chấm mastery | Client / raw optional | Giảm precision nếu đủ; không thu touch stream, GPS, sensors. |
| `decision_id`, `policy_version`, `candidate_set_ref`, `reason_code`, `evidence_refs`, `exposure_id`, `execution_id`, `outcome_id` | Auditable scheduler và causal lifecycle | Backend / raw + derived | Chỉ candidate summary/ref cần tái hiện; tránh chụp mọi hành vi UI. |
| `placement_version`, `starting_band`, `uncertainty_reason`, `goal_id`, `focus_id`, `target_cycles` | Khởi điểm, intent tách ability | Server / derived & preference | User được xem/sửa preference; provisional band không biến thành chứng chỉ. |
| `due_flag`, `repeated_error_flag`, `streak_day`, `reward_id` | Scheduler/engagement | Backend / derived | Recompute được từ raw và rule version; không gộp vào mastery. |

**Chính sách trước khi thu:** lập data dictionary cho purpose, access, TTL, deletion/export và lawful notice theo yêu cầu địa phương ở pha bảo mật; TTL cụ thể chưa được evidence này quyết định, owner/product + privacy review đặt trước pilot. Với pilot nhỏ, có thể lưu event cần tái hiện trong vòng pilot/review; đừng thiết kế retention vô hạn. Ghi `license`, `source`, `attribution`, `content_revision` trong content metadata (không cần nhân bản vào từng telemetry event nếu revision là khóa bất biến). Nếu accessibility override tác động so sánh Check, chỉ ghi mode/điều kiện, tránh lưu chẩn đoán cá nhân.

## 10. Five-user pilot validation plan

**Thiết kế:** 5 người khác mức tự khai và hoàn cảnh học; 1 vòng onboarding + think-aloud; 5–7 ngày sử dụng tự nhiên nếu khả thi; phỏng vấn kết thúc và audit log từng người. Đây là usability/behavior/technical pilot, không là thử nghiệm efficacy. Nên có người nghe audio ở nơi không thuận tiện để kiểm tra skip/tiếp tục. Xin đồng ý thu dữ liệu và cho quyền rút lui, ưu tiên dữ liệu giả danh.

| Câu hỏi kiểm chứng | Quan sát / test | Gate nội bộ để tiến hành build tiếp, không phải hiệu quả học |
|---|---|---|
| Người dùng hiểu feed và reason? | Yêu cầu giải thích lại mục tiêu/“đến lúc ôn”, quan sát có hiểu skip và profile provisional không. | 5/5 tìm được điểm kết thúc và lý do cơ bản sau một lần dùng; mọi diễn giải “% mastery/CEFR certified” là lỗi wording cần sửa. |
| Placement có gây ma sát? | Đo thời gian và lý do abandon; hỏi cảm nhận dài/ngắn, kiểm tra nghe khi không có tai nghe. | Không có lỗi chặn đường vào feed; nghe bị skip vẫn có path hợp lệ. 3–6 phút chỉ là mục tiêu UX, nếu vượt phải điều chỉnh. |
| Scheduler có chọn đúng nội dung? | Review từng decision/exposure với log reason/evidence và content editor. | 0 trường hợp prerequisite bypass, item revision sai, lặp item vòng kín hoặc bịa lý do; mọi trường hợp phải có trace. |
| Đo lường có trung thực? | Các tình huống first wrong→retry correct, hint, replay, skip, offline late arrival, đổi timezone. | 0 overwrite first attempt; 0 duplicate progress/reward; event time và known_at đúng, Check điều kiện so sánh được. |
| Learning task có khả thi? | Quan sát lỗi hiểu instructions, transcript, độ khó, delayed check nếu có. | Ghi lỗi content, không dùng 5 người để ước lượng causal gain; revision pin và audit đầy đủ. |
| Trust/wellbeing? | Hỏi “hệ thống hiểu bạn ra sao?”, áp lực streak, giải thích gợi ý có quá cá nhân/đổ lỗi không. | Mọi câu nhãn suy đoán gây khó chịu được sửa; không có reward ép người dùng bỏ qua feedback. |

**Không được kết luận:** population efficacy, thắng đối chứng, 5 phút tối ưu, CEFR cut scores, calibrated mastery, sản phẩm phù hợp mọi người Việt, ổn định trọng số ML. Đếm failure case theo participant và transcript thay vì ý nghĩa thống kê; bản kết quả pilot cần issue list theo severity và quyết định revise/keep/retest.

## 11. Decision register

Phân loại ở đây là trạng thái **đề xuất**; `FREEZE NOW` nghĩa là đóng băng *nguyên tắc/ràng buộc* trong PRD sau owner review, không tuyên bố đã thay đổi V3.2. Trong các hàng `MVP HYPOTHESIS`, rule đã đủ rõ để thử nhưng tham số không được diễn giải như khoa học đã xác minh.

| Q | Decision | Classification | Evidence strength | Phase impact |
|---|---|---|---|---|
| 1 | Observable error; no one-click cause | FREEZE NOW | Moderate | Evidence model, PRD |
| 2 | Latency stored for QA, not mastery | FREEZE NOW | Moderate | Telemetry, assessment |
| 3 | Typed hints; assisted ≠ unassisted | FREEZE NOW | Moderate | Content, scoring boundary |
| 4 | Preserve first attempt; one practice retry | MVP HYPOTHESIS | Strong mechanism; retry count untested | Assessment PRD |
| 5 | Explicit skip, no mastery; remediate repeats | FREEZE NOW | Moderate; threshold untested | Feed, telemetry |
| 6 | Unlimited practice replay; 2-play Check | MVP HYPOTHESIS | Limited | Listening content, assessment |
| 7 | Meaning/audio/context/multiform retrieval | FREEZE NOW | Moderate | Content authoring |
| 8 | Explicit scaffold + attempt contextualized | MVP HYPOTHESIS | Moderate | Grammar content/UX |
| 9 | Increment difficulty within objective | MVP HYPOTHESIS | Moderate; thresholds untested | Feed/content |
| 10 | Respect focus with bounded review/gap | MVP HYPOTHESIS | Moderate principles | Scheduler/UX |
| 11 | Three-domain provisional placement | MVP HYPOTHESIS | Moderate principle; exact design untested | Onboarding |
| 12 | Qualitative, cited profile; no fake % | FREEZE NOW | Moderate | Profile/analytics |
| 13 | Optional goal, never bypass prerequisite | MVP HYPOTHESIS | Limited | Onboarding/content |
| 14 | One ~5m default, customizable cycles | MVP HYPOTHESIS | Product hypothesis | Engagement/UX |
| 15 | Retrieval-based streak separate target | MVP HYPOTHESIS | Engagement transfer limited | Rewards/offline |
| 16 | Progress/milestones, no XP farm | MVP HYPOTHESIS | Mixed/moderate | Rewards/UX |
| 17 | Browse/review/preview within constraints | MVP HYPOTHESIS | Moderate | Course map |
| 18 | One verifiable reason + details | MVP HYPOTHESIS | Limited | Feed/decision logs |

**DEFER** (không phải câu hỏi bỏ sót): Q1 causal error classifier; Q2 latency→ability; Q6 psychometric replay parameter; Q9 final mastery cutoffs; Q11 statistical CAT/CEFR certification; Q16 reward optimization; Q18 XAI model explanation. Các phương án này nằm ở later-phase của từng câu. **CHANGE REQUEST: 0 được chứng minh từ nguồn hiện có.**

## 12. Issues / Change Requests

**Implementation Issue II-01 — V3.2 source verification (blocking for contract-level implementation; not a change request yet).** Handoff nói V3.2 là authority nhưng không có full spec, migrations, checks hoặc app repo; chỉ có summary. Không đủ căn cứ khẳng định schema command/telemetry hiện hỗ trợ hint/replay/skip, times, reason, separate first attempt hay reward idempotency. Trước khi code các phần ấy: lấy bản gốc; lập mapping rule/field/transaction; chạy 115 contract + 22 SQL checks, kiểm thử pin revision, offline replay, scoring và worker. Nếu xung đột thật, mở CR với rule ID, reproduction, evidence, minimal patch, migration impact và tests. **Không tạo CR giả bằng suy đoán.**

**Implementation Issue II-02 — Phase boundary (deferrable design note).** Handoff Phase 1 nêu không chốt curriculum, mastery, adaptive path hay final risk label trước Phase 9. Bản này đề xuất guardrails PRD và rule thử nghiệm được version, **không tuyên bố freeze các tham số hoặc production policy**. Nếu bản V3.2 gốc cấm *cả* rule-based composition ở giai đoạn triển khai sau, khi đó cần CR hoặc điều chỉnh roadmap; hiện chưa có bằng chứng xung đột.

## 13. Updated Phase 1 status

**Phase 0: DONE (theo handoff). Phase 1: ACTIVE.** Research questions có bản đề xuất hoàn chỉnh, chưa phải owner-approved charter/PRD, chưa có bằng chứng repo chạy API/worker/Flutter, migration, CI và harness qua checklist Phase 1; không đạt gate DONE. Các phần thực thi Learning Core, Offline, Analytics, Learning Intelligence, Pilot lần lượt phụ thuộc Phase 5/6/8/9/15; trạng thái của chúng **DEFERRED** theo roadmap. **BLOCKED cục bộ:** đối chiếu hợp đồng V3.2 cụ thể cho các interface quan trọng khi thiếu artifact gốc; không tự động coi toàn Phase 1 blocked nếu vẫn làm được bootstrap độc lập.

## 14. Requirements to copy into Product Charter / MVP PRD

**Product Charter — các nguyên tắc cần owner xác nhận:**

1. Product học tiếng Anh A0(internal)–B2, Vocabulary/Grammar/Listening; learning evidence tách engagement/UX/giả thuyết; không hứa “AI hiểu năng lực chính xác”.
2. Finite adaptive cycle ~5 phút là giả thuyết trải nghiệm; phục vụ retrieval, spacing, feedback, transfer và delayed check; người học bấm tiếp chủ động.
3. Quyền tự chủ trong curriculum/prerequisite hợp lệ; giải thích gợi ý bằng quan sát; profile định tính có uncertainty.
4. V3.2 là authority; frozen architecture còn nguyên; các policy numbers versioned/configurable, không đóng băng mastery/risk/path trước Phase 9; 5-user pilot chỉ xác thực usability/behavior/telemetry.
5. Free-first pilot, OER/license provenance; không reward theo click hoặc biến streak thành học lực.

**MVP PRD — yêu cầu kiểm thử được:**

1. Hệ thống lưu first attempt bất biến, retry/assisted status, item/feedback revision, timestamps event/availability, source; server chấm canonical; replay command idempotent.
2. Hint theo modality trong practice; Check không hint trước submit; audio practice replay thoải mái, Check mặc định 2 play (policy version); accessibility condition hiển thị và lưu.
3. Skip tường minh, không hoàn thành/mastery; sau hai skip ở objective có support/alternative, không loop; latency optional không ảnh hưởng mastery.
4. Content object có objective, difficulty band provisional, prerequisite, item type, audio/gloss/context, answer/feedback, source/license/version; authoring review đối với distractor tag.
5. Scheduler filter published pinned revision + prerequisites; priority due/gap, focus/current objective, transfer/challenge; một reason code và evidence ref/decision, exposure và execution/outcome riêng; fallback deterministic khi ML/recommendation tắt.
6. Cycle có mục tiêu, feedback, closure, pause/resume và explicit continue; target 1/2/3+ cycles; streak bằng scored retrieval có feedback/ngày, tách target; reward server idempotent và không tác động score.
7. Onboarding có ba domain và skip Listening khi bất tiện; kết quả provisional/missingness, cập nhật qua Check sau; A0 chỉ là nội bộ; không hứa CEFR score.
8. Profile định tính theo skill/objective, evidence-backed insights và “chưa đủ bằng chứng”, report-insight action, reason explanation; không mastery %.
9. Privacy dictionary, minimum telemetry, offline replay, timezone/late-event reconciliation, content revision trace và QA audit; các ngày retention phải chốt trước pilot.
10. Acceptance test: wrong→retry correct giữ first wrong; hint/skip/replay không nâng unassisted state; stale content reject/pin; offline duplicate không cộng streak/reward; late event không leak vào earlier decision; no ML vẫn tạo chu kỳ hợp lệ; mọi reason có nguồn.

## 15. Sources and bibliography

Tra cứu web ngày **23/09/2026**. Đây là nguồn khoa học/chuẩn đo lường và dữ liệu sản phẩm để đánh giá **theo loại claim**; link dẫn tới trang nhà xuất bản/đơn vị gốc. Một số full text có paywall; trong trường hợp đó kết luận chỉ dựa trên abstract/metadata hiển thị, không diễn giải phân tích chi tiết vượt nguồn.

| ID | Nguồn, năm | Vai trò / giới hạn |
|---|---|---|
| S1 | Adesope et al., [*Rethinking the Use of Tests: A Meta-Analysis of Practice Testing*](https://journals.sagepub.com/doi/abs/10.3102/0034654316689306), 2017 | Meta-analysis practice testing; không ấn định format app. |
| S2 | Kim et al., [*The Effects of Spaced Practice on Second Language Learning*](https://onlinelibrary.wiley.com/doi/10.1111/lang.12479), 2022 | Meta-analysis L2 spacing; delayed retention khác immediate. |
| S3 | Wisniewski et al., [*The Power of Feedback Revisited*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2019.03087/full), 2020 | Meta-analysis, hiệu ứng không đồng nhất theo nội dung feedback. |
| S4 | Norris & Ortega, [*Effectiveness of L2 Instruction*](https://onlinelibrary.wiley.com/doi/abs/10.1111/0023-8333.00136), 2000; Spada & Tomita, [*Interactions Between Type of Instruction and Type of Language Feature*](https://onlinelibrary.wiley.com/doi/abs/10.1111/j.1467-9922.2010.00562.x), 2010 | Meta-analyses explicit/implicit, khác feature/outcome; không suy ra sequence duy nhất. |
| S5 | Yanagisawa et al., [*How Do Different Forms of Glossing Contribute to L2 Vocabulary Learning from Reading?*](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/how-do-different-forms-of-glossing-contribute-to-l2-vocabulary-learning-from-reading/38124150D59DF3039EE1FF5AE88FE922), 2020 | Meta-analysis gloss khi đọc; không trực tiếp chứng minh hint trong game. |
| S6 | Lei & Reynolds, [*Learning English vocabulary from word cards*](https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.984211/full), 2022 | Research synthesis; flashcard hữu ích, cần phân biệt loại knowledge. |
| S7 | Webb, [*Receptive and Productive Vocabulary Learning*](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/receptive-and-productive-vocabulary-learning-the-effects-of-reading-and-writing-on-word-knowledge/DDF362AE7B13D1949B1CD591DA2F3414), 2005 | Hai experiment, outcome và thời lượng task khác nhau. |
| S8 | Sailer & Homner, [*The Gamification of Learning: a Meta-analysis*](https://link.springer.com/article/10.1007/s10648-019-09498-w), 2020 | Dị biệt giữa game elements và outcome; không biện hộ riêng XP. |
| S9 | Duolingo, [*Improving the Streak*](https://blog.duolingo.com/improving-the-streak/), 2020 | A/B nội bộ: tách target/streak thay đổi return behavior; **chỉ engagement, không efficacy**, ngoại suy hạn chế. |
| S10 | Deci, Koestner & Ryan, [*A Meta-Analytic Review of Experiments Examining the Effects of Extrinsic Rewards on Intrinsic Motivation*](https://selfdeterminationtheory.org/wp-content/uploads/2014/04/1999_DeciKoestnerRyan_Meta.pdf), 1999 | Lo ngại với *một số* reward hữu hình; không kết luận cấm mọi reward. |
| S11 | [*Effects of Gamification on Behavioral Change in Education*](https://pubmed.ncbi.nlm.nih.gov/33805530/), 2021 | Meta-analysis hành vi; không đánh đồng hành vi với retention tiếng Anh. |
| S12 | Bolsinova et al., [*Conditional Dependence between Response Time and Accuracy*](https://pmc.ncbi.nlm.nih.gov/articles/PMC5312167/), 2017 | Tổng quan mô hình đo lường, không gán time thành ability trực tiếp. |
| S13 | Ofqual, [*Time limits and speed of working in assessments*](https://www.gov.uk/government/publications/time-limits-and-speed-of-working-in-assessments/time-limits-and-speed-of-working-in-assessments-when-and-to-what-extent-should-speed-of-working-be-part-of-what-is-assessed), 2025 | Guidance về construct-irrelevant variance của speededness. |
| S14 | Shi & Révész, [*The effects of repeating video-lecture-based tasks on learners’ L2 multimodal processing*](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/effects-of-repeating-videolecturebased-tasks-on-learners-l2-multimodal-processing-an-exploratory-study/9EA5A79606824F41997C5EBEC75845BA), online 2025 | Sơ cấp, nhóm nhỏ, lecture/video khác clip MVP; replay count không là ability. |
| S15 | Webb, [*Receptive and Productive Vocabulary Learning*](https://www.cambridge.org/core/journals/studies-in-second-language-acquisition/article/abs/receptive-and-productive-vocabulary-learning-the-effects-of-reading-and-writing-on-word-knowledge/DDF362AE7B13D1949B1CD591DA2F3414), 2005 | Tái dùng S7 để nhấn mạnh phép đo khác nhau. |
| S16 | Council of Europe, [CEFR Companion Volume](https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-companion-volume-and-its-language-versions), 2020; [CEFR levels](https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions) | Profile kỹ năng, Pre-A1; cần validation khi claim liên kết test với CEFR. |
| S17 | Council of Europe, [Developing tests and examining](https://www.coe.int/en/web/common-european-framework-reference-languages/developing-tests-examining) | Hướng dẫn xây và liên kết bài đánh giá với CEFR. |
| S18 | AERA/APA/NCME, [Standards for Educational and Psychological Testing](https://www.testingstandards.net/), 2014 | Chuẩn diễn giải/validity, không cung cấp cutoff của Mingo. |
| S19 | DataReportal, [Digital 2026 Global Overview](https://datareportal.com/reports/digital-2026-global-overview-report), 2025/2026 edition | Bối cảnh consumer/mobile; không chứng minh 5 phút tối ưu. |
| S20 | Chen et al., [*The effect of worked examples on learning solution steps*](https://www.tandfonline.com/doi/full/10.1080/01443410.2023.2273762), 2023/24 | Research guidance/cognitive load; ngoại suy từ domain khác sang grammar có giới hạn. |
| S21 | [*How effective is learner-controlled instruction under classroom conditions?*](https://www.sciencedirect.com/science/article/pii/S0023969022000704), 2022 | Systematic review; kết quả theo lứa tuổi/bối cảnh, không chốt tỷ lệ focus. |
| S22 | [*The Design, Development, and Implementation of Student-Facing Learning Analytics Dashboards*](https://eric.ed.gov/?id=EJ1194736), 2018 | Dashboard context; không chứng minh profile này cải thiện học. |
| S23 | [*Self-regulated learning training programs enhance university students’ academic performance...*](https://www.sciencedirect.com/science/article/pii/S0361476X21000357), 2021 | Meta-analysis đại học, ngoại suy sang app EFL có giới hạn. |
| S24 | Khosravi et al., [*Explainable Artificial Intelligence in education*](https://www.sciencedirect.com/science/article/pii/S2666920X22000297), 2022; Takami et al., [*Educational Explainable Recommender Usage*](https://dl.acm.org/doi/fullHtml/10.1145/3506860.3506882), 2022 | XAI/recommendation transparency; nhiều mệnh đề UI là hypothesis. |

**Acceptance gate của bản research: PASS có giới hạn.** Đã chốt một default cho 18/18 câu, phân tầng bằng chứng, xuất rule/telemetry/scheduler/pilot/PRD và đánh dấu các giả thuyết. PASS này **không** là phê duyệt owner, không chứng minh hiệu quả học, không xác minh chi tiết full V3.2 và không đóng Phase 1.
