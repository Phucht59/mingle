> Current implementation update — 2026-09-23: a new greenfield repository is now supplied under owner authorization; any older statement below that no source exists is historical. API/local storage and 10 tests have runtime evidence. Worker/PostgreSQL, Flutter boot, exact V3.2 checks, hosted CI and full-stack clean reproduction remain unverified. See PROJECT_STATE.md and ../evidence/VERIFICATION_REPORT.md. No original contract mapping is inferred from new infrastructure code.

# PostgreSQL Bootstrap and Migration Discipline

The exact V3.2 DDL/SQL verification source is missing. **No tables, columns, indexes, OpenAPI payloads or migrations are inferred here.**

1. Import/read approved V3.2 SQL and repository migration history; identify current schema head and its applied versions. If no repo exists, initialize migration tooling using original DDL as reviewed baseline rather than retyping remembered schema.
2. Local reproducibility: disposable PostgreSQL service, one setup command, migration apply, health query, seed only synthetic fixtures, teardown/rebuild. Object-storage adapter test uses local reversible fixture.
3. Migration rules: ordered immutable published migrations, explicit review of destructive/backfill operations, transaction boundary documented, rollback or forward-fix plan, CI runs new DB→head and old supported head→head.
4. Verify exact recorded 22 SQL checks and 115 contract checks using their original scripts; record checksum/commands/results. Tests must also cover transaction concurrency, idempotent retry and pinned content revisions; schema-only PASS is insufficient.
5. Preserve event time and knowledge/availability time for analytics without retroactive information leakage; use server-authoritative canonical writes and separate telemetry. Never model a mastery field or risk probability from memory.

Gate: local reproducible connection/migration + old/new migration smoke + original checks + integration/concurrency harness. Until original source arrives, this document is an actionable strategy and implementation is locally blocked.
