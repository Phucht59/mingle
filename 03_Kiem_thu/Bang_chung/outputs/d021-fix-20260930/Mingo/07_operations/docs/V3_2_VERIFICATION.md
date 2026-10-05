# Re-run the exact original V3.2 suites

Prerequisites: Python 3.12 and Node.js 24.19.0 with npm. These are verification
dependencies; the application runtime remains FastAPI/Python plus Flutter.

From the repository root, Windows PowerShell:

```powershell
py -3.12 -m venv .local/v32-venv
.local/v32-venv/Scripts/python.exe -m pip install -r 07_operations/requirements-v3_2.lock
.local/v32-venv/Scripts/python.exe -m pip check
.local/v32-venv/Scripts/python.exe -m unittest discover -s 07_operations/tests -v
.local/v32-venv/Scripts/python.exe -X utf8 07_operations/scripts/check_original_contracts.py
```

On Linux/macOS, use `python3.12 -m venv .local/v32-venv` and replace the interpreter
path with `.local/v32-venv/bin/python`. No application DB credentials are required
for these original checks; SQL uses the original PGlite PostgreSQL WASM engine.

The adapter verifies all 102 original file hashes, copies the package to a new
ignored working directory, runs `npm ci` against its unchanged package lock and
invokes the original Python and JavaScript programs. It discards historical reports
only from the disposable copy, requires fresh reports, derives counts from individual
results and fails on bad hashes, dependencies, command exits, reports or counts.

Every run writes timestamped command logs, exits, reports, commit and tool versions
under `06_quality/evidence/v3_2/`. The nine adapter guard tests are additional tests;
they are never counted as part of the original 115 contract or 22 SQL checks.
`--integrity-only` checks provenance only and explicitly reports that suites were not run.

The original source tree is immutable. Never run the upstream report-writing programs
directly inside `04_architecture/contracts/v3_2/source/`. Preserve `.gitattributes`
so Windows/Linux checkouts retain identical original bytes. A source revision needs
new owner-supplied provenance, not regenerated hashes to excuse unexplained changes.

Native PostgreSQL foundation tests and actual Flutter/API/worker boot remain separate
gates described in `LOCAL_RUNTIME.md`. Original SQL verification does not implement
or validate the full future domain submit/auth/offline flow.
