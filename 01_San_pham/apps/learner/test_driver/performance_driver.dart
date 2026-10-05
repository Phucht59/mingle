import 'dart:convert';
import 'dart:io';

import 'package:integration_test/integration_test_driver.dart';

Future<void> main() async {
  final directory = Platform.environment['MINGO_PERFORMANCE_OUT'];
  if (directory == null || directory.isEmpty) {
    throw StateError('Set MINGO_PERFORMANCE_OUT to a fresh local evidence folder.');
  }
  final output = File('$directory${Platform.pathSeparator}frame_timings.json');
  if (await output.exists()) {
    throw StateError('Preserve previous evidence: frame_timings.json already exists.');
  }
  await integrationDriver(
    timeout: const Duration(minutes: 20),
    writeResponseOnFailure: true,
    responseDataCallback: (data) async {
      await output.parent.create(recursive: true);
      await output.writeAsString(const JsonEncoder.withIndent('  ').convert(data));
    },
  );
}
