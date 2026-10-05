import 'package:flutter/material.dart';
import 'catalog.dart';
import 'design.dart';
import 'fixtures.dart';
import 'lesson.dart';
import 'lesson_content.dart';
import 'audio.dart';
import 'journey.dart';

class LearnerApp extends StatefulWidget {
  const LearnerApp({
    super.key,
    this.initialScreen = 'L-002',
    this.reviewState,
    this.textScale,
    this.initialDomain = LessonDomain.vocabulary,
    this.initialDark = false,
  });
  final String initialScreen;
  final String? reviewState;
  final double? textScale;
  final LessonDomain initialDomain;
  final bool initialDark;
  @override
  State<LearnerApp> createState() => _LearnerAppState();
}

class _LearnerAppState extends State<LearnerApp> {
  late String id = widget.initialScreen;
  late LessonDomain domain = widget.initialDomain;
  late final prefs = ReviewPreferences()..dark = widget.initialDark;
  final practices = <String, PracticeFixture>{};
  final audioClips = <String, SampleAudio>{};
  final history = <(String, LessonDomain)>[];
  String search = '';
  void go(String value, {LessonDomain? lessonDomain}) {
    setState(() {
      history.add((id, domain));
      id = value;
      if (lessonDomain != null) domain = lessonDomain;
    });
  }

  void back() {
    setState(() {
      if (history.isEmpty) {
        id = 'L-010';
        domain = LessonDomain.vocabulary;
      } else {
        final previous = history.removeLast();
        id = previous.$1;
        domain = previous.$2;
      }
    });
  }

