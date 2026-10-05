import 'package:flutter_test/flutter_test.dart';
import 'package:adaptive_learner/main.dart';

void main() {
  testWidgets('shell renders without learning claims or overflow', (tester) async {
    await tester.pumpWidget(const FoundationApp());
    expect(find.text('Your learning space'), findsOneWidget);
    expect(find.textContaining('mastery'), findsNothing);
    expect(tester.takeException(), isNull);
  });
}
