> Canonical-layout update — 2026-09-24: active source is organized under `05_code/`; Phase 1 remains ACTIVE / GATE NOT PASSED. Current status: `01_governance/PROJECT_STATE.md`; observed runtime evidence: `06_quality/evidence/VERIFICATION_REPORT.md`. Exact original V3.2 verification sources remain absent.

# PostgreSQL Bootstrap and Migration Discipline

The exact V3.2 DDL/SQL verification source is missing. **No tables, columns, indexes, OpenAPI payloads or migrations are inferred here.**

1. Import/read approved V3.2 SQL and repository migration history; identify current schema head and its applied versions. The canonical repo now exists; when exact V3.2 DDL arrives, map/import it with provenance rather than retyping remembered schema.
2. Local reproducibility: disposable PostgreSQL service, one setup command, migration apply, health query, seed only synthetic fixtures, teardown/rebuild. Object-storage adapter test uses local reversible fixture.
3. Migration rules: ordered immutable published migrations, explicit review of destructive/backfill operations, transaction boundary documented, rollback or forward-fix plan, CI runs new DB→head and old supported head→head.
4. Verify exact recorded 22 SQL checks and 115 contract checks using their original scripts; record checksum/commands/results. Tests must also cover transaction concurrency, idempotent retry and pinned content revisions; schema-only PASS is insufficient.
5. Preserve event time and knowledge/availability time for analytics without retroactive information leakage; use server-authoritative canonical writes and separate telemetry. Never model a mastery field or risk probability from memory.

Gate: local reproducible connection/migration + old/new migration smoke + original checks + integration/concurrency harness. Until original source arrives, this document is an actionable strategy and implementation is locally blocked.
