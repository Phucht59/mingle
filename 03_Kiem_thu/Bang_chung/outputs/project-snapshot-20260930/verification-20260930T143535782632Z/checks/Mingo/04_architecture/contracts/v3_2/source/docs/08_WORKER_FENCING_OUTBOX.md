# 08 — Worker Fencing & Outbox

## Outbox

Business transaction writes outbox message atomically.

Relay creates/activates jobs idempotently using:
`UNIQUE(outbox_message_id, handler_type, handler_version)`.

Crash after job creation but before marking outbox delivered cannot create duplicate logical job.

## Lease fencing

Job has:
- `lease_generation` integer;
- `lease_owner`;
- `lease_until`.

On acquisition:
- increment generation atomically.

Worker completion/update must include:
`WHERE job_id=? AND lease_owner=? AND lease_generation=? AND status='leased'`.

If lease expired and another worker reacquired, old worker completion affects zero rows.

## Effect idempotency

Each handler declares an effect key.

Examples:
- summary: `(learner_id,enrollment_id,summary_kind,source_revision,computation_version)`
- evidence publication: `(source_type,source_id,source_revision)`
- deletion step: `(deletion_request_id,step_name,generation)`
- export: `(export_request_id,generation)`

Database uniqueness or equivalent deterministic check protects side effects.

## Dead letter

After max/non-retryable failures:
- dead state;
- full error metadata;
- audited manual replay;
- replay creates a new execution record but retains logical effect idempotency.

## Stale derived output

Worker cannot update latest pointer without numeric source-revision CAS in the appropriate computation scope.

## V3.2 transaction-level fencing

Protect the effect write and job completion together, not only the final job status update. In the final publish transaction, lock the job row; verify status, owner, generation and `lease_until > clock_timestamp()`. Acquire/check subject deletion generation in the same transaction, then insert the unique effect/update latest and complete the job. If any fence fails, rollback all database effects. Use a consistent lock order (subject gate before job gate if both needed) across handlers and deletion workflows.

External object writes use staging names. Only the guarded DB publication pointer exposes the object. A fenced-out worker discards staging data; cleanup retries are idempotent. Revocable/signed download authorization still checks deletion status, so an old export link does not bypass deletion through a cached pointer.

`logical_effect_key` is required for timer jobs whose outbox ID is null, since nullable unique outbox keys do not deduplicate those jobs. Manual replay resets the same logical job/effect identity and appends an execution/audit record; it does not bypass uniqueness. Max attempts 8, exponential backoff starting 2 seconds capped 5 minutes with jitter, lease 60 seconds and heartbeat 20 seconds are versioned pilot defaults, not throughput claims.