  @override
  void dispose() {
    prefs.dispose();
    for (final p in practices.values) {
      p.dispose();
    }
    for (final a in audioClips.values) {
      a.dispose();
    }
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: prefs,
    builder: (c, _) => MaterialApp(
      title: 'Mingo',
      debugShowCheckedModeBanner: false,
      theme: mingoTheme(dark: prefs.dark),
      builder: (context, child) => MediaQuery(
        data: MediaQuery.of(context).copyWith(
          textScaler: widget.textScale == null
              ? MediaQuery.textScalerOf(context)
              : TextScaler.linear(widget.textScale!),
          disableAnimations:
              prefs.reducedMotion || MediaQuery.of(context).disableAnimations,
        ),
        child: child!,
      ),
      home: Builder(
        builder: (c) {
          final spec = screenById(id);
          final lesson = RegExp(
            r'L-02[1-9]|L-030|L-031|L-032|L-005',
          ).hasMatch(id);
          final main = [
            'L-010',
            'L-011',
            'L-012',
            'L-020',
            'L-040',
            'L-050',
            'L-070',
            'L-071',
          ].contains(id);
          final compactNavigation =
              MediaQuery.textScalerOf(c).scale(1) > 1.3 ||
              MediaQuery.sizeOf(c).width < 360;
          final currentTab = id.startsWith('L-01')
              ? 'Trang chủ'
              : id == 'L-020' || id == 'L-071'
              ? 'Học'
              : id == 'L-040'
              ? 'Lộ trình'
              : 'Tôi';
          return PopScope<void>(
            canPop: history.isEmpty && ['L-001', 'L-002', 'L-010'].contains(id),
            onPopInvokedWithResult: (didPop, _) {
              if (!didPop) back();
            },
            child: Scaffold(
              appBar: AppBar(
                title: const Wordmark(),
                backgroundColor: Theme.of(c).colorScheme.surface,
                leading: main || id == 'L-002'
                    ? null
                    : IconButton(
                        tooltip: 'Quay lại',
                        onPressed: back,
                        icon: const Icon(Icons.arrow_back_rounded),
                      ),
                actions: [
                  if (!lesson)
                    IconButton(
                      tooltip: 'Thông báo',
                      onPressed: () => go('L-073'),
                      icon: const Icon(Icons.notifications_none_rounded),
                    ),
                ],
              ),
              body: Column(
                children: [
                  const ReviewLabel(),
                  Expanded(
                    child: lesson
                        ? LessonPage(
                            key: ValueKey(id),
                            id: id,
                            domain: domain,
                            audio: audioClips.putIfAbsent(
                              '${domain.name}/$id',
                              () => SampleAudio(
                                budget: id == 'L-027' || id == 'L-005'
                                    ? 2
                                    : null,
                              ),
                            ),
                            practice: practices.putIfAbsent(
                              '${domain.name}/$id',
                              () => PracticeFixture(
                                check: id == 'L-027' || id == 'L-005',
                              ),
                            ),
                            reviewState: widget.reviewState,
                            onNavigate: go,
                          )
                        : PageBody(
                            children: [
                              if (widget.reviewState != null)
                                StateNotice(state: widget.reviewState!),
                              ...content(c, spec),
                            ],
                          ),
                  ),
                ],
              ),
              bottomNavigationBar: main
                  ? SafeArea(
                      child: Container(
                        decoration: BoxDecoration(
                          color: Theme.of(c).colorScheme.surfaceContainerLowest,
                          border: const Border(
                            top: BorderSide(color: MingoColors.line),
                          ),
                        ),
                        child: Column(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            if (compactNavigation)
                              Padding(
                                padding: const EdgeInsets.fromLTRB(
                                  16,
                                  8,
                                  16,
                                  0,
                                ),
                                child: Text(
                                  currentTab,
                                  textAlign: TextAlign.center,
                                  style: const TextStyle(
                                    fontSize: 14,
                                    fontWeight: FontWeight.w600,
                                  ),
                                ),
                              ),
                            Row(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                nav(
                                  c,
                                  'Trang chủ',
                                  Icons.home_outlined,
                                  'L-010',
                                  id.startsWith('L-01'),
                                ),
                                nav(
                                  c,
                                  'Học',
                                  Icons.menu_book_outlined,
                                  'L-020',
                                  id == 'L-020' || id == 'L-071',
                                ),
                                nav(
                                  c,
                                  'Lộ trình',
                                  Icons.route_outlined,
                                  'L-040',
                                  id == 'L-040',
                                ),
                                nav(
                                  c,
                                  'Tôi',
                                  Icons.person_outline,
                                  'L-050',
                                  id == 'L-050' || id == 'L-070',
                                ),
                              ],
                            ),
                          ],
                        ),
                      ),
                    )
                  : null,
            ),
          );
        },
      ),
    ),
  );
  Widget nav(
    BuildContext c,
    String title,
    IconData icon,
    String target,
    bool selected,
  ) => Expanded(
    child: Semantics(
      selected: selected,
      child:
          MediaQuery.textScalerOf(c).scale(1) > 1.3 ||
              MediaQuery.sizeOf(c).width < 360
          ? IconButton(
              tooltip: title,
              onPressed: () => go(target),
              style: IconButton.styleFrom(
                minimumSize: const Size(64, 64),
                foregroundColor: selected
                    ? Theme.of(c).colorScheme.primary
                    : Theme.of(c).colorScheme.onSurface,
              ),
              icon: Icon(icon),
            )
          : TextButton(
              onPressed: () => go(target),
              child: Column(
                mainAxisSize: MainAxisSize.min,
                children: [
                  Icon(icon),
                  const SizedBox(height: 4),
                  Text(
                    title,
                    textAlign: TextAlign.center,
                    style: TextStyle(
                      fontSize: 14,
                      fontWeight: FontWeight.w600,
                      color: Theme.of(c).colorScheme.onSurface,
                    ),
                  ),
                ],
              ),
            ),
    ),
  );
  Widget primary(String label, String target) => SizedBox(
    width: double.infinity,
    child: FilledButton(
      onPressed: () {
        go(
          target,
          lessonDomain: target == 'L-021' ? LessonDomain.vocabulary : null,
        );
      },
      child: Text(label, textAlign: TextAlign.center),
    ),
  );
  Widget domainRow(String title, String detail, LessonDomain choice) =>
      ActionRow(
        title: title,
        detail: detail,
        icon: choice == LessonDomain.grammar
            ? Icons.text_fields
            : Icons.headphones_outlined,
        onTap: () {
          go('L-021', lessonDomain: choice);
        },
      );
  Widget row(
    String title,
    String detail,
    String target, {
    IconData icon = Icons.arrow_forward_rounded,
  }) => ActionRow(
    title: title,
    detail: detail,
    onTap: () {
      go(
        target,
        lessonDomain: target == 'L-021' ? LessonDomain.vocabulary : null,
      );
    },
    icon: icon,
  );
  List<Widget> content(BuildContext c, ScreenSpec s) {
    final state = (widget.reviewState ?? '').toLowerCase();
    if (id == 'L-041' && state == 'locked') {
      return [
        heading(c, s.title, 'Xem mục tiêu trước khi bắt đầu.'),
        const Notice(
          title: 'Cần đủ bằng chứng ở bước trước',
          detail:
              'Bạn có thể xem mục tiêu; bài này chưa thể bắt đầu. Xem trước không tự mở khóa.',
        ),
        primary('Xem bước trước', 'L-040'),
      ];
    }
    if ((id == 'L-020' || id == 'L-071') &&
        (state == 'content-gap' || state == 'empty')) {
      return [
        heading(c, s.title),
        const Notice(
          title: 'Chưa có bài phù hợp',
          detail:
              'Bạn có thể quay lại lộ trình để xem mục tiêu. Không tạo một bài thay thế không hợp lệ.',
        ),
        primary('Xem lộ trình', 'L-040'),
      ];
    }
    switch (id) {
      case 'L-001':
        return [
          const Center(child: Mascot(height: 230)),
          heading(c, 'Một bước nhỏ, một thế giới mới.'),
          primary('Bắt đầu', 'L-002'),
        ];
      case 'L-002':
        return [
          CompanionCard(
            title: 'Học nhẹ nhàng.\nKhám phá mỗi ngày.',
            subtitle: 'Những bài ngắn, vừa sức và gần với cuộc sống của bạn.',
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Ngôn ngữ mở ra những thế giới mới.',
                  style: Theme.of(c).textTheme.titleMedium,
                ),
                const SizedBox(height: 20),
                primary('Bắt đầu hành trình', 'L-003'),
              ],
            ),
          ),
          TextButton(
            onPressed: () => go('L-010'),
            child: const Text('Khám phá trước'),
          ),
        ];
      case 'L-003':
      case 'L-052':
        return [
          heading(
            c,
            s.title,
            'Chọn điều gần với bạn nhất. Bạn có thể đổi sau.',
          ),
          for (final goal in [
            'Giao tiếp hằng ngày',
            'Học tập',
            'Công việc',
            'Khám phá văn hóa',
          ])
            ActionRow(
              title: goal,
              detail: goal == prefs.goal ? 'Đang chọn' : '',
              selected: goal == prefs.goal,
              icon: goal == prefs.goal
                  ? Icons.check_circle_outline
                  : Icons.circle_outlined,
              onTap: () => prefs.setGoal(goal),
            ),
          primary(
            id == 'L-003' ? 'Tiếp tục' : 'Lưu lựa chọn trong bản xem trước',
            id == 'L-003' ? 'L-004' : 'L-050',
          ),
        ];
      case 'L-004':
        return [
          heading(
            c,
            s.title,
            'Thử vài câu để xem nên bắt đầu từ đâu. Bạn có thể học ngay và làm sau.',
          ),
          const Surface(
            child: Text(
              'Không phải bài thi. Chưa đủ câu trả lời thì Mingo sẽ nói rõ.',
            ),
          ),
          primary('Thử một câu', 'L-005'),
          TextButton(
            onPressed: () => go('L-010'),
            child: const Text('Để sau, bắt đầu học'),
          ),
        ];
      case 'L-006':
        return [
          heading(c, s.title, 'Bạn đã thử một câu chào hỏi.'),
          const Notice(
            title: 'Cần thêm bằng chứng',
            detail:
                'Một câu trả lời chưa đủ để kết luận trình độ. Hãy bắt đầu với bài cơ bản.',
          ),
          primary('Đến bài đầu tiên', 'L-010'),
        ];
      case 'L-010':
      case 'L-011':
      case 'L-012':
        return [
          CompanionCard(
            title: 'Chào bạn!',
            subtitle: 'Hôm nay, một bước nhỏ cũng đủ để bắt đầu.',
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'BÀI HỌC HÔM NAY',
                  style: TextStyle(
                    fontSize: 14,
                    fontWeight: FontWeight.w600,
                    letterSpacing: 1.1,
                    color: Theme.of(c).colorScheme.onSurfaceVariant,
                  ),
                ),
                const SizedBox(height: 12),
                Text(
                  'Chào hỏi và làm quen',
                  style: Theme.of(c).textTheme.titleLarge,
                ),
                const SizedBox(height: 8),
                const Text('Khoảng 5 phút · Cơ bản'),
                const SizedBox(height: 12),
                Text(
                  nextLessonReason(
                    due: state != 'nothing-due',
                    recommendationEnabled:
                        widget.reviewState != 'recommendation-unavailable',
                  ),
                ),
                const SizedBox(height: 20),
                primary('Bắt đầu học', 'L-021'),
              ],
            ),
          ),
          TextButton.icon(
            onPressed: () => go('L-070'),
            icon: const Icon(Icons.eco_outlined),
            label: const Text('Nhìn lại những bước đã đi'),
          ),
          const Text('Mẫu: 2 buổi luyện gần đây. Thói quen khác với năng lực.'),
          if (id != 'L-010')
            StateNotice(state: id == 'L-011' ? 'offline' : 'syncing'),
        ];
      case 'L-020':
      case 'L-071':
        return [
          heading(c, s.title, 'Chọn một chủ đề gần với cuộc sống của bạn.'),
          TextField(
            decoration: const InputDecoration(
              labelText: 'Tìm chủ đề',
              prefixIcon: Icon(Icons.search),
            ),
            onChanged: (v) => setState(() => search = v),
          ),
          if (search.isEmpty || 'chào hỏi'.contains(search.toLowerCase()))
            TopicCard(
              title: 'Chào hỏi cơ bản',
              detail: 'Chào ai đó và đáp lại · Khoảng 5 phút · Cơ bản',
              label: 'Từ vựng',
              icon: Icons.waving_hand_outlined,
              onTap: () => go('L-021', lessonDomain: LessonDomain.vocabulary),
            ),
          if (search.isEmpty ||
              'câu giới thiệu ngữ pháp'.contains(search.toLowerCase()))
            TopicCard(
              title: 'Câu giới thiệu cơ bản',
              detail: 'Khoảng 5 phút · Cơ bản',
              label: 'Ngữ pháp',
              icon: Icons.text_fields,
              onTap: () => go('L-021', lessonDomain: LessonDomain.grammar),
            ),
          if (search.isEmpty || 'nghe lời chào'.contains(search.toLowerCase()))
            TopicCard(
              title: 'Nghe lời chào',
              detail: 'Khoảng 5 phút · Cơ bản',
              label: 'Nghe',
              icon: Icons.headphones_outlined,
              onTap: () => go('L-021', lessonDomain: LessonDomain.listening),
            ),
          if (search.isEmpty)
            row(
              'Đồ ăn và nhà hàng',
              'Hỏi một món ăn · Khoảng 6 phút · Xem trước',
              'L-042',
              icon: Icons.restaurant_outlined,
            ),
          if (search.isEmpty)
            row(
              'Đi quanh thành phố',
              'Hỏi đường · Khoảng 5 phút · Xem trước',
              'L-042',
              icon: Icons.map_outlined,
            ),
          if (search.isNotEmpty &&
              !'chào hỏi'.contains(search.toLowerCase()) &&
              !'câu giới thiệu ngữ pháp'.contains(search.toLowerCase()) &&
              !'nghe lời chào'.contains(search.toLowerCase()))
            const Notice(
              title: 'Chưa tìm thấy bài phù hợp',
              detail: 'Thử từ “chào” hoặc xóa từ khóa để xem các chủ đề.',
            ),
          row(
            'Bài đang học dở',
            'Tiếp tục đúng phiên bản đã bắt đầu',
            'L-033',
            icon: Icons.history,
          ),
        ];
      case 'L-033':
        return [
          heading(
            c,
            s.title,
            'Bài mẫu đang ở phần thử tự nhớ. Phiên bản bài đã bắt đầu được giữ riêng.',
          ),
          const Notice(
            title: 'Câu trước vẫn được giữ',
            detail: 'Quay lại không tạo thêm bằng chứng trả lời độc lập.',
          ),
          primary('Tiếp tục bài', 'L-024'),
        ];
      case 'L-040':
        return [
          heading(c, s.title, 'Học từng bước, quay lại khi cần.'),
          const ClipRRect(
            borderRadius: BorderRadius.all(Radius.circular(24)),
            child: ScenicWindow(),
          ),
          Column(
            children: [
              JourneyMilestone(
                title: '1. Chào hỏi',
                detail: 'Đã luyện (mẫu) · Có thể ôn lại',
                icon: Icons.check_circle_outline,
                onTap: () => go('L-041'),
              ),
              const TrailConnector(),
              JourneyMilestone(
                title: '2. Làm quen',
                detail: 'Cần thêm lần tự trả lời',
                current: true,
                icon: Icons.trip_origin,
                onTap: () => go('L-041'),
              ),
              const TrailConnector(reverse: true),
              JourneyMilestone(
                title: '3. Trong quán ăn',
                detail: 'Xem trước · Cần hoàn thành mục tiêu trước',
                icon: Icons.lock_outline,
                onTap: () => go('L-042'),
              ),
            ],
          ),
          const Text(
            'Mở bài dựa trên bằng chứng học; xem trước không tự mở khóa.',
          ),
        ];
      case 'L-041':
        return [
          heading(
            c,
            s.title,
            'Bạn sẽ nhận biết lời chào và đáp lại trong một tình huống mới.',
          ),
          const Surface(
            child: Text(
              'Mục tiêu mẫu: tự trả lời đúng ở hai câu khác nhau, có một câu thử không dùng gợi ý. Lần có hỗ trợ được giữ riêng.',
            ),
          ),
          primary('Ôn lại lời chào', 'L-021'),
          if (state.isEmpty || state == 'eligible')
            TextButton(
              onPressed: () => go('L-026'),
              child: const Text('Tự thử một câu mới'),
            ),
          row('Xem những gì đã luyện', 'Câu đã làm và phần còn thiếu', 'L-051'),
        ];
      case 'L-042':
        return [
          heading(c, s.title, 'Xem mục tiêu trước khi bắt đầu.'),
          const Notice(
            title: 'Bạn có thể khám phá trước',
            detail:
                'Để bắt đầu bài tiếp theo, cần đủ bằng chứng ở bài chào hỏi. Xem trước không phải hoàn thành.',
          ),
          row(
            'Quay lại bước hiện tại',
            'Luyện thêm một câu không dùng gợi ý',
            'L-041',
          ),
        ];
      case 'L-050':
        return [
          Surface(
            tint: true,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const Center(child: Mascot(height: 104)),
                heading(c, 'Góc của bạn', 'Học theo nhịp phù hợp với bạn.'),
              ],
            ),
          ),
          row(
            'Mục tiêu hiện tại',
            prefs.goal,
            'L-052',
            icon: Icons.flag_outlined,
          ),
          row(
            'Những bước đã đi',
            'Xem lần thực hành và phần cần luyện thêm',
            'L-070',
            icon: Icons.insights_outlined,
          ),
          row(
            'Học ngoại tuyến',
            'Bài đã tải và các bài đang chờ gửi',
            'L-054',
            icon: Icons.download_outlined,
          ),
          row(
            'Cài đặt',
            'Giao diện, thông báo và chuyển động',
            'L-072',
            icon: Icons.settings_outlined,
          ),
        ];
      case 'L-051':
      case 'L-070':
        return [
          heading(
            c,
            s.title,
            'Nhìn lại điều đã làm; không phải điểm năng lực.',
          ),
          const Surface(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Chào hỏi · dữ liệu mẫu',
                  style: TextStyle(fontSize: 20, fontWeight: FontWeight.w600),
                ),
                SizedBox(height: 16),
                EvidenceFact(
                  value: '2 câu đã thực hành',
                  label: 'Điều đã làm, không phải điểm năng lực.',
                  icon: Icons.menu_book_outlined,
                ),
                EvidenceFact(
                  value: '1 câu tự trả lời đúng ở lần đầu',
                  label: 'Một quan sát độc lập trong bài mẫu.',
                  icon: Icons.lightbulb_outline,
                ),
                EvidenceFact(
                  value: '1 câu có gợi ý',
                  label: 'Lần có hỗ trợ được giữ riêng.',
                  icon: Icons.chat_bubble_outline,
                ),
                EvidenceFact(
                  value: 'Chưa thử lại sau một khoảng thời gian',
                  label: 'Chưa có bằng chứng ghi nhớ lâu hơn.',
                  icon: Icons.schedule,
                ),
              ],
            ),
          ),
          const Notice(
            title: 'Chưa đủ để kết luận đã vững',
            detail:
                'Cần thêm câu độc lập ở tình huống mới và lần ôn sau. Số buổi học chỉ mô tả thói quen.',
          ),
          primary('Luyện một câu mới', 'L-021'),
        ];
      case 'L-053':
      case 'L-072':
        return [
          heading(c, s.title, 'Điều chỉnh để học thoải mái hơn.'),
          SwitchListTile(
            contentPadding: EdgeInsets.zero,
            title: const Text('Giảm chuyển động'),
            subtitle: const Text(
              'Ưu tiên chuyển màn hình ngay, không hiệu ứng.',
            ),
            value: prefs.reducedMotion,
            onChanged: prefs.setMotion,
          ),
          SwitchListTile(
            contentPadding: EdgeInsets.zero,
            title: const Text('Giao diện tối'),
            value: prefs.dark,
            onChanged: prefs.setDark,
          ),
          SwitchListTile(
            contentPadding: EdgeInsets.zero,
            title: const Text('Nhắc học nhẹ nhàng'),
            subtitle: const Text('Lựa chọn mẫu; chưa gửi thông báo thật.'),
            value: prefs.notifications,
            onChanged: prefs.setNotifications,
          ),
          const Text(
            'Cỡ chữ theo cài đặt của thiết bị. Lựa chọn ở đây chỉ tồn tại trong bản xem trước.',
          ),
          row('Bài học ngoại tuyến', 'Xem trạng thái tải', 'L-054'),
        ];
      case 'L-054':
        return [
          heading(
            c,
            s.title,
            'Học những bài đã tải, ngay cả khi không có mạng.',
          ),
          row(
            'Chào hỏi · sẵn sàng (mẫu)',
            'Phiên bản mẫu r1 · Chỉ dùng bài còn hợp lệ',
            'L-021',
            icon: Icons.offline_pin_outlined,
          ),
          const Notice(
            title: 'Chưa có tải xuống thật',
            detail:
                'Bản xem trước chỉ minh họa các trạng thái tải, hết hạn và thử lại. Không ghi nhận tải thành công.',
          ),
          row('Bài còn chờ gửi', 'Xem trạng thái từng phần', 'L-060'),
        ];
      case 'L-060':
      case 'L-061':
      case 'L-064':
        return [
          heading(
            c,
            s.title,
            'Bài đã lưu và bài đã được xác nhận là hai trạng thái khác nhau.',
          ),
          StateNotice(
            state:
                widget.reviewState ??
                (id == 'L-064' ? 'reauth' : 'local-queued'),
          ),
          const Surface(
            child: Text(
              'Mẫu: 1 bài đang chờ gửi; 1 bài đã có xác nhận mẫu. Bản xem trước chưa có hàng đợi bền vững hoặc dịch vụ đồng bộ thật.',
            ),
          ),
          row('Xem bài đã tải', 'Bạn có thể học bài còn hợp lệ', 'L-054'),
          row('Quay về trang chủ', 'Tiếp tục khi bạn sẵn sàng', 'L-010'),
        ];
      case 'L-062':
      case 'L-063':
        return [
          heading(c, s.title),
          const Center(child: Mascot(height: 130)),
          StateNotice(
            state:
                widget.reviewState ?? (id == 'L-062' ? 'error' : 'nothing-due'),
          ),
          primary('Khám phá bài học', 'L-020'),
        ];
      case 'L-073':
        return [
          heading(
            c,
            s.title,
            'Những lời nhắc vừa đủ, bạn chọn khi nào muốn nhận.',
          ),
          const Notice(
            title: 'Chưa có thông báo mới',
            detail: 'Không có nhắc học thật trong bản xem trước.',
          ),
          row('Tùy chọn thông báo', 'Bật hoặc tắt lời nhắc mẫu', 'L-072'),
        ];
      default:
        return [heading(c, s.title), primary('Về trang chủ', 'L-010')];
    }
  }
}
