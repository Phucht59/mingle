// Technical candidate checks, prior to updating any golden. These are not
// human design approval, TalkBack verification or product-effect evidence.
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mingo_ui/mingo_ui.dart';
import 'package:mingo_ui/src/journey.dart';

Future<void> settleImages(WidgetTester t) async {
  final c = t.element(find.byType(Scaffold).first);
  final providers = t
      .widgetList<Image>(find.byType(Image))
      .map((w) => w.image)
      .toList();
  await t.runAsync(() async {
    for (final provider in providers) {
      await precacheImage(provider, c);
    }
  });
  await t.pumpAndSettle();
}

void main() {
  setUpAll(() async {
    final font = FontLoader('packages/mingo_ui/Inter');
    font.addFont(rootBundle.load('packages/mingo_ui/assets/fonts/Inter.ttf'));
    await font.load();
    final icons = FontLoader('MaterialIcons');
    icons.addFont(rootBundle.load('fonts/MaterialIcons-Regular.otf'));
    await icons.load();
  });
  testWidgets('tiny decorations retain nonempty decoded dimensions', (t) async {
    for (final width in [0.0, .1, 1.0, 8.0]) {
      await t.pumpWidget(MaterialApp(home: Scaffold(body: Center(child: Column(
        mainAxisSize: MainAxisSize.min, children: [
          SizedBox(width: width, height: width / 2.6, child: const ScenicWindow()),
          const Mascot(height: 0),
        ])))));
      for (final image in t.widgetList<Image>(find.byType(Image))) {
        final provider = image.image as ResizeImage;
        expect(provider.width ?? provider.height, greaterThanOrEqualTo(16));
      }
      await settleImages(t);
      expect(t.takeException(), isNull, reason: 'Small/initial layout must not request an empty texture');
    }
  });
  const core = [
    'L-002',
    'L-010',
    'L-020',
    'L-024',
    'L-027',
    'L-032',
    'L-040',
    'L-050',
    'L-070',
    'L-072',
  ];
  for (final dark in [false, true]) {
    for (final id in core) {
      testWidgets(
        'candidate $id ${dark ? "dark" : "light"}: 12 responsive observations',
        (t) async {
          t.view.devicePixelRatio = 1;
          addTearDown(t.view.resetDevicePixelRatio);
          addTearDown(t.view.resetPhysicalSize);
          for (final width in [360.0, 412.0, 430.0]) {
            t.view.physicalSize = Size(width, 915);
            for (final scale in [1.0, 1.3, 1.5, 2.0]) {
              await t.pumpWidget(
                LearnerApp(
                  key: UniqueKey(),
                  initialScreen: id,
                  initialDark: dark,
                  textScale: scale,
                ),
              );
              await settleImages(t);
              expect(
                t.takeException(),
                isNull,
                reason: '$id width=$width scale=$scale dark=$dark',
              );
              expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
            }
          }
        },
      );
    }
    for (final id in ['L-010', 'L-020', 'L-032', 'L-040', 'L-070']) {
      testWidgets(
        'candidate $id ${dark ? "dark" : "light"}: targets labels contrast',
        (t) async {
          final semantics = t.ensureSemantics();
          t.view.physicalSize = const Size(412, 915);
          t.view.devicePixelRatio = 1;
          addTearDown(t.view.resetDevicePixelRatio);
          addTearDown(t.view.resetPhysicalSize);
          await t.pumpWidget(LearnerApp(initialScreen: id, initialDark: dark));
          await settleImages(t);
          await expectLater(t, meetsGuideline(androidTapTargetGuideline));
          await expectLater(t, meetsGuideline(labeledTapTargetGuideline));
          await expectLater(t, meetsGuideline(textContrastGuideline));
        semantics.dispose();
        },
      );
    }
  }
  testWidgets('Home primary action visible before scrolling at360x800', (
    t,
  ) async {
    t.view.physicalSize = const Size(360, 800);
    t.view.devicePixelRatio = 1;
    addTearDown(t.view.resetDevicePixelRatio);
    addTearDown(t.view.resetPhysicalSize);
    await t.pumpWidget(const LearnerApp(initialScreen: 'L-010'));
    await settleImages(t);
    final button = find.widgetWithText(FilledButton, 'Bắt đầu học');
    final bottom = t.getBottomRight(button).dy;
    final navigationTop = t.getTopLeft(find.text('Trang chủ')).dy;
    expect(
      bottom,
      lessThan(navigationTop),
      reason: 'Action must fit above navigation, without ensureVisible',
    );
  });
  testWidgets('long Vietnamese topic copy wraps at320px200percent', (t) async {
    t.view.physicalSize = const Size(320, 915);
    t.view.devicePixelRatio = 1;
    addTearDown(t.view.resetDevicePixelRatio);
    addTearDown(t.view.resetPhysicalSize);
    await t.pumpWidget(
      MaterialApp(
        builder: (c, child) => MediaQuery(
          data: MediaQuery.of(c).copyWith(
            textScaler: const TextScaler.linear(2),
            disableAnimations: true,
          ),
          child: child!,
        ),
        home: Scaffold(
          body: SingleChildScrollView(
            child: TopicCard(
              title:
                  'Chào hỏi và giới thiệu một người trong tình huống giao tiếp hằng ngày',
              detail:
                  'Bạn có thể học từng bước và quay lại nghe mẫu khi cần thêm hỗ trợ.',
              label: 'Từ vựng trong ngữ cảnh',
              icon: Icons.menu_book_outlined,
              onTap: () {},
            ),
          ),
        ),
      ),
    );
    await settleImages(t);
    expect(t.takeException(), isNull);
  });
}
