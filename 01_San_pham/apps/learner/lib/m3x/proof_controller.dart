import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'learning_state.dart';
import 'learning_store.dart';
import 'proof_server.dart';

class ProofController extends ChangeNotifier {
  ProofController._(
    this.store,
    this.server,
    this._state,
    this.policy,
    this.online,
  );
  final LearningStore store;
  final CommandServer server;
  final PracticePolicy policy;
  LearningState _state;
  LearningState get state => _state;
  bool online, needsReauth = false, busy = false;
  String? error;
  Future<void> _tail = Future.value();
  bool _disposed = false;
  static Future<ProofController> open(
    LearningStore store,
    CommandServer server, {
    PracticePolicy policy = const PracticePolicy(),
    bool online = true,
  }) async {
    final saved = await store.read();
    var state = saved == null
        ? LearningState(owner: fixtureId(1))
        : LearningState.fromJson(saved);
    if (state.owner != fixtureId(1)) {
      throw StateError('Account mismatch: preserve own pending data');
    }
    // An interrupted transport never implies ACK on relaunch.
    state = state.copy(
      commands: {
        for (final e in state.commands.entries)
          e.key: e.value.phase == SyncPhase.syncing
              ? e.value.withState(SyncPhase.pending)
              : e.value,
      },
    );
    await store.write(state.toJson());
    final controller = ProofController._(store, server, state, policy, online);
    controller.needsReauth = state.commands.values.any(
      (q) => q.phase == SyncPhase.reauth,
    );
    return controller;
  }

  TaskSession task(String key) => state.tasks[key]!;
  QueuedCommand? current(String key) =>
      state.commands[task(key).currentCommand];
  bool canRetry(String key) {
    final task = this.task(key), command = current(key);
    if (task.item.check ||
        command?.phase != SyncPhase.synced ||
        command?.correct == null) {
      return false;
    }
    if (task.responses.length - 1 >= policy.maxRetries) return false;
    return command!.correct! ? policy.retryCorrect : policy.retryIncorrect;
  }

  String get homeReason => 'Bạn đang học dở. Tiếp tục đúng chỗ đã dừng.';
  String get nextAction => state.resumeKey;
  int nextDecisionCount = 0;
  String? decideProofNextAction() {
    nextDecisionCount++;
    if (needsReauth ||
        current(state.resumeKey)?.phase == SyncPhase.conflict ||
        current(state.resumeKey)?.phase == SyncPhase.rejected ||
        current(state.resumeKey)?.phase == SyncPhase.reauth) {
      return null;
    }
    return state.resumeKey;
  }

  void _notify() {
    if (!_disposed) notifyListeners();
  }

  Future<bool> _commit(LearningState Function(LearningState) change) {
    final operation = _tail.then((_) async {
      busy = true;
      error = null;
      _notify();
      try {
        final next = change(state);
        await store.write(next.toJson());
        _state = next;
        return true;
      } catch (_) {
        error =
            'Chưa lưu được thay đổi này. Dữ liệu đã lưu trước đó vẫn được giữ. Thử lại.';
        return false;
      } finally {
        busy = false;
        _notify();
      }
    });
    _tail = operation.then<void>((_) {}, onError: (Object _, StackTrace __) {});
    return operation;
  }

  Future<bool> origin(int tab, double offset) =>
      _commit((s) => s.copy(tab: tab, homeOffset: offset));
  Future<bool> pause(String key) => _commit((s) => s.copy(resumeKey: key));
  Future<bool> select(String key, String answer) {
    if (_submitting ||
        task(key).submitted ||
        !task(key).item.options.containsKey(answer)) {
      return Future.value(false);
    }
    return _commit(
      (s) => s.copy(
        tasks: {
          ...s.tasks,
          key: s.tasks[key]!.copy(selection: answer),
        },
      ),
    );
  }

  Future<bool> hint(String key) {
    if (_submitting ||
        task(key).item.check ||
        !policy.hint ||
        task(key).submitted) {
      return Future.value(false);
    }
    return _commit(
      (s) =>
          s.copy(tasks: {...s.tasks, key: s.tasks[key]!.copy(hintSeen: true)}),
    );
  }

  Future<bool> retry(String key) {
    if (!canRetry(key)) return Future.value(false);
    return _commit(
      (s) => s.copy(
        tasks: {
          ...s.tasks,
          key: s.tasks[key]!.copy(
            clearSelection: true,
            clearCommand: true,
            retrying: true,
          ),
        },
      ),
    );
  }

