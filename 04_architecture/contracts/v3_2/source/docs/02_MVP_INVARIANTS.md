# 02 — Technical MVP Invariants

## 1. Activity/question rule

For `mcq_single_v1` and `listening_mcq_v1`:
- each published activity revision has at least 1 question;
- each question has exactly one correct option;
- each submission must contain **exactly one answer for every question revision in the activity revision**;
- duplicate question IDs are invalid;
- question IDs outside the pinned activity revision are invalid;
- answer must be one valid `option_id`;
- unanswered/partial submission is not supported in pilot.

## 2. Scoring policy `completion_policy_v1`

For every question:
- correct = 1 point;
- incorrect = 0 points;
- no partial credit.

For an attempt:
- `raw_score = Σ awarded_points`;
- `max_score = question_count`;
- `score_fraction = raw_score / max_score`.

Published activity must have at least one question, so `max_score > 0`.

## 3. Completion meaning

`activity_completed = true` means:
- command was valid;
- attempt was fully scored;
- activity completion rule executed.

It does **not** mean:
- mastery achieved;
- risk is low;
- learner passed a pedagogical threshold.

## 4. Completion credit

A release declares `required_for_completion` per release activity.

`eligible_activity_count` =
number of `required_for_completion=true` release activities in the pinned course release.

Publication rule:
- `eligible_activity_count >= 1`.

Only a required activity can create a completion credit in the pilot. Optional activities are scored but create no credit, do not increment the required count, and do not advance progress revision. A learner gets at most one completion credit for:
`(enrollment_id, release_activity_id)`.

Repeat attempts may change latest/best score statistics later, but do not add a second completion credit.

`completion_fraction = completed_required_credit_count / eligible_activity_count`.

The value must be between 0 and 1.

## 5. Attempt immutability

A finalized attempt cannot have answers replaced.

Rules:
- retry same command ID + same semantic payload → same persisted receipt;
- same command ID + different semantic payload → conflict;
- different command ID + same finalized attempt ID → terminal rejection `ATTEMPT_ALREADY_FINALIZED`;
- retry learning activity intentionally → new attempt ID.

## 6. Concurrency

Database invariants:
- unique `(learner_id, command_id)`;
- attempt ID globally unique and bound to one learner/enrollment/activity revision;
- unique `(enrollment_id, release_activity_id)` completion credit.

Progress update:
- lock the enrollment progress row or use equivalent CAS;
- insert completion credit with unique conflict handling;
- recompute/increment only if a **new** completion credit was created;
- revision increments exactly once per canonical state change.

Two devices may create two attempts for one activity, but only one completion credit.

## 7. Command digest `command_digest_v1`

Digest uses RFC 8785 JSON Canonicalization Scheme (JCS) semantics over a normalized semantic command object.

Normalization:
- exclude `command_id`;
- remove optional fields whose value is `null`;
- sort `answers` ascending by `question_revision_id`;
- preserve `occurred_at`, `submission_mode`, grant reference, enrollment, attempt, activity revision and answers;
- reject duplicate question IDs before hashing;
- extra fields are forbidden by schema.

Then:
`payload_digest = SHA-256(JCS(normalized_semantic_payload))`.

Whitespace and object-key order do not change the digest.  
Changing an answer, attempt, content revision, grant or occurrence time does.

Digest algorithm version is stored with the receipt.

## 8. Canonical reason codes

Initial business rejection catalog:
- `INVALID_QUESTION_SET`
- `INVALID_OPTION`
- `ATTEMPT_ALREADY_FINALIZED`
- `CONTENT_NOT_IN_ENROLLMENT_RELEASE`
- `CONTENT_HARD_REVOKED`
- `OFFLINE_GRANT_REQUIRED`
- `OFFLINE_GRANT_INVALID`
- `OFFLINE_UPLOAD_WINDOW_EXPIRED`

Auth/permission failures are transport/auth errors, not persisted business rejection receipts.

## V3.2 protocol decisions

`submit_attempt_v1` is an independent append command: `expected_state_version` is absent/null only. A stale global progress revision must not reject a distinct valid attempt. CAS protects server-side writes, not independent client attempts.

The reference transaction serializes per learner by locking that learner row before receipt lookup (details in 14). Unique keys remain the final protection. The application may later narrow locks after real concurrency tests preserve these semantics.

Offline submissions also bind `package_id` and `device_installation_id`; both are included in the digest. The installation ID is account/session-bound routing metadata, not a secret or proof of hardware possession. The server validates its session binding; a self-declared body value is insufficient.

API raw JSON parsing rejects duplicate object keys, NaN/Infinity and values outside supported JCS numeric limits. Timestamp strings are preserved; retries must reuse the serialized command. Semantically equal timestamp spellings are not normalized implicitly.

Published learner content contains prompts/options and immutable media references. Correct-option keys are server-only. The pilot provides no authoritative offline scoring; the UI shows submitted/pending until canonical scoring arrives. `artifacts/server_only` is never included in a learner download package.

Reason-code authority is `contracts/reason_code_catalog_v1.json`; owner mismatch is FORBIDDEN, with no persisted business receipt and no disclosure of the other owner.
