# 14 — Normative submit algorithm, V3.2

This is the reference behavior to implement in FastAPI, not a deployed handler.
All tables below belong to the same PostgreSQL transaction. The pilot chooses
per-learner serialization for correctness; no distributed lock service is needed.

## Request admission

1. Parse strict JSON and schema. Reject duplicate keys, unknown fields and invalid types before side effects. Submit is append-only, so expected_state_version must be omitted/null.
2. Verify JWT issuer/audience/signature/expiry and active account. Resolve installation from account/session context when offline; never trust a body learner_id.
3. Perform privacy-safe object checks. A foreign enrollment/attempt/grant returns denied/403 without a receipt and without identifying the actual owner. Retain batch item IDs for result correlation.
4. Normalize/hash command with `command_digest_v1`. Preserve original command bytes/semantic fields in the client retry queue. Raw JSON key order and answer array order are canonicalized as specified.

## Transaction sequence

1. BEGIN at READ COMMITTED for the command transaction.
2. Lock the authenticated learner row FOR UPDATE. Recheck account/deletion state under that same gate. All pilot submit handlers use this lock order.
3. Lookup `(learner_id,command_id)` receipt. Same digest: return original terminal outcome after transaction, with current state only if accepted. Different digest: conflict; no overwrite. This precedes NEW-command expiry/revoke validation.
4. For a new command, recheck enrollment/release ownership and relevant access/grant rows within the transaction. Shared row locks on access/grant records must conflict with the administrative update that revokes them. Revoke and submit are ordered by lock acquisition; no stale precheck authorizes a later write.
5. Check global attempt ID. Own finalized attempt under a new command: persist rejected ATTEMPT_ALREADY_FINALIZED. Foreign ID: privacy-safe denied; no receipt. If a cross-account insert races, handle unique violation inside a savepoint or rollback/retry lookup; never convert it to silent overwrite or expose ownership.
6. Apply access precedence in 04. NEW online submissions permit published/retired only. NEW offline submissions bind grant/package/session installation and obey deadlines. Current server receipt observation determines upload deadline; client occurrence is not an anti-cheat credential.
7. Validate exact activity question set and option membership using pinned immutable server content; resolve server-only scoring key/version. Deterministic terminal business failure writes only a rejected receipt, no attempt/score/credit. Audit may be separate, but no fake accepted event is emitted.
8. For valid work allocate receipt/score IDs, insert finalized attempt, one answer per question and score revision 1. Receipt FK is deferred until commit, allowing the accepted receipt to be inserted after computing the canonical result. Finalized rows cannot be edited; rescore is a separate revision workflow, disabled in the first pilot UI.
9. Lock enrollment progress row. If activity is REQUIRED, insert unique completion credit ON CONFLICT DO NOTHING. Only a new required credit increments completed count and progress_revision. Optional activity and repeated required attempts create no credit/progress increment.
10. Build typed immutable canonical result from inserted rows/current transaction state: attempt identity/revision, scoring identity/version/raw/max/fraction, completion_credit_created and scoped progress_after_command. Run shape/numeric consistency checks.
11. Insert accepted terminal receipt and outbox in the same transaction. Deferred DB constraints reject accepted partial state or progress/credit drift.
12. COMMIT. No authoritative result before confirmed commit. Connection lost around commit means UNKNOWN_COMMIT_OUTCOME and retry the same command ID.
13. Return receipt and current canonical state. Result-at-command is immutable; current state may already be newer. If the current-state read temporarily fails, retain/retry the original command, never regenerate an attempt. Receipt lookup provides recovery.

## Consistency and errors

- A duplicate rejected command returns delivery_status=duplicate, original rejected receipt and null current state; the UI keeps its business rejection reason.
- A batch validates structure/unique IDs first, then uses a separate transaction per item. Authentication failure is whole-request; object denial is an item denied with no stored receipt.
- No client-driven absolute progress counter writes. No telemetry-driven scoring/completion.
- Current state comparisons require same enrollment/release identity. Client revision 7 never rolls back from an old receipt at revision 5.
- Receipt/idempotency identity is retained for the account lifetime in pilot. Archived receipts remain resolvable; do not delete keys and allow a historical command to be re-executed. Account deletion revokes access and follows the deletion ledger workflow.
- The application must run native PostgreSQL multi-connection tests. Included PGlite tests establish FK/check/trigger/rollback behavior, not real handler concurrency or network exactly-once delivery.

## Publish adapter responsibilities

The SQL is a complete reference core subset, not all future product tables. The publish adapter checks manifest JCS hash, at least one required activity, resource checksums, exact activity/question/option graph, one correct option per question, question_count and scoring_version consistency before committing the immutable release. The server-only key is never returned from public content/resource endpoints.

Profile/auth integration, curriculum data entry, RLS/role grants, API service code, deployment and future ML tables remain implementation work behind these contracts. They are not claimed as existing software in this package.
