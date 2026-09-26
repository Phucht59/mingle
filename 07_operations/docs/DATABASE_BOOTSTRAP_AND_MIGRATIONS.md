> Updated 2026-09-26: active source is under `05_code/`; Phase 1 is DONE / GATE PASSED. Current status: `01_governance/PROJECT_STATE.md`; current DB evidence: `06_quality/evidence/clean_reproduction/README.md`. Exact V3.2 originals are now preserved and verified separately.

# PostgreSQL Bootstrap and Migration Discipline

The exact V3.2 reference DDL is preserved under `04_architecture/contracts/v3_2/source/contracts/core_ddl_postgresql.sql`. Its original PGlite SQL suite passes. Reference DDL is not automatically an applied application migration; future domain migrations follow the immutable baseline and their phase-specific acceptance gates.

1. Import/read approved V3.2 SQL and repository migration history; identify current schema head and its applied versions. The canonical repo and exact original DDL now exist; derive future implementation from the preserved authority with provenance.
2. Local reproducibility: disposable PostgreSQL service, one setup command, migration apply, health query, seed only synthetic fixtures, teardown/rebuild. Object-storage adapter test uses local reversible fixture.
3. Migration rules: ordered immutable published migrations, explicit review of destructive/backfill operations, transaction boundary documented, rollback or forward-fix plan, CI runs new DB→head and old supported head→head.
4. Verify exact recorded 22 SQL checks and 115 contract checks using their original scripts; record checksum/commands/results. Tests must also cover transaction concurrency, idempotent retry and pinned content revisions; schema-only PASS is insufficient.
5. Preserve event time and knowledge/availability time for analytics without retroactive information leakage; use server-authoritative canonical writes and separate telemetry. Never model a mastery field or risk probability from memory.

The infrastructure-only `foundation` migrations now run on `mingo` using role
`mingo_app`; destructive integration tests run only on `mingo_test`. Blank-database
application and checksum-preserving repeat migration pass locally and on CI. Follow
the root README and `LOCAL_RUNTIME.md` for commands. Exact domain DDL and its original
checks are now present and verified; infrastructure checks remain separate.
