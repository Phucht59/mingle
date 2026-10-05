# Architecture

Architecture/contract baseline is V3.2. The owner's exact supplied package is preserved
under `contracts/v3_2/source`, with byte hashes and intake provenance under
`02_Tai_lieu_du_an/08_Ban_giao/provenance/v3_2/`. The verification adapter executes its unchanged original
115 contract and 22 PGlite SQL checks on a disposable copy and fails on missing,
modified or failing sources. Reference DDL is not automatically an application migration.

Use `baseline` for frozen technical summaries, `V3_2_COMPATIBILITY_MATRIX.md` for implementation mapping, and `data_ml` for analytics/learning-intelligence boundaries.
