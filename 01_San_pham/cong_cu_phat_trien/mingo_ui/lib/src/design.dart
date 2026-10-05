import 'package:flutter/material.dart';

abstract final class MingoColors {
  static const blue = Color(0xFF2459D3);
  static const ink = Color(0xFF172B4D);
  static const muted = Color(0xFF52627A);
  static const paper = Color(0xFFFAF9F6);
  static const surface = Colors.white;
  static const mist = Color(0xFFEDF3FF);
  static const line = Color(0xFFD7DFEB);
  static const success = Color(0xFF226645);
  static const error = Color(0xFFAD3434);
  static const orange = Color(0xFFAF4B0D);
}

ThemeData mingoTheme({bool dark = false}) {
  final scheme =
      ColorScheme.fromSeed(
        seedColor: MingoColors.blue,
        brightness: dark ? Brightness.dark : Brightness.light,
      ).copyWith(
        primary: dark ? const Color(0xFFAEC7FF) : MingoColors.blue,
        onPrimary: dark ? MingoColors.ink : Colors.white,
        error: dark ? const Color(0xFFFFB4AB) : MingoColors.error,
        surface: dark ? const Color(0xFF182230) : MingoColors.paper,
      );
  return ThemeData(
    useMaterial3: true,
    colorScheme: scheme,
    fontFamily: 'packages/mingo_ui/Inter',
    scaffoldBackgroundColor: scheme.surface,
    textTheme: Typography.material2021().black
        .apply(
          fontFamily: 'packages/mingo_ui/Inter',
          bodyColor: dark ? Colors.white : MingoColors.ink,
          displayColor: dark ? Colors.white : MingoColors.ink,
        )
        .copyWith(
          headlineLarge: TextStyle(
            fontSize: 32,
            fontWeight: FontWeight.w700,
            color: scheme.onSurface,
          ),
          headlineMedium: TextStyle(
            fontSize: 26,
            fontWeight: FontWeight.w700,
            color: scheme.onSurface,
          ),
          titleLarge: TextStyle(
            fontSize: 21,
            fontWeight: FontWeight.w600,
            color: scheme.onSurface,
          ),
          bodyLarge: TextStyle(
            fontSize: 16,
            height: 1.5,
            color: scheme.onSurface,
          ),
          bodyMedium: TextStyle(
            fontSize: 16,
            fontWeight: FontWeight.w500,
            height: 1.5,
            color: scheme.onSurface,
          ),
        ),
    filledButtonTheme: FilledButtonThemeData(
      style: FilledButton.styleFrom(
        minimumSize: const Size(48, 56),
        padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 16),
        textStyle: const TextStyle(
          fontFamily: 'packages/mingo_ui/Inter',
          fontSize: 16,
          fontWeight: FontWeight.w600,
        ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(18)),
      ),
    ),
    textButtonTheme: TextButtonThemeData(
      style: TextButton.styleFrom(
        minimumSize: const Size(48, 48),
        padding: const EdgeInsets.all(14),
        foregroundColor: scheme.onSurface,
        textStyle: const TextStyle(
          fontFamily: 'packages/mingo_ui/Inter',
          fontSize: 16,
          fontWeight: FontWeight.w600,
        ),
      ),
    ),
    outlinedButtonTheme: OutlinedButtonThemeData(
      style: OutlinedButton.styleFrom(
        minimumSize: const Size(48, 52),
        padding: const EdgeInsets.all(16),
        foregroundColor: scheme.onSurface,
        textStyle: const TextStyle(
          fontFamily: 'packages/mingo_ui/Inter',
          fontSize: 16,
          fontWeight: FontWeight.w600,
        ),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      ),
    ),
    inputDecorationTheme: InputDecorationTheme(
      filled: true,
      fillColor: scheme.surfaceContainerLowest,
      border: OutlineInputBorder(borderRadius: BorderRadius.circular(16)),
      contentPadding: const EdgeInsets.all(18),
    ),
    iconButtonTheme: IconButtonThemeData(
      style: IconButton.styleFrom(minimumSize: const Size(48, 48)),
    ),
    dividerColor: MingoColors.line,
  );
}

