-- V3.2 reference core migration, PostgreSQL-compatible.
-- Auth/JWT, RLS/grants, content publication and atomic command handler remain
-- application responsibilities. Execute only in a new isolated schema/database.
CREATE TABLE learner (learner_id uuid PRIMARY KEY);
CREATE TABLE course_release (
 course_release_id uuid PRIMARY KEY,
 manifest_sha256 text NOT NULL CHECK (manifest_sha256 ~ '^[a-f0-9]{64}$'),
 eligible_activity_count integer NOT NULL CHECK (eligible_activity_count>=1),
 UNIQUE(course_release_id,eligible_activity_count)
);
CREATE TABLE enrollment (
 enrollment_id uuid PRIMARY KEY, learner_id uuid NOT NULL REFERENCES learner,
 course_release_id uuid NOT NULL REFERENCES course_release,
 UNIQUE(enrollment_id,learner_id,course_release_id)
);
CREATE TABLE activity_revision (
 activity_revision_id uuid PRIMARY KEY, scoring_version_id uuid NOT NULL,
 question_count integer NOT NULL CHECK(question_count BETWEEN 1 AND 100),
 UNIQUE(activity_revision_id,scoring_version_id,question_count)
);
CREATE TABLE release_activity (
 release_activity_id uuid PRIMARY KEY,
 course_release_id uuid NOT NULL REFERENCES course_release,
 activity_revision_id uuid NOT NULL REFERENCES activity_revision,
 required_for_completion boolean NOT NULL,
 UNIQUE(release_activity_id,course_release_id,activity_revision_id),
 UNIQUE(release_activity_id,course_release_id,required_for_completion)
);
CREATE TABLE question_option (
 activity_revision_id uuid NOT NULL REFERENCES activity_revision,
 question_revision_id uuid NOT NULL, option_id text NOT NULL CHECK(length(option_id)>0),
 is_correct boolean NOT NULL,
 PRIMARY KEY(activity_revision_id,question_revision_id,option_id)
);
-- Publish validator requires exactly one correct option and >=2 options per question.
CREATE UNIQUE INDEX at_most_one_correct_option
 ON question_option(activity_revision_id,question_revision_id) WHERE is_correct;
