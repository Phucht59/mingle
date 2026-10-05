# 10 — Retention / Delete / Restore Race Controls

## Tombstone generation

Deletion request has:
- subject;
- deletion generation;
- requested time;
- status.

Analytical/worker publish operations must re-check the current deletion generation before publishing subject-derived output.

## Restore safety

A DB restore can rewind before deletion.

Therefore production runbook must maintain deletion/tombstone replay information in a recovery source not lost with the same restore point, e.g.:
- provider/audit system with independent retention;
- separately backed-up append-only deletion ledger.

After restore:
1. replay deletion ledger/tombstones;
2. block analytical jobs for deleted subjects;
3. resume service only after reconciliation according to runbook.

## Export race

An export job:
- pins subject deletion generation when requested;
- rechecks before publishing export;
- aborts/cleans artifact if deletion generation changed.

## Async job race

All subject-derived jobs:
- check deletion state at lease/start;
- check generation again before final publish.

This prevents a long-running job from recreating data after deletion was requested.

## V3.2 atomic deletion/publish gate

A second unprotected read of deletion generation can race with deletion before publish. The publish and deletion transactions must lock the same subject gate row and compare generation while holding the lock through commit. If publication linearizes first, the subsequent deletion removes it; if deletion linearizes first, publication aborts. Authorization blocks export downloads as soon as deletion is requested. Staged objects from aborted workers are cleaned by a retryable job.

The independent deletion ledger is replicated/retained outside the DB restore timeline. Restore stays in maintenance mode until the ledger is replayed, affected objects/jobs reconciled, and access checks pass. This is a required deployment procedure, not a guarantee established by a document or by a single-user database test.
