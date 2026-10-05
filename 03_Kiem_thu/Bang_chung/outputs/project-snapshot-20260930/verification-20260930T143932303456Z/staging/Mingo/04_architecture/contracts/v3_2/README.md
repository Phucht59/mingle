# Exact V3.2 source boundary

The owner supplied `ADAPTIVE_LANGUAGE_LEARNING_BASELINE_COMPLETED.zip` on 2026-09-26.
`source/` contains all 102 original files, unchanged. Intake verified every entry in
the original manifest. Provenance and SHA-256 inventory are under
`08_handoff/provenance/v3_2/`.

The original suites execute from copies through
`07_operations/scripts/check_original_contracts.py`; their first observed rerun is
115/115 contract checks and 22/22 SQL checks PASS. Hosted CI must also pass before
closing the Phase 1 gate. See `original_verification/README.md` for entry points.

Do not edit or regenerate originals in this tree, including historical reports.
PGlite SQL checks remain distinct from the six native PostgreSQL foundation tests.
The live `foundation` schema contains infrastructure probes; imported reference DDL
does not automatically become an applied application migration.
