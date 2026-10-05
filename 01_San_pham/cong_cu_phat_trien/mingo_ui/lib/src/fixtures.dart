import 'package:flutter/foundation.dart';

/// Presentation-only exercise model. Never calculates canonical scores/mastery.
class PracticeFixture extends ChangeNotifier {
  PracticeFixture({this.check = false});
  final bool check;
  int? selected, firstResponse;
  int retries = 0;
  bool hinted = false, submitted = false, skipped = false;
  bool get correct => selected == 0;
  bool get canRetry => !check && submitted && !correct && retries < 1;
  bool get assisted => hinted || retries > 0;
  void choose(int value) {
    if (!submitted && !skipped) {
      selected = value;
      notifyListeners();
    }
  }

  bool submit() {
    if (selected == null || submitted || skipped) return false;
    firstResponse ??= selected;
    submitted = true;
    notifyListeners();
    return true;
  }

  bool retry() {
    if (!canRetry) return false;
    retries++;
    selected = null;
    submitted = false;
    notifyListeners();
    return true;
  }

  bool hint() {
    if (check || submitted || skipped) return false;
    hinted = true;
    notifyListeners();
    return true;
  }

  bool skip() {
    if (check || submitted) return false;
    skipped = true;
    notifyListeners();
    return true;
  }
}

class ReviewPreferences extends ChangeNotifier {
  String goal = 'Giao tiếp hằng ngày';
  bool reducedMotion = false, notifications = false, dark = false;
  void setGoal(String value) {
    goal = value;
    notifyListeners();
  }

  void setMotion(bool value) {
    reducedMotion = value;
    notifyListeners();
  }

  void setNotifications(bool value) {
    notifications = value;
    notifyListeners();
  }

  void setDark(bool value) {
    dark = value;
    notifyListeners();
  }
}

/// Immutable sample, with a separate editable draft. No production publishing.
class ContentFixture {
  static const publishedTitle = 'Chào hỏi và làm quen';
  final String publishedRevision = 'sample-r1';
  String draftTitle = publishedTitle;
  bool licenseVerified = false, reviewed = false;
  bool get previewAllowed => licenseVerified && reviewed;
  void newDraft() {
    draftTitle = publishedTitle;
    licenseVerified = false;
    reviewed = false;
  }
}

String nextLessonReason({
  bool recommendationEnabled = true,
  bool hasResume = false,
  bool due = true,
}) {
  if (hasResume) return 'Bạn đang học dở bài này.';
  if (due) return 'Đến lúc ôn lại lời chào đã luyện.';
  return recommendationEnabled
      ? 'Phù hợp mục tiêu giao tiếp hằng ngày.'
      : 'Bài tiếp theo trong lộ trình của bạn.';
}
