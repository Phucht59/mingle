# Product Owner UAT — Phase 2

**PENDING.** Đây là prototype UX với mock state; UAT không phải kiểm chứng hiệu quả học tập hoặc production backend. Candidate R1 và independent technical PASS giữ nguyên. Mở prototype bằng hướng dẫn server trong TALKBACK_MANUAL_RUNBOOK.md; dùng desktop Chrome cho staff và Android/viewport learner cho learner.

Trình bày từng nhóm dưới, chờ người dùng xem/ghi nhận rồi mới sang nhóm kế. Không dump 57 screens. Feedback giữa nhóm không phải signoff. Mọi hàng dưới chưa được Owner thực thi/chấp nhận.

## Nhóm 1 — lần đầu và Home (khoảng 5 phút)

1. First-use demo → Start learning → chọn goal → Continue → Take placement. Trả lời Vocabulary `Hello`, Grammar `She is here.`, Listening sau phát audio chọn `Good morning`; mỗi lần Submit rồi Next. Xem starting point provisional, Go to Home.
2. First-use demo → Start learning → Skip for now → Start without it → Go to Home. Goal và placement thật sự optional; không có chứng nhận CEFR giả.
3. Home: nhận ra đề xuất, reason, khoảng thời gian và Start cycle. Toolbar No recommendation: vẫn có Browse eligible cycles; Nothing due: giải thích chưa có eligible work, không giả hoàn thành khóa.

Owner quan sát: có hiểu bước đầu và biết bắt đầu ở đâu không? Ghi vấn đề/ảnh cụ thể. Kết quả nhóm: ______.

## Nhóm 2 — vòng Vocabulary, assistance và đường dừng (5–8 phút)

1. Home → Start cycle → Begin → Hello → Submit → Continue → Continue.
2. Retrieve: Need a hint? → Go to school. → Submit → Try once more → I’m good, thanks. → Submit. Hiểu sai lần đầu, assistance và practice retry; retry không xóa first response, chỉ một retry.
3. Continue → Good morning! → Submit → Continue → Start Check → Nice to meet you too. → Submit → Continue. Check không hint/retry. Summary trình bày evidence context, assistance và Done for now; không mastery/reward giả.
4. Chạy vòng mới tới Retrieve → Skip for now → Continue. Skip rõ nghĩa, không được coi là completion/correct.

Owner quan sát: feedback có dễ hiểu và hỗ trợ học không? Có biết khi nào kết thúc không? Kết quả nhóm: ______.

## Nhóm 3 — Grammar / Listening (5–8 phút)

1. Learn → card Grammar / Start cycle → Begin. Review `She is a student.`; Retrieve `is`; Transfer `They are classmates.`; Check `am`. Dùng Submit/Continue và Start Check theo từng bước. Xem summary.
2. Learn → card Listening / Start cycle → Begin. Phát audio trước khi trả lời: Review `Hello`; Retrieve `I’m good, thanks.`; Transfer `Good morning!`; Check `Nice to meet you too.`. Check tối đa hai lần phát theo prototype policy, không hint/retry.
3. Flow Listening mới → Simulate offline ở bước cần media: phải giải thích media unavailable và đường skip/leave phù hợp, không tự ghi điểm.

Owner quan sát: phân biệt practice/Check và tình trạng audio có rõ không? Kết quả nhóm: ______.

## Nhóm 4 — course, profile, offline/sync (5 phút)

1. Course → locked preview → đóng: biết prerequisite và không unlock ngoài điều kiện.
2. Profile: “Building”, “Needs more evidence”, không phần trăm mastery/diagnosis giả. Edit goal → Save goal không thay evidence.
3. Vocabulary Begin → Simulate offline → Hello → Submit: saved locally/queued. Bật online bằng Simulate offline lần nữa, Profile → Sync status: chưa tự synced.
4. Start sync → Simulate failure → Retry safely; Simulate partial → Sync remaining; Simulate server acknowledgement: chỉ sau ack mới synced. Re-auth/Canonical refresh là recovery riêng, không yêu cầu submit duplicate answer.

Owner quan sát: có phân biệt “trên thiết bị” và “server đã nhận” không? Kết quả nhóm: ______.

## Nhóm 5 — staff lifecycle (5–8 phút)

1. Staff → Dashboard: mock operational shell được thể hiện rõ.
2. Content → Create draft → sửa Prompt/Correct answer/Feedback → Save draft → Preview → ← Editor. Nội dung giữ, Preview không publish. Thử trống Prompt → Submit for review: phải có lỗi, rồi điền lại để tiếp tục.
3. Submit for review: license chưa xác nhận thì Approve disabled. Request changes → sửa draft → Submit for review → Open source & license. Source rỗng phải bị chặn; điền source → Mark verified for prototype.
4. Approve → đọc immutable warning → Cancel → Approve → Confirm publish. Xem Published revision read-only, không Edit; historical attempts pin đúng revision.
5. Create new draft from revision: có draft/revision mới, bản Published trước không bị sửa.

Owner quan sát: có hiểu hậu quả publish, license gate và cách sửa nội dung đã publish không? Kết quả nhóm: ______.

## Quyết định sau khi đã xem các nhóm

Product Owner UAT decision: **ACCEPT, REJECT, hay NEED CHANGES?**

Name/role: ______. Decision: ______. Date: ______. Evidence/explicit message: ______. Required changes: ______.

Không suy diễn “trông ổn” thành ACCEPT. Nếu phát hiện lỗi, log targeted defect mới; không khởi động lại Phase 2 từ đầu. Các quyết định D021/D022, Tech Lead và real AT vẫn riêng biệt. Final gate acknowledgement chỉ hỏi sau khi TalkBack PASS và đủ signoff/disposition.
