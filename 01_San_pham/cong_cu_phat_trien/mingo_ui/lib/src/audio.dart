import 'package:audioplayers/audioplayers.dart';
import 'package:flutter/foundation.dart';

/// Local licensed sample playback. Requests are not proof of physical listening.
class SampleAudio extends ChangeNotifier {
  SampleAudio({this.budget, this.requestPlayback});
  final Future<void> Function()? requestPlayback;
  bool _disposed = false;
  final int? budget;
  AudioPlayer? _player;
  int requests = 0;
  bool busy = false, failed = false;
  bool get limited => budget != null && requests >= budget!;
  Future<void> play() async {
    if (busy || limited) return;
    busy = true;
    failed = false;
    requests++;
    notifyListeners();
    try {
      if (requestPlayback != null) {
        await requestPlayback!();
        return;
      }
      _player ??= AudioPlayer()
        // This short sample has no position/progress UI. Do not schedule frames.
        ..positionUpdater = null
        ..audioCache = AudioCache(prefix: 'packages/mingo_ui/assets/');
      await _player!.play(AssetSource('hello.ogg'));
    } catch (_) {
      failed = true;
    } finally {
      busy = false;
      if (!_disposed) {
        notifyListeners();
      }
    }
  }

  @override
  void dispose() {
    _disposed = true;
    _player?.dispose();
    super.dispose();
  }
}
