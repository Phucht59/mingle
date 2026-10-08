import 'dart:async';
import 'package:flutter/cupertino.dart';
import 'package:flutter/semantics.dart';
import 'package:flutter/services.dart';
import 'learning_state.dart';
import 'proof_controller.dart';
import 'proof_server.dart';
import 'open_store_unsupported.dart'
    if (dart.library.io) 'open_store_native.dart';

const _blue = CupertinoDynamicColor.withBrightness(
  color: Color(0xff2857c7),
  darkColor: Color(0xffacc0ff),
);
const _surface = CupertinoDynamicColor.withBrightness(
  color: Color(0xffffffff),
  darkColor: Color(0xff1c222d),
);
Color _resolve(Color color, BuildContext context) =>
    CupertinoDynamicColor.resolve(color, context);
Widget _copy(String text, {bool heading = false}) => Padding(
  padding: const EdgeInsets.only(bottom: 12),
  child: Text(
    text,
    style: TextStyle(
      fontSize: heading ? 24 : 17,
      fontWeight: heading ? FontWeight.w600 : FontWeight.normal,
    ),
  ),
);
Widget _primary(String label, VoidCallback? onPressed, {Key? key}) => SizedBox(
  width: double.infinity,
  child: CupertinoButton.filled(
    key: key,
    onPressed: onPressed,
    child: Text(label, textAlign: TextAlign.center),
  ),
);
Widget _reviewLabel([
  String text = 'Proof • dữ liệu mẫu, danh tính được cấp quyền mẫu',
]) => Padding(
  padding: const EdgeInsets.symmetric(vertical: 8),
  child: Text(text, style: const TextStyle(fontSize: 13)),
);

class M3xProofApp extends StatefulWidget {
  const M3xProofApp({super.key, this.controller, this.brightness});
  final ProofController? controller;
  final Brightness? brightness;
  @override
  State<M3xProofApp> createState() => _M3xProofAppState();
}

class _M3xProofAppState extends State<M3xProofApp> {
  late Future<ProofController> _future = _load();
  ProofController? _owned;
  Future<ProofController> _load() async {
    if (widget.controller != null) return widget.controller!;
    final store = await openNativeStore('learning');
    final server = ControlledProofServer(
      await openNativeStore('server_receipts'),
    )..ackEnabled = !const bool.fromEnvironment('MINGO_M3X_WITHHOLD_ACK');
    return _owned = await ProofController.open(
      store,
      server,
      online: !const bool.fromEnvironment('MINGO_M3X_OFFLINE'),
    );
  }

  @override
  void dispose() {
    _owned?.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) => CupertinoApp(
    title: 'Mingo • Native Companion proof',
    debugShowCheckedModeBanner: false,
    theme: CupertinoThemeData(
      brightness: widget.brightness,
      primaryColor: _blue,
      barBackgroundColor: _surface,
      primaryContrastingColor: const CupertinoDynamicColor.withBrightness(
        color: Color(0xffffffff),
        darkColor: Color(0xff14203c),
      ),
    ),
    home: FutureBuilder<ProofController>(
      future: _future,
      builder: (context, snapshot) {
        if (snapshot.hasData) return _ProofShell(controller: snapshot.data!);
        return CupertinoPageScaffold(
          child: SafeArea(
            child: Padding(
              padding: const EdgeInsets.all(24),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  _copy(
                    snapshot.hasError
                        ? 'Chưa mở được dữ liệu trên thiết bị. Dữ liệu được giữ để khôi phục; chưa ghi nhận thêm kết quả.'
                        : 'Đang mở dữ liệu trên thiết bị…',
                  ),
                  if (snapshot.hasError)
                    _primary(
                      'Thử mở lại',
                      () => setState(() => _future = _load()),
                    ),
                ],
              ),
            ),
          ),
        );
      },
    ),
  );
}

class _ProofShell extends StatefulWidget {
  const _ProofShell({required this.controller});
  final ProofController controller;
  @override
  State<_ProofShell> createState() => _ProofShellState();
}

