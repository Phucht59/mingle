# 03 — Receipt & Sync Protocol

## 1. Persisted receipt vs transport result

### Persisted CommandReceipt
Created only for a **terminal business result**:
- `accepted`
- `rejected`

It never changes from accepted → duplicate.

### Transport CommandSyncResult
Describes this delivery/retry:
- `accepted`
- `duplicate`
- `rejected`
- `retryable`
- `conflict`
- `denied` (batch item object scope failure)

A duplicate transport result references the original persisted receipt.

## 2. Receipt timestamps

Receipt uses:
- `recorded_at`: server clock when receipt row is created inside its successful transaction.

It is **not named commit time** and is not used as analytical knowledge-availability time.

If the transaction does not commit, the receipt is not visible/persisted.

## 3. Accepted receipt canonical result

Accepted receipt includes immutable result-at-command:
- attempt ID;
- attempt state/revision;
- raw/max score;
- scoring record revision;
- whether this command created the first completion credit;
- progress revision resulting from this command.

This historical result never changes.

## 4. Reconciliation state

For an accepted receipt (whether first delivery or duplicate), transport result additionally returns:
`current_canonical_state`.

This includes at minimum:
- current progress revision;
- current completion fraction.

Thus an old duplicate receipt can close the queue while the client also receives current state.

## 5. Client anti-rollback

Flutter:
- closes queue item on accepted/duplicate terminal reconciliation;
- applies canonical progress only if incoming revision > local canonical revision;
- if equal, verifies compatible value;
- if lower, does **not** roll back; stores transport history only;
- if higher but incompatible/invariant failure, triggers full state refetch.

## 6. Rejected receipt

Persisted only after:
- authentication succeeded;
- learner/object scope is known;
- command semantic payload is valid enough to identify the command;
- business validation deterministically says this exact command can never be accepted unchanged.

To retry after correcting payload:
- create a **new command ID**.

Do not mutate payload behind an old command ID.

## 7. Retryable

Temporary failures do not create terminal business receipt.

Examples:
- temporary DB dependency outage before known commit;
- temporary internal dependency unavailable.

Response tells client:
- retry **same command ID and same payload**.

## 8. Unknown commit outcome

If API loses certainty around commit result:
- return `503` with `UNKNOWN_COMMIT_OUTCOME`;
- client retries same command ID/payload;
- server resolves by command receipt uniqueness.

Never tell client to create a new command ID for unknown commit outcome.

## 9. Conflict

Same `(learner_id, command_id)` with different digest:
- `409 COMMAND_PAYLOAD_CONFLICT`;
- no overwrite;
- original receipt remains authoritative if one exists.

## 10. Batch semantics

`POST /v1/sync/commands`:
- each item processed independently;
- one item failure does not roll back already committed items;
- accepted/duplicate/rejected items return a typed terminal receipt;
- accepted receipts return current canonical state; a duplicate rejected receipt returns the original rejection with null current state;
- retryable/conflict return reason and retry guidance.

## 11. Receipt lookup

`GET /v1/command-receipts/{command_id}`:
- authenticated current learner only;
- returns terminal receipt if it exists;
- returns current canonical progress for accepted receipts; null for rejected receipts.

A command already accepted remains historically queryable even if its content later expires/revokes, subject to account authorization/data-retention policy.

## 12. Local queue deletion UX

Terminal delivery does not immediately erase all local evidence.

Flutter moves terminal item to a local reconciliation history until:
- canonical result was applied/refetched;
- user-visible recovery state for rejected/conflict was surfaced where required.

This avoids silent loss of unsynced-looking work.

## V3.2 complete response matrix

| Delivery | Stored receipt | Current state | Retry same command |
|---|---|---|---|
| accepted | accepted | required | false |
| duplicate of accepted | original accepted | required | false |
| rejected | rejected | null | false |
| duplicate of rejected | original rejected | null | false |
| retryable | null | null | true |
| conflict | null | null | false |
| denied | null | null | false |

`denied` is a per-item object-authorization failure in an authenticated command batch. It stores no terminal receipt. Auth failure for the whole HTTP request is 401. The business command may be retried unchanged if access is subsequently restored; the UI must not automatically loop denied responses.

Batch structure and unique command IDs are validated before any item is processed; max 50 commands, max 1 MiB body. Syntactically invalid whole batch receives 400/422 and no items start. Valid items have independent transactions. Result order matches request order exactly, one result per command. A lost batch response may hide successful commits; retry the original IDs, never regenerate IDs.

`current_canonical_state.progress` includes enrollment and release IDs; compare revisions only within that scope. Historical receipt immutable results are never used to overwrite a newer client state. The receipt lookup returns null current state for rejected receipts. Missing or foreign receipt lookup always returns 404 within the authenticated learner namespace.

A terminal receipt already present is evaluated before NEW-command grant/revoke deadlines, after current identity/read authorization. This rule covers both accepted and rejected receipts. No new work is performed when replaying either kind.
