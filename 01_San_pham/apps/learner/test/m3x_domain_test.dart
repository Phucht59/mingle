import 'dart:convert';
import 'dart:io';
import 'package:flutter_test/flutter_test.dart';
import 'package:adaptive_learner/m3x/learning_state.dart';
import 'package:adaptive_learner/m3x/learning_store.dart';
import 'package:adaptive_learner/m3x/proof_controller.dart';
import 'package:adaptive_learner/m3x/proof_server.dart';

class MemoryStore implements LearningStore {
  Map<String, dynamic>? saved;
  bool failNext = false;
  @override
  Future<Map<String, dynamic>?> read() async => saved == null
      ? null
      : jsonDecode(jsonEncode(saved)) as Map<String, dynamic>;
  @override
  Future<void> write(Map<String, dynamic> value) async {
    if (failNext) {
      failNext = false;
      throw const FileSystemException('Injected storage-full failure');
    }
    saved = jsonDecode(jsonEncode(value)) as Map<String, dynamic>;
  }
}

class TransformedServer implements CommandServer {
  TransformedServer(this.server, this.change);
  final CommandServer server;
  final void Function(Map<String, dynamic>) change;
  @override
  Future<ServerDelivery> deliver(String owner, String command) async {
    final value = await server.deliver(owner, command);
    final wire = jsonDecode(jsonEncode(value.wire)) as Map<String, dynamic>;
    change(wire);
    return ServerDelivery(wire, feedback: value.feedback);
  }
}

