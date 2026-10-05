CREATE TABLE foundation.worker_heartbeats (
    worker_id text PRIMARY KEY,
    last_seen_at timestamptz NOT NULL DEFAULT clock_timestamp()
);
