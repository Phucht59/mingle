# Quality, Security, and Runtime Principles

## Schema pass != runtime pass

The project explicitly rejects treating schema/contract validation as proof of runtime correctness.

Implementation requires tests for:

- integration flows;
- transactional behavior;
- concurrency;
- offline replay/idempotency;
- permissions/security;
- version pinning;
- asynchronous worker behavior;
- failure recovery.

## Product resilience

Core learning must continue to function when:

- ML is disabled;
- recommendation is disabled;
- asynchronous intelligence is temporarily unavailable.

## Scale discipline

Do not introduce distributed infrastructure before a measurable requirement justifies it.
