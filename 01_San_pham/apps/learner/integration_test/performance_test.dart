import 'dart:math' as math;
import 'dart:ui' as ui;

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:mingo_ui/mingo_ui.dart';

// Engineering instrumentation only. No learner telemetry or server command.
// Profile frames on an emulator do not certify physical Android performance.
void main() {
  final binding = IntegrationTestWidgetsFlutterBinding.ensureInitialized();
  testWidgets('profile the real sample core journey without physical claims', (
    tester,
  ) async {
    if (!kProfileMode) {
      throw StateError('Frame benchmark requires --profile; debug is invalid.');
    }
    final view = binding.platformDispatcher.views.first;
    final report = <String, dynamic>{
      'schema': 'mingo.performance.v1',
      'build_mode': 'profile',
      'capture_utc': DateTime.now().toUtc().toIso8601String(),
      'physical_device_claim': false,
      'scope': 'Phase 2 sample presentation, not learning or offline runtime',
      'refresh_hz_start': view.display.refreshRate,
      'physical_width': view.physicalSize.width,
      'physical_height': view.physicalSize.height,
      'device_pixel_ratio': view.devicePixelRatio,
      'scenarios': <String, dynamic>{},
    };
    binding.reportData = <String, dynamic>{'mingo_performance': report};
    final scenarios = report['scenarios'] as Map<String, dynamic>;

    Future<void> pause() async {
      await tester.runAsync(
        () => Future<void>.delayed(const Duration(milliseconds: 1100)),
      );
    }
    Future<void> measure(String name, Future<void> Function() action, {bool scrolling = false}) async {
      // Engine timing callbacks are batched. Flush preceding frames before
      // installing this listener and retain settling frames after the action.
      await pause();
      final timings = <ui.FrameTiming>[];
      final void Function(List<ui.FrameTiming>) listener = timings.addAll;
      final refresh = view.display.refreshRate;
      final scrollPosition = scrolling
          ? tester.state<ScrollableState>(find.byType(Scrollable).first).position
          : null;
      final watch = Stopwatch()..start();
      binding.addTimingsCallback(listener);
      try {
        await action();
        await tester.pumpAndSettle();
        final actionWallMs = watch.elapsedMicroseconds / 1000;
        await pause();
        final unique = <String, ui.FrameTiming>{
          for (final timing in timings)
            '${timing.frameNumber}/${timing.timestampInMicroseconds(ui.FramePhase.buildStart)}': timing,
        }.values.toList();
        scenarios[name] = _summarize(unique, refresh)
          ..['action_wall_ms_includes_test_driver'] = actionWallMs
          ..['image_cache_bytes'] = PaintingBinding.instance.imageCache.currentSizeBytes
          ..['image_cache_entries'] = PaintingBinding.instance.imageCache.currentSize
          ..['image_cache_live_entries'] = PaintingBinding.instance.imageCache.liveImageCount;
        if (scrollPosition != null) {
          (scenarios[name] as Map<String, dynamic>)['scroll_extent_logical_px'] = scrollPosition.maxScrollExtent;
          (scenarios[name] as Map<String, dynamic>)['interaction_status'] = scrollPosition.maxScrollExtent > 0
              ? 'SCROLLABLE_CONTENT_MEASURED'
              : 'NOT_APPLICABLE_NO_SCROLL_EXTENT_ON_THIS_VIEWPORT';
        }
      } finally {
        binding.removeTimingsCallback(listener);
        watch.stop();
      }
      expect(tester.takeException(), isNull, reason: name);
    }

    Future<void> mount(String id, {double? scale, String? state}) async {
      await tester.pumpWidget(LearnerApp(
        key: UniqueKey(),
        initialScreen: id,
        textScale: scale,
        reviewState: state,
      ));
      await tester.pumpAndSettle();
    }
    Future<void> tapText(String text) async {
      final target = find.text(text).last;
      expect(target, findsOneWidget, reason: 'Missing benchmark action: $text');
      await tester.ensureVisible(target);
      await tester.pumpAndSettle();
      await tester.tap(target);
      await tester.pumpAndSettle();
    }
    Future<void> primary() async {
      final target = find.byType(FilledButton).first;
      expect(target, findsOneWidget);
      await tester.ensureVisible(target);
      await tester.pumpAndSettle();
      await tester.tap(target);
      await tester.pumpAndSettle();
    }
    Future<void> scroll() async {
      final target = find.byType(Scrollable).first;
      expect(target, findsOneWidget);
      if (tester.state<ScrollableState>(target).position.maxScrollExtent <= 0) {
        await tester.pump();
        return;
      }
      for (var i = 0; i < 16; i++) {
        await tester.fling(target, Offset(0, i.isEven ? -420 : 420), 900);
        await tester.pumpAndSettle();
      }
    }

    PaintingBinding.instance.imageCache.clear();
    PaintingBinding.instance.imageCache.clearLiveImages();
    await measure('first_home_widget_mount_not_android_cold_start', () => mount('L-010'));
    await measure('home_scroll', scroll, scrolling: true);
    await measure('home_to_lesson', () => tapText('Bắt đầu học'));
    await primary(); // Intro to the first question; actual navigation.
    await measure('answer_interaction', () => tapText('Good morning!'));
    await measure('immediate_feedback', primary);
    await measure('lesson_to_result', () async {
      await primary(); // Review feedback -> Learn.
      await primary(); // Learn -> Retrieve.
      await tapText('Good morning!');
      await primary(); // Retrieve answer -> feedback.
      await primary(); // -> Transfer.
      await tapText('Good morning!');
      await primary();
      await primary(); // -> Check introduction.
      await primary(); // -> Unaided check.
      await tapText('Good morning!');
      await primary();
      await primary(); // -> Summary.
      expect(find.text('Đến bước tiếp theo'), findsOneWidget);
    });
    await measure('result_to_course', () => tapText('Đến bước tiếp theo'));
    await measure('course_scroll', scroll, scrolling: true);
    await mount('L-010', scale: 2);
    await measure('home_scroll_text_200_percent', scroll, scrolling: true);
    await measure('offline_fixture_render_not_network_sync', () => mount('L-011', state: 'offline'));
    await measure('warm_home_widget_mount_not_android_warm_start', () => mount('L-010'));
    report['refresh_hz_end'] = view.display.refreshRate;
    report['codec_samples'] = await tester.runAsync(() => _decodeAssets(view));
    report['limitations'] = <String>[
      'Frame budget violations are jank proxies, not compositor dropped-frame counts.',
      'Action wall time includes instrumentation, scrolling and settling; it is not tap latency.',
      'Android process cold/warm launch and real background return are measured by the host script.',
      'Text scale is a preview override; offline is a fixture, not real networking.',
      'A cached bundle decode is not a cold filesystem read or GPU texture allocation.',
      'Frame timing and image cache do not measure battery, thermal or total process memory.',
    ];
  }, timeout: const Timeout(Duration(minutes: 15)));
}