class _ProofShellState extends State<_ProofShell> {
  ProofController get c => widget.controller;
  late final tabs = CupertinoTabController(initialIndex: c.state.tab);
  late final homeScroll = ScrollController(
    initialScrollOffset: c.state.homeOffset,
  );
  @override
  void dispose() {
    tabs.dispose();
    homeScroll.dispose();
    super.dispose();
  }

  Future<void> _openTask(String key) async {
    if (!await c.origin(
      tabs.index,
      homeScroll.hasClients ? homeScroll.offset : c.state.homeOffset,
    )) {
      return;
    }
    if (!await c.pause(key) || !mounted) return;
    await Navigator.of(context).push(
      CupertinoPageRoute<void>(
        fullscreenDialog: true,
        builder: (_) => ProofTaskPage(controller: c, taskKey: key),
      ),
    );
  }

  Future<void> _openResult(bool pending) async {
    final key = pending ? 'closure-pending' : 'closure-confirmed';
    if (!await c.seedClosure(pending: pending, key: key) || !mounted) return;
    await Navigator.of(context).push(
      CupertinoPageRoute<void>(
        fullscreenDialog: true,
        builder: (_) => ProofResultPage(controller: c, taskKey: key),
      ),
    );
  }

  void _fixtures() => showCupertinoModalPopup<void>(
    context: context,
    builder: (sheet) => _OpaqueActionSheet(
      title: const Text('Bộ fixture M3.X • công cụ review'),
      message: const Text(
        'Check và Result là các fixture độc lập; một câu Practice không hoàn tất chu trình học.',
      ),
      actions: [
        CupertinoActionSheetAction(
          onPressed: () {
            Navigator.pop(sheet);
            unawaited(_openTask('check'));
          },
          child: const Text('Independent Check'),
        ),
        CupertinoActionSheetAction(
          onPressed: () {
            Navigator.pop(sheet);
            unawaited(_openResult(false));
          },
          child: const Text('Result'),
        ),
        CupertinoActionSheetAction(
          onPressed: () {
            Navigator.pop(sheet);
            unawaited(_openResult(true));
          },
          child: const Text('Result Pending Sync'),
        ),
        CupertinoActionSheetAction(
          onPressed: () {
            Navigator.pop(sheet);
            Navigator.of(context).push(
              CupertinoPageRoute<void>(
                fullscreenDialog: true,
                builder: (_) => ProofSyncPage(controller: c),
              ),
            );
          },
          child: const Text('Sync Recovery'),
        ),
        CupertinoActionSheetAction(
          onPressed: () {
            Navigator.pop(sheet);
            Navigator.of(context).push(
              CupertinoPageRoute<void>(
                fullscreenDialog: true,
                builder: (_) => _WelcomeFixture(
                  onExplore: () {
                    tabs.index = 1;
                    unawaited(c.origin(1, c.state.homeOffset));
                  },
                ),
              ),
            );
          },
          child: const Text('Welcome • anchor polish'),
        ),
      ],
      cancelButton: CupertinoActionSheetAction(
        onPressed: () => Navigator.pop(sheet),
        child: const Text('Đóng'),
      ),
    ),
  );
  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: c,
    builder: (context, _) => CupertinoTabScaffold(
      controller: tabs,
      tabBar: CupertinoTabBar(
        backgroundColor: _resolve(_surface, context),
        onTap: (index) {
          unawaited(
            c.origin(
              index,
              homeScroll.hasClients ? homeScroll.offset : c.state.homeOffset,
            ),
          );
        },
        items: const [
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.house),
            label: 'Hôm nay',
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.book),
            label: 'Học',
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.chart_bar),
            label: 'Tiến độ',
          ),
          BottomNavigationBarItem(
            icon: Icon(CupertinoIcons.person),
            label: 'Hồ sơ',
          ),
        ],
      ),
      tabBuilder: (context, index) {
        if (index != 0) {
          return CupertinoPageScaffold(
            navigationBar: CupertinoNavigationBar(
              middle: Text(['Hôm nay', 'Học', 'Tiến độ', 'Hồ sơ'][index]),
            ),
            child: SafeArea(
              child: ListView(
                padding: const EdgeInsets.all(24),
                children: [
                  _reviewLabel(
                    'Fixture shell • nội dung đích này chưa được triển khai trong slice',
                  ),
                  _copy(
                    index == 1
                        ? 'Khám phá một tình huống'
                        : index == 2
                        ? 'Bằng chứng học được giữ riêng'
                        : 'Cài đặt và hồ sơ',
                  ),
                  CupertinoButton(
                    onPressed: () => setState(() => tabs.index = 0),
                    child: const Text('Về Hôm nay'),
                  ),
                ],
              ),
            ),
          );
        }
        final key = c.nextAction, item = c.task(key).item;
        return CupertinoPageScaffold(
          child: CustomScrollView(
            key: const ValueKey('home-scroll'),
            controller: homeScroll,
            slivers: [
              CupertinoSliverNavigationBar(
                largeTitle: const Text('Hôm nay'),
                trailing: CupertinoButton(
                  padding: EdgeInsets.zero,
                  onPressed: _fixtures,
                  child: Semantics(
                    label: 'Mở bộ fixture',
                    button: true,
                    child: const Icon(CupertinoIcons.ellipsis),
                  ),
                ),
              ),
              SliverPadding(
                padding: const EdgeInsets.fromLTRB(24, 12, 24, 40),
                sliver: SliverList.list(
                  children: [
                    _reviewLabel(),
                    _copy('Một việc nhỏ, có ý nghĩa.'),
                    Container(
                      padding: const EdgeInsets.all(20),
                      decoration: BoxDecoration(
                        color: _resolve(_surface, context),
                        borderRadius: BorderRadius.circular(16),
                      ),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          _copy('Đang học'),
                          _copy(item.situation, heading: true),
                          _copy(c.homeReason),
                          _copy(
                            c.task(key).submitted
                                ? 'Nối lại câu trả lời đã gửi.'
                                : 'Nối lại từ câu trả lời đang dở.',
                          ),
                          _primary(
                            'Tiếp tục bài học',
                            () => unawaited(_openTask(key)),
                          ),
                        ],
                      ),
                    ),
                    const SizedBox(height: 16),
                    if (c.current(key) != null)
                      ProofSyncTruth(command: c.current(key)!),
                    CupertinoButton(
                      alignment: Alignment.centerLeft,
                      onPressed: () {
                        setState(() => tabs.index = 1);
                        unawaited(
                          c.origin(
                            1,
                            homeScroll.hasClients
                                ? homeScroll.offset
                                : c.state.homeOffset,
                          ),
                        );
                      },
                      child: const Text('Khám phá'),
                    ),
                    _copy('Ngữ cảnh của bạn', heading: true),
                    _copy(
                      'Bạn có thể dừng và quay lại câu đang học. Các lần trả lời đầu tiên và lần luyện sau hỗ trợ được giữ riêng; không suy ra mức thành thạo từ một câu.',
                    ),
                    if (c.error != null) _copy(c.error!),
                  ],
                ),
              ),
            ],
          ),
        );
      },
    ),
  );
}

