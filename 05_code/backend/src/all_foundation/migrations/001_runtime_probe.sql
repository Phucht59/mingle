-- New infrastructure-only sandbox. NOT the missing V3.2 domain schema.
CREATE TABLE foundation.jobs (
    id uuid PRIMARY KEY,
    dedupe_key text NOT NULL UNIQUE,
    kind text NOT NULL CHECK (kind = 'foundation.noop'),
    state text NOT NULL DEFAULT 'pending'
        CHECK (state IN ('pending','running','done','dead')),
    attempts integer NOT NULL DEFAULT 0 CHECK (attempts >= 0),
    run_after timestamptz NOT NULL DEFAULT clock_timestamp(),
    lease_until timestamptz,
    lease_token uuid,
    last_error_type text,
    created_at timestamptz NOT NULL DEFAULT clock_timestamp()
);
CREATE INDEX jobs_claim_idx ON foundation.jobs(state, run_after);
CREATE TABLE foundation.probe_effects (
    job_id uuid PRIMARY KEY REFERENCES foundation.jobs(id),
    completed_at timestamptz NOT NULL DEFAULT clock_timestamp()
);
