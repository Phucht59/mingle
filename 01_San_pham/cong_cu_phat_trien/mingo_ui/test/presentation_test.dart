import 'dart:io';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mingo_ui/mingo_ui.dart';

const capture = ValueKey('screen-capture');
Future<void> font() async {
  final loader = FontLoader('packages/mingo_ui/Inter');
  loader.addFont(rootBundle.load('packages/mingo_ui/assets/fonts/Inter.ttf'));
  await loader.load();
  final icons = FontLoader('MaterialIcons');
  icons.addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'));
  await icons.load();
}

Widget app(ScreenSpec s, String state, {double scale = 1}) => RepaintBoundary(
  key: capture,
  child: s.staff
      ? StaffApp(
          key: UniqueKey(),
          initialScreen: s.id,
          reviewState: state,
          textScale: scale,
        )
      : LearnerApp(
          key: UniqueKey(),
          initialScreen: s.id,
          reviewState: state,
          textScale: scale,
        ),
);
Future<void> tap(WidgetTester t, String label) async {
  final f = find.text(label).first;
  await t.ensureVisible(f);
  await t.tap(f);
  await t.pumpAndSettle();
}

Future<void> settleAssets(WidgetTester t) async {
  final context = t.element(find.byType(Scaffold).first);
  await t.runAsync(() async {
    await precacheImage(
      const AssetImage('assets/mascot.png', package: 'mingo_ui'),
      context,
    );
    await precacheImage(
      const AssetImage('assets/exploration.png', package: 'mingo_ui'),
      context,
    );
  });
  final providers = t.widgetList<Image>(find.byType(Image)).map((w) => w.image).toList();
  await t.runAsync(() async {
    for (final provider in providers) { await precacheImage(provider, context); }
  });
  await t.pumpAndSettle();
}

