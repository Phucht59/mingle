import 'dart:convert';
import 'dart:io';
import 'package:crypto/crypto.dart';

/// One shared boundary for session snapshots and the business command queue.
/// Telemetry never writes here. Successful commit is required before saved UX.
abstract interface class LearningStore {
  Future<Map<String, dynamic>?> read();
  Future<void> write(Map<String, dynamic> snapshot);
}

class FileLearningStore implements LearningStore {
  FileLearningStore(this.path);
  final String path;
  @override
  Future<Map<String, dynamic>?> read() async {
    final file = File(path);
    if (!await file.exists()) return null;
    final envelope =
        jsonDecode(await file.readAsString()) as Map<String, dynamic>;
    final bytes = envelope['bytes'] as String;
    if (envelope['sha256'] != sha256.convert(utf8.encode(bytes)).toString()) {
      throw const FormatException(
        'Local data checksum failed; retain file for recovery',
      );
    }
    return jsonDecode(bytes) as Map<String, dynamic>;
  }

  @override
  Future<void> write(Map<String, dynamic> snapshot) async {
    final bytes = jsonEncode(snapshot);
    if (utf8.encode(bytes).length > 20 * 1024 * 1024) {
      throw const FileSystemException(
        'Queue budget reached; existing work retained',
      );
    }
    final file = File(path);
    await file.parent.create(recursive: true);
    final temp = File('$path.tmp');
    await temp.writeAsString(
      jsonEncode({
        'bytes': bytes,
        'sha256': sha256.convert(utf8.encode(bytes)).toString(),
      }),
      flush: true,
    );
    // Same directory/volume. A killed writer leaves either the old snapshot or
    // the complete new snapshot; uncommitted .tmp is never advertised as saved.
    await temp.rename(path);
  }
}
