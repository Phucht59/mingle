import 'dart:convert';
import 'dart:math';
import 'package:crypto/crypto.dart';

String fixtureId(int value) =>
    '10000000-0000-4000-8000-${value.toRadixString(16).padLeft(12, '0')}';
String newId() {
  final random = Random.secure();
  final bytes = List.generate(16, (_) => random.nextInt(256));
  bytes[6] = (bytes[6] & 15) | 64;
  bytes[8] = (bytes[8] & 63) | 128;
  final hex = bytes.map((b) => b.toRadixString(16).padLeft(2, '0')).join();
  return '${hex.substring(0, 8)}-${hex.substring(8, 12)}-'
      '${hex.substring(12, 16)}-${hex.substring(16, 20)}-${hex.substring(20)}';
}

/// Only the string/null command subset is supported here; no generic JCS numbers.
String commandDigest(String bytes) {
  dynamic canonical(dynamic value) {
    if (value is Map) {
      final keys = value.keys.cast<String>().toList()..sort();
      return {for (final key in keys) key: canonical(value[key])};
    }
    if (value is List) return value.map(canonical).toList();
    if (value != null && value is! String) {
      throw FormatException('Unsupported semantic command value');
    }
    return value;
  }

  final payload = Map<String, dynamic>.from(jsonDecode(bytes) as Map)
    ..remove('command_id')
    ..removeWhere((_, value) => value == null);
  final answers =
      List<Map<String, dynamic>>.from(
        (payload['answers'] as List).map(
          (a) => Map<String, dynamic>.from(a as Map),
        ),
      )..sort(
        (a, b) => (a['question_revision_id'] as String).compareTo(
          b['question_revision_id'] as String,
        ),
      );
  if (answers.map((a) => a['question_revision_id']).toSet().length !=
      answers.length) {
    throw FormatException('Duplicate question revisions');
  }
  payload['answers'] = answers;
  return sha256.convert(utf8.encode(jsonEncode(canonical(payload)))).toString();
}

enum SyncPhase { pending, syncing, synced, failed, conflict, reauth, rejected }

class PracticePolicy {
  const PracticePolicy({
    this.hint = true,
    this.retryIncorrect = true,
    this.retryCorrect = false,
    this.maxRetries = 1,
  });
  final bool hint, retryIncorrect, retryCorrect;
  final int maxRetries;
}

class TaskItem {
  const TaskItem({
    required this.key,
    required this.activityRevision,
    required this.questionRevision,
    required this.releaseActivity,
    required this.situation,
    required this.prompt,
    required this.intent,
    required this.options,
    this.check = false,
  });
  final String key, activityRevision, questionRevision, releaseActivity;
  final String situation, prompt, intent;
  final Map<String, String> options;
  final bool check;
  Map<String, dynamic> toJson() => {
    'key': key,
    'activityRevision': activityRevision,
    'questionRevision': questionRevision,
    'releaseActivity': releaseActivity,
    'situation': situation,
    'prompt': prompt,
    'intent': intent,
    'options': options,
    'check': check,
  };
  factory TaskItem.fromJson(Map<String, dynamic> j) => TaskItem(
    key: j['key'] as String,
    activityRevision: j['activityRevision'] as String,
    questionRevision: j['questionRevision'] as String,
    releaseActivity: j['releaseActivity'] as String,
    situation: j['situation'] as String,
    prompt: j['prompt'] as String,
    intent: j['intent'] as String,
    check: j['check'] as bool,
    options: Map.unmodifiable(Map<String, String>.from(j['options'] as Map)),
  );
}

// Authenticated, eligible, already-downloaded proof content. No answer keys here.
final practiceItem = TaskItem(
  key: 'practice',
  activityRevision: fixtureId(10),
  questionRevision: fixtureId(11),
  releaseActivity: fixtureId(12),
  situation: 'Nhận phòng ở khách sạn',
  prompt: 'Welcome. Do you have a reservation?',
  intent: 'Bạn muốn nói rằng mình đã đặt phòng.',
  options: const {
    'reservation': 'Yes, I have a reservation.',
    'taxi': 'No, I need a taxi.',
    'station': 'Where is the station?',
  },
);
final checkItem = TaskItem(
  key: 'check',
  activityRevision: fixtureId(20),
  questionRevision: fixtureId(21),
  releaseActivity: fixtureId(22),
  situation: 'Gọi món ở quán ăn',
  prompt: 'Are you ready to order?',
  intent: 'Bạn muốn gọi món súp.',
  check: true,
  options: const {
    'soup': "Yes, I’d like the soup, please.",
    'taxi': 'No, I need a taxi.',
    'station': 'Where is the station?',
  },
);
TaskItem itemFor(String key) => key == 'check' ? checkItem : practiceItem;

