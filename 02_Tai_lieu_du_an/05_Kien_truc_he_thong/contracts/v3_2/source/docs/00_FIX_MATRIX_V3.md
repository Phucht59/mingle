# 00 — Closure and evidence matrix, V3.2

This version has been finalized directly. See FINALIZATION_REPORT_VI.md for findings and measured checks. Contract closure is not runtime certification.

| Item | Finalized artifacts | Evidence | Runtime gate |
|---|---|---|---|
| C1 | 02,14, scoring policy, corrected DDL, command/content schemas | scoring validation, scope FK, deferred completion, rollback tests | native concurrent handler/lock tests |
| C2 | 03,14, receipt/sync/current state schemas, OpenAPI | accepted/rejected duplicate, nested IDs, hash, progress tests | network response loss and Flutter reconciliation |
| C3 | 04,07, grant/package/content/status schemas, artifacts | deadlines, owner/package/revoke, JCS/asset hashes | device storage/download/session integration |
| C4 | 05, source capture/snapshot contracts | capture/hash/evidence future-time negative cases | original MVCC capture and replay pipeline |
| C5 | 06, model/prediction/feature schemas and validators | label/hash/entropy/dimensions/registry-gate negative cases | scientific model/evaluation/deployment approvals |
| Worker | 08, durable_job DDL | logical key and stale generation SQL cases | worker crash/reacquisition and atomic external publish |
| Delete/restore | 10,15 | explicit lock/ledger runbook | real restore/deletion race drill |
| Operations | 15 | targets and budgets documented | mixed load, auth, PITR, measured RPO/RTO |

Current measured results: 115 Python contract checks and 22 PostgreSQL-WASM SQL checks, zero failures. Detailed reports are included. All tests that require absent application code or real deployment are explicitly NOT RUN; no fabricated PASS.