void main() {
  late MemoryStore store, ledger;
  late ControlledProofServer server;
  late ProofController c;
  setUp(() async {
    store = MemoryStore();
    ledger = MemoryStore();
    server = ControlledProofServer(ledger);
    c = await ProofController.open(store, server);
  });
  tearDown(() => c.dispose());
  test(
    'first response immutable; retry appends assisted response and new attempt ID',
    () async {
      await c.select('practice', 'taxi');
      await c.submit('practice');
      final first = jsonEncode(c.task('practice').firstResponse!.toJson());
      expect(c.canRetry('practice'), isTrue);
      await c.retry('practice');
      await c.select('practice', 'reservation');
      await c.submit('practice');
      expect(jsonEncode(c.task('practice').firstResponse!.toJson()), first);
      expect(c.task('practice').responses.last.assisted, isTrue);
      expect(
        c.task('practice').responses.last.attemptId,
        isNot(c.task('practice').firstResponse!.attemptId),
      );
      expect(c.current('practice')!.correct, isTrue);
    },
  );
  test('hint condition committed before revealing assistance', () async {
    await c.hint('practice');
    await c.select('practice', 'reservation');
    await c.submit('practice');
    expect(c.task('practice').firstResponse!.assistance, ['hint']);
    expect(c.canRetry('practice'), isFalse);
  });
  test(
    'correct retry defaults hidden, explicit proof policy may permit it',
    () async {
      await c.select('practice', 'reservation');
      await c.submit('practice');
      expect(c.canRetry('practice'), isFalse);
      final configured = await ProofController.open(
        store,
        server,
        policy: const PracticePolicy(retryCorrect: true),
      );
      expect(configured.canRetry('practice'), isTrue);
      configured.dispose();
    },
  );
  test(
    'Independent Check rejects hint and retains independent condition',
    () async {
      expect(await c.hint('check'), isFalse);
      await c.select('check', 'soup');
      await c.submit('check');
      expect(c.task('check').firstResponse!.condition, 'independent-check');
      expect(c.task('check').firstResponse!.assisted, isFalse);
      expect(await c.retry('check'), isFalse);
    },
  );
  test('Home deterministic fixture is Resume with truthful reason', () {
    expect(c.nextAction, 'practice');
    expect(c.homeReason, contains('đang học dở'));
  });
  test(
    'network restoration and withheld ACK remain pending, explicit ACK syncs',
    () async {
      c.offline();
      await c.select('practice', 'taxi');
      await c.submit('practice');
      final bytes = c.current('practice')!.bytes;
      server.ackEnabled = false;
      c.networkRestored();
      expect(c.current('practice')!.phase, SyncPhase.pending);
      expect(c.current('practice')!.feedback, isNull);
      await c.syncPending();
      expect(c.current('practice')!.phase, SyncPhase.pending);
      server.ackEnabled = true;
      await c.syncPending();
      expect(c.current('practice')!.phase, SyncPhase.synced);
      expect(c.current('practice')!.bytes, bytes);
    },
  );
  test(
    'duplicate replay returns same immutable receipt; one server attempt',
    () async {
      await c.select('practice', 'taxi');
      await c.submit('practice');
      final command = c.current('practice')!,
          receipt = jsonEncode(command.delivery!['receipt']);
      await c.sync(command.id, replay: true);
      expect(c.current('practice')!.delivery!['delivery_status'], 'duplicate');
      expect(jsonEncode(c.current('practice')!.delivery!['receipt']), receipt);
      expect((ledger.saved!['attempts'] as Map).length, 1);
      expect((ledger.saved!['receipts'] as Map).length, 1);
    },
  );
  test(
    'same command ID with changed payload conflicts without overwrite',
    () async {
      await c.select('practice', 'taxi');
      await c.submit('practice');
      final original = c.current('practice')!, changed = original.payload;
      changed['answers'][0]['option_id'] = 'reservation';
      final delivery = await server.deliver(c.state.owner, jsonEncode(changed));
      expect(delivery.wire['delivery_status'], 'conflict');
      expect(
        (ledger.saved!['receipts']
            as Map)[original.id]['receipt']['payload_digest'],
        commandDigest(original.bytes),
      );
    },
  );
  test(
    'new command against finalized attempt is terminal rejected, not synced',
    () async {
      await c.select('practice', 'taxi');
      await c.submit('practice');
      final command = c.current('practice')!.payload..['command_id'] = newId();
      final delivery = await server.deliver(c.state.owner, jsonEncode(command));
      expect(delivery.wire['delivery_status'], 'rejected');
      expect(delivery.wire['reason_code'], 'ATTEMPT_ALREADY_FINALIZED');
    },
  );
  test('duplicate UI submission creates one durable response', () async {
    await c.select('practice', 'taxi');
    await Future.wait([c.submit('practice'), c.submit('practice')]);
    expect(c.task('practice').responses.length, 1);
    expect(c.state.commands.length, 1);
  });
  test(
    'failed durable submit preserves selection; does not claim response saved',
    () async {
      await c.select('practice', 'taxi');
      store.failNext = true;
      expect(await c.submit('practice'), isFalse);
      expect(c.task('practice').firstResponse, isNull);
      expect(c.state.commands, isEmpty);
      expect(c.task('practice').selection, 'taxi');
      expect(c.error, contains('Chưa lưu'));
    },
  );
  test(
    'failed hint write never exposes hint or contaminates unaided evidence',
    () async {
      store.failNext = true;
      expect(await c.hint('practice'), isFalse);
      expect(c.task('practice').hintSeen, isFalse);
    },
  );
  test(
    'stale/conflict retains exact serialized command across reopen/network',
    () async {
      c.offline();
      await c.select('practice', 'taxi');
      await c.submit('practice');
      final bytes = c.current('practice')!.bytes;
      server.forcedReason = 'COMMAND_PAYLOAD_CONFLICT';
      c.networkRestored();
      await c.syncPending();
      expect(c.current('practice')!.phase, SyncPhase.conflict);
      final reopened = await ProofController.open(store, server);
      reopened.networkRestored();
      expect(reopened.current('practice')!.phase, SyncPhase.conflict);
      expect(reopened.current('practice')!.bytes, bytes);
      reopened.dispose();
    },
  );
  test(
    'reauth retains own queue; connectivity does not clear auth state',
    () async {
      c.offline();
      await c.select('practice', 'taxi');
      await c.submit('practice');
      await c.requireReauth();
      c.networkRestored();
      await c.syncPending();
      expect(c.current('practice')!.phase, SyncPhase.reauth);
      expect(c.task('practice').firstResponse!.answer, 'taxi');
    },
  );
  for (final mismatch in ['owner', 'digest', 'attempt', 'scope']) {
    test('invalid ACK $mismatch cannot produce synced', () async {
      final transformed = TransformedServer(server, (wire) {
        switch (mismatch) {
          case 'owner':
            wire['receipt']['learner_id'] = fixtureId(99);
          case 'digest':
            wire['receipt']['payload_digest'] = '0' * 64;
          case 'attempt':
            wire['receipt']['canonical_result']['attempt']['attempt_id'] =
                newId();
          case 'scope':
            wire['current_canonical_state']['progress']['enrollment_id'] =
                fixtureId(99);
        }
      });
      final other = await ProofController.open(store, transformed);
      await other.select('practice', 'taxi');
      await other.submit('practice');
      expect(other.current('practice')!.phase, SyncPhase.conflict);
      other.dispose();
    });
  }
  test(
    'old duplicate ACK reconciles queue without rolling back newer progress',
    () async {
      await store.write(
        c.state.copy(progressRevision: 7, completionFraction: .75).toJson(),
      );
      final newer = await ProofController.open(store, server);
      await newer.select('practice', 'taxi');
      await newer.submit('practice');
      expect(newer.current('practice')!.phase, SyncPhase.synced);
      expect(newer.state.progressRevision, 7);
      expect(newer.state.completionFraction, .75);
      newer.dispose();
    },
  );
  test('equal revision incompatible progress requires refetch', () async {
    final transformed = TransformedServer(server, (wire) {
      wire['current_canonical_state']['progress']['completed_required_credit_count'] =
          1;
      wire['current_canonical_state']['progress']['eligible_activity_count'] =
          2;
      wire['current_canonical_state']['progress']['completion_fraction'] = .5;
    });
    final other = await ProofController.open(store, transformed);
    await other.select('practice', 'taxi');
    await other.submit('practice');
    expect(other.current('practice')!.reason, 'CANONICAL_REFETCH_REQUIRED');
    other.dispose();
  });
  test(
    'real file store restores response, origin, revision pins and pending bytes',
    () async {
      final directory = await Directory.systemTemp.createTemp(
        'mingo_m3x_domain_',
      );
      addTearDown(() => directory.delete(recursive: true));
      final fileStore = FileLearningStore('${directory.path}/learning.json');
      final first = await ProofController.open(
        fileStore,
        server,
        online: false,
      );
      await first.origin(0, 137);
      await first.select('check', 'soup');
      await first.submit('check');
      await first.pause('check');
      final bytes = first.current('check')!.bytes;
      first.dispose();
      final restored = await ProofController.open(
        FileLearningStore(fileStore.path),
        server,
        online: false,
      );
      expect(restored.state.homeOffset, 137);
      expect(restored.state.resumeKey, 'check');
      expect(restored.current('check')!.bytes, bytes);
      expect(restored.current('check')!.phase, SyncPhase.pending);
      expect(
        restored.current('check')!.payload['activity_revision_id'],
        checkItem.activityRevision,
      );
      restored.dispose();
    },
  );
  test(
    'corrupt committed snapshot is retained and never silently reset',
    () async {
      final directory = await Directory.systemTemp.createTemp(
        'mingo_m3x_corrupt_',
      );
      addTearDown(() => directory.delete(recursive: true));
      final file = File('${directory.path}/learning.json');
      await file.writeAsString('{"bytes":"{}","sha256":"wrong"}');
      await expectLater(
        FileLearningStore(file.path).read(),
        throwsFormatException,
      );
      expect(await file.readAsString(), contains('wrong'));
    },
  );
  test(
    'account mismatch blocks restore rather than remapping pending data',
    () async {
      await store.write(LearningState(owner: fixtureId(99)).toJson());
      await expectLater(ProofController.open(store, server), throwsStateError);
      expect(store.saved!['owner'], fixtureId(99));
    },
  );
  test(
    'late selection during durable submit cannot change submitted answer',
    () async {
      await c.select('practice', 'taxi');
      final operation = c.submit('practice', deliver: false);
      expect(await c.select('practice', 'reservation'), isFalse);
      await operation;
      expect(c.task('practice').selection, 'taxi');
      expect(c.task('practice').firstResponse!.answer, 'taxi');
    },
  );
  test(
    'draft restore uses cached pinned content; stale submit is terminal rejection',
    () async {
      final old = TaskItem.fromJson({
        ...practiceItem.toJson(),
        'activityRevision': fixtureId(90),
        'questionRevision': fixtureId(91),
        'prompt': 'Pinned older prompt',
      });
      await store.write(
        c.state
            .copy(
              tasks: {
                ...c.state.tasks,
                'practice': TaskSession(
                  key: 'practice',
                  item: old,
                  selection: 'taxi',
                ),
              },
            )
            .toJson(),
      );
      final restored = await ProofController.open(store, server);
      expect(restored.task('practice').item.prompt, 'Pinned older prompt');
      await restored.submit('practice');
      expect(restored.current('practice')!.phase, SyncPhase.rejected);
      expect(
        restored.current('practice')!.payload['activity_revision_id'],
        fixtureId(90),
      );
      expect(restored.current('practice')!.feedback, isNull);
      restored.dispose();
    },
  );
  test(
    'ACK reconciliation write failure retries original command/receipt after reopen',
    () async {
      final transformed = TransformedServer(server, (_) {
        store.failNext = true;
      });
      final first = await ProofController.open(store, transformed);
      await first.select('practice', 'taxi');
      await first.submit('practice');
      final bytes = first.current('practice')!.bytes;
      expect(first.current('practice')!.phase, isNot(SyncPhase.synced));
      first.dispose();
      final restored = await ProofController.open(store, server);
      await restored.syncPending();
      expect(restored.current('practice')!.phase, SyncPhase.synced);
      expect(restored.current('practice')!.bytes, bytes);
      expect(
        restored.current('practice')!.delivery!['delivery_status'],
        'duplicate',
      );
      expect((ledger.saved!['attempts'] as Map).length, 1);
      restored.dispose();
    },
  );
  test(
    'queue and response projections cannot mutate persisted history',
    () async {
      await c.select('practice', 'taxi');
      await c.submit('practice');
      expect(
        () => c.task('practice').responses.clear(),
        throwsUnsupportedError,
      );
      expect(
        () => c.current('practice')!.delivery!['receipt']['terminal_outcome'] =
            'rejected',
        throwsUnsupportedError,
      );
    },
  );
  test(
    'reauth is preserved across relaunch until explicit identity restoration',
    () async {
      c.offline();
      await c.select('practice', 'taxi');
      await c.submit('practice');
      await c.requireReauth();
      final restored = await ProofController.open(store, server);
      expect(restored.needsReauth, isTrue);
      restored.networkRestored();
      await restored.syncPending();
      expect(restored.current('practice')!.phase, SyncPhase.reauth);
      restored.restoreFixtureIdentity();
      await restored.syncPending();
      expect(restored.current('practice')!.phase, SyncPhase.synced);
      restored.dispose();
    },
  );
  test(
    'string-subset digest ignores JSON order/nulls but retains exact timestamp/revision',
    () {
      final bytes = makeCommand(practiceItem, 'taxi', online: true);
      final reordered = Map<String, dynamic>.fromEntries(
        (jsonDecode(bytes) as Map<String, dynamic>).entries.toList().reversed,
      )..['expected_state_version'] = null;
      expect(commandDigest(jsonEncode(reordered)), commandDigest(bytes));
      reordered['occurred_at'] = '2026-10-07T00:00:00Z';
      expect(commandDigest(jsonEncode(reordered)), isNot(commandDigest(bytes)));
    },
  );
}
