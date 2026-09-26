# Operations

Operational documentation and executable helper scripts.

Run scripts from the repository root unless noted otherwise. Scripts resolve the canonical `05_code/` and `06_quality/evidence/` paths themselves.

On Windows, use `scripts/verify_backend.ps1 -Python .\.venv\Scripts\python.exe` after installing the locked backend dependencies. Set `TEST_DATABASE_URL` to a disposable `*_test` database and add `-RunPostgres` to run the PostgreSQL integration/concurrency suite.
