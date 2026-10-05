# TalkBack / screen-reader — hướng dẫn thực thi thật

Trạng thái hiện tại: **BLOCKED BY ENVIRONMENT**. Các kết quả bên dưới là kỳ vọng, chưa phải kết quả quan sát. Dùng cùng ID trong TALKBACK_EVIDENCE_TEMPLATE.md. Không đánh PASS từ screenshot, DOM, AX tree hay log JavaScript.

## 1. Chuẩn bị bằng Android Studio hoặc Android thật

1. Trong Android Studio, mở Device Manager, chọn AVD mới `Mingo API 35` (`Mingo_API_35`). AVD này đã boot/Quick Boot qua Device Manager trên Windows; Android 15/API 35, TalkBack 15.0.0.639625893 và Google TTS hiện diện; speech chưa được kiểm. Chờ khởi động xong, mở khóa. Nếu AVD hiện có không phản hồi, người vận hành có thể chọn Cold Boot sau khi bảo toàn công việc; không Wipe Data để làm test pass. Đây là kiểm tra prototype thiết kế UX/UI, không phải triển khai ứng dụng production.
2. Dùng SDK platform-tools kiểm tra `adb devices -l`. Chỉ tiếp tục khi thiết bị mục tiêu có trạng thái `device`. Nếu nhiều thiết bị, luôn chỉ định `-s SERIAL`.
3. Ghi model/AVD, Android version/API/build từ About device; TalkBack version và TTS engine/version từ phần thông tin ứng dụng/cài đặt của thiết bị. Ghi Chrome version. Không suy ra API từ tên AVD.
4. Bật TalkBack trong Accessibility; xác nhận nghe được tên của một control trong Settings. Chọn giọng English phù hợp vì prototype dùng tiếng Anh. Ghi âm lượng, tốc độ nói, speech verbosity, text size và gesture mapping. Không thay đổi giữa flow mà không ghi chú.
5. Phục vụ **prototype R1 + bản sửa P2-D021** từ extraction riêng, không dùng Flutter foundation scaffold để thay cho Phase 2 UX. Trong terminal Windows chạy lệnh dưới; giữ terminal mở. Bản phục vụ là prototype QA, không phải production backend.

```powershell
& 'C:\Mingo\.venv\Scripts\python.exe' -m http.server 8765 --bind 127.0.0.1 --directory 'C:\Mingo\outputs\d021-fix-20260930\Mingo\02_product\ux_ui\phase2\prototype'
```

Nếu cổng đang được server của phiên này sử dụng, dùng server hiện có sau khi xác nhận trang đúng; không chạy chồng. Nếu đã dừng, chạy lại lệnh trên.

```powershell
& 'C:\Android\Sdk\platform-tools\adb.exe' -s SERIAL reverse tcp:8765 tcp:8765
```

6. Trong Chrome trên Android mở `http://127.0.0.1:8765/`. Với Android Emulator có thể dùng `http://10.0.2.2:8765/` nếu reverse không phù hợp và host server truy cập được. Chỉ ghi PASS sau khi thấy đúng tiêu đề “Mingo — Phase 2 UX Prototype R1”.
7. Bắt đầu ghi video **có âm thanh TalkBack thật**. Phát lại đoạn ngắn để xác nhận đã thu được tiếng. Nếu screen recorder không thu TTS, dùng microphone/thiết bị ghi riêng và đồng bộ timestamp. Không mặc định `adb screenrecord` thu được audio.
8. Xác nhận R1 base commit `a112f762ab08f6fa688cc4857b21d95d1055ab5c`, ZIP SHA-256 trong intake, và CSS bản sửa SHA-256 `df4df9ddf878db4aaf68d91aff13b609f6d2091125d87136d98eb013a3331ffb`. Tải lại trang giữa các flow độc lập để reset state mock; không reload khi đang kiểm tra sự lưu giữ first response/assisted/queue.

## 2. Cách thao tác và ghi nhận

Dùng vuốt sang phải/trái để di chuyển TalkBack focus, double-tap để kích hoạt, explore-by-touch khi cần. Nếu gesture khác trên thiết bị, ghi mapping thực tế. Không dùng click Playwright để giả tương tác TalkBack. Với mọi bước, ghi tên được đọc **nguyên văn**, role/state, focus trước/sau, thứ tự control, thông báo tự phát, và timestamp audio/video. Chờ speech queue ổn định trước bước kế tiếp; ghi nếu thông báo bị cắt, mất hoặc lặp toàn màn hình.