void main() {
  setUpAll(font);
  testWidgets(
    'changing lesson family resets to the selected vocabulary task; search finds grammar',
    (t) async {
      await t.pumpWidget(const LearnerApp(initialScreen: 'L-020'));
      await t.pumpAndSettle();
      await t.enterText(find.byType(TextField), 'ngữ pháp');
      await t.pump();
      expect(find.text('Câu giới thiệu cơ bản'), findsOneWidget);
      await tap(t, 'Câu giới thiệu cơ bản');
      expect(find.text('Giới thiệu một người'), findsOneWidget);
      await t.tap(find.byTooltip('Quay lại'));
      await t.pumpAndSettle();
      await t.enterText(find.byType(TextField), 'chào');
      await t.pump();
      await tap(t, 'Chào hỏi cơ bản');
      expect(find.text('Chào hỏi và làm quen'), findsOneWidget);
      expect(find.text('Giới thiệu một người'), findsNothing);
    },
  );
  for (final id in ['L-002', 'L-024', 'L-072', 'S-010', 'S-035']) {
    testWidgets('$id essential semantics labels targets and contrast', (
      t,
    ) async {
      final semantics = t.ensureSemantics();
      t.view.physicalSize = id.startsWith('S-')
          ? const Size(1440, 1000)
          : const Size(412, 915);
      t.view.devicePixelRatio = 1;
      addTearDown(t.view.resetPhysicalSize);
      addTearDown(t.view.resetDevicePixelRatio);
      await t.pumpWidget(
        id.startsWith('S-')
            ? StaffApp(initialScreen: id)
            : LearnerApp(initialScreen: id),
      );
      await settleAssets(t);
      await expectLater(t, meetsGuideline(androidTapTargetGuideline));
      await expectLater(t, meetsGuideline(labeledTapTargetGuideline));
      await expectLater(t, meetsGuideline(textContrastGuideline));
      semantics.dispose();
    });
  }
  testWidgets(
    'grammar full cycle uses distinct Retrieve Transfer and Check tasks',
    (t) async {
      await t.pumpWidget(const LearnerApp(initialScreen: 'L-020'));
      await t.pumpAndSettle();
      await tap(t, 'Câu giới thiệu cơ bản');
      await tap(t, 'Tiếp tục');
      await tap(t, 'She is a student.');
      await tap(t, 'Kiểm tra câu trả lời');
      await tap(t, 'Tiếp tục');
      await tap(t, 'Tiếp tục');
      await tap(t, 'is');
      await tap(t, 'Kiểm tra câu trả lời');
      await tap(t, 'Tiếp tục');
      expect(find.textContaining('They ___ classmates'), findsWidgets);
      await tap(t, 'are');
      await tap(t, 'Kiểm tra câu trả lời');
      await tap(t, 'Tiếp tục');
      await tap(t, 'Sẵn sàng, thử một câu');
      expect(find.text('Xem gợi ý'), findsNothing);
      await tap(t, 'is');
      await tap(t, 'Kiểm tra câu trả lời');
      await tap(t, 'Tiếp tục');
      expect(find.text('Bạn đã luyện câu giới thiệu'), findsOneWidget);
      await tap(t, 'Đến bước tiếp theo');
      await tap(t, 'Học');
      await tap(t, 'Chào hỏi cơ bản');
      for (var i = 0; i < 3; i++) {
        await t.binding.handlePopRoute();
        await t.pumpAndSettle();
      }
      expect(find.text('Bạn đã luyện câu giới thiệu'), findsOneWidget);
    },
  );
  for (final domain in [LessonDomain.grammar, LessonDomain.listening]) {
    for (final id in [
      'L-021',
      'L-022',
      'L-023',
      'L-024',
      'L-025',
      'L-026',
      'L-027',
      'L-032',
    ]) {
      testWidgets('${domain.name} / $id / responsive and capture', (t) async {
        t.view.devicePixelRatio = 1;
        addTearDown(t.view.resetDevicePixelRatio);
        addTearDown(t.view.resetPhysicalSize);
        for (final size in const [
          Size(360, 800),
          Size(412, 915),
          Size(800, 360),
        ]) {
          for (final scale in [1.0, 2.0]) {
            t.view.physicalSize = size;
            await t.pumpWidget(
              RepaintBoundary(
                key: capture,
                child: LearnerApp(
                  key: UniqueKey(),
                  initialScreen: id,
                  initialDomain: domain,
                  textScale: scale,
                ),
              ),
            );
            await t.pumpAndSettle();
            expect(t.takeException(), isNull);
          }
        }
        t.view.physicalSize = const Size(412, 915);
        await t.pumpWidget(
          RepaintBoundary(
            key: capture,
            child: LearnerApp(
              key: UniqueKey(),
              initialScreen: id,
              initialDomain: domain,
            ),
          ),
        );
        await t.pumpAndSettle();
        await settleAssets(t);
        await expectLater(
          find.byKey(capture),
          matchesGoldenFile(
            '../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/screenshots/${domain.name}_$id.png',
          ),
        );
      });
    }
  }
  for (final id in ['L-010', 'L-020', 'L-040', 'L-050']) {
    testWidgets('D021 V2 $id at320px200percent', (t) async {
      final semantics = t.ensureSemantics();
      t.view.physicalSize = const Size(320, 800);
      t.view.devicePixelRatio = 1;
      addTearDown(t.view.resetPhysicalSize);
      addTearDown(t.view.resetDevicePixelRatio);
      await t.pumpWidget(
        RepaintBoundary(
          key: capture,
          child: LearnerApp(initialScreen: id, textScale: 2),
        ),
      );
      await t.pumpAndSettle();
      expect(t.takeException(), isNull);
      await expectLater(t, meetsGuideline(androidTapTargetGuideline));
      await expectLater(t, meetsGuideline(labeledTapTargetGuideline));
      await settleAssets(t);
      await expectLater(
        find.byKey(capture),
        matchesGoldenFile(
          '../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/screenshots/${id}_320_200.png',
        ),
      );
      if (id == 'L-010') {
        await t.tap(find.byTooltip('Học'));
        await t.pumpAndSettle();
        expect(find.text('Khám phá bài học'), findsOneWidget);
        await t.tap(find.byTooltip('Tôi'));
        await t.pumpAndSettle();
        expect(find.text('Góc của bạn'), findsOneWidget);
      }
      semantics.dispose();
    });
  }
  testWidgets('learner optional onboarding reaches one next action', (t) async {
    await t.pumpWidget(const LearnerApp());
    await t.pumpAndSettle();
    await tap(t, 'Khám phá trước');
    expect(find.text('Bắt đầu học'), findsOneWidget);
    await tap(t, 'Bắt đầu học');
    expect(find.text('Trang chủ'), findsNothing);
    expect(find.text('Chào hỏi và làm quen'), findsOneWidget);
  });
  testWidgets(
    'missing lesson content and submitting state cannot advance or answer again',
    (t) async {
      await t.pumpWidget(
        const LearnerApp(
          initialScreen: 'L-021',
          reviewState: 'content-unavailable',
        ),
      );
      await t.pumpAndSettle();
      expect(find.text('Tiếp tục'), findsNothing);
      expect(find.text('Quay về danh sách bài'), findsOneWidget);
      await t.pumpWidget(
        const LearnerApp(
          key: ValueKey('submitting-check'),
          initialScreen: 'L-027',
          reviewState: 'submitting',
        ),
      );
      await t.pumpAndSettle();
      expect(find.text('Kiểm tra câu trả lời'), findsNothing);
      expect(find.text('Good morning!'), findsNothing);
    },
  );
  testWidgets(
    'locked objective permits preview and recovery but cannot start practice',
    (t) async {
      await t.pumpWidget(
        const LearnerApp(initialScreen: 'L-041', reviewState: 'locked'),
      );
      await t.pumpAndSettle();
      expect(find.text('Ôn lại lời chào'), findsNothing);
      await tap(t, 'Xem bước trước');
      expect(find.text('1. Chào hỏi'), findsOneWidget);
    },
  );
  testWidgets(
    'eligible sample objective offers a single unaided challenge without opening the next objective',
    (t) async {
      await t.pumpWidget(
        const LearnerApp(initialScreen: 'L-041', reviewState: 'Eligible'),
      );
      await t.pumpAndSettle();
      await tap(t, 'Tự thử một câu mới');
      await tap(t, 'Sẵn sàng, thử một câu');
      expect(find.text('Xem gợi ý'), findsNothing);
      expect(find.text('Bỏ qua câu này'), findsNothing);
      expect(find.text('Thử thêm một lần'), findsNothing);
      expect(find.text('Good morning!'), findsOneWidget);
    },
  );
  testWidgets('practice validates and allows one retry without Check hint', (
    t,
  ) async {
    await t.pumpWidget(const LearnerApp(initialScreen: 'L-024'));
    await t.pumpAndSettle();
    await tap(t, 'Kiểm tra câu trả lời');
    expect(find.text('Chọn một câu trả lời trước'), findsOneWidget);
    await tap(t, 'Good night!');
    await tap(t, 'Kiểm tra câu trả lời');
    await tap(t, 'Thử thêm một lần');
    await tap(t, 'Good morning!');
    await tap(t, 'Kiểm tra câu trả lời');
    expect(find.text('Phù hợp với buổi sáng!'), findsOneWidget);
    await t.pumpWidget(const LearnerApp(initialScreen: 'L-027'));
    await t.pumpAndSettle();
    expect(find.text('Xem gợi ý'), findsNothing);
    expect(find.text('Bỏ qua câu này'), findsNothing);
  });
  testWidgets('search gives a useful empty state and recovers', (t) async {
    await t.pumpWidget(const LearnerApp(initialScreen: 'L-020'));
    await t.enterText(find.byType(TextField), 'xyz');
    await t.pump();
    expect(find.text('Chưa tìm thấy bài phù hợp'), findsOneWidget);
    await t.enterText(find.byType(TextField), 'chào');
    await t.pump();
    expect(find.text('Chào hỏi cơ bản'), findsOneWidget);
  });
  testWidgets('practice response survives forward then back navigation', (
    t,
  ) async {
    await t.pumpWidget(const LearnerApp(initialScreen: 'L-024'));
    await t.pumpAndSettle();
    await tap(t, 'Good night!');
    await tap(t, 'Kiểm tra câu trả lời');
    await tap(t, 'Tiếp tục');
    await t.binding.handlePopRoute();
    await t.pumpAndSettle();
    expect(find.text('Nhìn lại thời điểm trong ngày'), findsOneWidget);
    expect(find.text('Thử thêm một lần'), findsOneWidget);
  });
  testWidgets(
    'denied staff state hides learner evidence; processing cannot republish',
    (t) async {
      await t.pumpWidget(
        const StaffApp(initialScreen: 'S-021', reviewState: 'access-denied'),
      );
      await t.pumpAndSettle();
      expect(find.text('Xem câu đã làm'), findsNothing);
      await t.pumpWidget(
        const StaffApp(initialScreen: 'S-036', reviewState: 'processing'),
      );
      await t.pumpAndSettle();
      expect(find.text('Xem xác nhận mẫu'), findsNothing);
    },
  );
  testWidgets('narrow staff menu closes after selecting content', (t) async {
    t.view.physicalSize = const Size(600, 800);
    t.view.devicePixelRatio = 1;
    addTearDown(t.view.resetPhysicalSize);
    addTearDown(t.view.resetDevicePixelRatio);
    await t.pumpWidget(const StaffApp());
    await t.pumpAndSettle();
    final scaffold = t.state<ScaffoldState>(find.byType(Scaffold));
    await t.tap(find.byTooltip('Mở danh mục'));
    await t.pumpAndSettle();
    await tap(t, 'Nội dung');
    expect(scaffold.isDrawerOpen, isFalse);
    expect(find.text('Nội dung học'), findsOneWidget);
  });
  testWidgets(
    'staff license and review precede confirmation; draft is separate',
    (t) async {
      t.view.physicalSize = const Size(1440, 1000);
      t.view.devicePixelRatio = 1;
      addTearDown(t.view.resetPhysicalSize);
      addTearDown(t.view.resetDevicePixelRatio);
      await t.pumpWidget(const StaffApp(initialScreen: 'S-035'));
      await t.pumpAndSettle();
      await tap(t, 'Kiểm tra nguồn và giấy phép');
      await tap(t, 'Đã kiểm tra nguồn trong quy trình mẫu');
      await tap(t, 'Tiếp tục kiểm tra bài');
      await tap(t, 'Nội dung mẫu đã được kiểm tra');
      await tap(t, 'Xem bước xác nhận');
      await tap(t, 'Xem xác nhận mẫu');
      expect(find.text('Xem bản mẫu'), findsOneWidget);
      await t.sendKeyEvent(LogicalKeyboardKey.escape);
      await t.pumpAndSettle();
      expect(find.text('Xem bản mẫu'), findsNothing);
      await tap(t, 'Xem xác nhận mẫu');
      await tap(t, 'Xem bản mẫu');
      expect(find.textContaining('Bất biến'), findsOneWidget);
      await tap(t, 'Tạo bản nháp mẫu mới');
      expect(find.byType(TextFormField), findsNWidgets(2));
    },
  );
  testWidgets('essential actions have labels and Android 48dp targets', (
    t,
  ) async {
    final handle = t.ensureSemantics();
    await t.pumpWidget(const LearnerApp(initialScreen: 'L-010'));
    await t.pumpAndSettle();
    await expectLater(t, meetsGuideline(androidTapTargetGuideline));
    await expectLater(t, meetsGuideline(labeledTapTargetGuideline));
    await expectLater(t, meetsGuideline(textContrastGuideline));
    handle.dispose();
  });
  testWidgets(
    'reduced motion follows preference and system text scale is preserved',
    (t) async {
      await t.pumpWidget(
        const LearnerApp(initialScreen: 'L-072', textScale: 2),
      );
      await t.pumpAndSettle();
      final toggle = find.widgetWithText(SwitchListTile, 'Giảm chuyển động');
      await t.ensureVisible(toggle);
      await t.tap(toggle);
      await t.pumpAndSettle();
      final c = t.element(find.text('Điều chỉnh để học thoải mái hơn.'));
      expect(MediaQuery.of(c).disableAnimations, isTrue);
      expect(MediaQuery.textScalerOf(c).scale(10), 20);
    },
  );
  for (final s in screens) {
    for (final state in s.states) {
      testWidgets('${s.id} | $state | responsive + screenshot', (t) async {
        t.view.devicePixelRatio = 1;
        addTearDown(t.view.resetDevicePixelRatio);
        addTearDown(t.view.resetPhysicalSize);
        final sizes = s.staff
            ? const [
                Size(1280, 900),
                Size(1440, 1000),
                Size(1920, 1080),
                Size(768, 1024),
                Size(600, 800),
              ]
            : const [
                Size(360, 800),
                Size(412, 915),
                Size(430, 932),
                Size(412, 1100),
                Size(800, 360),
              ];
        for (final size in sizes) {
          for (final scale in [1.0, 1.3, 1.5, 2.0]) {
            t.view.physicalSize = size;
            await t.pumpWidget(app(s, state, scale: scale));
            await t.pumpAndSettle();
            expect(
              t.takeException(),
              isNull,
              reason: '${s.id}/$state at $size scale $scale',
            );
            expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
          }
        }
        t.view.physicalSize = s.staff
            ? const Size(1440, 1000)
            : const Size(412, 915);
        await t.pumpWidget(app(s, state));
        await t.pumpAndSettle();
        await settleAssets(t);
        final slug = state.replaceAll(RegExp('[^a-zA-Z0-9-]'), '_');
        await expectLater(
          find.byKey(capture),
          matchesGoldenFile(
            '../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/screenshots/${s.id}_$slug.png',
          ),
        );
      });
    }
  }
  test('inventory uniqueness and machine evidence scope', () {
    expect(screens.map((s) => s.id).toSet().length, screens.length);
    final out = File(
      '../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/flutter_matrix_scope.json',
    );
    out.writeAsStringSync(
      jsonEncode({
        'screens': screens.length,
        'states': screens.fold<int>(0, (n, s) => n + s.states.length),
        'sizes_per_state': 5,
        'text_scales': [1, 1.3, 1.5, 2],
        'meaning':
            'Declared test matrix, not a PASS. Read flutter test exit and JSON events.',
      }),
    );
  });
}