CREATE TABLE command_receipt (
 receipt_id uuid PRIMARY KEY,learner_id uuid NOT NULL REFERENCES learner,
 command_id uuid NOT NULL,command_type text NOT NULL CHECK(command_type='submit_attempt_v1'),
 digest_version text NOT NULL CHECK(digest_version='command_digest_v1'),
 payload_digest text NOT NULL CHECK(payload_digest ~ '^[a-f0-9]{64}$'),
 terminal_outcome text NOT NULL CHECK(terminal_outcome IN ('accepted','rejected')),
 reason_code text,recorded_at timestamptz NOT NULL,canonical_result jsonb,
 UNIQUE(learner_id,command_id),UNIQUE(receipt_id,learner_id),
 CHECK((terminal_outcome='accepted' AND canonical_result IS NOT NULL AND
        jsonb_typeof(canonical_result)='object' AND reason_code IS NULL)
    OR (terminal_outcome='rejected' AND length(reason_code)>0 AND canonical_result IS NULL))
);
CREATE TABLE attempt (
 attempt_id uuid PRIMARY KEY,learner_id uuid NOT NULL,enrollment_id uuid NOT NULL,
 course_release_id uuid NOT NULL,release_activity_id uuid NOT NULL,activity_revision_id uuid NOT NULL,
 receipt_id uuid NOT NULL,attempt_state text NOT NULL CHECK(attempt_state='finalized'),
 attempt_revision bigint NOT NULL CHECK(attempt_revision=1),occurred_at timestamptz NOT NULL,
 created_at timestamptz NOT NULL,
 FOREIGN KEY(enrollment_id,learner_id,course_release_id) REFERENCES enrollment(enrollment_id,learner_id,course_release_id),
 FOREIGN KEY(release_activity_id,course_release_id,activity_revision_id) REFERENCES release_activity(release_activity_id,course_release_id,activity_revision_id),
 FOREIGN KEY(receipt_id,learner_id) REFERENCES command_receipt(receipt_id,learner_id) DEFERRABLE INITIALLY DEFERRED,
 UNIQUE(receipt_id),UNIQUE(attempt_id,activity_revision_id),
 UNIQUE(attempt_id,enrollment_id,release_activity_id,course_release_id)
);
CREATE TABLE answer_submission (
 attempt_id uuid NOT NULL,activity_revision_id uuid NOT NULL,question_revision_id uuid NOT NULL,option_id text NOT NULL,
 PRIMARY KEY(attempt_id,question_revision_id),
 FOREIGN KEY(attempt_id,activity_revision_id) REFERENCES attempt(attempt_id,activity_revision_id),
 FOREIGN KEY(activity_revision_id,question_revision_id,option_id) REFERENCES question_option
);
CREATE TABLE scoring_record (
 scoring_record_id uuid PRIMARY KEY,attempt_id uuid NOT NULL,activity_revision_id uuid NOT NULL,
 scoring_record_revision bigint NOT NULL CHECK(scoring_record_revision>=1),
 scoring_version_id uuid NOT NULL,raw_score integer NOT NULL CHECK(raw_score>=0),
 max_score integer NOT NULL CHECK(max_score>0),
 score_fraction numeric GENERATED ALWAYS AS (raw_score::numeric/max_score) STORED,
 recorded_at timestamptz NOT NULL,
 FOREIGN KEY(attempt_id,activity_revision_id) REFERENCES attempt(attempt_id,activity_revision_id),
 FOREIGN KEY(activity_revision_id,scoring_version_id,max_score) REFERENCES activity_revision(activity_revision_id,scoring_version_id,question_count),
 UNIQUE(attempt_id,scoring_record_revision),CHECK(raw_score<=max_score)
);
-- Pilot credits only REQUIRED activities. Optional attempts are scored but
-- create no credit and do not increment progress revision/count.
CREATE TABLE completion_credit (
 completion_credit_id uuid PRIMARY KEY,enrollment_id uuid NOT NULL,
 release_activity_id uuid NOT NULL,course_release_id uuid NOT NULL,
 required_for_completion boolean NOT NULL DEFAULT true CHECK(required_for_completion),
 first_attempt_id uuid NOT NULL,credited_at timestamptz NOT NULL,
 FOREIGN KEY(first_attempt_id,enrollment_id,release_activity_id,course_release_id)
   REFERENCES attempt(attempt_id,enrollment_id,release_activity_id,course_release_id),
 FOREIGN KEY(release_activity_id,course_release_id,required_for_completion)
   REFERENCES release_activity(release_activity_id,course_release_id,required_for_completion),
 UNIQUE(enrollment_id,release_activity_id)
);
CREATE TABLE progress_state (
 enrollment_id uuid PRIMARY KEY,learner_id uuid NOT NULL,course_release_id uuid NOT NULL,
 progress_revision bigint NOT NULL CHECK(progress_revision>=0),
 completed_required_credit_count integer NOT NULL DEFAULT 0 CHECK(completed_required_credit_count>=0),
 eligible_activity_count integer NOT NULL CHECK(eligible_activity_count>=1),
 completion_fraction numeric GENERATED ALWAYS AS (completed_required_credit_count::numeric/eligible_activity_count) STORED,
 updated_at timestamptz NOT NULL,
 FOREIGN KEY(enrollment_id,learner_id,course_release_id) REFERENCES enrollment(enrollment_id,learner_id,course_release_id),
 FOREIGN KEY(course_release_id,eligible_activity_count) REFERENCES course_release(course_release_id,eligible_activity_count),
 CHECK(completed_required_credit_count<=eligible_activity_count)
);
CREATE TABLE offline_download_grant (
 grant_id uuid PRIMARY KEY,learner_id uuid NOT NULL,enrollment_id uuid NOT NULL,course_release_id uuid NOT NULL,
 device_installation_id text NOT NULL CHECK(length(device_installation_id)>0),package_id uuid NOT NULL UNIQUE,
 release_manifest_sha256 text NOT NULL CHECK(release_manifest_sha256 ~ '^[a-f0-9]{64}$'),
 issued_at timestamptz NOT NULL,learn_until timestamptz NOT NULL,upload_until timestamptz NOT NULL,revoked_at timestamptz,
 FOREIGN KEY(enrollment_id,learner_id,course_release_id) REFERENCES enrollment(enrollment_id,learner_id,course_release_id),
 CHECK(issued_at<learn_until AND learn_until<upload_until),CHECK(revoked_at IS NULL OR revoked_at>=issued_at)
);
CREATE TABLE outbox_message (
 outbox_message_id uuid PRIMARY KEY,receipt_id uuid REFERENCES command_receipt,
 message_type text NOT NULL,aggregate_type text NOT NULL,aggregate_id text NOT NULL,
 payload jsonb NOT NULL,created_at timestamptz NOT NULL
);
CREATE TABLE durable_job (
 job_id uuid PRIMARY KEY,outbox_message_id uuid REFERENCES outbox_message,
 handler_type text NOT NULL,handler_version text NOT NULL,logical_effect_key text NOT NULL,
 status text NOT NULL CHECK(status IN ('pending','leased','completed','dead')),
 lease_owner text,lease_generation bigint NOT NULL DEFAULT 0 CHECK(lease_generation>=0),lease_until timestamptz,
 available_at timestamptz NOT NULL,attempt_count integer NOT NULL DEFAULT 0 CHECK(attempt_count>=0),
 max_attempts integer NOT NULL DEFAULT 8 CHECK(max_attempts>0),last_error text,created_at timestamptz NOT NULL,updated_at timestamptz NOT NULL,
 UNIQUE(outbox_message_id,handler_type,handler_version),UNIQUE(handler_type,handler_version,logical_effect_key),
 CHECK(status<>'leased' OR (lease_owner IS NOT NULL AND lease_until IS NOT NULL AND lease_generation>0))
);
CREATE INDEX job_pending ON durable_job(available_at) WHERE status='pending';
CREATE TABLE evidence_publication (
 evidence_publication_id uuid PRIMARY KEY,learner_id uuid NOT NULL REFERENCES learner,enrollment_id uuid REFERENCES enrollment,
 source_type text NOT NULL,source_id text NOT NULL,source_revision bigint NOT NULL CHECK(source_revision>=1),
 source_occurred_at timestamptz,published_available_at timestamptz NOT NULL,
 payload_sha256 text NOT NULL CHECK(payload_sha256 ~ '^[a-f0-9]{64}$'),created_at timestamptz NOT NULL,
 UNIQUE(learner_id,source_type,source_id,source_revision)
);
CREATE TABLE recommendation_decision_identity (
 decision_id uuid PRIMARY KEY,learner_id uuid NOT NULL REFERENCES learner,
 UNIQUE(decision_id,learner_id)
);
CREATE TABLE recommendation_exposure (
 exposure_id uuid NOT NULL,learner_id uuid NOT NULL,decision_id uuid NOT NULL,
 exposed_at timestamptz NOT NULL,surface text NOT NULL,
 PRIMARY KEY(learner_id,exposure_id),
 FOREIGN KEY(decision_id,learner_id) REFERENCES recommendation_decision_identity(decision_id,learner_id)
);
-- Prevent normal mutation of accepted history. Controlled deletion remains
-- an audited privileged workflow; DELETE is intentionally not blocked here.
CREATE FUNCTION forbid_history_update() RETURNS trigger LANGUAGE plpgsql AS $$
BEGIN RAISE EXCEPTION 'immutable history: create a new revision' USING ERRCODE='23514'; END $$;
CREATE TRIGGER attempt_immutable BEFORE UPDATE ON attempt FOR EACH ROW EXECUTE FUNCTION forbid_history_update();
CREATE TRIGGER answer_immutable BEFORE UPDATE ON answer_submission FOR EACH ROW EXECUTE FUNCTION forbid_history_update();
CREATE TRIGGER score_immutable BEFORE UPDATE ON scoring_record FOR EACH ROW EXECUTE FUNCTION forbid_history_update();
CREATE TRIGGER receipt_immutable BEFORE UPDATE ON command_receipt FOR EACH ROW EXECUTE FUNCTION forbid_history_update();
CREATE TRIGGER credit_immutable BEFORE UPDATE ON completion_credit FOR EACH ROW EXECUTE FUNCTION forbid_history_update();
-- Validate accepted submission completeness at COMMIT, allowing all rows to be
-- inserted within one transaction and rejecting partial accepted state.
CREATE FUNCTION check_accepted_receipt() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE a attempt;expected integer;got integer;computed integer;stored integer;
BEGIN
 IF NEW.terminal_outcome='accepted' THEN
  SELECT * INTO a FROM attempt WHERE receipt_id=NEW.receipt_id;
  IF NOT FOUND THEN RAISE EXCEPTION 'accepted receipt requires attempt' USING ERRCODE='23514'; END IF;
  SELECT question_count INTO expected FROM activity_revision WHERE activity_revision_id=a.activity_revision_id;
  SELECT count(*),coalesce(sum(CASE WHEN qo.is_correct THEN 1 ELSE 0 END),0)
    INTO got,computed FROM answer_submission ans JOIN question_option qo USING(activity_revision_id,question_revision_id,option_id)
    WHERE ans.attempt_id=a.attempt_id;
  SELECT raw_score INTO stored FROM scoring_record WHERE attempt_id=a.attempt_id AND scoring_record_revision=1;
  IF got<>expected OR stored IS NULL OR computed<>stored THEN
   RAISE EXCEPTION 'accepted attempt needs exact answers and correct score' USING ERRCODE='23514'; END IF;
  IF EXISTS(SELECT 1 FROM release_activity WHERE release_activity_id=a.release_activity_id AND required_for_completion)
    AND NOT EXISTS(SELECT 1 FROM completion_credit WHERE enrollment_id=a.enrollment_id AND release_activity_id=a.release_activity_id) THEN
   RAISE EXCEPTION 'required activity needs completion credit' USING ERRCODE='23514'; END IF;
  IF NOT EXISTS(SELECT 1 FROM outbox_message WHERE receipt_id=NEW.receipt_id) THEN
   RAISE EXCEPTION 'accepted receipt requires outbox' USING ERRCODE='23514'; END IF;
 ELSE
  IF EXISTS(SELECT 1 FROM attempt WHERE receipt_id=NEW.receipt_id) THEN
   RAISE EXCEPTION 'rejected receipt cannot own attempt' USING ERRCODE='23514'; END IF;
 END IF;
 RETURN NULL;
