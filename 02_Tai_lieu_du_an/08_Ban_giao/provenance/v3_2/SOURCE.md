# Exact V3.2 source intake — 2026-09-26

The project owner supplied `ADAPTIVE_LANGUAGE_LEARNING_BASELINE_COMPLETED.zip`
from their Downloads directory in this conversation to resolve II-01.

- Archive SHA-256: `1b4c9c10afad5245517d2593e5bbd98c7f233fc662c221ee8332cc386c83fe0a`
- Package version: `3.2.0`; original creation time recorded in `REVISION.txt`.
- ZIP contains 102 files. All 101 entries in its manifest match their declared byte
  lengths and SHA-256 hashes; no unexpected or missing members.
- `04_architecture/contracts/v3_2/source/` preserves every original file byte-for-byte,
  including the original manifest, historical reports and handoff document.
- `SHA256SUMS.txt` additionally records all 102 imported files, including the manifest.
  Git attributes disable text conversion for this entire source boundary.

The ZIP checksum anchors this user-supplied intake. Its embedded manifest identifies
an earlier V3 input ZIP; that predecessor archive is not independently supplied here.
No claim of external digital signature or predecessor verification is made.

## Executable authority

- Contract suite: `source/validators/run_checks.py`, using its unchanged validator,
  schema, artifact, example and fixture dependencies.
- SQL suite: `source/tests/check_sql.mjs`, using unchanged DDL and locked PGlite 0.5.8.
- Historical expected counts: 115 contract checks, 22 SQL checks. The adapter invokes
  the actual programs and validates fresh reports against their individual results.
- Runs use disposable copies under ignored `.local/v3_2-runs/`; original reports are
  never overwritten. New evidence belongs under `06_quality/evidence/v3_2/`.

The source is a specification/contract baseline, not a complete application. PGlite
checks do not prove native multi-connection concurrency. The existing six native
PostgreSQL tests cover the Phase 1 infrastructure foundation, not a domain submit
handler. Baseline requirements for later product acceptance remain recorded separately.

The imported handoff prompt is retained as historical source material. It does not
override the current owner's Phase 1 scope or authorize starting Phase 2.