  bool _submitting = false;
  Future<bool> submit(String key, {bool deliver = true}) async {
    if (_submitting || task(key).selection == null || task(key).submitted) {
      return false;
    }
    _submitting = true;
    try {
      final t = task(key), item = task(key).item;
      final bytes = makeCommand(item, t.selection!, online: online);
      final payload = jsonDecode(bytes) as Map<String, dynamic>;
      final id = payload['command_id'] as String;
      final response = ResponseRecord(
        commandId: id,
        attemptId: payload['attempt_id'] as String,
        answer: t.selection!,
        condition: item.check ? 'independent-check' : 'practice',
        assistance: [if (t.hintSeen) 'hint', if (t.retrying) 'explanation'],
      );
      final saved = await _commit(
        (s) => s.copy(
          resumeKey: key,
          tasks: {
            ...s.tasks,
            key: t.copy(
              currentCommand: id,
              responses: [...t.responses, response],
            ),
          },
          commands: {
            ...s.commands,
            id: QueuedCommand(id: id, bytes: bytes),
          },
        ),
      );
      if (saved && deliver && online) await sync(id);
      return saved;
    } finally {
      _submitting = false;
    }
  }

  void networkRestored() {
    online = true;
    _notify();
  }

  void offline() {
    online = false;
    _notify();
  }

  Future<bool> requireReauth() async {
    needsReauth = true;
    return _commit(
      (s) => s.copy(
        commands: {
          for (final e in s.commands.entries)
            e.key: e.value.phase == SyncPhase.synced
                ? e.value
                : e.value.withState(SyncPhase.reauth),
        },
      ),
    );
  }

  void restoreFixtureIdentity() {
    needsReauth = false;
    _notify();
  }

  final Set<String> _inFlight = {};
  Future<void> sync(String id, {bool replay = false}) async {
    if (_inFlight.contains(id) || !state.commands.containsKey(id)) return;
    final command = state.commands[id]!;
    if (!replay &&
        [
          SyncPhase.synced,
          SyncPhase.conflict,
          SyncPhase.rejected,
        ].contains(command.phase)) {
      return;
    }
    if (!online) return;
    if (needsReauth) {
      await requireReauth();
      return;
    }
    _inFlight.add(id);
    try {
      if (!await _commit(
        (s) => s.copy(
          commands: {...s.commands, id: command.withState(SyncPhase.syncing)},
        ),
      )) {
        return;
      }
      final response = await server.deliver(state.owner, command.bytes);
      await _commit((s) => _reconcile(s, command, response));
    } catch (_) {
      await _commit(
        (s) => s.copy(
          commands: {
            ...s.commands,
            id: command.withState(SyncPhase.failed, reason: 'TRANSPORT_FAILED'),
          },
        ),
      );
    } finally {
      _inFlight.remove(id);
    }
  }

