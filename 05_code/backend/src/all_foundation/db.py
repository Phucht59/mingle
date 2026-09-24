import hashlib
from importlib.resources import files
from pathlib import Path

import psycopg
from psycopg.rows import dict_row


def connect(url: str):
    return psycopg.connect(url, connect_timeout=3, row_factory=dict_row)


def migrate(url: str, directory: Path | None = None):
    source = directory or Path(str(files("all_foundation").joinpath("migrations")))
    applied = []
    with connect(url) as conn:
        # Serialize migrators across API/worker starts without external infrastructure.
        conn.execute("SELECT pg_advisory_xact_lock(7310923)")
        conn.execute("CREATE SCHEMA IF NOT EXISTS foundation")
        conn.execute("""
            CREATE TABLE IF NOT EXISTS foundation.schema_migrations (
                name text PRIMARY KEY, sha256 text NOT NULL,
                applied_at timestamptz NOT NULL DEFAULT clock_timestamp()
            )
        """)
        for path in sorted(source.glob("*.sql")):
            body = path.read_bytes()
            digest = hashlib.sha256(body).hexdigest()
            old = conn.execute(
                "SELECT sha256 FROM foundation.schema_migrations WHERE name=%s", (path.name,)
            ).fetchone()
            if old:
                if old["sha256"] != digest:
                    raise RuntimeError(f"Applied migration checksum mismatch: {path.name}")
                continue
            conn.execute(body.decode("utf-8"))
            conn.execute(
                "INSERT INTO foundation.schema_migrations(name,sha256) VALUES (%s,%s)",
                (path.name, digest),
            )
            applied.append(path.name)
    return applied


def schema_ready(url: str):
    source = Path(str(files("all_foundation").joinpath("migrations")))
    expected = {p.name: hashlib.sha256(p.read_bytes()).hexdigest() for p in source.glob("*.sql")}
    with connect(url) as conn:
        actual = {
            r["name"]: r["sha256"]
            for r in conn.execute("SELECT name, sha256 FROM foundation.schema_migrations")
        }
    return expected == actual