class ProofTaskPage extends StatefulWidget {
  const ProofTaskPage({
    super.key,
    required this.controller,
    required this.taskKey,
  });
  final ProofController controller;
  final String taskKey;
  @override
  State<ProofTaskPage> createState() => _ProofTaskPageState();
}

class _ProofTaskPageState extends State<ProofTaskPage> {
  ProofController get c => widget.controller;
  String get key => widget.taskKey;
  String? _lastAnnounced;
  @override
  void initState() {
    super.initState();
    _lastAnnounced = c.current(key)?.phase == SyncPhase.synced
        ? c.current(key)?.id
        : null;
    c.addListener(_announce);
  }

  void _announce() {
    final command = c.current(key);
    if (command?.phase == SyncPhase.synced &&
        command?.feedback != null &&
        command?.id != _lastAnnounced) {
      _lastAnnounced = command!.id;
      unawaited(
        SemanticsService.announce(
          command.feedback!['verdict'] as String,
          TextDirection.ltr,
        ),
      );
    }
  }

  @override
  void dispose() {
    c.removeListener(_announce);
    super.dispose();
  }

  Future<void> _close() async {
    if (await c.pause(key) && mounted) Navigator.pop(context);
  }

  void _responses() => showCupertinoModalPopup<void>(
    context: context,
    builder: (sheet) => _OpaqueActionSheet(
      title: const Text('Các lần trả lời'),
      message: Column(
        children: [
          for (final (index, response) in c.task(key).responses.indexed)
            Padding(
              padding: const EdgeInsets.only(bottom: 16),
              child: Text(
                '${index == 0 ? 'Lần đầu' : 'Lần luyện ${index + 1}'}: ${c.task(key).item.options[response.answer]}\n'
                '${response.assisted
                    ? 'Có hỗ trợ: ${response.assistance.contains('hint') ? 'gợi ý' : 'sau giải thích'}'
                    : c.task(key).item.check
                    ? 'Tự làm trong bước kiểm tra'
                    : 'Không dùng gợi ý'}',
              ),
            ),
        ],
      ),
      cancelButton: CupertinoActionSheetAction(
        onPressed: () => Navigator.pop(sheet),
        child: const Text('Đóng'),
      ),
    ),
  );
  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: c,
    builder: (context, _) {
      final t = c.task(key), item = c.task(key).item, command = c.current(key);
      final feedback = command?.phase == SyncPhase.synced
          ? command?.feedback
          : null;
      final evaluated = feedback != null;
      final actions = Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          if (!t.submitted && !item.check && c.policy.hint)
            CupertinoButton(
              onPressed: c.busy ? null : () => unawaited(c.hint(key)),
              child: const Text('Gợi ý'),
            ),
          if (c.canRetry(key))
            CupertinoButton(
              onPressed: c.busy ? null : () => unawaited(c.retry(key)),
              child: const Text('Thử lại'),
            ),
          if (t.responses.isNotEmpty)
            CupertinoButton(
              onPressed: _responses,
              child: const Text('Các lần trả lời'),
            ),
          _primary(
            evaluated
                ? 'Về Hôm nay'
                : t.submitted
                ? 'Đã gửi • chờ xác nhận'
                : item.check
                ? 'Gửi câu trả lời'
                : 'Kiểm tra',
            evaluated
                ? () => unawaited(_close())
                : c.busy || t.selection == null || t.submitted
                ? null
                : () => unawaited(c.submit(key)),
            key: const ValueKey('task-primary'),
          ),
        ],
      );
      final large =
          MediaQuery.textScalerOf(context).scale(17) > 24 ||
          MediaQuery.sizeOf(context).height < 500;
      return CupertinoPageScaffold(
        navigationBar: CupertinoNavigationBar(
          middle: Text(item.check ? 'Tự kiểm tra' : 'Luyện tập'),
          leading: CupertinoButton(
            padding: EdgeInsets.zero,
            onPressed: () => unawaited(_close()),
            child: const Text('Đóng'),
          ),
        ),
        child: SafeArea(
          child: Column(
            children: [
              Expanded(
                child: ListView(
                  padding: const EdgeInsets.all(20),
                  children: [
                    _reviewLabel(),
                    _copy(item.situation),
                    if (item.check)
                      _copy(
                        'Tự làm • không gợi ý. Câu trả lời được giữ riêng với phần luyện tập.',
                      ),
                    _copy(item.prompt, heading: true),
                    _copy(item.intent),
                    for (final option in item.options.entries)
                      _AnswerUnit(
                        key: ValueKey('${item.questionRevision}/${option.key}'),
                        text: option.value,
                        selected: t.selection == option.key,
                        enabled: !t.submitted && !c.busy,
                        feedback: t.selection == option.key ? feedback : null,
                        onSelect: () async {
                          final changed = t.selection != option.key;
                          if (await c.select(key, option.key) &&
                              changed &&
                              const bool.fromEnvironment('MINGO_M3X_HAPTICS')) {
                            await HapticFeedback.selectionClick();
                          }
                        },
                      ),
                    if (t.hintSeen)
                      _copy(
                        'Gợi ý: “reservation” nói về việc đặt phòng trước. Lần này có hỗ trợ.',
                      ),
                    if (command != null) ...[
                      _copy(
                        t.responses.last.assisted
                            ? 'Lần luyện sau hỗ trợ • lần đầu vẫn được giữ.'
                            : item.check
                            ? 'Câu trả lời trong điều kiện tự làm.'
                            : 'Lần đầu • không dùng gợi ý.',
                      ),
                      ProofSyncTruth(command: command),
                    ],
                    if (t.submitted &&
                        command?.phase == SyncPhase.synced &&
                        feedback == null)
                      _copy(
                        'Giải thích chưa sẵn sàng. Kết quả đã được xác nhận; chưa có lời giải để hiển thị.',
                      ),
                    if (c.error != null) _copy(c.error!),
                    if (large) actions,
                  ],
                ),
              ),
              if (!large)
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 8, 20, 12),
                  child: actions,
                ),
            ],
          ),
        ),
      );
    },
  );
}

