# Definition of Done

For each Phase 1 ticket: intent and V3.2 rule reference identified; acceptance behavior and negative path written; code/doc reviewed; migrations/versioning considered; security/privacy/observability checked; relevant focused tests pass; original contract checks pass where applicable; clean setup instructions updated; issue/CR record updated if behavior diverges. Mark as DONE only on observed evidence, not on an authored specification.

For **Phase 1 as a whole**:

1. Repository and module layout documented against actual source.
2. Backend API and durable worker boot separately from same codebase.
3. Flutter Android learner shell and Flutter Web staff shell boot.
4. PostgreSQL local connectivity/migrations and object-storage adapter reproducible.
5. Original V3.2 contract/SQL verification wired into CI and passing or an approved exception recorded.
6. Integration/concurrency/security harnesses and command/telemetry separation present.
7. Structured logging/errors/health/readiness and developer instructions tested from clean environment.
8. Product documents, compatibility matrix, issue/CR register and Phase 1 evidence report reviewed.

If any mandatory item lacks evidence, Phase 1 remains ACTIVE or locally BLOCKED and Phase 2 cannot be declared started. See `06_quality/gates/PHASE_1_GATE.md` for the current result.
