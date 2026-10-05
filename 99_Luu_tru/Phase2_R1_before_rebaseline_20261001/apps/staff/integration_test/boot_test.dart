import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:adaptive_staff/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('boots application on target device', (tester) async {
    app.main();
    await tester.pumpAndSettle();
    expect(find.text('Learning workspace'), findsOneWidget);
  });
}
