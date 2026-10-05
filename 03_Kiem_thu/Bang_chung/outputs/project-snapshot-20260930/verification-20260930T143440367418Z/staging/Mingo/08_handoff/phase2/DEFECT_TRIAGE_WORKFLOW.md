# Phase 2 Defect Triage Workflow

1. QA creates defect ID `P2-D###` and links failing test case/screen/component.
2. Record expected vs actual and governing source (V3.2, PRD, Phase 2 spec).
3. Assign severity P0–P3 using `QA_DEFECT_SEVERITY.md`.
4. Owner/Tech Lead decides: fix, accepted minor defer, duplicate, or specification issue.
5. Frozen-rule conflict cannot be resolved by design preference; open Implementation Issue/CR when needed.
6. Fix produces new candidate revision/package; update changelog.
7. QA retests failing case plus regression set for affected area.
8. Close only with evidence link and reviewer.