PASS cần vừa thao tác được vừa nghe/hiểu được thông tin bắt buộc. Khác biệt cách TTS đọc dấu câu được ghi nhận; mất tên, sai state, thiếu thông báo critical hoặc không tới được hành động là finding. Một flow không chạy được vì thiếu speech = BLOCKED, không PASS.

## 3. Learner — onboarding và Vocabulary

| ID | Thao tác | Kỳ vọng cụ thể cần nghe/quan sát |
|---|---|---|
| AT-01 | Reload, duyệt từ đầu trang | Phân biệt toolbar QA với learner; đọc được tên “Start learning”, role button; thứ tự không nhảy mất control |
| AT-02 | Start learning → Skip for now → Start without it → Go to Home | Mỗi đổi trang focus tới title mới; optional goal/placement không chặn Home; starting evidence là provisional/not enough evidence, không tự gán CEFR |
| AT-03 | Home → Start cycle → Begin | Title mới được đọc; prompt Review, các lựa chọn và Submit có tên; Submit chưa chọn là disabled và không thể advance |
| AT-04 | Chọn Hello | Đọc “Hello” với trạng thái selected/pressed; focus còn ở lựa chọn, chưa submit, không đọc lại toàn trang |
| AT-05 | Submit | Nghe feedback correctness và trạng thái saved locally/queue; không gọi là server-synced. Continue xuất hiện và tới được; ghi nguyên văn thứ tự thông báo |
| AT-06 | Continue → Continue | Qua Learn tới Retrieve; prompt “How are you?” và ba lựa chọn tới được theo thứ tự; focus route/title hợp lý |
| AT-07 | Need a hint? | Nội dung gợi ý được tiếp cận/đọc; assistance được giữ khi chọn và submit, không biến thành unaided |
| AT-08 | Chọn Go to school. → Submit | “Not quite.” và hướng dẫn retry/first response nghe được; focus không lạc ra toolbar; Try once more tới được |
| AT-09 | Try once more → I’m good, thanks. → Submit | “Correct.” và “Practice retry”/first response preserved có thể tiếp cận; retry không xóa lần sai đầu; không có retry thứ hai |
| AT-10 | Continue → Good morning! → Submit → Continue | Transfer có prompt/option/result rõ; selection và Submit tách rời; chuyển tới Check intro |
| AT-11 | Start Check | Title Check được đọc; không có hint trước submit hoặc practice retry; Submit disabled trước lựa chọn |
| AT-12 | Nice to meet you too. → Submit → Continue | Result và Summary đọc được; summary nêu assistance/evidence context, không kết luận mastered; Done for now và Continue learning đều tới được |
| AT-13 | Done for now | Quay Home, focus title hợp lý; có đường dừng hữu hạn |
| AT-14 | Lặp flow mới tới Retrieve, chọn Skip for now | “Skipped for now.” và không tạo completion/mastery; Continue tới Transfer; skip không bị đọc thành câu đúng |

## 4. Grammar và Listening

Reload → thực hiện AT-02 để vào Home. Dùng Learn rồi nút Start cycle nằm trong card tương ứng; nhiều nút cùng tên phải kiểm tra context domain có thể được hiểu bằng screen reader.

| ID | Thao tác | Kỳ vọng |
|---|---|---|
| AT-15 | Learn → Grammar / Start cycle → Begin; She is a student. → Submit → Continue → Continue | Nhận biết domain Grammar và prompt đúng; route focus/title, labels, feedback đều nghe được |
| AT-16 | is → Submit → Continue; They are classmates. → Submit → Continue; Start Check → am → Submit → Continue | Hoàn thành representative Grammar tới summary; Check không hint/retry; không cần suy đoán tên nút |
| AT-17 | Flow mới: Learn → Listening / Start cycle → Begin; kích hoạt audio control | Nghe được tên/role audio control, nội dung audio thực tế, không bị TalkBack che mất mà không có đường nghe lại; ghi riêng TTS ứng dụng và TalkBack |
| AT-18 | Hello → Submit → Continue → Continue; phát audio → I’m good, thanks. → Submit → Continue | Audio và feedback tiếp cận được; focus ổn định khi chọn, không tự advance |
| AT-19 | Phát audio → Good morning! → Submit → Continue → Start Check; phát audio tối đa hai lần | Số lượt/giới hạn và trạng thái hết lượt hiểu được qua speech; lượt thứ ba không phát; Check không hint/retry |
| AT-20 | Nice to meet you too. → Submit → Continue | Listening summary đọc được; playback không được coi là proof of listening hoặc mastery |
| AT-21 | Flow Listening mới → Begin → Simulate offline | Media unavailable đọc được; practice có Skip for now, không tạo kết quả giả. Nếu thử tại Check, chỉ Leave cycle an toàn, không submit đánh giá từ media thiếu |