class Wordmark extends StatelessWidget {
  const Wordmark({super.key});
  @override
  Widget build(BuildContext context) => Semantics(
    label: 'Mingo',
    excludeSemantics: true,
    child: Text(
      'Mingo',
      style: Theme.of(context).textTheme.titleLarge?.copyWith(
        letterSpacing: -0.8,
        fontWeight: FontWeight.w800,
        color: Theme.of(context).colorScheme.primary,
      ),
    ),
  );
}

/// Ten logical uses of the same canonical companion. Unavailable poses reuse
/// the neutral master; they never synthesize emotion or a learner diagnosis.
enum CompanionUse {
  neutral,
  reading,
  listening,
  thinking,
  support,
  encouraging,
  completion,
  offline,
  empty,
  errorSupport,
}

class Mascot extends StatelessWidget {
  const Mascot({super.key, this.height = 180, this.use = CompanionUse.neutral});
  final double height;
  final CompanionUse use;
  @override
  Widget build(BuildContext context) => ExcludeSemantics(
    child: Image.asset(
      'assets/mascot.png',
      package: 'mingo_ui',
      height: height,
      cacheHeight: (height * MediaQuery.devicePixelRatioOf(context))
          .ceil()
          .clamp(16, 1536),
      fit: BoxFit.contain,
    ),
  );
}

class ExplorationHero extends StatelessWidget {
  const ExplorationHero({super.key});
  @override
  Widget build(BuildContext context) => ExcludeSemantics(
    child: ClipRRect(
      borderRadius: BorderRadius.circular(24),
      child: AspectRatio(
        aspectRatio: 1.6,
        child: LayoutBuilder(
          builder: (c, bounds) => Image.asset(
            'assets/exploration.png',
            package: 'mingo_ui',
            fit: BoxFit.cover,
            cacheWidth: (bounds.maxWidth * MediaQuery.devicePixelRatioOf(c))
                .ceil()
              .clamp(16, 1536),
          ),
        ),
      ),
    ),
  );
}

class Surface extends StatelessWidget {
  const Surface({super.key, required this.child, this.tint = false});
  final Widget child;
  final bool tint;
  @override
  Widget build(BuildContext context) => Container(
    width: double.infinity,
    padding: const EdgeInsets.all(24),
    decoration: BoxDecoration(
      color: tint
          ? Theme.of(context).colorScheme.primaryContainer.withValues(alpha: .3)
          : Theme.of(context).colorScheme.surfaceContainerLowest,
      borderRadius: BorderRadius.circular(24),
      border: Border.all(color: MingoColors.line),
    ),
    child: child,
  );
}

class PageBody extends StatelessWidget {
  const PageBody({super.key, required this.children, this.maxWidth = 760});
  final List<Widget> children;
  final double maxWidth;
  @override
  Widget build(BuildContext context) => SingleChildScrollView(
    padding: const EdgeInsets.fromLTRB(24, 24, 24, 40),
    child: Align(
      alignment: Alignment.topCenter,
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: maxWidth),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            for (final w in children) ...[w, const SizedBox(height: 24)],
          ],
        ),
      ),
    ),
  );
}

Widget heading(BuildContext c, String title, [String? subtitle]) => Column(
  crossAxisAlignment: CrossAxisAlignment.start,
  children: [
    Semantics(
      header: true,
      child: Text(title, style: Theme.of(c).textTheme.headlineMedium),
    ),
    if (subtitle != null) ...[
      const SizedBox(height: 12),
      Text(subtitle, style: Theme.of(c).textTheme.bodyLarge),
    ],
  ],
);

