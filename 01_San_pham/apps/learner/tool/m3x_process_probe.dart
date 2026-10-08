import 'dart:async';
import 'dart:convert';
import 'dart:io';
import 'package:adaptive_learner/m3x/learning_state.dart';
import 'package:adaptive_learner/m3x/learning_store.dart';
import 'package:adaptive_learner/m3x/proof_server.dart';

// Host probe uses EXACTLY the same snapshot/queue store as the native app.
Future<void> main(List<String> args) async {
  final mode = args[0], store = FileLearningStore(args[1]);
  if (mode == 'read') {
    stdout.writeln(jsonEncode(await store.read()));
    return;
  }
  if (mode == 'wire') {
    final bytes = makeCommand(practiceItem, 'taxi', online: false);
    final server = ControlledProofServer(store);
    final delivery = await server.deliver(fixtureId(1), bytes);
    final duplicate = await server.deliver(fixtureId(1), bytes);
    final altered = (jsonDecode(bytes) as Map<String, dynamic>)
      ..['command_id'] = newId();
    final rejected = await server.deliver(fixtureId(1), jsonEncode(altered));
    final duplicateRejected = await server.deliver(
      fixtureId(1),
      jsonEncode(altered),
    );
    final conflictPayload = jsonDecode(bytes) as Map<String, dynamic>;
    conflictPayload['answers'][0]['option_id'] = 'reservation';
    final conflict = await server.deliver(
      fixtureId(1),
      jsonEncode(conflictPayload),
    );
    final denied = await server.deliver(fixtureId(99), bytes);
    server.ackEnabled = false;
    final retryable = await server.deliver(fixtureId(1), bytes);
    stdout.writeln(
      jsonEncode({
        'command': jsonDecode(bytes),
        'delivery': delivery.wire,
        'variants': {
          'duplicateAccepted': duplicate.wire,
          'rejected': rejected.wire,
          'duplicateRejected': duplicateRejected.wire,
          'conflict': conflict.wire,
          'denied': denied.wire,
          'retryable': retryable.wire,
        },
      }),
    );
    return;
  }
  final first = makeCommand(practiceItem, 'taxi', online: false);
  final retry = makeCommand(practiceItem, 'reservation', online: false);
  ResponseRecord response(String bytes, List<String> assistance) {
    final j = jsonDecode(bytes) as Map<String, dynamic>;
    return ResponseRecord(
      commandId: j['command_id'] as String,
      attemptId: j['attempt_id'] as String,
      answer: j['answers'][0]['option_id'] as String,
      condition: 'practice',
      assistance: assistance,
    );
  }

  final responses = [
    response(first, []),
    response(retry, ['explanation']),
  ];
  final state = LearningState(
    owner: fixtureId(1),
    homeOffset: 137,
    tasks: {
      'practice': TaskSession(
        key: 'practice',
        selection: 'reservation',
        currentCommand: responses.last.commandId,
        responses: responses,
        retrying: true,
      ),
      'check': TaskSession(key: 'check'),
    },
    commands: {
      responses.first.commandId: QueuedCommand(
        id: responses.first.commandId,
        bytes: first,
      ),
      responses.last.commandId: QueuedCommand(
        id: responses.last.commandId,
        bytes: retry,
      ),
    },
  );
  await store.write(state.toJson());
  stdout.writeln(
    jsonEncode({'ready': true, 'pid': pid, 'snapshot': state.toJson()}),
  );
  await stdout.flush();
  Timer.periodic(const Duration(minutes: 1), (_) {});
  await Completer<void>().future;
}
