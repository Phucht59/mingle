# Staff/Admin Journeys

These journeys define Phase 2 IA/UX only. Authentication is Phase 3; content backend is Phase 4; interventions/analytics/admin domain implementation occurs later.

## J-S01 — Content authoring and review

Content Library → Create Draft → Draft Editor → Source & License → Preview → Submit for Review → Review Queue → Review Detail → Approve/Request Changes → Publish Confirmation → Published Revision.

Published content is visually immutable. Further changes start a new draft/revision; old attempts remain pinned to historical revision.

## J-S02 — License/provenance block

Draft → missing/invalid source/license → review/publish gate is blocked with explicit reason → author fixes provenance → resubmit. “Publicly accessible” is never treated as sufficient reuse permission.

## J-S03 — Learner support

Learners → search assigned learner → Overview → Evidence / Activity → future intervention entry. Evidence language separates learning from engagement and uncertainty; no unobserved mental-state diagnosis.

## J-S04 — Future intervention audit

Interventions → detail shows recommendation reason/evidence and later lifecycle sections Decision → Exposure → Execution → Outcome. Phase 2 deliberately avoids implying these records already exist.

## J-S05 — Analytics shell

Analytics → metric cards/table → metric detail shows definition, time window/cohort/source context. No invented production metric values are required in the prototype.

## J-S06 — Administration shell

Administration → Roles & Permissions / Audit. UI visibility never substitutes server authorization; privileged operations are designed for explicit confirmation and audit.


## Rework R1 executable publication path

The reference prototype now exercises `Draft Editor → Preview → Review (license blocked) → Source & License → Review (approvable) → Publish Confirmation → Immutable Published Revision → Create New Draft`. Request Changes returns a reviewer note to the draft. No published revision exposes direct Edit.