class ActionRow extends StatelessWidget {
  const ActionRow({
    super.key,
    required this.title,
    required this.detail,
    required this.onTap,
    this.icon = Icons.arrow_forward_rounded,
    this.selected = false,
  });
  final String title, detail;
  final VoidCallback onTap;
  final IconData icon;
  final bool selected;
  @override
  Widget build(BuildContext c) => Padding(
    padding: const EdgeInsets.only(bottom: 12),
    child: OutlinedButton(
      onPressed: onTap,
      style: OutlinedButton.styleFrom(
        backgroundColor: selected
            ? Theme.of(c).colorScheme.primaryContainer.withValues(alpha: .3)
            : Theme.of(c).colorScheme.surfaceContainerLowest,
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Icon(icon),
          const SizedBox(width: 16),
          Expanded(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(title, style: Theme.of(c).textTheme.titleMedium),
                if (detail.isNotEmpty)
                  Text(detail, style: Theme.of(c).textTheme.bodyMedium),
              ],
            ),
          ),
        ],
      ),
    ),
  );
}

class Notice extends StatelessWidget {
  const Notice({
    super.key,
    required this.title,
    required this.detail,
    this.error = false,
  });
  final String title, detail;
  final bool error;
  @override
  Widget build(BuildContext c) => Semantics(
    liveRegion: true,
    child: Surface(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 12,
            crossAxisAlignment: WrapCrossAlignment.center,
            children: [
              Icon(
                Icons.info_outline,
                color: error
                    ? Theme.of(c).colorScheme.error
                    : Theme.of(c).colorScheme.primary,
              ),
              Text(title, style: Theme.of(c).textTheme.titleMedium),
            ],
          ),
          const SizedBox(height: 8),
          Text(detail),
        ],
      ),
    ),
  );
}

/// Review data is disclosed at the boundary of every screen; never a server receipt.
class ReviewLabel extends StatelessWidget {
  const ReviewLabel({super.key});
  @override
  Widget build(BuildContext c) => Container(
    width: double.infinity,
    color: Theme.of(c).colorScheme.surfaceContainerLow,
    padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 8),
    child: const Text(
      'Bản xem trước · dữ liệu mẫu',
      style: TextStyle(fontSize: 14, fontWeight: FontWeight.w600),
    ),
  );
}

