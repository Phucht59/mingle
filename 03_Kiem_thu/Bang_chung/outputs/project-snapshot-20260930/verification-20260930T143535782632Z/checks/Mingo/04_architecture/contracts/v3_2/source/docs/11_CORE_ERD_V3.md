# 11 — Logical ERD V3

```mermaid
erDiagram
  USER ||--o{ ENROLLMENT : owns
  USER ||--o{ OFFLINE_DOWNLOAD_GRANT : owns
  USER ||--o{ COMMAND_RECEIPT : owns
  USER ||--o{ TELEMETRY_EVENT : owns

  STAFF ||--o{ STAFF_ASSIGNMENT : has
  USER ||--o{ STAFF_ASSIGNMENT : scoped_learner

  COURSE ||--o{ COURSE_RELEASE : publishes
  COURSE_RELEASE ||--o{ RELEASE_UNIT : contains
  RELEASE_UNIT ||--o{ RELEASE_LESSON : contains
  RELEASE_LESSON ||--o{ RELEASE_ACTIVITY : contains

  ACTIVITY ||--o{ ACTIVITY_REVISION : versions
  ACTIVITY_REVISION ||--o{ QUESTION_REVISION : contains
  RELEASE_ACTIVITY }o--|| ACTIVITY_REVISION : pins
  ACTIVITY_REVISION ||--o{ SCORING_VERSION : scored_by

  COURSE_RELEASE ||--o{ ENROLLMENT : pinned_release
  ENROLLMENT ||--o{ ATTEMPT : has
  RELEASE_ACTIVITY ||--o{ ATTEMPT : attempts
  ATTEMPT ||--o{ ANSWER_SUBMISSION : contains
  QUESTION_REVISION ||--o{ ANSWER_SUBMISSION : pins
  ATTEMPT ||--o{ SCORING_RECORD : scored
  SCORING_VERSION ||--o{ SCORING_RECORD : uses

  ENROLLMENT ||--o{ COMPLETION_CREDIT : credits
  RELEASE_ACTIVITY ||--o{ COMPLETION_CREDIT : credited_once
  ENROLLMENT ||--|| PROGRESS_STATE : canonical

  COURSE_RELEASE ||--o{ RELEASE_ACCESS_STATUS : status_history
  ENROLLMENT ||--o{ OFFLINE_DOWNLOAD_GRANT : scoped

  COMMAND_RECEIPT ||--o{ OUTBOX_MESSAGE : emits
  OUTBOX_MESSAGE ||--o{ JOB : creates

  TELEMETRY_EVENT ||--o{ EVIDENCE_PUBLICATION : publishes
  COMMAND_RECEIPT ||--o{ EVIDENCE_PUBLICATION : publishes
  SCORING_RECORD ||--o{ EVIDENCE_PUBLICATION : publishes

  USER ||--o{ SOURCE_CAPTURE : captures
  SOURCE_CAPTURE ||--o{ FEATURE_SNAPSHOT : inputs
  FEATURE_SNAPSHOT ||--o{ PREDICTION : predicts

  USER ||--o{ RECOMMENDATION_DECISION : receives
  PREDICTION o|--o{ RECOMMENDATION_DECISION : optional_input
  RECOMMENDATION_DECISION ||--o{ RECOMMENDATION_EXPOSURE : exposed
  RECOMMENDATION_DECISION ||--o{ ACTION_EXECUTION : executes
  RECOMMENDATION_DECISION ||--o{ OUTCOME_OBSERVATION : observes
  ACTION_EXECUTION o|--o{ OUTCOME_OBSERVATION : optional_execution
```

## Important uniqueness

- command receipt: `(learner_id, command_id)`
- completion credit: `(enrollment_id, release_activity_id)`
- exposure: `(learner_id, exposure_id)`
- evidence publication: `(source_type, source_id, source_revision)`
- outbox handler effect: `(outbox_message_id, handler_type, handler_version)`