class _AnswerUnit extends StatelessWidget {
  const _AnswerUnit({
    super.key,
    required this.text,
    required this.selected,
    required this.enabled,
    required this.onSelect,
    this.feedback,
  });
  final String text;
  final bool selected, enabled;
  final Future<void> Function() onSelect;
  final Map<String, dynamic>? feedback;
  @override
  Widget build(BuildContext context) {
    final dark =
        CupertinoTheme.of(context).brightness == Brightness.dark ||
        (CupertinoTheme.of(context).brightness == null &&
            MediaQuery.platformBrightnessOf(context) == Brightness.dark);
    final correct = feedback?['correct'] == true;
    final border = feedback != null
        ? (correct
              ? (dark ? const Color(0xffb1e3c5) : const Color(0xff236145))
              : (dark ? const Color(0xffffd0ac) : const Color(0xff8a482a)))
        : selected
        ? _resolve(_blue, context)
        : dark
        ? const Color(0xff8390a9)
        : const Color(0xff8793a8);
    final content = Container(
      decoration: BoxDecoration(
        color: _resolve(_surface, context),
        border: Border.all(color: border, width: selected ? 2 : 1),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Semantics(
            container: true,
            label: text,
            button: true,
            selected: selected,
            enabled: enabled,
            inMutuallyExclusiveGroup: true,
            onTap: enabled ? () => unawaited(onSelect()) : null,
            child: ExcludeSemantics(
              child: CupertinoButton(
                padding: const EdgeInsets.all(16),
                onPressed: enabled ? () => unawaited(onSelect()) : null,
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Icon(
                      selected
                          ? CupertinoIcons.largecircle_fill_circle
                          : CupertinoIcons.circle,
                      size: 22,
                      color: border,
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Text(
                        text,
                        style: TextStyle(
                          color: CupertinoTheme.of(
                            context,
                          ).textTheme.textStyle.color,
                        ),
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
          if (feedback != null)
            Padding(
              padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Semantics(
                    container: true,
                    header: true,
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        ExcludeSemantics(
                          child: Icon(
                            correct
                                ? CupertinoIcons.check_mark_circled
                                : CupertinoIcons.info,
                            color: border,
                            size: 20,
                          ),
                        ),
                        const SizedBox(width: 8),
                        Expanded(
                          child: Text(
                            feedback!['verdict'] as String,
                            style: TextStyle(
                              color: border,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(feedback!['explanation'] as String),
                  const SizedBox(height: 8),
                  const Text('Câu phù hợp', style: TextStyle(fontSize: 14)),
                  Text(feedback!['correction'] as String),
                ],
              ),
            ),
        ],
      ),
    );
    final reduced =
        MediaQuery.disableAnimationsOf(context) ||
        MediaQuery.accessibleNavigationOf(context);
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: reduced
          ? content
          : AnimatedSize(
              duration: const Duration(milliseconds: 260),
              alignment: Alignment.topCenter,
              child: content,
            ),
    );
  }
}

class ProofSyncTruth extends StatelessWidget {
  const ProofSyncTruth({super.key, required this.command});
  final QueuedCommand command;
  @override
  Widget build(BuildContext context) {
    final text = switch (command.phase) {
      SyncPhase.pending =>
        'Đã lưu trên thiết bị • chờ đồng bộ. Máy chủ chưa xác nhận kết quả.',
      SyncPhase.syncing => 'Đang đồng bộ • chờ máy chủ xác nhận.',
      SyncPhase.synced => 'Đã đồng bộ • máy chủ đã xác nhận bản ghi.',
      SyncPhase.failed =>
        'Chưa đồng bộ • dữ liệu đã lưu trên thiết bị. Có thể thử lại.',
      SyncPhase.conflict =>
        'Cần xử lý xung đột • câu trả lời và phiên bản gốc vẫn được giữ.',
      SyncPhase.reauth =>
        'Cần đăng nhập lại • dữ liệu riêng trên thiết bị vẫn được giữ.',
      SyncPhase.rejected =>
        'Máy chủ chưa chấp nhận • bản ghi gốc vẫn được giữ để khôi phục.',
    };
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 12),
      child: Semantics(
        label: text,
        child: ExcludeSemantics(
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Icon(
                command.phase == SyncPhase.synced
                    ? CupertinoIcons.check_mark_circled
                    : CupertinoIcons.doc_text,
                size: 22,
              ),
              const SizedBox(width: 10),
              Expanded(child: Text(text)),
            ],
          ),
        ),
      ),
    );
  }
}

class ProofResultPage extends StatelessWidget {
  const ProofResultPage({
    super.key,
    required this.controller,
    required this.taskKey,
  });
  final ProofController controller;
  final String taskKey;
  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: controller,
    builder: (context, _) => CupertinoPageScaffold(
      navigationBar: const CupertinoNavigationBar(
        middle: Text('Kết quả'),
        automaticallyImplyLeading: false,
      ),
      child: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(24),
          children: [
            _reviewLabel(
              'Result fixture • chu trình hoàn tất mẫu, độc lập với Practice tương tác',
            ),
            _copy('Phiên mẫu đã khép lại.', heading: true),
            _copy('Bạn đã luyện cách xác nhận đặt phòng.'),
            _copy('Một điều mang theo'),
            _copy('“I have a reservation.”', heading: true),
            _copy('Xác nhận rằng bạn đã đặt phòng trước.'),
            _copy(
              'Bằng chứng mẫu: câu trả lời được ghi cùng điều kiện luyện tập. Một phiên ngắn chưa đủ để kết luận mức thành thạo.',
            ),
            if (controller.current(taskKey) != null)
              ProofSyncTruth(command: controller.current(taskKey)!),
            _primary('Xong', () => Navigator.pop(context)),
            CupertinoButton(
              onPressed: () {
                final decision = controller.decideProofNextAction();
                showCupertinoModalPopup<void>(
                  context: context,
                  builder: (sheet) => _OpaqueActionSheet(
                    title: const Text('Chọn việc tiếp theo'),
                    message: Text(
                      decision == null
                          ? 'Chưa có việc học hợp lệ để tiếp tục. Dữ liệu cũ vẫn được giữ.'
                          : controller.homeReason,
                    ),
                    actions: [
                      if (decision != null)
                        CupertinoActionSheetAction(
                          onPressed: () {
                            Navigator.pop(sheet);
                            Navigator.pop(context);
                          },
                          child: const Text('Xem việc tiếp theo trên Hôm nay'),
                        ),
                    ],
                    cancelButton: CupertinoActionSheetAction(
                      onPressed: () => Navigator.pop(sheet),
                      child: const Text('Chọn sau'),
                    ),
                  ),
                );
              },
              child: const Text('Học tiếp'),
            ),
          ],
        ),
      ),
    ),
  );
}

