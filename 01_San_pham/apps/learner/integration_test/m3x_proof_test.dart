import 'package:flutter/cupertino.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:adaptive_learner/m3x/learning_state.dart';
import 'package:adaptive_learner/m3x/open_store_native.dart';
import 'package:adaptive_learner/m3x/proof_app.dart';
import 'package:adaptive_learner/m3x/proof_controller.dart';
import 'package:adaptive_learner/m3x/proof_server.dart';

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('native Home/Practice/Close/Resume and durable pending/ACK', (
    t,
  ) async {
    final run = newId();
    final store = await openNativeStore('integration_$run');
    final server = ControlledProofServer(
      await openNativeStore('server_integration_$run'),
    );
    final c = await ProofController.open(store, server, online: false);
    addTearDown(c.dispose);
    await t.pumpWidget(M3xProofApp(controller: c));
    await t.pumpAndSettle();
    Future<void> tap(String text) async {
      final finder = find.text(text).first;
      await t.ensureVisible(finder);
      await t.pumpAndSettle();
      await t.tap(finder);
      await t.runAsync(() async {
        // Native file writes finish on the real event loop, independently of
        // pumpAndSettle. Do not mistake a settled animation for a saved answer.
        await Future<void>.delayed(const Duration(milliseconds: 50));
        final deadline = DateTime.now().add(const Duration(seconds: 10));
        while (c.busy && DateTime.now().isBefore(deadline)) {
          await Future<void>.delayed(const Duration(milliseconds: 20));
        }
        expect(c.busy, isFalse, reason: 'Native persistence did not settle');
      });
      await t.pumpAndSettle();
    }

    await tap('Tiếp tục bài học');
    await tap('No, I need a taxi.');
    await tap('Kiểm tra');
    expect(c.current('practice')!.phase, SyncPhase.pending);
    await tap('Đóng');
    await tap('Tiếp tục bài học');
    expect(c.task('practice').firstResponse!.answer, 'taxi');
    final restored = await ProofController.open(store, server, online: false);
    addTearDown(restored.dispose);
    expect(restored.current('practice')!.bytes, c.current('practice')!.bytes);
    server.ackEnabled = false;
    restored.networkRestored();
    await restored.syncPending();
    expect(restored.current('practice')!.phase, SyncPhase.pending);
    server.ackEnabled = true;
    await restored.syncPending();
    expect(restored.current('practice')!.phase, SyncPhase.synced);
    expect(find.byType(CupertinoTabBar), findsNothing);
  });
}