END $$;
CREATE CONSTRAINT TRIGGER accepted_receipt_complete AFTER INSERT ON command_receipt
 DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION check_accepted_receipt();
-- A deferred count guard catches forgotten or duplicate progress effects.
CREATE FUNCTION check_progress_credit_count() RETURNS trigger LANGUAGE plpgsql AS $$
DECLARE eid uuid;actual bigint;stored integer;
BEGIN
 eid=NEW.enrollment_id;
 SELECT completed_required_credit_count INTO stored FROM progress_state WHERE enrollment_id=eid;
 SELECT count(*) INTO actual FROM completion_credit WHERE enrollment_id=eid;
 IF stored IS NULL OR actual<>stored THEN RAISE EXCEPTION 'progress/credit count mismatch' USING ERRCODE='23514'; END IF;
 RETURN NULL;
END $$;
CREATE CONSTRAINT TRIGGER credit_progress_match AFTER INSERT ON completion_credit
 DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION check_progress_credit_count();
CREATE CONSTRAINT TRIGGER progress_credit_match AFTER INSERT OR UPDATE ON progress_state
 DEFERRABLE INITIALLY DEFERRED FOR EACH ROW EXECUTE FUNCTION check_progress_credit_count();
-- Normative application transaction pseudocode is in docs/14_SUBMIT_ALGORITHM.md.
-- Seed/publish adapters must validate manifest, question count, answer-key
-- completeness and access/grant ownership before writing immutable content.
