import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:adaptive_staff/main.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('V2 boots with an honest review boundary', (tester) async {
    await tester.pumpWidget(const FoundationApp());
    await tester.pumpAndSettle();
    expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
