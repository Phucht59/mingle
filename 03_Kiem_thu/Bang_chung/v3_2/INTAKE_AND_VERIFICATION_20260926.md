# Exact originals recovered and rerun — 2026-09-26

The owner supplied `ADAPTIVE_LANGUAGE_LEARNING_BASELINE_COMPLETED.zip` after the
earlier missing-artifact report. Those earlier failed/blocked logs remain historical.

## Provenance

- ZIP SHA-256: `1b4c9c10afad5245517d2593e5bbd98c7f233fc662c221ee8332cc386c83fe0a`.
- 102 files imported unchanged; all 101 embedded manifest entries match hashes and
  byte lengths. The original manifest itself is covered by the new intake inventory.
- Source/adapter/CI commit: `d4165e8acdffa4e0a747b11ac3e1c3c852674293`.
- Source intake, exact checksums and original package identity are under
  `08_handoff/provenance/v3_2/`.

## Actual runs

| Environment | Contract | SQL | Evidence |
|---|---|---|---|
| Initial Windows integration, Python 3.12.10 / Node 24.19.0 | 115 PASS / 0 FAIL | 22 PASS / 0 FAIL | `20260926T153133959523Z/`; working changes explicitly recorded |
| Fresh Git clone of `d4165e8`, fresh virtualenv and locked dependencies | 115 PASS / 0 FAIL | 22 PASS / 0 FAIL | `clean-d4165e8/20260926T153556896060Z/`; initially clean working tree |
| Final adapter lint/diagnostic polish, Windows | 115 PASS / 0 FAIL | 22 PASS / 0 FAIL | `20260926T154406968964Z/`; working changes and exact adapter hash recorded |

The fresh-clone check used `git clone --no-local`, an empty virtualenv, a new npm
installation in a disposable copy, and no DB credentials. All command exits were 0.
`pip check` passes. Nine independent adapter guard tests pass, including changed,
missing and extra source rejection and detection of dishonest/truncated result counts.

The adapter removes the copied historical reports before execution and validates the
new per-check result lists. Original files and reports retain their exact hashes after
every run and across Git checkout. No original assertion or source file was modified.

SQL uses **PGlite PostgreSQL WASM**, exactly as supplied. It does not prove native
multi-connection domain concurrency. Existing native foundation test evidence and
actual application-shell boot evidence remain separate.

## Clean reproduction coverage

Application source under `05_code/` is unchanged from the fully reproduced runtime
revision `4cdecb4`. This fresh-clone run adds the newly supplied original verification
to that existing full runtime reproduction. The hosted workflow at `d4165e8` reruns
backend, PostgreSQL, both Flutter builds, adapter guards and originals together.
Use the corresponding CI report for the observed hosted conclusion.
