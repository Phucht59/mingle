import 'dart:io';
import 'dart:ui' as ui;
import 'package:flutter/cupertino.dart';
import 'package:flutter/rendering.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:adaptive_learner/m3x/learning_state.dart';
import 'package:adaptive_learner/m3x/proof_app.dart';
import 'package:adaptive_learner/m3x/proof_controller.dart';
import 'package:adaptive_learner/m3x/proof_server.dart';
import 'm3x_domain_test.dart' show MemoryStore;

const capture = ValueKey('proof-capture');
Future<void> tap(WidgetTester t, String label) async {
  final matches = find.text(label);
  if (matches.evaluate().isEmpty) {
    await t.scrollUntilVisible(
      matches,
      200,
      scrollable: find.byType(Scrollable).first,
      maxScrolls: 50,
    );
  }
  final finder = matches.first;
  await t.ensureVisible(finder);
  await t.pumpAndSettle();
  await t.runAsync(() => t.tap(finder));
  await t.runAsync(() => Future<void>.delayed(Duration.zero));
  await t.pumpAndSettle();
  await t.runAsync(() => Future<void>.delayed(Duration.zero));
  await t.pumpAndSettle();
}

Future<void> screenshot(WidgetTester t, String name) async {
  final directory = Platform.environment['M3X_EVIDENCE_DIR'];
  if (directory == null) return;
  await t.runAsync(() async {
    final boundary = t.renderObject<RenderRepaintBoundary>(find.byKey(capture));
    final image = await boundary.toImage(pixelRatio: 1);
    final bytes = await image.toByteData(format: ui.ImageByteFormat.png);
    await File(
      '$directory/$name.png',
    ).writeAsBytes(bytes!.buffer.asUint8List());
    image.dispose();
  });
}

