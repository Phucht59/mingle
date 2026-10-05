# 01 — Master Baseline V3

## Locked architecture

```text
Flutter Android / Flutter Web
        │
        ├─ local content cache
        ├─ durable command queue
        └─ durable telemetry queue
        │
        ▼
FastAPI modular monolith
        │
        ├─ Identity / Access
        ├─ Content
        ├─ Assessment
        ├─ Learning Core
        ├─ Sync / Telemetry
        ├─ Analytics / Intelligence
        └─ Recommendation
        │
        ▼
PostgreSQL
  state + receipts + outbox + jobs + lineage
        │
        ├─ API process
        └─ durable worker process
        │
        ▼
Object Storage
  media + immutable manifests + exports + model artifacts
```

## Integrity hierarchy

1. Authenticated server identity owns learner scope.
2. Published content revisions are immutable.
3. Enrollment is pinned to a course release.
4. Business command is the only path to authoritative attempt/score/progress change.
5. Command transaction writes receipt + authoritative state + outbox atomically.
6. Telemetry is observational and cannot directly grant completion/score.
7. Completion credit is separately unique from attempt count.
8. Client state is provisional until canonical reconciliation.
9. Derived summaries/features never mutate raw/authoritative history.
10. Published prediction/decision records are immutable.

## Data/time hierarchy

- event occurrence time: client observation;
- server receipt time: ingestion observation;
- evidence publication time: post-commit analytical availability;
- source capture: exact immutable evidence set/view used for derived computation;
- serving replay: only data actually published/available by the knowledge boundary.

## Intelligence hierarchy

Learning Evidence
→ optional Learning State
→ optional Risk
→ Decision Context
→ Candidates
→ Policy
→ Decision
→ Exposure
→ Action Execution
→ Outcome Observation

Risk is optional. Mastery and risk remain different concepts.

## No new infrastructure added

V3 does not introduce:
- microservices;
- Kafka;
- Redis requirement;
- Kubernetes;
- warehouse;
- external feature store.

The unresolved issues were protocol/invariant issues, not technology-selection issues.
