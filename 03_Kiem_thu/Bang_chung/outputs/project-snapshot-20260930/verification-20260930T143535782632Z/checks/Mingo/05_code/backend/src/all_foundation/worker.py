import argparse
import logging
import signal
import threading
from uuid import uuid4

from all_foundation.config import Settings
from all_foundation.db import connect, schema_ready
from all_foundation.logging import configure_logging

log = logging.getLogger("worker")


def enqueue(url: str, dedupe_key: str):
    if not dedupe_key or len(dedupe_key) > 200:
        raise ValueError("Invalid probe dedupe key")
    with connect(url) as conn:
        row = conn.execute(
            """
            INSERT INTO foundation.jobs(id,dedupe_key,kind) VALUES (%s,%s,'foundation.noop')
            ON CONFLICT(dedupe_key) DO UPDATE SET dedupe_key=EXCLUDED.dedupe_key
            RETURNING id
        """,
            (uuid4(), dedupe_key),
        ).fetchone()
    return row["id"]


def claim(config: Settings):
    token = uuid4()
    with connect(config.database_url) as conn:
        # Exhausted crashed workers cannot reclaim forever.
        conn.execute(
            """
            UPDATE foundation.jobs SET state='dead', lease_token=NULL, lease_until=NULL
            WHERE state='running' AND lease_until < clock_timestamp() AND attempts >= %s
        """,
            (config.max_attempts,),
        )
        row = conn.execute(
            """
            SELECT id FROM foundation.jobs
            WHERE attempts < %s AND (
                (state='pending' AND run_after <= clock_timestamp()) OR
                (state='running' AND lease_until < clock_timestamp()))
            ORDER BY created_at,id FOR UPDATE SKIP LOCKED LIMIT 1
        """,
            (config.max_attempts,),
        ).fetchone()
        if not row:
            return None
        return conn.execute(
            """
            UPDATE foundation.jobs SET state='running', attempts=attempts+1,
                lease_token=%s, lease_until=clock_timestamp()+(%s * interval '1 second')
            WHERE id=%s RETURNING id,lease_token,attempts
        """,
            (token, config.lease_seconds, row["id"]),
        ).fetchone()


def complete(config: Settings, job: dict, before_effect=None):
    with connect(config.database_url) as conn:
        current = conn.execute(
            """
            SELECT id FROM foundation.jobs
            WHERE id=%s AND lease_token=%s AND state='running'
                AND lease_until > clock_timestamp() FOR UPDATE
        """,
            (job["id"], job["lease_token"]),
        ).fetchone()
        if not current:
            return False
        if before_effect:
            before_effect()
        # Probe side effect and completion commit atomically.
        # External effects will require their own idempotency contract at V3.2 mapping.
        conn.execute(
            """
            INSERT INTO foundation.probe_effects(job_id) VALUES (%s) ON CONFLICT DO NOTHING
        """,
            (job["id"],),
        )
        conn.execute(
            """
            UPDATE foundation.jobs SET state='done',lease_token=NULL,lease_until=NULL
            WHERE id=%s
        """,
            (job["id"],),
        )
    return True


def fail(config: Settings, job: dict, error: Exception):
    with connect(config.database_url) as conn:
        conn.execute(
            """
            UPDATE foundation.jobs SET
                state=CASE WHEN attempts >= %s THEN 'dead' ELSE 'pending' END,
                run_after=clock_timestamp()+(attempts * interval '1 second'),
                last_error_type=%s, lease_token=NULL, lease_until=NULL
            WHERE id=%s AND lease_token=%s AND state='running'
        """,
            (config.max_attempts, type(error).__name__, job["id"], job["lease_token"]),
        )


def heartbeat(config: Settings):
    with connect(config.database_url) as conn:
        conn.execute(
            """
            INSERT INTO foundation.worker_heartbeats(worker_id) VALUES (%s)
            ON CONFLICT(worker_id) DO UPDATE SET last_seen_at=clock_timestamp()
        """,
            (config.worker_id,),
        )


def healthy(config: Settings):
    with connect(config.database_url) as conn:
        return bool(
            conn.execute(
                """
            SELECT 1 FROM foundation.worker_heartbeats
            WHERE worker_id=%s AND last_seen_at > clock_timestamp()-interval '15 seconds'
        """,
                (config.worker_id,),
            ).fetchone()
        )


def run_once(config: Settings):
    heartbeat(config)
    job = claim(config)
    if job is None:
        return False
    try:
        if complete(config, job):
            log.info("job.completed")
        else:
            log.warning("job.lease_lost")
    except Exception as error:
        fail(config, job, error)
        log.warning("job.retry_or_dead")
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true")
    parser.add_argument("--healthcheck", action="store_true")
    args = parser.parse_args()
    configure_logging()
    config = Settings.from_env()
    if args.healthcheck:
        try:
            raise SystemExit(0 if healthy(config) else 1)
        except Exception:
            raise SystemExit(1) from None
    try:
        ready = schema_ready(config.database_url)
    except Exception:
        log.error("worker.database_unavailable")
        raise SystemExit(1) from None
    if not ready:
        log.error("worker.migrations_not_current")
        raise SystemExit(1)
    stop = threading.Event()
    signal.signal(signal.SIGTERM, lambda *_: stop.set())
    signal.signal(signal.SIGINT, lambda *_: stop.set())
    log.info("worker.started")
    while not stop.is_set():
        try:
            worked = run_once(config)
        except Exception:
            log.error("worker.dependency_unavailable")
            if args.once:
                raise
            worked = False
        if args.once:
            break
        if not worked:
            stop.wait(1)
    log.info("worker.stopped")


if __name__ == "__main__":
    main()