class ProofSyncPage extends StatelessWidget {
  const ProofSyncPage({super.key, required this.controller});
  final ProofController controller;
  @override
  Widget build(BuildContext context) => ListenableBuilder(
    listenable: controller,
    builder: (context, _) => CupertinoPageScaffold(
      navigationBar: CupertinoNavigationBar(
        middle: const Text('Đồng bộ'),
        leading: CupertinoButton(
          padding: EdgeInsets.zero,
          onPressed: () => Navigator.pop(context),
          child: const Text('Đóng'),
        ),
      ),
      child: SafeArea(
        child: ListView(
          padding: const EdgeInsets.all(24),
          children: [
            _reviewLabel('Sync Recovery • công cụ điều khiển server fixture'),
            for (final command in controller.state.commands.values)
              ProofSyncTruth(command: command),
            if (controller.state.commands.isEmpty)
              _copy('Chưa có bản ghi chờ đồng bộ.'),
            _primary(
              'Thử đồng bộ',
              controller.busy
                  ? null
                  : () => unawaited(controller.syncPending()),
            ),
            if (controller.server is ControlledProofServer) ...[
              CupertinoButton(
                onPressed: () {
                  (controller.server as ControlledProofServer).ackEnabled =
                      false;
                  controller.networkRestored();
                },
                child: const Text('Kết nối lại • chưa ACK'),
              ),
              CupertinoButton(
                onPressed: () {
                  (controller.server as ControlledProofServer).ackEnabled =
                      true;
                  unawaited(controller.syncPending());
                },
                child: const Text('Cho server fixture trả ACK'),
              ),
              CupertinoButton(
                onPressed: () => unawaited(controller.requireReauth()),
                child: const Text('Fixture • cần đăng nhập lại'),
              ),
              CupertinoButton(
                onPressed: controller.restoreFixtureIdentity,
                child: const Text('Fixture • khôi phục danh tính mẫu'),
              ),
            ],
            if (controller.state.commands.values.any(
              (q) => q.phase == SyncPhase.conflict,
            ))
              _copy(
                'Giữ nguyên câu trả lời và phiên bản gốc. Chưa có chính sách khôi phục tự động; có thể đóng an toàn và xem lại trạng thái.',
              ),
            if (controller.error != null) _copy(controller.error!),
          ],
        ),
      ),
    ),
  );
}

