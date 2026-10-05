# Prototype — Rework R1

Open `prototype/index.html` directly or serve the directory with a local HTTP server. No CDN/network resource is required.

The prototype now includes:
- executable first-use + optional placement;
- Vocabulary, Grammar and Listening representative finite cycles;
- required-response validation, bounded retry and persistent assisted state;
- explicit offline queue/sync/ack/failure/partial/re-auth/canonical-refresh states;
- locked-objective preview with no progress side effect;
- full staff Draft → Preview → Review → provenance fix → Approve → Publish Confirmation → immutable Published → New Draft path;
- targeted live regions, route-heading focus and modal focus restore;
- stable `data-screen-id` / `data-testid` hooks.

Top controls are test-only. “Simulate offline” changes connectivity only; it deliberately does **not** produce a synced state when queued work exists.

This remains mock-only Phase 2 UX behavior, not production Flutter/FastAPI logic.