class StateNotice extends StatelessWidget {
  const StateNotice({super.key, required this.state});
  final String state;
  @override
  Widget build(BuildContext c) {
    final s = state.toLowerCase();
    if ([
      'default',
      'ready',
      'online',
      'observations',
      'clean',
      'preview',
      'eligible',
      'open',
      'available',
      'selected',
    ].contains(s)) {
      return const SizedBox.shrink();
    }
    String title = 'Sẵn sàng cho bước tiếp theo',
        detail = 'Bạn có thể tiếp tục khi thấy phù hợp.';
    if (s.contains('load') ||
        s == 'submitting' ||
        s == 'processing' ||
        s == 'saving') {
      title = 'Đang chuẩn bị';
      detail =
          'Bạn có thể quay lại. Bản xem trước không gửi dữ liệu đến máy chủ.';
    } else if (s.contains('reauth') || s.contains('access')) {
      title = 'Cần quyền truy cập';
      detail =
          'Phần đăng nhập và cấp quyền sẽ được triển khai ở giai đoạn sau. Không có quyền thật được cấp trong bản xem trước.';
    } else if (s.contains('sync') || s.contains('queued') || s == 'partial') {
      title = s == 'synced'
          ? 'Đã nhận xác nhận (mẫu)'
          : s == 'syncing'
          ? 'Đang chờ gửi (mẫu)'
          : 'Đã lưu trên máy (mẫu)';
      detail =
          'Kết nối mạng chưa đồng nghĩa với gửi thành công. Bài còn chờ sẽ được giữ để thử lại.';
    } else if (s.contains('offline')) {
      title = 'Bạn vẫn có thể học';
      detail =
          'Chỉ những bài đã tải và còn đúng phiên bản mới dùng được khi không có mạng.';
    } else if (s.contains('immutable')) {
      title = 'Bản xuất bản chỉ để đọc';
      detail =
          'Muốn chỉnh sửa, hãy tạo bản nháp mới. Bài đang học giữ phiên bản đã bắt đầu.';
    } else if (s.contains('locked') ||
        s.contains('license') ||
        s.contains('play-limit')) {
      title = 'Cần hoàn thành bước trước';
      detail = s.contains('license')
          ? 'Cần nguồn và giấy phép hợp lệ trước khi xuất bản.'
          : s.contains('play-limit')
          ? 'Lượt nghe cho câu thử đã hết. Bạn vẫn có thể chọn câu trả lời.'
          : 'Bạn xem được mục tiêu. Cần đủ bằng chứng của bài trước để bắt đầu.';
    } else if (s.contains('hint')) {
      title = 'Đang dùng gợi ý';
      detail =
          'Lần luyện này có hỗ trợ; không được tính thành một lần tự trả lời.';
    } else if (s.contains('retry')) {
      title = s.contains('exhausted')
          ? 'Lần thử thêm đã hết'
          : 'Bạn có thể thử thêm một lần';
      detail =
          'Câu trả lời đầu tiên vẫn được giữ riêng. Bạn có thể xem giải thích rồi tiếp tục.';
    } else if (s.contains('skipped')) {
      title = 'Đã bỏ qua câu này';
      detail =
          'Bỏ qua không phải hoàn thành và không cung cấp bằng chứng trả lời đúng.';
    } else if (s.contains('insufficient') ||
        s.contains('evidence') ||
        s.contains('building')) {
      title = 'Cần thêm một chút thực hành';
      detail = 'Chưa có đủ câu trả lời độc lập để kết luận về kỹ năng của bạn.';
    } else if (s.contains('empty') ||
        s.contains('nothing') ||
        s.contains('no-')) {
      title = 'Chưa có mục phù hợp';
      detail =
          'Bạn có thể quay lại bài đang học hoặc khám phá một chủ đề khác.';
    } else if (s.contains('error') ||
        s.contains('failed') ||
        s.contains('unavailable') ||
        s.contains('expired') ||
        s.contains('refresh') ||
        s == 'fatal') {
      title = 'Cần kiểm tra trước khi tiếp tục';
      detail = s.contains('audio') || s.contains('media')
          ? 'Âm thanh chưa sẵn sàng. Không tự chấm một câu nghe khi thiếu âm thanh.'
          : s.contains('refresh') || s.contains('expired')
          ? 'Bài cần đúng phiên bản. Hãy tải lại; bài cũ và câu đã làm được giữ riêng.'
          : 'Hãy thử lại hoặc quay về. Mingo chưa xác nhận thao tác này thành công.';
    } else if (s.contains('result') ||
        s.contains('complete') ||
        s.contains('saved') ||
        s.contains('verified') ||
        s.contains('created')) {
      title = 'Kết quả trong bản xem trước';
      detail =
          'Đây là dữ liệu minh họa để duyệt giao diện, chưa phải kết quả máy chủ.';
    } else if (s == 'dirty' || s.contains('changes')) {
      title = 'Có thay đổi cần xem lại';
      detail = 'Bản nháp mẫu chưa phải bản đã xuất bản.';
    } else if (s == 'filtered') {
      title = 'Kết quả đã lọc';
      detail = 'Chỉ hiển thị các mục phù hợp với lựa chọn hiện tại.';
    } else if (s == 'placeholder') {
      title = 'Dành cho giai đoạn sau';
      detail =
          'Màn hình tham chiếu; chưa có dịch vụ, dữ liệu phân tích hoặc quyết định hỗ trợ thật.';
    }
    return Notice(
      title: title,
      detail: detail,
      error:
          s.contains('error') ||
          s.contains('failed') ||
          s.contains('unavailable'),
    );
  }
}
