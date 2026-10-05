# Checklist QA — Phase 1 và Phase 2 V2

Điền tên người kiểm thử, ngày, OS/thiết bị, build SHA và bằng chứng trong bản kết quả riêng. Những ô dưới đây đang **PENDING**; đây không phải biên bản QA đã chạy.

## Phase 1 foundation

- [ ] Xác nhận API live/ready, worker hoàn tất probe bền vững, PostgreSQL concurrency và storage theo [runbook](04_SOURCE/04_Van_hanh/Runbook/PHASE1_FOUNDATION.md). Phân biệt 7 skipped của lượt unit với 6 ca PostgreSQL chạy riêng.
- [ ] Chạy lại các kiểm tra Phase 1 trên môi trường QA khi có dependencies; đối chiếu [log baseline](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/phase1_revalidation_pwsh.log).
- [ ] Xác nhận backend/V3.2 không bị sửa về business rule; [hash và test V3.2](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/V3_2_INTEGRITY_REPORT.md).

## Learner Android/Web

- [ ] Onboarding tùy chọn → mục tiêu → Home có một hành động chính, nhãn “dữ liệu mẫu” rõ.
- [ ] Đi hết Vocabulary, Grammar và Listening qua Review → Learn → Retrieve → Transfer → Check → Summary; nội dung/ngữ cảnh từng loại bài khác nhau.
- [ ] Trả lời sai lần đầu, xem feedback, retry một lần; Back của Android giữ đúng loại bài và phản hồi. Check không lộ hint; skipped/assisted không bị ghi nhận thành câu đúng độc lập.
- [ ] Search, empty state, locked objective, offline/recovery, unavailable/submitting/revision-invalid/corrupt states có giải thích và hành động phù hợp, không tiến bài khi thiếu nội dung.
- [ ] Kiểm tra 320px/200%, 360/412/430px, nhãn điều hướng, 48dp, tương phản, reduced motion; TalkBack đọc tên/focus/feedback thực tế.
- [ ] Nghe sample audio trên thiết bị có âm thanh; Android test trước đó chỉ chứng minh khởi tạo playback trên emulator `-no-audio`.

## Staff Web

- [ ] Dashboard → học viên → chứng cứ học; access-denied/empty/no-evidence không lộ hồ sơ hoặc kết luận.
- [ ] Draft → preview → nguồn/giấy phép → review → xác nhận mẫu; Escape đóng modal; published sample và draft tách biệt. Đây là fixture, không phải publication server thật.
- [ ] 600px mở menu rồi chọn Nội dung phải đóng menu và hiển thị đúng trang; kiểm tra thêm 1280/1440/1920px và keyboard focus.

## Kiểm tra độc lập và gate

- [ ] Đối chiếu [195 ảnh](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/SCREENSHOT_GALLERY.html), [screen/state traceability](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/SCREEN_STATE_TRACEABILITY.csv), [PRD traceability](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/PRD_TRACEABILITY_V2.csv); ghi nhận lỗi bằng screenshot/steps.
- [ ] Rà D021 Linux R1 và ra quyết định closure riêng; bốn ca V2 Windows không tự đóng finding cũ.
- [ ] Mở cả workbook D022 original và corrected, kiểm tra hiển thị/dashboard, ghi quyết định độc lập; [hash](04_SOURCE/03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/d022_preservation.json) chỉ chứng minh bảo toàn byte.
- [ ] Product Owner, Tech Lead, content và accessibility reviewer ghi nhận kết quả thực, [yêu cầu human gate](04_SOURCE/02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2/HUMAN_APPROVAL_REQUIRED.md). Giữ Phase 3 HOLD cho đến khi gate hợp lệ.
