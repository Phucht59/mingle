# Full screen inventory V2

61screens:57preservedR1IDs plus4approvedpresentationentries(progress/search/settings/notifications).175declaredstates. Data comes from the sealed pre-rework inventory; template :id/:step is a fixture route, not a backend API. Each row is presentation only; later services/permission/auth are not implemented. No speaking/shop/AI chat route.

| ID | Role | Route | User task / heading | States |
|---|---|---|---|---|
| L-001 | learner | /launch | Mở Mingo | Loading, error, offline bootstrap |
| L-002 | learner | /welcome | Chào bạn | Default, loading |
| L-003 | learner | /onboarding/goal | Bạn muốn học để làm gì? | Default, selected, error |
| L-004 | learner | /onboarding/placement | Chọn điểm bắt đầu | Default, unavailable |
| L-005 | learner | /placement/:step | Thử một câu ngắn | Ready, selected, validation-error, submitting, result, skipped-domain, audio-unavailable |
| L-006 | learner | /placement/result | Điểm bắt đầu của bạn | Complete, insufficient-evidence |
| L-010 | learner | /home | Chào bạn! | Online, offline, syncing, nothing-due, recommendation-unavailable |
| L-011 | learner | /home?offline=1 | Học khi không có mạng | Offline, queued |
| L-012 | learner | /home?syncing=1 | Đang gửi bài đã lưu | Syncing, partial |
| L-020 | learner | /learn | Khám phá bài học | Ready, resume, content-gap |
| L-021 | learner | /learn/cycle/intro | Chào hỏi và làm quen | Ready, offline-capable, content-unavailable |
| L-022 | learner | /learn/cycle/review | Nhớ lại một chút | Ready, selected, validation-error, submitted-result, skipped |
| L-023 | learner | /learn/cycle/learn | Một cách chào mới | Ready, audio-loading, audio-unavailable |
| L-024 | learner | /learn/cycle/retrieve | Thử tự nhớ | Ready, selected, hinted, submitted-result, retry-available, retry-exhausted, skipped |
| L-025 | learner | /learn/cycle/transfer | Dùng trong tình huống mới | Ready, selected, validation-error, submitted-result, skipped |
| L-026 | learner | /learn/cycle/check-intro | Thử không cần gợi ý | Ready |
| L-027 | learner | /learn/cycle/check | Chọn lời chào phù hợp | Ready, selected, validation-error, submitting, result, audio-ready, audio-unavailable, play-limit-reached |
| L-028 | learner | /learn/feedback/correct | Bạn đã tìm ra rồi | Default |
| L-029 | learner | /learn/feedback/retry | Thử thêm một lần | Retry available, retry used, retry exhausted |
| L-030 | learner | /learn/hint | Một gợi ý nhỏ | Default, unavailable |
| L-031 | learner | /learn/skip | Bạn có thể quay lại | Default |
| L-032 | learner | /learn/cycle/summary | Những gì bạn vừa luyện | Complete, partial, sync-queued |
| L-033 | learner | /learn/resume | Tiếp tục từ đây | Resume, stale-content refresh |
| L-040 | learner | /course | Lộ trình của bạn | Open, due-review, locked, empty |
| L-041 | learner | /course/objective/:id | Chào hỏi cơ bản | Eligible, due, locked, insufficient-evidence |
| L-042 | learner | /course/objective/:id/preview | Bài học phía trước | Preview-open, preview-close |
| L-050 | learner | /profile | Góc của bạn | Default, insufficient-evidence |
| L-051 | learner | /profile/evidence/:domain | Điều bạn đã thực hành | Building, more-evidence-needed |
| L-052 | learner | /profile/goal | Mục tiêu học tập | Default, saved, error |
| L-053 | learner | /profile/preferences | Cách bạn muốn học | Default, saved |
| L-054 | learner | /profile/offline | Bài học ngoại tuyến | Available, downloading, downloaded, expired, failed |
| L-060 | learner | /sync | Bài đã lưu trên máy | offline-available, local-queued, syncing, synced, partial |
| L-061 | learner | /sync/error | Cần bạn kiểm tra | failed-retryable, reauth, canonical-refresh, media-unavailable |
| L-062 | learner | /error | Mình thử lại nhé | Recoverable, fatal |
| L-063 | learner | /learn/empty | Sẵn sàng khi bạn muốn | Nothing-due, no-valid-cycle, media-unavailable |
| L-064 | learner | /reauth | Cần đăng nhập lại | Default |
| S-001 | staff | /staff | Không gian nhân viên | Loading, access-required |
| S-010 | staff | /staff/dashboard | Công việc hôm nay | Default, empty, partial |
| S-020 | staff | /staff/learners | Học viên | Loading, empty, filtered, error |
| S-021 | staff | /staff/learners/:id | Hồ sơ học viên | Default, insufficient-evidence, access-denied |
| S-022 | staff | /staff/learners/:id/evidence | Bằng chứng học tập | Loading, no-evidence |
| S-023 | staff | /staff/learners/:id/activity | Hoạt động gần đây | Default, empty |
| S-030 | staff | /staff/content | Nội dung học | Default, empty, filtered |
| S-031 | staff | /staff/content/drafts/:id | Soạn bài học | clean, dirty, saving, saved, validation-error, reviewer-changes |
| S-032 | staff | /staff/content/drafts/:id/preview | Xem trước bài học | preview |
| S-033 | staff | /staff/content/drafts/:id/source | Nguồn và giấy phép | license-pending, license-verified, validation-error |
| S-034 | staff | /staff/content/review | Hàng chờ duyệt | Empty, filtered |
| S-035 | staff | /staff/content/review/:id | Kiểm tra bài học | license-blocked, approvable, changes-requested |
| S-036 | staff | /staff/content/publish/:id | Xác nhận xuất bản | confirmation-open, processing, error |
| S-037 | staff | /staff/content/published/:id | Bản đã xuất bản | published-immutable, new-draft-created |
| S-040 | staff | /staff/interventions | Hỗ trợ học viên | Placeholder, empty |
| S-041 | staff | /staff/interventions/:id | Chi tiết hỗ trợ | Placeholder, unavailable |
| S-050 | staff | /staff/analytics | Phân tích học tập | Placeholder, no-data |
| S-051 | staff | /staff/analytics/:metric | Chi tiết chỉ số | Placeholder, insufficient-data |
| S-060 | staff | /staff/admin | Quản trị | Placeholder, access-denied |
| S-061 | staff | /staff/admin/roles | Vai trò | Placeholder |
| S-062 | staff | /staff/admin/audit | Lịch sử thao tác | Placeholder, filtered |
| L-070 | learner | /progress | Những bước bạn đã đi | observations, insufficient-evidence |
| L-071 | learner | /learn/search | Tìm bài học | ready, filtered, empty |
| L-072 | learner | /profile/settings | Cài đặt | ready, saved |
| L-073 | learner | /notifications | Thông báo | ready, empty |

Screenshot/state linkage is in SCREEN_STATE_TRACEABILITY.csv. Captures show one viewport; scrollable detail is reachable but may be outside that screenshot. Matrix tests check all175states at20size/scale combinations, not backend outcomes. Future screens display explicit reference placeholders.