class ResponseRecord {
  ResponseRecord({
    required this.commandId,
    required this.attemptId,
    required this.answer,
    required this.condition,
    required List<String> assistance,
  }) : assistance = List.unmodifiable(assistance);
  final String commandId, attemptId, answer, condition;
  final List<String> assistance;
  bool get assisted => assistance.isNotEmpty;
  Map<String, dynamic> toJson() => {
    'commandId': commandId,
    'attemptId': attemptId,
    'answer': answer,
    'condition': condition,
    'assistance': assistance,
  };
  factory ResponseRecord.fromJson(Map<String, dynamic> j) => ResponseRecord(
    commandId: j['commandId'] as String,
    attemptId: j['attemptId'] as String,
    answer: j['answer'] as String,
    condition: j['condition'] as String,
    assistance: List<String>.from(j['assistance'] as List),
  );
}

class TaskSession {
  TaskSession({
    required this.key,
    TaskItem? item,
    this.selection,
    this.currentCommand,
    this.hintSeen = false,
    this.retrying = false,
    List<ResponseRecord> responses = const [],
  }) : responses = List.unmodifiable(responses),
       item = item ?? itemFor(key);
  final String key;
  final TaskItem item;
  final String? selection, currentCommand;
  final bool hintSeen, retrying;
  final List<ResponseRecord> responses;
  ResponseRecord? get firstResponse =>
      responses.isEmpty ? null : responses.first;
  bool get submitted => currentCommand != null;
  TaskSession copy({
    String? selection,
    String? currentCommand,
    bool clearSelection = false,
    bool clearCommand = false,
    bool? hintSeen,
    bool? retrying,
    List<ResponseRecord>? responses,
  }) => TaskSession(
    key: key,
    item: item,
    selection: clearSelection ? null : selection ?? this.selection,
    currentCommand: clearCommand ? null : currentCommand ?? this.currentCommand,
    hintSeen: hintSeen ?? this.hintSeen,
    retrying: retrying ?? this.retrying,
    responses: responses ?? this.responses,
  );
  Map<String, dynamic> toJson() => {
    'key': key,
    'item': item.toJson(),
    'selection': selection,
    'currentCommand': currentCommand,
    'hintSeen': hintSeen,
    'retrying': retrying,
    'responses': responses.map((r) => r.toJson()).toList(),
  };
  factory TaskSession.fromJson(Map<String, dynamic> j) => TaskSession(
    key: j['key'] as String,
    item: TaskItem.fromJson(Map<String, dynamic>.from(j['item'] as Map)),
    selection: j['selection'] as String?,
    currentCommand: j['currentCommand'] as String?,
    hintSeen: j['hintSeen'] as bool,
    retrying: j['retrying'] as bool,
    responses: (j['responses'] as List)
        .map(
          (r) => ResponseRecord.fromJson(Map<String, dynamic>.from(r as Map)),
        )
        .toList(),
  );
}

dynamic _freezeJson(dynamic value) {
  if (value is Map) {
    return Map<String, dynamic>.unmodifiable(
      value.map((key, v) => MapEntry(key as String, _freezeJson(v))),
    );
  }
  if (value is List) return List<dynamic>.unmodifiable(value.map(_freezeJson));
  return value;
}

class QueuedCommand {
  QueuedCommand({
    required this.id,
    required this.bytes,
    this.phase = SyncPhase.pending,
    Map<String, dynamic>? delivery,
    Map<String, dynamic>? feedback,
    this.reason,
  }) : delivery = delivery == null
           ? null
           : _freezeJson(delivery) as Map<String, dynamic>,
       feedback = feedback == null
           ? null
           : _freezeJson(feedback) as Map<String, dynamic>;
  final String id, bytes;
  final SyncPhase phase;
  final String? reason;
  final Map<String, dynamic>? delivery, feedback;
  Map<String, dynamic> get payload => jsonDecode(bytes) as Map<String, dynamic>;
  bool? get correct => feedback?['correct'] as bool?;
  QueuedCommand withState(
    SyncPhase phase, {
    Map<String, dynamic>? delivery,
    Map<String, dynamic>? feedback,
    String? reason,
  }) => QueuedCommand(
    id: id,
    bytes: bytes,
    phase: phase,
    delivery: delivery ?? this.delivery,
    feedback: feedback ?? this.feedback,
    reason: reason,
  );
  Map<String, dynamic> toJson() => {
    'id': id,
    'bytes': bytes,
    'phase': phase.name,
    'delivery': delivery,
    'feedback': feedback,
    'reason': reason,
  };
  factory QueuedCommand.fromJson(Map<String, dynamic> j) => QueuedCommand(
    id: j['id'] as String,
    bytes: j['bytes'] as String,
    phase: SyncPhase.values.byName(j['phase'] as String),
    delivery: j['delivery'] == null
        ? null
        : Map<String, dynamic>.from(j['delivery'] as Map),
    feedback: j['feedback'] == null
        ? null
        : Map<String, dynamic>.from(j['feedback'] as Map),
    reason: j['reason'] as String?,
  );
}

