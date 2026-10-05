import 'package:flutter/material.dart';
import 'catalog.dart';
import 'design.dart';
import 'fixtures.dart';

class StaffApp extends StatefulWidget {
  const StaffApp({
    super.key,
    this.initialScreen = 'S-010',
    this.reviewState,
    this.textScale,
  });
  final String initialScreen;
  final String? reviewState;
  final double? textScale;
  @override
  State<StaffApp> createState() => _StaffAppState();
}

class _StaffAppState extends State<StaffApp> {
  late String id = widget.initialScreen;
  final fixture = ContentFixture();
  String filter = '';
  bool saved = false;
  void go(String target) => setState(() => id = target);
  Widget row(
    String title,
    String detail,
    String target, {
    IconData icon = Icons.arrow_forward_rounded,
  }) => ActionRow(
    title: title,
    detail: detail,
    onTap: () => go(target),
    icon: icon,
  );
  Widget primary(String text, VoidCallback action) => FilledButton(
    onPressed: action,
    child: Text(text, textAlign: TextAlign.center),
  );
  @override
  Widget build(BuildContext c) => MaterialApp(
    title: 'Mingo · Nhân viên',
    debugShowCheckedModeBanner: false,
    theme: mingoTheme(),
    builder: (c, child) => MediaQuery(
      data: MediaQuery.of(c).copyWith(
        textScaler: widget.textScale == null
            ? MediaQuery.textScalerOf(c)
            : TextScaler.linear(widget.textScale!),
      ),
      child: child!,
    ),
    home: Builder(
      builder: (c) => LayoutBuilder(
        builder: (c, box) {
          final wide =
              box.maxWidth >= 1000 && MediaQuery.textScalerOf(c).scale(1) < 1.5;
          return Scaffold(
            appBar: AppBar(
              title: const Wordmark(),
              leading: wide
                  ? null
                  : Builder(
                      builder: (context) => IconButton(
                        tooltip: 'Mở danh mục',
                        icon: const Icon(Icons.menu),
                        onPressed: () => Scaffold.of(context).openDrawer(),
                      ),
                    ),
              actions: [
                Padding(
                  padding: const EdgeInsets.all(16),
                  child: Text(
                    'Không gian nhân viên',
                    style: Theme.of(c).textTheme.bodyMedium?.copyWith(
                      fontWeight: FontWeight.w600,
                    ),
                  ),
                ),
              ],
            ),
            drawer: wide
                ? null
                : Drawer(
                    child: SafeArea(
                      child: Builder(builder: (context) => menu(context)),
                    ),
                  ),
            body: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (wide) SizedBox(width: 240, child: menu(c)),
                Expanded(
                  child: Column(
                    children: [
                      const ReviewLabel(),
                      Expanded(
                        child: PageBody(
                          maxWidth: 1100,
                          children: [
                            if (widget.reviewState != null)
                              StateNotice(state: widget.reviewState!),
                            ...content(c),
                          ],
                        ),
                      ),
                    ],
                  ),
                ),
              ],
            ),
          );
        },
      ),
    ),
  );
  Widget menu(BuildContext c) => SingleChildScrollView(
    padding: const EdgeInsets.all(16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        const Padding(
          padding: EdgeInsets.symmetric(vertical: 24),
          child: Text(
            'MINGO WORKSPACE',
            style: TextStyle(
              fontSize: 14,
              fontWeight: FontWeight.w600,
              letterSpacing: 1,
            ),
          ),
        ),
        for (final (title, icon, target) in <(String, IconData, String)>[
          ('Hôm nay', Icons.dashboard_outlined, 'S-010'),
          ('Học viên', Icons.people_outline, 'S-020'),
          ('Nội dung', Icons.menu_book_outlined, 'S-030'),
          ('Duyệt bài', Icons.fact_check_outlined, 'S-034'),
          ('Hỗ trợ', Icons.support_agent_outlined, 'S-040'),
          ('Phân tích', Icons.insights_outlined, 'S-050'),
          ('Quản trị', Icons.settings_outlined, 'S-060'),
        ])
          TextButton(
            onPressed: () {
              if (Scaffold.maybeOf(c)?.isDrawerOpen ?? false) Navigator.pop(c);
              go(target);
            },
            child: Row(
              children: [
                Icon(icon),
                const SizedBox(width: 12),
                Expanded(child: Text(title)),
              ],
            ),
          ),
        const SizedBox(height: 32),
        const Text(
          'Bản xem trước quy trình.\nChưa kết nối dữ liệu thật.',
          style: TextStyle(
            fontSize: 14,
            fontWeight: FontWeight.w600,
            color: MingoColors.ink,
          ),
        ),
      ],
    ),
  );
  List<Widget> content(BuildContext c) {
    final s = screenById(id);
    final state = (widget.reviewState ?? '').toLowerCase();
    final header = heading(
      c,
      s.title,
      id == 'S-010' ? 'Tập trung vào việc cần xử lý tiếp theo.' : null,
    );
    if (state.contains('access-denied') || state.contains('access-required')) {
      return [
        header,
        const Notice(
          title: 'Chưa có quyền xem nội dung này',
          detail:
              'Không hiển thị hồ sơ hoặc thao tác dữ liệu. Đăng nhập và phân quyền thuộc giai đoạn sau.',
        ),
        primary('Quay về không gian mẫu', () => go('S-010')),
      ];
    }
    if (state == 'loading' || state == 'processing' || state == 'saving') {
      return [
        header,
        const Notice(
          title: 'Đang chờ xử lý (mẫu)',
          detail:
              'Chưa có xác nhận thành công. Bạn có thể quay lại; không thực hiện thêm thao tác trùng lặp.',
        ),
        primary('Quay về công việc hôm nay', () => go('S-010')),
      ];
    }
    if (state == 'empty' ||
        state == 'no-evidence' ||
        state == 'no-data' ||
        state == 'insufficient-data') {
      return [
        header,
        const Notice(
          title: 'Chưa có dữ liệu phù hợp',
          detail:
              'Không suy ra điểm năng lực, dự đoán hay kết luận khi thiếu dữ liệu.',
        ),
        primary('Quay về công việc hôm nay', () => go('S-010')),
      ];
    }
    switch (id) {
      case 'S-001':
        return [
          header,
          const Notice(
            title: 'Chưa triển khai đăng nhập',
            detail:
                'Phase 3 đang HOLD. Bản xem trước không xác thực hoặc cấp quyền người dùng.',
          ),
          primary('Xem không gian mẫu', () => go('S-010')),
        ];
      case 'S-010':
        return [
          header,
          Surface(
            tint: true,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Một bài đang chờ kiểm tra (mẫu)',
                  style: Theme.of(c).textTheme.titleLarge,
                ),
                const SizedBox(height: 12),
                const Text(
                  'Kiểm tra nội dung, bằng chứng và giấy phép trước khi xuất bản.',
                ),
                const SizedBox(height: 24),
                primary('Xem hàng chờ duyệt', () => go('S-034')),
              ],
            ),
          ),
          row('Xem học viên', 'Bằng chứng trước, kết luận sau', 'S-020'),
          row('Soạn nội dung', 'Bản nháp có thể chỉnh sửa', 'S-030'),
        ];
      case 'S-020':
        return [
          header,
          TextField(
            decoration: const InputDecoration(
              labelText: 'Tìm học viên mẫu',
              prefixIcon: Icon(Icons.search),
            ),
            onChanged: (v) => setState(() => filter = v),
          ),
          if (filter.isEmpty || 'học viên a'.contains(filter.toLowerCase()))
            row(
              'Học viên A',
              'Chào hỏi · Cần thêm bằng chứng · Dữ liệu mẫu',
              'S-021',
              icon: Icons.person_outline,
            )
          else
            const Notice(
              title: 'Không có kết quả',
              detail: 'Thử một tên khác. Bản xem trước chỉ có Học viên A.',
            ),
          const Text('Không có dữ liệu cá nhân thật trong bản xem trước.'),
        ];
      case 'S-021':
        return [
          header,
          heading(c, 'Học viên A', 'Mục tiêu mẫu: giao tiếp hằng ngày'),
          const Notice(
            title: 'Chưa đủ bằng chứng để kết luận',
            detail: 'Một bài ngắn không đủ để đánh giá năng lực hoặc rủi ro.',
          ),
          row(
            'Xem câu đã làm',
            'Phân biệt lần đầu, gợi ý và lần thử thêm',
            'S-022',
          ),
          row(
            'Hoạt động gần đây',
            'Thời điểm học và thời điểm hệ thống biết',
            'S-023',
          ),
        ];
      case 'S-022':
        return [
          header,
          const Surface(
            child: Text(
              'Câu 1 · Tự trả lời, đúng lần đầu (mẫu)\nCâu 2 · Có gợi ý; không tính là bằng chứng độc lập\nChưa có lần ôn sau một khoảng thời gian.',
            ),
          ),
          const Notice(
            title: 'Chưa suy ra năng lực hoặc rủi ro',
            detail:
                'Bằng chứng học, dự đoán và quyết định hỗ trợ là các lớp riêng.',
          ),
          row(
            'Xem hoạt động',
            'Giữ nguồn và thời điểm của từng sự kiện',
            'S-023',
          ),
        ];
      case 'S-023':
        return [
          header,
          const Surface(
            child: Text(
              'Hoạt động mẫu\nHọc: 09:00 · Hệ thống biết: 09:10\nNguồn: bản xem trước; không phải sự kiện production.\nKhông dùng thông tin tương lai để đánh giá quá khứ.',
            ),
          ),
          row('Quay lại hồ sơ', 'Học viên A', 'S-021'),
        ];
      case 'S-030':
      case 'S-034':
        return [
          header,
          TextField(
            decoration: const InputDecoration(
              labelText: 'Tìm bài học',
              prefixIcon: Icon(Icons.search),
            ),
            onChanged: (v) => setState(() => filter = v),
          ),
          if (filter.isEmpty || 'chào hỏi'.contains(filter.toLowerCase()))
            row(
              'Chào hỏi và làm quen',
              id == 'S-034'
                  ? 'Chờ kiểm tra nguồn và giấy phép (mẫu)'
                  : 'Bản nháp mẫu · Chưa xuất bản',
              id == 'S-034' ? 'S-035' : 'S-031',
              icon: Icons.article_outlined,
            )
          else
            const Notice(
              title: 'Chưa có bài phù hợp',
              detail: 'Xóa từ khóa để xem bản nháp mẫu.',
            ),
          if (id == 'S-030') primary('Mở bản nháp mẫu', () => go('S-031')),
        ];
      case 'S-031':
        return [
          header,
          const Text('Chỉnh sửa bản nháp mẫu, không thay đổi bản đã xuất bản.'),
          TextFormField(
            initialValue: fixture.draftTitle,
            decoration: const InputDecoration(labelText: 'Tên bài học'),
            onChanged: (v) {
              fixture.draftTitle = v;
              saved = false;
            },
          ),
          TextFormField(
            initialValue: 'Chào một người và đáp lại vào buổi sáng.',
            decoration: const InputDecoration(labelText: 'Mục tiêu học'),
            maxLines: 3,
          ),
          if (saved)
            const Notice(
              title: 'Đã giữ trong phiên xem trước',
              detail:
                  'Chưa lưu lên máy chủ. Thoát bản xem trước sẽ mất thay đổi.',
            ),
          primary(
            'Giữ bản nháp trong phiên xem trước',
            () => setState(() => saved = true),
          ),
          row('Xem trước', 'Kiểm tra câu hỏi và phản hồi', 'S-032'),
          row('Nguồn và giấy phép', 'Bước bắt buộc trước xuất bản', 'S-033'),
        ];
      case 'S-032':
        return [
          header,
          Surface(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  fixture.draftTitle,
                  style: Theme.of(c).textTheme.titleLarge,
                ),
                const SizedBox(height: 16),
                const Text(
                  'Câu hỏi mẫu: Bạn đến lớp buổi sáng. Bạn chào thế nào?\n\nGood morning!\nGood night!\nSee you later!\n\nPhản hồi: “Good morning” dùng vào buổi sáng.',
                ),
              ],
            ),
          ),
          row(
            'Kiểm tra nguồn và giấy phép',
            'Không thể bỏ qua khi xuất bản',
            'S-033',
          ),
        ];
      case 'S-033':
        return [
          header,
          const Surface(
            child: Text(
              'Nội dung minh họa tự viết. Mascot tạo mới bằng ImageGen; Inter có giấy phép OFL. Đây chưa phải phê duyệt license của bài học production.',
            ),
          ),
          CheckboxListTile(
            contentPadding: EdgeInsets.zero,
            title: const Text('Đã kiểm tra nguồn trong quy trình mẫu'),
            value: fixture.licenseVerified,
            onChanged: (v) =>
                setState(() => fixture.licenseVerified = v ?? false),
          ),
          primary('Tiếp tục kiểm tra bài', () => go('S-035')),
        ];
      case 'S-035':
        return [
          header,
          const Surface(
            child: Text(
              'Kiểm tra: mục tiêu rõ · câu trả lời đúng · phản hồi giải thích · mức độ phù hợp · media có bản quyền · đủ điều kiện xuất bản.',
            ),
          ),
          CheckboxListTile(
            contentPadding: EdgeInsets.zero,
            title: const Text('Nội dung mẫu đã được kiểm tra'),
            value: fixture.reviewed,
            onChanged: (v) => setState(() => fixture.reviewed = v ?? false),
          ),
          if (!fixture.licenseVerified)
            const Notice(
              title: 'Cần kiểm tra giấy phép',
              detail:
                  'Không cho phép xem bước xác nhận xuất bản khi thiếu bước này.',
              error: true,
            ),
          primary(
            fixture.previewAllowed
                ? 'Xem bước xác nhận'
                : 'Kiểm tra nguồn và giấy phép',
            () => go(fixture.previewAllowed ? 'S-036' : 'S-033'),
          ),
        ];
      case 'S-036':
        return [
          header,
          const Notice(
            title: 'Chỉ mô phỏng xác nhận',
            detail:
                'Không gọi API, không xuất bản thật và không cấp quyền. Bản xuất bản thật phải bất biến và có phiên bản.',
          ),
          if (fixture.previewAllowed || widget.initialScreen == 'S-036')
            primary('Xem xác nhận mẫu', () => confirm(c))
          else
            primary('Hoàn thành kiểm tra trước', () => go('S-035')),
        ];
      case 'S-037':
        return [
          header,
          Surface(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  ContentFixture.publishedTitle,
                  style: Theme.of(c).textTheme.titleLarge,
                ),
                const SizedBox(height: 12),
                Text(
                  'Phiên bản ${fixture.publishedRevision} · Bất biến · Dữ liệu mẫu',
                ),
                const SizedBox(height: 12),
                const Text(
                  'Bản đang học giữ nguyên phiên bản. Bản nháp mới không ghi đè bản này.',
                ),
              ],
            ),
          ),
          primary('Tạo bản nháp mẫu mới', () {
            fixture.newDraft();
            go('S-031');
          }),
        ];
      default:
        return [
          header,
          const Notice(
            title: 'Màn hình tham chiếu cho giai đoạn sau',
            detail:
                'Chưa có ML, analytics, quyết định hỗ trợ hoặc phân quyền thật. Sản phẩm học phải hoạt động khi các thành phần này bị tắt.',
          ),
          if (id == 'S-040')
            row(
              'Xem bố cục hỗ trợ',
              'Chưa có quyết định hoặc thực thi thật',
              'S-041',
            ),
          if (id == 'S-050')
            row(
              'Xem cách đọc chỉ số',
              'Không dùng dữ liệu mẫu làm kết luận',
              'S-051',
            ),
          if (id == 'S-060') ...[
            row('Vai trò', 'Chưa triển khai cấp quyền', 'S-061'),
            row('Lịch sử thao tác', 'Chưa ghi nhật ký production', 'S-062'),
          ],
          primary('Quay về công việc hôm nay', () => go('S-010')),
        ];
    }
  }

  Future<void> confirm(BuildContext c) async {
    final accepted = await showDialog<bool>(
      context: c,
      builder: (c) => AlertDialog(
        title: const Text('Xem bản xuất bản mẫu?'),
        content: const Text(
          'Thao tác này chỉ chuyển màn hình. Không xuất bản dữ liệu hoặc thay đổi bài đang học.',
        ),
        actions: [
          TextButton(
            onPressed: () => Navigator.pop(c, false),
            child: const Text('Quay lại'),
          ),
          FilledButton(
            onPressed: () => Navigator.pop(c, true),
            child: const Text('Xem bản mẫu'),
          ),
        ],
      ),
    );
    if (accepted == true && mounted) go('S-037');
  }
}
