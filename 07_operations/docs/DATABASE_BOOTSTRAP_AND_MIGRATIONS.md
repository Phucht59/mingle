> Updated 2026-09-26: active source is under `05_code/`; Phase 1 remains ACTIVE / GATE NOT PASSED. Current status: `01_governance/PROJECT_STATE.md`; current DB evidence: `06_quality/evidence/clean_reproduction/README.md`. Exact original V3.2 verification sources remain absent.

# PostgreSQL Bootstrap and Migration Discipline

The exact V3.2 DDL/SQL verification source is missing. **No tables, columns, indexes, OpenAPI payloads or migrations are inferred here.**

1. Import/read approved V3.2 SQL and repository migration history; identify current schema head and its applied versions. The canonical repo now exists; when exact V3.2 DDL arrives, map/import it with provenance rather than retyping remembered schema.
2. Local reproducibility: disposable PostgreSQL service, one setup command, migration apply, health query, seed only synthetic fixtures, teardown/rebuild. Object-storage adapter test uses local reversible fixture.
3. Migration rules: ordered immutable published migrations, explicit review of destructive/backfill operations, transaction boundary documented, rollback or forward-fix plan, CI runs new DB→head and old supported head→head.
4. Verify exact recorded 22 SQL checks and 115 contract checks using their original scripts; record checksum/commands/results. Tests must also cover transaction concurrency, idempotent retry and pinned content revisions; schema-only PASS is insufficient.
5. Preserve event time and knowledge/availability time for analytics without retroactive information leakage; use server-authoritative canonical writes and separate telemetry. Never model a mastery field or risk probability from memory.

The infrastructure-only `foundation` migrations now run on `mingo` using role
`mingo_app`; destructive integration tests run only on `mingo_test`. Blank-database
application and checksum-preserving repeat migration pass locally and on CI. Follow
the root README and `LOCAL_RUNTIME.md` for commands. Exact domain DDL and its original
checks remain blocked by II-01; infrastructure checks do not substitute for them.
