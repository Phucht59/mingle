# Phase 1 Acceptance Checklist

Use this as the gate before entering Phase 2.

## Repository and structure

- [ ] Monorepo/repository structure is explicit and documented.
- [ ] Backend API process boots locally.
- [ ] Durable worker process boots locally from the same codebase.
- [ ] Flutter Android learner app boots.
- [ ] Flutter Web staff/admin shell boots.
- [ ] Environment/config strategy is documented.

## Data foundation

- [ ] PostgreSQL local/dev connection is reproducible.
- [ ] Migration workflow is deterministic.
- [ ] V3.2 schema/contract references are wired into implementation work.
- [ ] No business rule is silently changed from V3.2.

## Storage

- [ ] Object-storage interface is defined at the appropriate abstraction level.
- [ ] Local/dev storage behavior is reproducible.

## Testing

- [ ] Existing contract/SQL verification remains runnable.
- [ ] Integration-test harness exists.
- [ ] Database transaction/concurrency test harness exists.
- [ ] Security/auth testing structure can be added in Phase 3 without redesigning the repo.
- [ ] CI can run baseline automated checks.

## Offline/telemetry preparedness

- [ ] Command vs telemetry boundary is represented in interfaces/modules.
- [ ] Later durable client queues can be implemented without collapsing command and telemetry semantics.

## Operations

- [ ] Structured logging conventions exist.
- [ ] Error handling conventions exist.
- [ ] Health/readiness endpoints or equivalent backend checks exist.
- [ ] Developer setup documentation works from a clean environment.

## Gate condition

Phase 1 is complete only when the above foundation is demonstrably runnable and tested, not merely documented.
