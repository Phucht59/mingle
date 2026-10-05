// Requirement-derived challenge tests. Development-team verification only:
// these do not certify human independent QA, usability, efficacy or backend auth.
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mingo_ui/mingo_ui.dart';

Future<void> tapAction(WidgetTester tester, String label) async {
  final finder = find.text(label).first;
  await tester.ensureVisible(finder);
  await tester.tap(finder);
  await tester.pumpAndSettle();
}

void main() {
  setUpAll(() async {
    final font = FontLoader('packages/mingo_ui/Inter');
    font.addFont(rootBundle.load('packages/mingo_ui/assets/fonts/Inter.ttf'));
    await font.load();
  });

  testWidgets(
    'IV-01 PRD-02 Check first response cannot be rewritten by a late answer tap',
    (tester) async {
      await tester.pumpWidget(const LearnerApp(initialScreen: 'L-027'));
      await tester.pumpAndSettle();
      await tapAction(tester, 'Good night!');
      await tapAction(tester, 'Kiểm tra câu trả lời');
      expect(find.text('Nhìn lại thời điểm trong ngày'), findsOneWidget);
      await tapAction(tester, 'Good morning!');
      expect(find.text('Nhìn lại thời điểm trong ngày'), findsOneWidget);
      expect(find.text('Phù hợp với buổi sáng!'), findsNothing);
      expect(find.text('Thử thêm một lần'), findsNothing);
      expect(find.text('Xem gợi ý'), findsNothing);
      expect(find.text('Bỏ qua câu này'), findsNothing);
    },
  );

  testWidgets(
    'IV-02 PRD-04 skip then Android Back does not manufacture correct feedback',
    (tester) async {
      await tester.pumpWidget(const LearnerApp(initialScreen: 'L-024'));
      await tester.pumpAndSettle();
      await tapAction(tester, 'Bỏ qua câu này');
      expect(find.text('Đã bỏ qua trong bản xem trước'), findsOneWidget);
      await tapAction(tester, 'Tiếp tục');
      expect(find.text('Dùng trong tình huống mới'), findsOneWidget);
      await tester.binding.handlePopRoute();
      await tester.pumpAndSettle();
      expect(find.text('Thử tự nhớ'), findsOneWidget);
      expect(find.text('Phù hợp với buổi sáng!'), findsNothing);
      expect(find.text('Nhìn lại thời điểm trong ngày'), findsNothing);
      expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
      expect(tester.takeException(), isNull);
    },
  );

  testWidgets(
    'IV-03 PRD-14 direct confirmation without review evidence stays blocked',
    (tester) async {
      tester.view.physicalSize = const Size(1440, 1000);
      tester.view.devicePixelRatio = 1;
      addTearDown(tester.view.resetPhysicalSize);
      addTearDown(tester.view.resetDevicePixelRatio);
      await tester.pumpWidget(const StaffApp(initialScreen: 'S-036'));
      await tester.pumpAndSettle();
      expect(find.text('Xem xác nhận mẫu'), findsNothing);
      await tapAction(tester, 'Hoàn thành kiểm tra trước');
      expect(find.text('Cần kiểm tra giấy phép'), findsOneWidget);
      expect(find.text('Xem bước xác nhận'), findsNothing);
      expect(find.textContaining('Bất biến'), findsNothing);
    },
  );

  testWidgets(
    'IV-04 V3 security missing evidence does not expose fabricated learner answers',
    (tester) async {
      await tester.pumpWidget(
        const StaffApp(initialScreen: 'S-022', reviewState: 'no-evidence'),
      );
      await tester.pumpAndSettle();
      expect(find.text('Chưa có dữ liệu phù hợp'), findsOneWidget);
      expect(find.textContaining('Câu 1 · Tự trả lời'), findsNothing);
      expect(find.textContaining('82%'), findsNothing);
      expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
    },
  );

  testWidgets(
    'IV-05 PRD-16 recommendation outage retains a usable curriculum next step',
    (tester) async {
      await tester.pumpWidget(
        const LearnerApp(
          initialScreen: 'L-010',
          reviewState: 'recommendation-unavailable',
        ),
      );
      await tester.pumpAndSettle();
      await tapAction(tester, 'Bắt đầu học');
      expect(find.text('Chào hỏi và làm quen'), findsOneWidget);
      expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
      expect(find.text('Tiếp tục'), findsOneWidget);
      expect(tester.takeException(), isNull);
    },
  );
}