// The pinned SDK has no Reduce Transparency signal. Put the STANDARD platform
// action sheet on a solid surface for all settings, instead of inventing glass.
class _OpaqueActionSheet extends StatelessWidget {
  const _OpaqueActionSheet({
    this.title,
    this.message,
    this.actions,
    this.cancelButton,
  });
  final Widget? title, message, cancelButton;
  final List<Widget>? actions;
  @override
  Widget build(BuildContext context) => DecoratedBox(
    decoration: BoxDecoration(
      color: _resolve(_surface, context),
      borderRadius: BorderRadius.circular(14),
    ),
    child: CupertinoActionSheet(
      title: title,
      message: message,
      actions: actions,
      cancelButton: cancelButton,
    ),
  );
}

class _WelcomeFixture extends StatelessWidget {
  const _WelcomeFixture({required this.onExplore});
  final VoidCallback onExplore;
  @override
  Widget build(BuildContext context) => CupertinoPageScaffold(
    child: SafeArea(
      child: ListView(
        padding: const EdgeInsets.all(24),
        children: [
          _reviewLabel('Welcome fixture • chưa triển khai onboarding/auth'),
          _copy('Học một điều. Dùng trong đời sống.', heading: true),
          _copy(
            'Một tình huống gần gũi. Lời giải thích rõ ràng. Một bước theo nhịp của bạn.',
          ),
          _primary('Bắt đầu', () => Navigator.pop(context)),
          CupertinoButton(
            onPressed: () {
              Navigator.pop(context);
              onExplore();
            },
            child: const Text('Khám phá trước'),
          ),
        ],
      ),
    ),
  );
}
