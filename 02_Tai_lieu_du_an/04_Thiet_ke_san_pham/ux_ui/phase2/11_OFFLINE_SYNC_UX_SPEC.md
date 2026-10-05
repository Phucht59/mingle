# Offline / Sync UX Specification

Phase 2 defines observable UX states only; Phase 6 implements the durable sync engine.

| State | Learner-facing meaning | Allowed actions | Must not imply |
|---|---|---|---|
| ONLINE_SYNCED | Server-confirmed state is current | Normal learning | — |
| OFFLINE_AVAILABLE | Network unavailable; downloaded eligible work can continue | Start/resume offline-capable work | That all content is available |
| LOCAL_QUEUED | Business action saved locally awaiting sync | Continue where safe, view status | Server acceptance/canonical progress |
| SYNCING | Queue is being reconciled | Keep app usable | Guaranteed success until receipt |
| SYNCED | Canonical result confirmed | Normal use | — |
| SYNC_PARTIAL | Some work synced; some still pending | Inspect/retry pending | All-or-nothing loss |
| SYNC_FAILED_RETRYABLE | Temporary failure | Safe retry/later | Need to re-enter duplicate answer |
| SYNC_REAUTH | Session/permission needs refresh | Re-auth | Local permission bypass |
| CANONICAL_REFRESH | Server state differs/stale local view | Refresh canonical state | Local overwrite of server truth |
| MEDIA_UNAVAILABLE | Required media not on device | Choose valid alternative/sync | Fabricated assessment completion |

Unknown commit outcome is handled by retrying the same durable command identity in implementation, not by asking the learner to submit a new duplicate action. Telemetry upload is separate from business-command status.


## Rework R1 authoritative transition rule

Connectivity restoration is **not** a state transition to `SYNCED`. If one or more business actions are `LOCAL_QUEUED`, returning online leaves them queued until sync starts and authoritative acknowledgement/canonical refresh is received. The Phase 2 prototype exposes explicit test controls for `SYNCING`, retryable failure, partial sync, re-auth and canonical refresh. `MEDIA_UNAVAILABLE` blocks media-required assessment rather than inventing a result.
