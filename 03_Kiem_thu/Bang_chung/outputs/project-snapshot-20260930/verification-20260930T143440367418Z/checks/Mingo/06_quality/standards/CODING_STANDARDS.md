# Coding Standards — Phase 1

- Keep modular-monolith domain boundaries explicit; import through public module interfaces, avoid circular calls and duplicate canonical state.
- Make server transaction and idempotency boundaries visible in code review. A telemetry delivery failure must not silently change authoritative score or progress; scoring cannot trust client timestamps/results without validation.
- Use typed Python/FastAPI settings, request/response validation and explicit errors; use Flutter state management consistent with the actual repo. Avoid dict/stringly event types when a typed/validated alternative exists.
- Name events by observable action (`answer_submitted`, `hint_viewed`) rather than inferred trait (`learner_careless`). Distinguish event time and known-at time; use timezone-aware timestamps.
- Version content and policy; store reason codes and underlying evidence references. Separate mastery, risk and recommendation; never compute these from streak by convenience.
- Review migrations, permissions, immutable content, idempotency and replay paths with tests. No secrets or raw sensitive answers in logs; no free-text diagnostics identifying learners.
- Format/lint/type check changed code and run focused tests; include reason for any exception. Do not add distributed infra without a measured need and owner-reviewed architecture change.

These are contribution guidelines, not a substitute for the original V3.2 coding/contracts or current repo style. Resolve a real disagreement by authority and a documented issue.