## 5. Modal, navigation và sync

| ID | Thao tác | Kỳ vọng |
|---|---|---|
| AT-22 | Home → Course → locked preview | Đọc dialog title/prerequisite; vuốt tới cuối/đầu và explore-by-touch không kích hoạt nền ngoài modal; đóng trở lại đúng trigger; không unlock |
| AT-23 | Duyệt Home → Learn → Course → Profile bằng bottom nav | Đọc tên từng đích, thứ tự Home/Learn/Course/Profile; title/focus sau chuyển trang đúng; không mất action vì keyboard hoặc zoom |
| AT-24 | Flow Vocabulary mới: Begin → Simulate offline → Hello → Submit | Thông báo offline và saved locally/queued hiểu được, không đồng nghĩa synced |
| AT-25 | Simulate offline lần nữa để online; Profile → Sync status | Queue vẫn chờ server, nghe title/status; mạng online không tự biến thành All caught up |
| AT-26 | Start sync → Simulate failure → Retry safely | Nghe sync started/no acknowledgement, failure rồi retry; queue không yêu cầu nhập lại câu trả lời, không báo thành công giả |
| AT-27 | Simulate partial → Sync remaining → Simulate server acknowledgement | Partial còn pending; sau mock acknowledgement mới nghe synced. Ghi nguyên văn announcements và focus, không dùng DOM text làm speech evidence |
| AT-28 | Re-auth → Simulate re-auth complete; Canonical refresh → Refresh canonical state | Nghe session/refresh notices; local queue và canonical authority được phân biệt; xác nhận controls vẫn tới được |

## 6. Staff screen-reader smoke thật trên desktop

Dùng screen reader có speech trên Windows/desktop (ví dụ NVDA hoặc Narrator đã có), browser ở viewport tối thiểu 1024px. Ghi OS, browser, screen-reader/version, speech engine, keyboard layout và browse/focus mode. Mở cùng URL trên host. Ghi speech thực tế; Tab/Shift+Tab là keyboard test bổ sung, không thay thế speech.

| ID | Thao tác | Kỳ vọng |
|---|---|---|
| AT-29 | Reload → Staff → Content → Create draft | Dashboard/Content/editor titles đọc được; mỗi input/textarea/select có label ổn định, không chỉ placeholder; đọc tên Prompt, Correct answer, Feedback, Source reference theo label thực tế |
| AT-30 | Xóa Prompt → Submit for review | Chặn review; thông báo “Prompt and correct answer are required.” nghe được; trường cần sửa xác định được; không chuyển trạng thái thành công |
| AT-31 | Điền Prompt → Save draft → Preview → ← Editor → Submit for review | Nội dung giữ qua Preview/Review; Preview không publish; heading focus hợp lý |
| AT-32 | Review khi license chưa verified | Đọc License Needs confirmation; Approve disabled; Request changes/Open source & license có tên rõ |
| AT-33 | Open source & license → xóa Source reference → Mark verified for prototype | Nghe lỗi source required, không approve; điền source rồi Mark verified for prototype trở về review, license Verified |
| AT-34 | Approve; Tab/Shift+Tab và lệnh duyệt của screen reader; Cancel | Đọc “Publish Revision …?” và immutable warning; focus trong modal, nền không hoạt động; Cancel khôi phục tới Approve |
| AT-35 | Approve → Confirm publish | Nghe revision published và immutable; published view không Edit; historical attempts pinned, Create new draft from revision có tên rõ |
| AT-36 | Create new draft from revision | Nghe draft mới/lineage; editor của draft mới, không sửa published revision cũ |

## 7. Kết thúc

Mỗi AT-01..36 phải có actual speech/focus, PASS/FAIL/BLOCKED và evidence timestamp. Tổng hợp riêng learner TalkBack và staff screen reader. Nếu critical flow FAIL hoặc finding P0/P1: dừng gate ngay, lưu evidence, log ID mới sau D022 (D022 đã dành cho workbook), không tự sửa rồi tự ký closure. Sau fix cần impacted regression và independent closure riêng. Không tự sửa expected để hợp thức hóa speech sai.

Khi chưa nghe được speech, để BLOCKED. Chỉ khi tất cả checkpoint bắt buộc có evidence đạt yêu cầu mới chuyển kết quả session sang PASS; việc đó vẫn không thay Tech Lead/Owner acceptance.
