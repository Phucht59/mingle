# Canonical tracked-source handoff — 2026-09-26

Runtime revision verified locally, from a clean clone and on hosted CI:
`4cdecb426d33b2996f4a3a72cc78da6a276b713f`. Later handoff commits contain governance,
documentation and observed evidence; use the external ZIP sidecar for the exact
packaged final commit and SHA-256 (avoids a self-referencing archive checksum).

## Packaging verification

A `git archive --format=zip --prefix=Mingo/ HEAD` export at the verified revision
contained 264 entries and passed ZIP integrity validation. No path contained `.git`,
`.venv`, `.local`, `.dart_tool`, `build`, `.pytest_cache`, `.ruff_cache`, `__pycache__`,
IDE directories, `*.egg-info`, or a real `.env`. The final handoff is regenerated
with the same check after committing evidence and governance.

Historical packages under `99_Luu_tru/` and provenance remain tracked deliberately.
They are not current implementation authority. The supplied polluted `Mingo (2).zip`
was preserved; it is superseded for onboarding by the canonical Git/ZIP delivery.

Known local database passwords, the active Git credential and token/private-key
patterns were checked against tracked and prospective tracked files with no matches.
Only placeholders and ephemeral public CI fixture credentials belong in source.

## Gate

Phase 1 remains **ACTIVE / NOT PASSED** because exact approved V3.2 source and the
original executable 115 contract + 22 SQL suites are absent. A clean package does
not close that external artifact blocker. Phase 2 stays deferred.