  LearningState _reconcile(
    LearningState state,
    QueuedCommand command,
    ServerDelivery response,
  ) {
    final wire = response.wire, status = wire['delivery_status'];
    LearningState hold(SyncPhase phase, String reason) => state.copy(
      commands: {
        ...state.commands,
        command.id: command.withState(phase, delivery: wire, reason: reason),
      },
    );
    if (wire['command_id'] != command.id) {
      return hold(SyncPhase.conflict, 'ACK_COMMAND_MISMATCH');
    }
    if (status == 'retryable') {
      return hold(SyncPhase.pending, wire['reason_code'] as String);
    }
    if (status == 'conflict') {
      return hold(SyncPhase.conflict, wire['reason_code'] as String);
    }
    if (status == 'denied') {
      needsReauth = true;
      return hold(SyncPhase.reauth, 'FORBIDDEN');
    }
    if (!['accepted', 'duplicate', 'rejected'].contains(status)) {
      return hold(SyncPhase.failed, 'INVALID_DELIVERY');
    }
    final receipt = wire['receipt'];
    if (receipt is! Map ||
        receipt['learner_id'] != state.owner ||
        receipt['command_id'] != command.id ||
        receipt['command_type'] != 'submit_attempt_v1' ||
        receipt['digest_version'] != 'command_digest_v1' ||
        receipt['payload_digest'] != commandDigest(command.bytes) ||
        wire['retry_same_command'] != false ||
        receipt['receipt_id'] is! String ||
        DateTime.tryParse(receipt['recorded_at'] as String? ?? '') == null) {
      return hold(SyncPhase.conflict, 'INVALID_ACK_IDENTITY');
    }
    if (receipt['terminal_outcome'] == 'rejected') {
      if (status == 'accepted' ||
          wire['current_canonical_state'] != null ||
          receipt['canonical_result'] != null) {
        return hold(SyncPhase.conflict, 'INVALID_REJECTION');
      }
      return hold(SyncPhase.rejected, receipt['reason_code'] as String);
    }
    if (status == 'rejected' || receipt['terminal_outcome'] != 'accepted') {
      return hold(SyncPhase.conflict, 'INVALID_ACK_OUTCOME');
    }
    final canonical = receipt['canonical_result'];
    final progress = wire['current_canonical_state']?['progress'];
    final payload = command.payload;
    if (canonical is! Map ||
        progress is! Map ||
        canonical['attempt']?['attempt_id'] != payload['attempt_id'] ||
        canonical['attempt']?['state'] != 'finalized' ||
        canonical['attempt']?['attempt_revision'] != 1 ||
        progress['enrollment_id'] != payload['enrollment_id'] ||
        progress['course_release_id'] != fixtureId(3)) {
      return hold(SyncPhase.conflict, 'INVALID_ACK_SCOPE');
    }
    final score = canonical['score'],
        historicalProgress = canonical['progress_after_command'];
    if (score is! Map ||
        score['max_score'] != 1 ||
        ![0, 1].contains(score['raw_score']) ||
        score['score_fraction'] != score['raw_score'] ||
        score['scoring_record_revision'] != 1 ||
        score['scoring_version_id'] != fixtureId(6) ||
        score['scoring_record_id'] is! String ||
        historicalProgress is! Map ||
        historicalProgress['enrollment_id'] != payload['enrollment_id'] ||
        historicalProgress['course_release_id'] != fixtureId(3) ||
        canonical['completion_credit_created'] != false ||
        wire['reason_code'] != null ||
        receipt['reason_code'] != null) {
      return hold(SyncPhase.conflict, 'INVALID_ACK_RESULT');
    }
    final revision = progress['progress_revision'],
        fraction = progress['completion_fraction'];
    final completed = progress['completed_required_credit_count'],
        eligible = progress['eligible_activity_count'];
    if (revision is! int ||
        revision < 0 ||
        fraction is! num ||
        completed is! int ||
        eligible is! int ||
        eligible < 1 ||
        completed < 0 ||
        completed > eligible ||
        fraction != completed / eligible) {
      return hold(SyncPhase.conflict, 'INVALID_PROGRESS');
    }
    if (revision == state.progressRevision &&
        fraction != state.completionFraction) {
      return hold(SyncPhase.conflict, 'CANONICAL_REFETCH_REQUIRED');
    }
    final feedback = response.feedback;
    if (feedback != null && feedback['correct'] != (score['raw_score'] == 1)) {
      return hold(SyncPhase.conflict, 'INVALID_FEEDBACK');
    }
    return state.copy(
      commands: {
        ...state.commands,
        command.id: command.withState(
          SyncPhase.synced,
          delivery: wire,
          feedback: feedback,
        ),
      },
      progressRevision: revision > state.progressRevision
          ? revision
          : state.progressRevision,
      completionFraction: revision > state.progressRevision
          ? fraction.toDouble()
          : state.completionFraction,
    );
  }

  Future<void> syncPending() async {
    for (final id in state.commands.keys.toList()) {
      await sync(id);
    }
  }

  Future<bool> seedClosure({
    required bool pending,
    String key = 'closure',
  }) async {
    final origin = state.resumeKey;
    if (!state.tasks.containsKey(key)) {
      if (!await _commit(
        (s) => s.copy(
          tasks: {
            ...s.tasks,
            key: TaskSession(key: key),
          },
        ),
      )) {
        return false;
      }
      await select(key, 'reservation');
      if (!await submit(key, deliver: false)) return false;
    }
    if (!pending) await sync(task(key).currentCommand!);
    await _commit((s) => s.copy(resumeKey: origin));
    return true;
  }

  @override
  void dispose() {
    _disposed = true;
    super.dispose();
  }
}
