# 15 — Operations, retention and delivery defaults

These are versioned engineering defaults for the pilot, not measured service results or a legal compliance certification.

## Capacity and latency targets

| Item | Pilot target/default |
|---|---|
| Load envelope | 1,000 DAU; 200 telemetry events/learner/day; about 6 million events/30 days |
| Mixed load test | 20 API requests/s for 30 minutes; 50 event/s burst for 5 minutes, workers and dashboard active |
| Data volume test | Load 30-day volume first, then test growth toward 180-day retention before expansion |
| API availability | 99.5% monthly target |
| Read / submit p95 | <300 ms / <500 ms server-side, media excluded |
| Event batch p95 | <500 ms for <=100 events, <=512 KiB body |
| Command batch | <=50 items, <=1 MiB body, independent item commits |
| Summary freshness | <=5 min normal; <=30 min degraded, expose as-of/stale state |
| Worker backlog alert | Oldest pending >10 min |
| Pool budget | <=10/API replica, <=2 initial replicas, <=5 worker connections; preserve provider headroom |
| Recovery | RPO <=15 min; RTO <=4 hours; must be demonstrated before real pilot |

Measure submit/read/event latency separately, publish workload mix and errors/retries. No statement that PostgreSQL is already optimized. Start without event partitioning; index actual queries. Add archive/partitioning when maintenance or measured load justifies it, preserving dedup semantics. The operational DB remains the transactional source of truth.

## Retention matrix

| Class | Default |
|---|---|
| Active account attempts/progress/receipts and compact idempotency keys | Account lifetime |
| Deleted-account personal data | Complete deletion workflow target <=30 days, documented exception only |
| Raw telemetry hot DB | 180 days |
| Archived raw telemetry | At most 365 days from receipt |
| Derived summaries/features | 180 days unless an approved study requires a specific period |
| Prediction/recommendation audit | 180 days |
| Staff/admin audit | 365 days, minimize personal payload |
| Temporary export objects | 7 days; revoke access immediately on deletion request |
| Backups | 30-day rolling retention with PITR capability meeting RPO |
| Offline commands | Keep pending until reconciled/recovery surfaced; no silent eviction |
| Telemetry retry eligibility | New event receipt within 11 days of occurred_at; skewed/implausible clocks rejected or quarantined, never used to grant completion |
| Telemetry dedup keys | 180 days; old replay beyond supported admission window rejected |

Identity, purpose and legal scope must be confirmed before a real pilot. That deployment gate does not require redefining curriculum or blocking repository work. Deletion also covers captures, exports, debug logs, staged objects and future training datasets. Never retain raw model artifacts with personal training data accidentally in build logs.

## Recovery procedure

1. Stop public writes; create a recovery incident record and identify restore point.
2. Restore DB and object references into isolated recovery environment.
3. Replay independently retained deletion ledger newer than the restore point, suppress revoked accounts and related jobs.
4. Verify receipt/attempt/score/credit counts, object hashes, latest pointers and pending job/effect identities.
5. Reconcile partial exports/staging objects and idempotent jobs, then perform authorization checks.
6. Record actual data-loss window and elapsed recovery time. Resume service only after gates pass.

A provider without the necessary PITR/backup features cannot satisfy a 15-minute RPO merely because the spec says so. Select capabilities and run a restore drill before enabling the pilot.

## Release order

1. Repository/migrations plus one immutable test release and enrollment seed.
2. Android download and persistent per-account command queue; FastAPI submit/sync and receipt lookup.
3. Atomic scoring/progress/outbox; required concurrency/auth/revoke tests on native PostgreSQL.
4. Worker, summaries, freshness/lag visibility, failure recovery and operational pilot gates.
5. Learning Intelligence domain analysis; future mastery/target/labels/features.
6. Data/model evaluation, shadow and controlled release only with valid target and trusted approvals.

No production model is needed in steps 1–4. The fixture bundle remains non-deployable. Keep microservices/Kafka/warehouse/Kubernetes deferred until a measured requirement exists.
