import 'package:flutter_test/flutter_test.dart';
import 'package:adaptive_learner/main.dart';

void main() {
  testWidgets('V2 entry discloses review fixture and renders without overflow', (tester) async {
    await tester.pumpWidget(const FoundationApp());
    await tester.pumpAndSettle();
    expect(find.text('Bắt đầu hành trình'), findsOneWidget);
    expect(find.text('Bản xem trước · dữ liệu mẫu'), findsOneWidget);
    expect(tester.takeException(), isNull);
  });
}
