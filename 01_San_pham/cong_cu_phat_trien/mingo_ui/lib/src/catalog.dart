// Generated from the preserved R1 inventory; see SCREEN_CATALOG.json.
import 'package:flutter/foundation.dart';

@immutable
class ScreenSpec {
  const ScreenSpec(this.id, this.route, this.title, this.states);
  final String id, route, title;
  final List<String> states;
  bool get staff => id.startsWith('S');
}

const screens = <ScreenSpec>[
  ScreenSpec("L-001", "/launch", "Mở Mingo", [
    "Loading",
    "error",
    "offline bootstrap",
  ]),
  ScreenSpec("L-002", "/welcome", "Chào bạn", ["Default", "loading"]),
  ScreenSpec("L-003", "/onboarding/goal", "Bạn muốn học để làm gì?", [
    "Default",
    "selected",
    "error",
  ]),
  ScreenSpec("L-004", "/onboarding/placement", "Chọn điểm bắt đầu", [
    "Default",
    "unavailable",
  ]),
  ScreenSpec("L-005", "/placement/:step", "Thử một câu ngắn", [
    "Ready",
    "selected",
    "validation-error",
    "submitting",
    "result",
    "skipped-domain",
    "audio-unavailable",
  ]),
  ScreenSpec("L-006", "/placement/result", "Điểm bắt đầu của bạn", [
    "Complete",
    "insufficient-evidence",
  ]),
  ScreenSpec("L-010", "/home", "Chào bạn!", [
    "Online",
    "offline",
    "syncing",
    "nothing-due",
    "recommendation-unavailable",
  ]),
  ScreenSpec("L-011", "/home?offline=1", "Học khi không có mạng", [
    "Offline",
    "queued",
  ]),
  ScreenSpec("L-012", "/home?syncing=1", "Đang gửi bài đã lưu", [
    "Syncing",
    "partial",
  ]),
  ScreenSpec("L-020", "/learn", "Khám phá bài học", [
    "Ready",
    "resume",
    "content-gap",
  ]),
  ScreenSpec("L-021", "/learn/cycle/intro", "Chào hỏi và làm quen", [
    "Ready",
    "offline-capable",
    "content-unavailable",
  ]),
  ScreenSpec("L-022", "/learn/cycle/review", "Nhớ lại một chút", [
    "Ready",
    "selected",
    "validation-error",
    "submitted-result",
    "skipped",
  ]),
  ScreenSpec("L-023", "/learn/cycle/learn", "Một cách chào mới", [
    "Ready",
    "audio-loading",
    "audio-unavailable",
  ]),
  ScreenSpec("L-024", "/learn/cycle/retrieve", "Thử tự nhớ", [
    "Ready",
    "selected",
    "hinted",
    "submitted-result",
    "retry-available",
    "retry-exhausted",
    "skipped",
  ]),
  ScreenSpec("L-025", "/learn/cycle/transfer", "Dùng trong tình huống mới", [
    "Ready",
    "selected",
    "validation-error",
    "submitted-result",
    "skipped",
  ]),
  ScreenSpec("L-026", "/learn/cycle/check-intro", "Thử không cần gợi ý", [
    "Ready",
  ]),
  ScreenSpec("L-027", "/learn/cycle/check", "Chọn lời chào phù hợp", [
    "Ready",
    "selected",
    "validation-error",
    "submitting",
    "result",
    "audio-ready",
    "audio-unavailable",
    "play-limit-reached",
  ]),
  ScreenSpec("L-028", "/learn/feedback/correct", "Bạn đã tìm ra rồi", [
    "Default",
  ]),
  ScreenSpec("L-029", "/learn/feedback/retry", "Thử thêm một lần", [
    "Retry available",
    "retry used",
    "retry exhausted",
  ]),
  ScreenSpec("L-030", "/learn/hint", "Một gợi ý nhỏ", [
    "Default",
    "unavailable",
  ]),
  ScreenSpec("L-031", "/learn/skip", "Bạn có thể quay lại", ["Default"]),
  ScreenSpec("L-032", "/learn/cycle/summary", "Những gì bạn vừa luyện", [
    "Complete",
    "partial",
    "sync-queued",
  ]),
  ScreenSpec("L-033", "/learn/resume", "Tiếp tục từ đây", [
    "Resume",
    "stale-content refresh",
  ]),
  ScreenSpec("L-040", "/course", "Lộ trình của bạn", [
    "Open",
    "due-review",
    "locked",
    "empty",
  ]),
  ScreenSpec("L-041", "/course/objective/:id", "Chào hỏi cơ bản", [
    "Eligible",
    "due",
    "locked",
    "insufficient-evidence",
  ]),
  ScreenSpec("L-042", "/course/objective/:id/preview", "Bài học phía trước", [
    "Preview-open",
    "preview-close",
  ]),
  ScreenSpec("L-050", "/profile", "Góc của bạn", [
    "Default",
    "insufficient-evidence",
  ]),
  ScreenSpec("L-051", "/profile/evidence/:domain", "Điều bạn đã thực hành", [
    "Building",
    "more-evidence-needed",
  ]),
  ScreenSpec("L-052", "/profile/goal", "Mục tiêu học tập", [
    "Default",
    "saved",
    "error",
  ]),
  ScreenSpec("L-053", "/profile/preferences", "Cách bạn muốn học", [
    "Default",
    "saved",
  ]),
  ScreenSpec("L-054", "/profile/offline", "Bài học ngoại tuyến", [
    "Available",
    "downloading",
    "downloaded",
    "expired",
    "failed",
  ]),
  ScreenSpec("L-060", "/sync", "Bài đã lưu trên máy", [
    "offline-available",
    "local-queued",
    "syncing",
    "synced",
    "partial",
  ]),
  ScreenSpec("L-061", "/sync/error", "Cần bạn kiểm tra", [
    "failed-retryable",
    "reauth",
    "canonical-refresh",
    "media-unavailable",
  ]),
  ScreenSpec("L-062", "/error", "Mình thử lại nhé", ["Recoverable", "fatal"]),
  ScreenSpec("L-063", "/learn/empty", "Sẵn sàng khi bạn muốn", [
    "Nothing-due",
    "no-valid-cycle",
    "media-unavailable",
  ]),
  ScreenSpec("L-064", "/reauth", "Cần đăng nhập lại", ["Default"]),
  ScreenSpec("S-001", "/staff", "Không gian nhân viên", [
    "Loading",
    "access-required",
  ]),
  ScreenSpec("S-010", "/staff/dashboard", "Công việc hôm nay", [
    "Default",
    "empty",
    "partial",
  ]),
  ScreenSpec("S-020", "/staff/learners", "Học viên", [
    "Loading",
    "empty",
    "filtered",
    "error",
  ]),
  ScreenSpec("S-021", "/staff/learners/:id", "Hồ sơ học viên", [
    "Default",
    "insufficient-evidence",
    "access-denied",
  ]),
  ScreenSpec("S-022", "/staff/learners/:id/evidence", "Bằng chứng học tập", [
    "Loading",
    "no-evidence",
  ]),
  ScreenSpec("S-023", "/staff/learners/:id/activity", "Hoạt động gần đây", [
    "Default",
    "empty",
  ]),
  ScreenSpec("S-030", "/staff/content", "Nội dung học", [
    "Default",
    "empty",
    "filtered",
  ]),
  ScreenSpec("S-031", "/staff/content/drafts/:id", "Soạn bài học", [
    "clean",
    "dirty",
    "saving",
    "saved",
    "validation-error",
    "reviewer-changes",
  ]),
  ScreenSpec(
    "S-032",
    "/staff/content/drafts/:id/preview",
    "Xem trước bài học",
    ["preview"],
  ),
  ScreenSpec(
    "S-033",
    "/staff/content/drafts/:id/source",
    "Nguồn và giấy phép",
    ["license-pending", "license-verified", "validation-error"],
  ),
  ScreenSpec("S-034", "/staff/content/review", "Hàng chờ duyệt", [
    "Empty",
    "filtered",
  ]),
  ScreenSpec("S-035", "/staff/content/review/:id", "Kiểm tra bài học", [
    "license-blocked",
    "approvable",
    "changes-requested",
  ]),
  ScreenSpec("S-036", "/staff/content/publish/:id", "Xác nhận xuất bản", [
    "confirmation-open",
    "processing",
    "error",
  ]),
  ScreenSpec("S-037", "/staff/content/published/:id", "Bản đã xuất bản", [
    "published-immutable",
    "new-draft-created",
  ]),
  ScreenSpec("S-040", "/staff/interventions", "Hỗ trợ học viên", [
    "Placeholder",
    "empty",
  ]),
  ScreenSpec("S-041", "/staff/interventions/:id", "Chi tiết hỗ trợ", [
    "Placeholder",
    "unavailable",
  ]),
  ScreenSpec("S-050", "/staff/analytics", "Phân tích học tập", [
    "Placeholder",
    "no-data",
  ]),
  ScreenSpec("S-051", "/staff/analytics/:metric", "Chi tiết chỉ số", [
    "Placeholder",
    "insufficient-data",
  ]),
  ScreenSpec("S-060", "/staff/admin", "Quản trị", [
    "Placeholder",
    "access-denied",
  ]),
  ScreenSpec("S-061", "/staff/admin/roles", "Vai trò", ["Placeholder"]),
  ScreenSpec("S-062", "/staff/admin/audit", "Lịch sử thao tác", [
    "Placeholder",
    "filtered",
  ]),
  ScreenSpec("L-070", "/progress", "Những bước bạn đã đi", [
    "observations",
    "insufficient-evidence",
  ]),
  ScreenSpec("L-071", "/learn/search", "Tìm bài học", [
    "ready",
    "filtered",
    "empty",
  ]),
  ScreenSpec("L-072", "/profile/settings", "Cài đặt", ["ready", "saved"]),
  ScreenSpec("L-073", "/notifications", "Thông báo", ["ready", "empty"]),
];
ScreenSpec screenById(String id) => screens.firstWhere((s) => s.id == id);

/// Presentation routes only; template IDs are never sent to an API.
ScreenSpec? screenByRoute(String route) {
  for (final s in screens) {
    if (s.route == route) {
      return s;
    }
  }
  final path = Uri.parse(route).path;
  for (final s in screens) {
    final pattern = s.route
        .split('?')
        .first
        .split('/')
        .map((part) => part.startsWith(':') ? '[^/]+' : RegExp.escape(part))
        .join('/');
    if (RegExp('^$pattern\$').hasMatch(path)) {
      return s;
    }
  }
  return null;
}