class LearningState {
  LearningState({
    required this.owner,
    Map<String, TaskSession>? tasks,
    Map<String, QueuedCommand> commands = const {},
    this.tab = 0,
    this.homeOffset = 0,
    this.progressRevision = 0,
    this.completionFraction = 0,
    this.resumeKey = 'practice',
  }) : tasks = Map.unmodifiable(
         tasks ??
             {
               'practice': TaskSession(key: 'practice'),
               'check': TaskSession(key: 'check'),
             },
       ),
       commands = Map.unmodifiable(commands);
  final String owner, resumeKey;
  final Map<String, TaskSession> tasks;
  final Map<String, QueuedCommand> commands;
  final int tab, progressRevision;
  final double homeOffset, completionFraction;
  LearningState copy({
    Map<String, TaskSession>? tasks,
    Map<String, QueuedCommand>? commands,
    int? tab,
    double? homeOffset,
    int? progressRevision,
    double? completionFraction,
    String? resumeKey,
  }) => LearningState(
    owner: owner,
    tasks: tasks ?? this.tasks,
    commands: commands ?? this.commands,
    tab: tab ?? this.tab,
    homeOffset: homeOffset ?? this.homeOffset,
    progressRevision: progressRevision ?? this.progressRevision,
    completionFraction: completionFraction ?? this.completionFraction,
    resumeKey: resumeKey ?? this.resumeKey,
  );
  Map<String, dynamic> toJson() => {
    'version': 1,
    'owner': owner,
    'tab': tab,
    'homeOffset': homeOffset,
    'resumeKey': resumeKey,
    'progressRevision': progressRevision,
    'completionFraction': completionFraction,
    'tasks': {
      for (final entry in tasks.entries) entry.key: entry.value.toJson(),
    },
    'commands': {
      for (final entry in commands.entries) entry.key: entry.value.toJson(),
    },
  };
  factory LearningState.fromJson(Map<String, dynamic> j) {
    if (j['version'] != 1) throw FormatException('Unsupported local schema');
    return LearningState(
      owner: j['owner'] as String,
      tab: j['tab'] as int,
      homeOffset: (j['homeOffset'] as num).toDouble(),
      resumeKey: j['resumeKey'] as String,
      progressRevision: j['progressRevision'] as int,
      completionFraction: (j['completionFraction'] as num).toDouble(),
      tasks: (j['tasks'] as Map).map(
        (k, v) => MapEntry(
          k as String,
          TaskSession.fromJson(Map<String, dynamic>.from(v as Map)),
        ),
      ),
      commands: (j['commands'] as Map).map(
        (k, v) => MapEntry(
          k as String,
          QueuedCommand.fromJson(Map<String, dynamic>.from(v as Map)),
        ),
      ),
    );
  }
}

String makeCommand(
  TaskItem item,
  String answer, {
  required bool online,
  String? commandId,
  String? attemptId,
  String? occurredAt,
}) => jsonEncode({
  'command_id': commandId ?? newId(),
  'attempt_id': attemptId ?? newId(),
  'enrollment_id': fixtureId(2),
  'release_activity_id': item.releaseActivity,
  'activity_revision_id': item.activityRevision,
  'submission_mode': online ? 'online' : 'offline',
  'occurred_at': occurredAt ?? DateTime.now().toUtc().toIso8601String(),
  if (!online) ...{
    'offline_grant_id': fixtureId(4),
    'package_id': fixtureId(5),
    'device_installation_id': 'm3x-authenticated-fixture-installation',
  },
  'answers': [
    {'question_revision_id': item.questionRevision, 'option_id': answer},
  ],
});
