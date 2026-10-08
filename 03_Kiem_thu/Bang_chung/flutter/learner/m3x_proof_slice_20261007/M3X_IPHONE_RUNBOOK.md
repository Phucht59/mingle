# Chạy proof M3.X trên iPhone Air

**Trạng thái hiện tại: source đã chuẩn bị; iOS chưa build, chưa ký, chưa chạy.** iPhone Air/iOS 27 beta là thông tin chủ máy cung cấp; cần ghi phiên bản beta/build chính xác. Các bước dưới đây tạo một lượt bằng chứng mới, không sửa các bản ghi NOT EXECUTED hiện tại.

Gói `MINGO_M3X_IPHONE_SOURCE_BUILD_INPUT_20261007.zip` chứa source có manifest, iOS host chuẩn do Flutter 3.32.8 sinh, và báo cáo host. Không có IPA hay chứng chỉ. Dùng Flutter **3.32.8 / Dart 3.8.1** trước. Nếu Xcode/iOS beta không tương thích, giữ log lỗi và ghi implementation issue; không tự nâng toàn bộ dependencies để làm mất khả năng so sánh.

Mac/Xcode và development signing là điều kiện để chạy Flutter trên iPhone. Làm theo [hướng dẫn iOS chính thức của Flutter](https://docs.flutter.dev/platform-integration/ios/setup) cho thiết lập Xcode, CocoaPods, Trust và Developer Mode. Trang hiện hành mô tả SDK mới hơn; phần source của proof vẫn giữ SDK đã pin. Chưa có kết luận phiên bản Xcode nào tương thích với beta cụ thể của máy này.

## 1. Chuẩn bị và ghi môi trường

1. Trên iPhone, mở Cài đặt → Cài đặt chung → Giới thiệu. Ghi **tên model, phiên bản iOS đầy đủ và build number**. Không cần ghi serial/IMEI.
2. Trên Mac, kết nối iPhone qua USB, mở khóa và xác nhận Trust. Bật Developer Mode theo hướng dẫn hệ thống. Ghi macOS và Xcode thực tế.
3. Giải nén ZIP vào thư mục mới dành riêng cho lượt proof. Giữ nguyên manifest và source gốc. Từ thư mục gốc vừa giải nén:

```bash
mkdir -p device-run
sw_vers > device-run/macos.txt
xcodebuild -version > device-run/xcode.txt
flutter --version > device-run/flutter.txt
flutter doctor -v > device-run/doctor.txt
flutter devices --machine > device-run/devices.json
cp -R generated-ios/ios source/01_San_pham/apps/learner/ios
cd source/01_San_pham/apps/learner
flutter pub get
```

4. `generated-ios/ios` có deployment target template 12.0 và bundle ID placeholder `com.example.adaptiveLearner`. Chưa có chứng cứ về minimum OS. Các registrant/config chứa đường dẫn Windows đã bị loại khỏi ZIP; Flutter trên Mac sẽ sinh lại.
5. Mở `ios/Runner.xcworkspace` trong Xcode. Ở Runner → Signing & Capabilities, chọn development team của người chạy và một bundle ID riêng cho bản proof. Ghi bundle ID đã dùng vào biên bản. Nếu dùng nhiều bản cài để lặp fixture, ghi rõ bản nào tương ứng video nào. Không đưa certificate/private key vào evidence.

## 2. Build và chạy simulator trước

1. Mở simulator phù hợp từ Xcode, lấy device ID trong `flutter devices`.
2. Chạy các lệnh sau từ thư mục learner. Lưu stdout/stderr và exit code vào `device-run` bằng cơ chế ghi terminal của Mac:

```bash
flutter analyze --no-pub
flutter test --no-pub
flutter build ios --simulator --debug --dart-define=MINGO_M3X_PROOF=true
flutter test integration_test/m3x_proof_test.dart -d '<simulator-id>'
```

3. Nếu build hoặc integration fail, giữ nguyên log đầu tiên, sửa đúng lỗi và tạo log mới. Một simulator pass vẫn chưa đủ đóng VoiceOver/physical durability gate. Integration test tạo tên store riêng theo run ID; nó không xóa dữ liệu fixture đang review.

## 3. Cài bản release để kiểm tra tắt app và mở lại

1. Chọn ID của iPhone trong `flutter devices`. Chạy:

```bash
flutter run --release -d '<iphone-id>' --dart-define=MINGO_M3X_PROOF=true --dart-define=MINGO_M3X_OFFLINE=true --dart-define=MINGO_M3X_WITHHOLD_ACK=true
```

2. Dùng **release** cho lượt force-quit → mở từ icon để tránh phụ thuộc vòng đời debug/JIT. Ghi command, build mode và source manifest vào biên bản. Nếu máy không mở được bản release, ghi FAIL/build issue; không thay bằng background/foreground rồi gọi process-death pass.
3. Đây là fixture danh tính hợp lệ và server điều khiển trong app. `OFFLINE`/`WITHHOLD_ACK` là trạng thái transport mẫu, không tự phản ánh Wi-Fi/airplane mode của iPhone. Chúng cho phép kiểm tra “kết nối lại chưa phải ACK” một cách xác định; real networking là debt riêng.

## 4. Video A — pending, tắt tiến trình, Resume, ACK

1. Bắt đầu ghi màn hình. Ghi text size mặc định, appearance, VoiceOver off, Reduce Motion/Transparency off.
2. Tại Hôm nay, ghi vị trí nội dung. Nếu nội dung có thể cuộn trên thiết lập hiện tại, dừng ở một vị trí khác đầu trang. Bấm **Tiếp tục bài học**. Tab bar phải biến mất trong Practice.
3. Chọn **No, I need a taxi.** → **Kiểm tra**. Phải thấy “Đã lưu trên thiết bị • chờ đồng bộ”; chưa có verdict/score xác nhận. Không có biểu tượng báo đã đồng bộ.
4. Bấm **Đóng**. Home phải giữ đúng ngữ cảnh/vị trí. Bấm Resume; câu đã chọn và trạng thái pending phải còn.
5. Từ Xcode, mở thiết bị → ứng dụng proof → Download Container nếu công cụ hỗ trợ. Lưu bản `before-kill.xcappdata`. Trong container, tìm `Library/Application Support/m3x_authenticated_fixture/learning.json` (vị trí gốc Application Support có thể được hệ thống thể hiện khác). Giữ cả envelope `bytes` và checksum.
6. Mở app switcher và **vuốt đóng hẳn app proof**, không chỉ về màn hình chính. Nếu dùng công cụ termination của Xcode thay thế, ghi tên thao tác và log. Video cần thể hiện đóng app rồi bấm icon mở lại.
7. Mở app từ icon → Resume. Kiểm tra cùng prompt, lựa chọn, điều kiện, bản ghi đầu và pending. Download Container thành `after-relaunch.xcappdata`. So sánh `commandId`, `attemptId`, nguyên chuỗi command `bytes`, item/revision, firstResponse và origin với bản trước. Chỉ chuyển app nền rồi mở lại không đủ.
8. Đóng về Home → menu **…** → **Sync Recovery** → **Kết nối lại • chưa ACK** → **Thử đồng bộ**. Vẫn phải pending, chưa verdict/đã đồng bộ.
9. Bấm **Cho server fixture trả ACK**. Chỉ sau bước này mới hiện **Đã đồng bộ**. Đóng → Resume: verdict sai và explanation phải mở ngay trong đáp án taxi.
10. Bấm **Các lần trả lời**, ghi lần đầu. Đóng sheet → **Thử lại** → chọn **Yes, I have a reservation.** → Kiểm tra. Lần đầu taxi vẫn giữ, lần sau ghi có hỗ trợ; đúng không tự hiện Retry theo policy mặc định. Export container cuối, đối chiếu hai attempt/command ID khác nhau.

Giữ video gốc liên tục, container và log. Bản `server_receipts.json` là ledger fixture; các lệnh retry transport không được tạo thêm attempt cho cùng command. Các replay/changed-payload negative cases đã có test domain, nhưng chỉ đánh dấu DEVICE PASS cho trường hợp thực sự chạy/đối chiếu trên máy.

## 5. Video B — VoiceOver và Focus

1. Dùng một bản cài proof mới/disposable để có lượt Practice chưa submit, hoặc ghi rõ container hiện tại và test phần Resume đã có. **Trước khi reset bản proof, lưu container của lượt trước.** Không xóa app/dữ liệu sản phẩm khác.
2. Bật VoiceOver trong Cài đặt → Trợ năng; dùng ngôn ngữ/giọng đọc thực tế, ghi vào biên bản. Ghi màn hình có tiếng hoặc dùng một máy khác quay kèm tiếng nếu iOS không thu được VoiceOver.
3. Vuốt qua prompt, ý định và từng đáp án. Ghi VoiceOver đọc **tên, vai trò, trạng thái chọn, enabled/disabled** ra sao. Chọn đáp án taxi; nó phải truyền đạt đã chọn trong nhóm chọn một.
4. Focus nút Kiểm tra và kích hoạt. Dùng ACK được phép cho lượt này (bản build không có WITHHOLD_ACK hoặc bật ACK qua Sync Recovery). Verdict chỉ được thông báo một lần cho submit mới. Focus không tự nhảy lên đầu màn hình.
5. Duyệt tiếp: verdict → explanation → câu sửa phải gắn với đáp án đã chọn, đọc đủ và có hành động tiếp theo. Đóng/mở response sheet phải có focus hợp lý.
6. Đóng → Home → Resume. Ghi việc quay đúng origin và không lặp thông báo verdict như một kết quả mới. Nếu VoiceOver gọi vai trò/state không rõ, ghi chính xác lời đọc và vị trí lỗi; semantics “button + selected” chưa được chốt trước lượt này.

## 6. Text, appearance, thao tác native và fixture phụ

1. Ở Cài đặt → Trợ năng → Màn hình & cỡ chữ → Chữ lớn hơn, bật các cỡ trợ năng và chọn cỡ lớn nhất. Ghi tên/vị trí slider. Kiểm tra Practice, feedback, response sheet, Result và Sync Recovery: không cắt chữ thiết yếu; đáp án tăng chiều cao; nút chính cuộn tới được; không đè safe area.
2. Bật Reduce Motion; lặp submit/feedback ở một fixture mới. Phải hiểu kết quả khi không có animation. Bật Reduce Transparency và Increase Contrast; kiểm tra bars/sheets/answer, rồi lặp ở Dark Mode. Ghi từng cấu hình riêng.
3. Kiểm tra Close, sheet dismiss, tab đổi qua lại và cử chỉ hệ thống. Không dùng Back thay Close. Kiểm tra cả vùng bấm **…**, Đóng, answer, primary CTA, sheet actions đạt ít nhất 44×44 logical points bằng inspector/measurement nếu có.
4. Menu **… → Independent Check**: trước submit không có Hint. Chọn một câu, đóng và Resume; điều kiện/item phải giữ. Không tự retry sau khi đã gửi.
5. **Result**: Xong là chính; Học tiếp mở một quyết định mới, không tự chạy bài. **Result Pending Sync**: lời kết phiên mẫu không tuyên bố server đã ghi nhận. Fixture pending chỉ seed một lần mỗi installation/key; sau ACK, nó phải thể hiện synced trung thực. Dùng bản proof mới cho lần demo pending tiếp theo.
6. **Welcome • anchor polish**: Bắt đầu chính; Khám phá trước phụ và đi tới shell Học. Đây là anchor fixture, không phải onboarding/Auth hoàn chỉnh.

## 7. Performance và haptic experiment

1. Chạy bản profile với cùng source:

```bash
flutter run --profile -d '<iphone-id>' --dart-define=MINGO_M3X_PROOF=true
```

2. Thu trace Flutter DevTools khi chọn → submit → inline feedback và Close → Resume; lưu trace gốc cùng build/settings, ghi frame bị trễ và độ phản hồi quan sát được. Muốn lặp nhiều lượt chưa submit, dùng fixture installation mới sau khi lưu evidence. Không suy ra 60/120fps từ cảm giác hoặc từ widget test.
3. Haptic mặc định tắt. Chỉ chạy lượt riêng với `--dart-define=MINGO_M3X_HAPTICS=true` để đánh giá selection haptic trên phần cứng. Không có haptic phạt câu sai; không chốt haptic trước review.

## 8. Gửi lại bộ evidence và xét gate

Ghi vào một thư mục mới `device-run-<thời điểm>`: source manifest, build logs/exit codes, model/iOS beta/build/macOS/Xcode/Flutter, build mode, text size, ngôn ngữ VoiceOver, appearance/contrast/motion/transparency, video gốc, screenshots, container trước/sau kill và sau ACK, trace profile, bảng từng case PASS/FAIL/NOT EXECUTED với lỗi quan sát được. Chỉ chia sẻ container fixture; không đưa signing secrets hoặc dữ liệu cá nhân khác.

Gate hiện tại vẫn **HOLD**. Có iPhone chưa đủ để đóng gate; cần bản build chạy được và evidence các ca bắt buộc. Lượt này không đóng M3 tổng thể, customer validation, certification hoặc các debt ngoài slice.
