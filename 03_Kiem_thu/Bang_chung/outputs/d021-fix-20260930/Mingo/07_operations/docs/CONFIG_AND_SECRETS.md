# Configuration and Secrets Convention

Purpose: reproducible settings without coupling policy hypotheses to hard-coded application logic. Names below are **conceptual**, not V3.2 contract keys.

| Category | Examples | Handling |
|---|---|---|
| Runtime | environment, API/worker mode, DB connection, object-store endpoint | Typed validation on startup, documented defaults for local only |
| Security | signing keys, DB password, storage credentials | Secret manager or local ignored env file; rotate; never commit or print |
| Learning policy | retry cap=1, Check play cap=2, default target=1 cycle, skip/error threshold=2, due insertion cap=1, target cycle≈5m | Versioned config; reviewed changes and deterministic test vectors; no direct alteration of scoring invariant |
| Observability | log level, tracing rate | Avoid learner answers, tokens, microphone or PII |
| Feature availability | ML/recommendation enabled, offline capability | Explicit disabled mode tested; no silent non-null model substitute |

Supply `.env.example` placeholders after inspecting repo, never actual secrets. Startup checks missing required config and fails with sanitized errors. Record policy version and effective relevant values on decisions so historical explanations remain reproducible. Owner/business signoff only if a parameter change modifies a frozen V3.2 business rule; otherwise use normal review and pilot evidence.
