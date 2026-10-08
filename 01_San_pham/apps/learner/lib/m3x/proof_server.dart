import 'dart:convert';
import 'learning_state.dart';
import 'learning_store.dart';

class ServerDelivery {
  const ServerDelivery(this.wire, {this.feedback});
  final Map<String, dynamic> wire;
  final Map<String, dynamic>? feedback;
}

abstract interface class CommandServer {
  Future<ServerDelivery> deliver(String owner, String serializedCommand);
}

/// PROOF INFRASTRUCTURE ONLY. Not a deployed server or production authorization.
/// Answer keys live at this boundary; the offline client never evaluates them.
/// This ledger is server receipt history, NOT a second client offline queue.
class ControlledProofServer implements CommandServer {
  ControlledProofServer(this.ledger);
  final LearningStore ledger;
  bool ackEnabled = true;
  String? forcedReason;
  Map<String, dynamic>? lastDelivery;
  Future<void> _tail = Future.value();
  @override
  Future<ServerDelivery> deliver(String owner, String serializedCommand) {
    final future = _tail.then((_) => _deliver(owner, serializedCommand));
    _tail = future.then<void>((_) {}, onError: (Object _, StackTrace __) {});
    return future;
  }

  Future<ServerDelivery> _deliver(String owner, String bytes) async {
    final command = jsonDecode(bytes) as Map<String, dynamic>;
    final id = command['command_id'] as String;
    ServerDelivery nonterminal(String status, String reason) => ServerDelivery({
      'command_id': id,
      'delivery_status': status,
      'reason_code': reason,
      'retry_same_command': status == 'retryable',
      'receipt': null,
      'current_canonical_state': null,
    });
    if (owner != fixtureId(1)) return nonterminal('denied', 'FORBIDDEN');
    if (!ackEnabled) return nonterminal('retryable', 'UNKNOWN_COMMIT_OUTCOME');
    final saved =
        await ledger.read() ??
        {'receipts': <String, dynamic>{}, 'attempts': <String, dynamic>{}};
    final receipts = Map<String, dynamic>.from(saved['receipts'] as Map);
    final attempts = Map<String, dynamic>.from(saved['attempts'] as Map);
    final digest = commandDigest(bytes);
    final previous = receipts[id] as Map<String, dynamic>?;
    if (previous != null) {
      if (previous['receipt']['payload_digest'] != digest) {
        return nonterminal('conflict', 'COMMAND_PAYLOAD_CONFLICT');
      }
      final wire = Map<String, dynamic>.from(previous['wire'] as Map)
        ..['delivery_status'] = 'duplicate';
      lastDelivery = wire;
      return ServerDelivery(
        wire,
        feedback: Map<String, dynamic>.from(previous['feedback'] as Map),
      );
    }
    Future<ServerDelivery> reject(String reason) async {
      final receipt = {
        'receipt_id': newId(),
        'learner_id': owner,
        'command_id': id,
        'command_type': 'submit_attempt_v1',
        'digest_version': 'command_digest_v1',
        'payload_digest': digest,
        'terminal_outcome': 'rejected',
        'reason_code': reason,
        'canonical_result': null,
        'recorded_at': DateTime.now().toUtc().toIso8601String(),
      };
      final wire = {
        'command_id': id,
        'delivery_status': 'rejected',
        'retry_same_command': false,
        'reason_code': reason,
        'receipt': receipt,
        'current_canonical_state': null,
      };
      receipts[id] = {
        'receipt': receipt,
        'wire': wire,
        'feedback': <String, dynamic>{},
      };
      await ledger.write({'receipts': receipts, 'attempts': attempts});
      return ServerDelivery(wire);
    }

    if (forcedReason != null) return nonterminal('conflict', forcedReason!);
    final item = command['activity_revision_id'] == checkItem.activityRevision
        ? checkItem
        : practiceItem;
    final answers = command['answers'] as List;
    final valid =
        command['enrollment_id'] == fixtureId(2) &&
        command['release_activity_id'] == item.releaseActivity &&
        command['activity_revision_id'] == item.activityRevision &&
        answers.length == 1 &&
        answers.single['question_revision_id'] == item.questionRevision &&
        item.options.containsKey(answers.single['option_id']);
    if (!valid) {
      return reject('CONTENT_NOT_IN_ENROLLMENT_RELEASE');
    }
    final answer = answers.single['option_id'] as String;
    final correctOption = item.check ? 'soup' : 'reservation';
    final correct = answer == correctOption;
    final progress = {
      'progress_revision': 0,
      'completed_required_credit_count': 0,
      'eligible_activity_count': 1,
      'completion_fraction': 0.0,
      'enrollment_id': fixtureId(2),
      'course_release_id': fixtureId(3),
    };
    final alreadyFinalized = attempts.containsKey(command['attempt_id']);
    final result = {
      'attempt': {
        'attempt_id': command['attempt_id'],
        'state': 'finalized',
        'attempt_revision': 1,
      },
      'score': {
        'raw_score': correct ? 1 : 0,
        'max_score': 1,
        'score_fraction': correct ? 1.0 : 0.0,
        'scoring_record_revision': 1,
        'scoring_record_id': newId(),
        'scoring_version_id': fixtureId(6),
      },
      // Proof activities are optional: no invented cycle-completion credit.
      'completion_credit_created': false, 'progress_after_command': progress,
    };
    final receipt = {
      'receipt_id': newId(),
      'learner_id': owner,
      'command_id': id,
      'command_type': 'submit_attempt_v1',
      'digest_version': 'command_digest_v1',
      'payload_digest': digest,
      'terminal_outcome': alreadyFinalized ? 'rejected' : 'accepted',
      'recorded_at': DateTime.now().toUtc().toIso8601String(),
      'reason_code': alreadyFinalized ? 'ATTEMPT_ALREADY_FINALIZED' : null,
      'canonical_result': alreadyFinalized ? null : result,
    };
    final wire = {
      'command_id': id,
      'delivery_status': alreadyFinalized ? 'rejected' : 'accepted',
      'retry_same_command': false,
      'reason_code': receipt['reason_code'],
      'receipt': receipt,
      'current_canonical_state': alreadyFinalized
          ? null
          : {'progress': progress},
    };
    final feedback = {
      'correct': correct,
      'verdict': correct ? 'Đúng với tình huống' : 'Chưa đúng với tình huống',
      'explanation': item.check
          ? 'Câu này dùng để gọi món một cách lịch sự.'
          : correct
          ? '“I have a reservation” cho biết bạn đã đặt phòng trước.'
          : answer == 'taxi'
          ? 'Câu bạn chọn nói về taxi. Lễ tân đang hỏi về đặt phòng.'
          : 'Câu bạn chọn hỏi về nhà ga. Lễ tân đang hỏi về đặt phòng.',
      'correction': item.options[correctOption],
    };
    receipts[id] = {'receipt': receipt, 'wire': wire, 'feedback': feedback};
    if (!alreadyFinalized) attempts[command['attempt_id'] as String] = id;
    await ledger.write({'receipts': receipts, 'attempts': attempts});
    lastDelivery = wire;
    return ServerDelivery(wire, feedback: alreadyFinalized ? null : feedback);
  }
}