Map<String, dynamic> _summarize(List<ui.FrameTiming> frames, double hz) {
  final knownRefresh = hz.isFinite && hz > 0;
  final budget = knownRefresh ? 1000000 / hz : null;
  Map<String, dynamic> stats(Iterable<int> source) {
    final values = source.toList()..sort();
    if (values.isEmpty) return <String, dynamic>{'samples': 0};
    double percentile(double p) => values[math.max(0, math.min(values.length - 1, (p * values.length).ceil() - 1))] / 1000;
    return <String, dynamic>{
      'samples': values.length,
      'mean_ms': values.reduce((a, b) => a + b) / values.length / 1000,
      'p50_ms': percentile(.5),
      'p95_ms': percentile(.95),
      'p99_ms': percentile(.99),
      'max_ms': values.last / 1000,
    };
  }
  final missed = budget == null ? null : frames.where((f) => f.buildDuration.inMicroseconds > budget || f.rasterDuration.inMicroseconds > budget).length;
  return <String, dynamic>{
    'frame_count': frames.length,
    'refresh_hz': hz,
    'budget_ms': budget == null ? null : budget / 1000,
    'sample_status': frames.isEmpty ? 'NO_FRAMES_CAPTURED' : frames.length < 300 ? 'INSUFFICIENT_SAMPLE_FOR_DEVICE_GATE' : 'ENGINEERING_SAMPLE_ONLY',
    'ui': stats(frames.map((f) => f.buildDuration.inMicroseconds)),
    'raster': stats(frames.map((f) => f.rasterDuration.inMicroseconds)),
    'total_span': stats(frames.map((f) => f.totalSpan.inMicroseconds)),
    'over_budget_frame_count_proxy': missed,
    'ui_over_budget_frame_count': budget == null ? null : frames.where((f) => f.buildDuration.inMicroseconds > budget).length,
    'raster_over_budget_frame_count': budget == null ? null : frames.where((f) => f.rasterDuration.inMicroseconds > budget).length,
    'over_budget_percent_proxy': missed == null || frames.isEmpty ? null : 100 * missed / frames.length,
    'exact_compositor_dropped_frames': null,
    'raw_frames': [for (final frame in frames) <String, dynamic>{
      'frame_number': frame.frameNumber,
      'build_start_engine_us': frame.timestampInMicroseconds(ui.FramePhase.buildStart),
      'ui_us': frame.buildDuration.inMicroseconds,
      'raster_us': frame.rasterDuration.inMicroseconds,
      'total_us': frame.totalSpan.inMicroseconds,
      'vsync_overhead_us': frame.vsyncOverhead.inMicroseconds,
    }],
  };
}

Future<List<Map<String, dynamic>>> _decodeAssets(ui.FlutterView view) async {
  final manifest = await AssetManifest.loadFromAssetBundle(rootBundle);
  final paths = manifest.listAssets().where((p) => p.startsWith('packages/mingo_ui/') && RegExp(r'\.(png|webp|jpe?g)$').hasMatch(p)).toList()..sort();
  final samples = <Map<String, dynamic>>[];
  for (final path in paths) {
    final target = path.contains('mascot')
        ? (180 * view.devicePixelRatio).ceil()
        : math.min(view.physicalSize.width, 760 * view.devicePixelRatio).ceil();
    final watch = Stopwatch()..start();
    final data = await rootBundle.load(path);
    final codec = await ui.instantiateImageCodec(data.buffer.asUint8List(data.offsetInBytes, data.lengthInBytes), targetWidth: target, allowUpscaling: false);
    try {
      final frame = await codec.getNextFrame();
      watch.stop();
      samples.add(<String, dynamic>{
        'asset': path,
        'encoded_bytes': data.lengthInBytes,
        'requested_decode_width_px': target,
        'decoded_width_px': frame.image.width,
        'decoded_height_px': frame.image.height,
        'decoded_rgba_bytes_estimate': frame.image.width * frame.image.height * 4,
        'bundle_load_and_first_codec_frame_ms': watch.elapsedMicroseconds / 1000,
        'cache_condition': 'AFTER_JOURNEY_NOT_COLD_FILESYSTEM',
        'production_image_provider_timing': false,
      });
      frame.image.dispose();
    } finally {
      codec.dispose();
    }
  }
  return samples;
}
