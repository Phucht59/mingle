import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mingo_ui/mingo_ui.dart';
import 'presentation_test.dart' as capture;
import 'visual_candidate_test.dart' show settleImages;

// Runs only after documented technical candidate approval. Human aesthetic
// approval remains pending; these images are deterministic regression fixtures.
void main() {
  setUpAll(capture.font);
  for (final id in ['L-002', 'L-010', 'L-020', 'L-024', 'L-027', 'L-032', 'L-040', 'L-050', 'L-070', 'L-072']) {
    testWidgets('$id dark capture', (t) async {
      t.view.physicalSize = const Size(412, 915);
      t.view.devicePixelRatio = 1;
      addTearDown(t.view.resetPhysicalSize);
      addTearDown(t.view.resetDevicePixelRatio);
      await t.pumpWidget(RepaintBoundary(key: capture.capture,
        child: LearnerApp(initialScreen: id, initialDark: true)));
      await settleImages(t);
      expect(t.takeException(), isNull);
      await expectLater(find.byKey(capture.capture), matchesGoldenFile(
        '../../../../03_Kiem_thu/QA_QC/phase2/evidence_gated_20261002/screenshots/${id}_dark.png'));
    });
  }
}