void main() {
  setUpAll(() async {
    for (final family in [
      'CupertinoSystemText',
      'CupertinoSystemDisplay',
      'packages/mingo_ui/Inter',
    ]) {
      final loader = FontLoader(family);
      loader.addFont(
        rootBundle.load('packages/mingo_ui/assets/fonts/Inter.ttf'),
      );
      await loader.load();
    }
    final icons = FontLoader('packages/cupertino_icons/CupertinoIcons');
    icons.addFont(
      rootBundle.load('packages/cupertino_icons/assets/CupertinoIcons.ttf'),
    );
    await icons.load();
  });
  late MemoryStore store;
  late ControlledProofServer server;
  late ProofController c;
  setUp(() async {
    store = MemoryStore();
    server = ControlledProofServer(MemoryStore());
    c = await ProofController.open(store, server);
  });
  tearDown(() => c.dispose());
  Future<void> app(WidgetTester t, {Brightness? brightness}) async {
    t.view.devicePixelRatio = 1;
    t.view.physicalSize = const Size(393, 852);
    addTearDown(t.view.resetDevicePixelRatio);
    addTearDown(t.view.resetPhysicalSize);
    await t.pumpWidget(
      RepaintBoundary(
        key: capture,
        child: M3xProofApp(controller: c, brightness: brightness),
      ),
    );
    await t.pumpAndSettle();
  }

  Future<void> task(
    WidgetTester t, {
    String key = 'practice',
    bool reduced = false,
  }) async {
    t.view.devicePixelRatio = 1;
    t.view.physicalSize = const Size(393, 852);
    addTearDown(t.view.resetDevicePixelRatio);
    addTearDown(t.view.resetPhysicalSize);
    await t.pumpWidget(
      RepaintBoundary(
        key: capture,
        child: CupertinoApp(
          builder: (context, child) => MediaQuery(
            data: MediaQuery.of(context).copyWith(disableAnimations: reduced),
            child: child!,
          ),
          home: ProofTaskPage(controller: c, taskKey: key),
        ),
      ),
    );
    await t.pumpAndSettle();
  }

  testWidgets('Home → Practice → feedback → Close → exact origin and Resume', (
    t,
  ) async {
    await app(t);
    await screenshot(t, 'home_resume');
    t.view.physicalSize = const Size(393, 600);
    await t.pumpAndSettle();
    final home = t.widget<CustomScrollView>(
      find.byKey(const ValueKey('home-scroll')),
    );
    home.controller!.jumpTo(60);
    await t.pumpAndSettle();
    await t.ensureVisible(find.text('Tiếp tục bài học'));
    await t.pumpAndSettle();
    final offset = home.controller!.offset;
    expect(offset, greaterThan(0));
    await tap(t, 'Tiếp tục bài học');
    await screenshot(t, 'practice_default');
    expect(find.byType(CupertinoTabBar), findsNothing);
    await tap(t, 'No, I need a taxi.');
    await screenshot(t, 'practice_selected');
    final unit = find.byKey(ValueKey('${practiceItem.questionRevision}/taxi'));
    final element = t.element(unit), top = t.getTopLeft(unit).dy;
    await tap(t, 'Kiểm tra');
    expect(c.current('practice')!.phase, SyncPhase.synced);
    expect(t.element(unit), same(element));
    expect(t.getTopLeft(unit).dy, top);
    expect(
      find.descendant(
        of: unit,
        matching: find.text('Chưa đúng với tình huống'),
      ),
      findsOneWidget,
    );
    await screenshot(t, 'feedback_incorrect');
    await tap(t, 'Đóng');
    expect(home.controller!.offset, offset);
    expect(c.state.homeOffset, offset);
    await tap(t, 'Tiếp tục bài học');
    expect(find.text('Chưa đúng với tình huống'), findsOneWidget);
    expect(c.task('practice').firstResponse!.answer, 'taxi');
  });
  testWidgets('single-choice answer exposes role selected enabled states', (
    t,
  ) async {
    final handle = t.ensureSemantics();
    await task(t);
    await tap(t, 'No, I need a taxi.');
    final node = t.getSemantics(find.bySemanticsLabel('No, I need a taxi.'));
    expect(node.hasFlag(ui.SemanticsFlag.isButton), isTrue);
    expect(node.hasFlag(ui.SemanticsFlag.isSelected), isTrue);
    expect(node.hasFlag(ui.SemanticsFlag.isInMutuallyExclusiveGroup), isTrue);
    expect(node.hasFlag(ui.SemanticsFlag.isEnabled), isTrue);
    await tap(t, 'Kiểm tra');
    expect(
      t
          .getSemantics(find.bySemanticsLabel('No, I need a taxi.'))
          .hasFlag(ui.SemanticsFlag.isEnabled),
      isFalse,
    );
    handle.dispose();
  });
  testWidgets(
    'correct feedback explains inline, hides policy-disallowed Retry',
    (t) async {
      await task(t);
      await tap(t, 'Yes, I have a reservation.');
      await tap(t, 'Kiểm tra');
      expect(find.text('Đúng với tình huống'), findsOneWidget);
      expect(find.text('Thử lại'), findsNothing);
      expect(find.text('Các lần trả lời'), findsOneWidget);
      expect(find.byIcon(CupertinoIcons.bookmark), findsNothing);
      await screenshot(t, 'feedback_correct');
    },
  );
  testWidgets(
    'verdict dispatch once, rebuilding does not announce repeatedly',
    (t) async {
      final messages = <dynamic>[];
      final messenger =
          TestDefaultBinaryMessengerBinding.instance.defaultBinaryMessenger;
      messenger.setMockDecodedMessageHandler<dynamic>(
        SystemChannels.accessibility,
        (message) async {
          messages.add(message);
          return null;
        },
      );
      addTearDown(
        () => messenger.setMockDecodedMessageHandler<dynamic>(
          SystemChannels.accessibility,
          null,
        ),
      );
      await task(t);
      await tap(t, 'No, I need a taxi.');
      await tap(t, 'Kiểm tra');
      c.networkRestored();
      await t.pumpAndSettle();
      expect(
        messages.where((m) => m is Map && m['type'] == 'announce').length,
        1,
      );
    },
  );
  testWidgets('Independent Check has no pre-submit Hint', (t) async {
    await task(t, key: 'check');
    expect(find.text('Gợi ý'), findsNothing);
    expect(find.textContaining('Tự làm • không gợi ý'), findsOneWidget);
    await screenshot(t, 'independent_check');
    await tap(t, "Yes, I’d like the soup, please.");
    await tap(t, 'Gửi câu trả lời');
    expect(c.task('check').firstResponse!.assisted, isFalse);
  });
  testWidgets(
    'Result Pending Done closes; Continue asks a new explicit decision',
    (t) async {
      await app(t);
      await t.tap(find.byIcon(CupertinoIcons.ellipsis));
      await t.pumpAndSettle();
      await tap(t, 'Result Pending Sync');
      expect(find.text('Xong'), findsOneWidget);
      expect(find.text('Học tiếp'), findsOneWidget);
      expect(
        find.textContaining('Đã lưu trên thiết bị • chờ đồng bộ'),
        findsOneWidget,
      );
      await screenshot(t, 'result_pending_sync');
      await tap(t, 'Học tiếp');
      expect(c.nextDecisionCount, 1);
      expect(find.text('Chọn việc tiếp theo'), findsOneWidget);
      expect(find.text('Luyện tập'), findsNothing);
      await tap(t, 'Chọn sau');
      await tap(t, 'Xong');
      expect(find.text('Tiếp tục bài học'), findsOneWidget);
      await t.tap(find.byIcon(CupertinoIcons.ellipsis));
      await t.pumpAndSettle();
      await tap(t, 'Result');
      expect(
        find.textContaining('Đã đồng bộ • máy chủ đã xác nhận'),
        findsOneWidget,
      );
      await screenshot(t, 'result');
    },
  );
  testWidgets(
    'Sync Recovery keeps pending on connectivity and shows synced only after ACK',
    (t) async {
      await t.runAsync(() async {
        c.offline();
        await c.select('practice', 'taxi');
        await c.submit('practice');
      });
      await t.pumpWidget(
        RepaintBoundary(
          key: capture,
          child: CupertinoApp(home: ProofSyncPage(controller: c)),
        ),
      );
      await t.pumpAndSettle();
      await tap(t, 'Kết nối lại • chưa ACK');
      expect(c.current('practice')!.phase, SyncPhase.pending);
      await tap(t, 'Thử đồng bộ');
      expect(c.current('practice')!.phase, SyncPhase.pending);
      await screenshot(t, 'sync_recovery_pending');
      await tap(t, 'Cho server fixture trả ACK');
      expect(
        find.textContaining('Đã đồng bộ • máy chủ đã xác nhận'),
        findsOneWidget,
      );
      await screenshot(t, 'sync_recovery_acked');
    },
  );
  testWidgets('failed disk write does not show locally saved feedback', (
    t,
  ) async {
    await task(t);
    await tap(t, 'No, I need a taxi.');
    store.failNext = true;
    await tap(t, 'Kiểm tra');
    expect(find.textContaining('Chưa lưu được thay đổi'), findsOneWidget);
    expect(find.textContaining('Đã lưu trên thiết bị'), findsNothing);
    expect(find.textContaining('Đúng với tình huống'), findsNothing);
  });
  testWidgets(
    'Reduce Motion keeps same answer/explanation with zero duration',
    (t) async {
      await task(t, reduced: true);
      await tap(t, 'No, I need a taxi.');
      await tap(t, 'Kiểm tra');
      expect(find.text('Chưa đúng với tình huống'), findsOneWidget);
      expect(find.byType(AnimatedSize), findsNothing);
    },
  );
  testWidgets(
    'large text at 320 width reflows and essential actions remain reachable',
    (t) async {
      await app(t);
      await tap(t, 'Tiếp tục bài học');
      t.view.physicalSize = const Size(320, 568);
      t.platformDispatcher.textScaleFactorTestValue = 3.2;
      addTearDown(t.platformDispatcher.clearTextScaleFactorTestValue);
      await t.pumpAndSettle();
      await tap(t, 'No, I need a taxi.');
      await tap(t, 'Kiểm tra');
      expect(t.takeException(), isNull);
      await t.scrollUntilVisible(
        find.text('Chưa đúng với tình huống'),
        -200,
        scrollable: find.byType(Scrollable).first,
        maxScrolls: 50,
      );
      await t.pumpAndSettle();
      await screenshot(t, 'large_text_320_320percent');
      await t.scrollUntilVisible(
        find.text('Về Hôm nay'),
        200,
        scrollable: find.byType(Scrollable).first,
        maxScrolls: 50,
      );
      expect(find.text('Về Hôm nay'), findsOneWidget);
    },
  );
  testWidgets('dark mode uses opaque surfaces and readable non-color verdict', (
    t,
  ) async {
    await app(t, brightness: Brightness.dark);
    await tap(t, 'Tiếp tục bài học');
    await tap(t, 'No, I need a taxi.');
    await tap(t, 'Kiểm tra');
    expect(find.text('Chưa đúng với tình huống'), findsOneWidget);
    expect(t.takeException(), isNull);
    await screenshot(t, 'dark_feedback');
  });
  testWidgets(
    'Welcome anchor starts with Bắt đầu and Explore remains secondary',
    (t) async {
      await app(t);
      await t.tap(find.byIcon(CupertinoIcons.ellipsis));
      await t.pumpAndSettle();
      await tap(t, 'Welcome • anchor polish');
      expect(find.text('Bắt đầu'), findsOneWidget);
      expect(find.text('Khám phá trước'), findsOneWidget);
      final primary = t.widget<CupertinoButton>(
        find.ancestor(
          of: find.text('Bắt đầu'),
          matching: find.byType(CupertinoButton),
        ),
      );
      expect(primary.onPressed, isNotNull);
      await screenshot(t, 'welcome_polish');
      await tap(t, 'Khám phá trước');
      expect(c.state.tab, 1);
      expect(find.text('Khám phá một tình huống'), findsOneWidget);
    },
  );
  testWidgets(
    'long Vietnamese/English content wraps at narrow width with reachable submit',
    (t) async {
      await t.runAsync(() async {
        final long = TaskItem.fromJson({
          ...practiceItem.toJson(),
          'activityRevision': fixtureId(70),
          'questionRevision': fixtureId(71),
          'prompt':
              'Welcome to the hotel. Could you please tell me whether you have already made a reservation for your stay?',
          'intent':
              'Bạn muốn giải thích rõ rằng mình đã đặt phòng trước và cần xác nhận thông tin với nhân viên lễ tân.',
          'options': {
            'reservation':
                'Yes, I have already made a reservation for my stay and would like to confirm the details with you.',
            'taxi': 'No, I need a taxi.',
            'station': 'Where is the station?',
          },
        });
        c.dispose();
        await store.write(
          LearningState(
            owner: fixtureId(1),
            tasks: {
              'practice': TaskSession(key: 'practice', item: long),
              'check': TaskSession(key: 'check'),
            },
          ).toJson(),
        );
        c = await ProofController.open(store, server);
      });
      t.view.devicePixelRatio = 1;
      t.view.physicalSize = const Size(320, 568);
      t.platformDispatcher.textScaleFactorTestValue = 2;
      addTearDown(t.view.resetDevicePixelRatio);
      addTearDown(t.view.resetPhysicalSize);
      addTearDown(t.platformDispatcher.clearTextScaleFactorTestValue);
      await t.pumpWidget(
        RepaintBoundary(
          key: capture,
          child: CupertinoApp(
            home: ProofTaskPage(controller: c, taskKey: 'practice'),
          ),
        ),
      );
      await t.pumpAndSettle();
      await tap(t, 'No, I need a taxi.');
      await t.scrollUntilVisible(
        find.text('Kiểm tra'),
        200,
        scrollable: find.byType(Scrollable).first,
        maxScrolls: 50,
      );
      await t.pumpAndSettle();
      expect(t.takeException(), isNull);
      await screenshot(t, 'long_vi_en_320_200percent');
    },
  );
  testWidgets(
    'essential answer and action controls meet 44 logical point minimum',
    (t) async {
      await task(t);
      for (final button in find.byType(CupertinoButton).evaluate()) {
        final size = t.getSize(find.byWidget(button.widget));
        expect(size.height, greaterThanOrEqualTo(44));
        expect(size.width, greaterThanOrEqualTo(44));
      }
    },
  );
}
