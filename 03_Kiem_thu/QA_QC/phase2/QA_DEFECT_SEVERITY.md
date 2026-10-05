# Phase 2 Defect Severity and Triage

| Severity | Meaning | Example | Exit rule |
|---|---|---|---|
| P0 Blocker | Candidate cannot be accepted or contradicts frozen rule | Skip shown as completion; Check has hint; core prototype cannot proceed | Must fix |
| P1 Major | Mandatory UX/state/traceability missing or misleading | queued shown as synced; published revision editable; keyboard cannot reach primary staff action | Must fix |
| P2 Minor | Workaround exists; non-core inconsistency | secondary responsive wrapping, inconsistent non-critical copy | Can defer only with explicit acceptance |
| P3 Polish | Cosmetic/no semantic impact | spacing/alignment micro-polish | May defer |

Triage fields: defect ID, test case, screen/component, expected, actual, severity, owner, decision, fix commit/package, retest evidence. Never close as “works as designed” without linking the governing rule/spec.
