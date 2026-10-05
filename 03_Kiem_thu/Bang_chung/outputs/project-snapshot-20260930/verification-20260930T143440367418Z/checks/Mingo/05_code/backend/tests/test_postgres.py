"""Requires a disposable real PostgreSQL database; never substitutes SQLite/mock.
Run explicitly with --run-postgres. Fixture refuses database names without _test suffix.
"""

import os
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urlparse

import pytest
from fastapi.testclient import TestClient

from all_foundation.api import create_app
from all_foundation.config import Settings
from all_foundation.db import connect, migrate, schema_ready
from all_foundation.worker import claim, complete, enqueue, fail, healthy, heartbeat

pytestmark = pytest.mark.postgres


@pytest.fixture
def cfg(tmp_path):
    url = os.environ.get("TEST_DATABASE_URL", "")
    if not urlparse(url).path.endswith("_test"):
        pytest.fail("TEST_DATABASE_URL must name a disposable database ending in _test")
    with connect(url) as conn:
        conn.execute("DROP SCHEMA IF EXISTS foundation CASCADE")
    migrate(url)
    return Settings(url, tmp_path)


def test_migration_idempotent_and_readiness(cfg):
    assert migrate(cfg.database_url) == []
    assert schema_ready(cfg.database_url)
    with TestClient(create_app(cfg)) as client:
        assert client.get("/health/ready").status_code == 200


def test_migration_checksum_and_atomic_failure(cfg, tmp_path):
    bad = tmp_path / "migrations"
    bad.mkdir()
    (bad / "001_runtime_probe.sql").write_text("SELECT 1;")
    with pytest.raises(RuntimeError, match="checksum"):
        migrate(cfg.database_url, bad)
    (bad / "001_runtime_probe.sql").unlink()
    (bad / "999_broken.sql").write_text("CREATE TABLE foundation.rolled_back(id int); INVALID SQL;")
    with pytest.raises(Exception):
        migrate(cfg.database_url, bad)
    with connect(cfg.database_url) as conn:
        assert (
            conn.execute("SELECT to_regclass('foundation.rolled_back') AS t").fetchone()["t"]
            is None
        )


def test_concurrent_idempotent_enqueue_and_claim(cfg):
    with ThreadPoolExecutor(max_workers=8) as pool:
        ids = list(pool.map(lambda _: enqueue(cfg.database_url, "same-command"), range(16)))
    assert len(set(ids)) == 1
    with ThreadPoolExecutor(max_workers=8) as pool:
        jobs = [j for j in pool.map(lambda _: claim(cfg), range(16)) if j]
    assert len(jobs) == 1
    assert complete(cfg, jobs[0])
    assert not complete(cfg, jobs[0])
    with connect(cfg.database_url) as conn:
        assert (
            conn.execute("SELECT count(*) AS n FROM foundation.probe_effects").fetchone()["n"] == 1
        )


def test_crash_recovery_and_stale_worker_fencing(cfg):
    enqueue(cfg.database_url, "crash")
    old = claim(cfg)
    with connect(cfg.database_url) as conn:
        conn.execute("UPDATE foundation.jobs SET lease_until=clock_timestamp()-interval '1 second'")
    new = claim(cfg)
    assert new["lease_token"] != old["lease_token"]
    assert not complete(cfg, old)
    assert complete(cfg, new)


def test_retry_exhaustion_and_no_partial_effect(cfg):
    enqueue(cfg.database_url, "retry")

    def crash():
        raise RuntimeError("sensitive exception payload")

    for _ in range(3):
        job = claim(cfg)
        with pytest.raises(RuntimeError):
            complete(cfg, job, before_effect=crash)
        fail(cfg, job, RuntimeError("sensitive exception payload"))
        with connect(cfg.database_url) as conn:
            conn.execute("UPDATE foundation.jobs SET run_after=clock_timestamp()")
    assert claim(cfg) is None
    with connect(cfg.database_url) as conn:
        row = conn.execute("SELECT state,last_error_type FROM foundation.jobs").fetchone()
        assert row == {"state": "dead", "last_error_type": "RuntimeError"}
        assert (
            conn.execute("SELECT count(*) AS n FROM foundation.probe_effects").fetchone()["n"] == 0
        )


def test_worker_health_expires(cfg):
    assert not healthy(cfg)
    heartbeat(cfg)
    assert healthy(cfg)
    with connect(cfg.database_url) as conn:
        conn.execute(
            "UPDATE foundation.worker_heartbeats "
            "SET last_seen_at=clock_timestamp()-interval '1 minute'"
        )
    assert not healthy(cfg)
