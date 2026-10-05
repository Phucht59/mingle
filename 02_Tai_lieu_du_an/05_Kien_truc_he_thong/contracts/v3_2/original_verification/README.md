# Original verification entry points

The exact original programs remain at their original relative paths in the immutable
`../source` tree. Moving them would break their package-relative references:

- Contract: `../source/validators/run_checks.py` and `validate_contracts.py`.
- SQL: `../source/tests/check_sql.mjs`.

Use `04_Van_hanh/Scripts/check_original_contracts.py` from the repository root.
It verifies provenance hashes, copies the complete package, installs the original npm
lock, invokes both suites unchanged and records their actual exits and fresh reports.
Install the original Python requirements in an isolated Python 3.12 environment first.
The SQL engine is PGlite, exactly as provided by the owner; the suite is not relabeled
as native PostgreSQL concurrency testing.
