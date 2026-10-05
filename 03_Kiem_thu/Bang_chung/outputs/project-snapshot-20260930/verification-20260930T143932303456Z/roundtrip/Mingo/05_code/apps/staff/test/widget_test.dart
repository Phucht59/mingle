import 'package:flutter_test/flutter_test.dart';
import 'package:adaptive_staff/main.dart';

void main() {
  testWidgets('shell renders without learning claims or overflow', (tester) async {
    await tester.pumpWidget(const FoundationApp());
    expect(find.text('Learning workspace'), findsOneWidget);
    expect(find.textContaining('mastery'), findsNothing);
    expect(tester.takeException(), isNull);
  });
}
