import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:adaptive_learner/main.dart';
import 'package:mingo_ui/mingo_ui.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('V2 boots with an honest review boundary', (tester) async {
    await tester.pumpWidget(const FoundationApp());
    await tester.pumpAndSettle();
    expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
    await tester.tap(find.text('Khám phá trước'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('Bắt đầu học'));
    await tester.pumpAndSettle();
    await tester.binding.handlePopRoute();
    await tester.pumpAndSettle();
    expect(find.text('Bắt đầu học'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
  testWidgets(
    'licensed sample initializes on Android and enforces its request budget',
    (tester) async {
      await tester.pumpWidget(const FoundationApp());
      await tester.pumpAndSettle();
      final audio = SampleAudio(budget: 2);
      await tester.runAsync(() async {
        await audio.play();
        expect(audio.failed, isFalse);
        await audio.play();
        expect(audio.failed, isFalse);
        await audio.play();
      });
      expect(audio.requests, 2);
      expect(audio.limited, isTrue);
      audio.dispose();
      expect(tester.takeException(), isNull);
      // Emulator playback initialization is not proof of physical hearing.
    },
  );
}
