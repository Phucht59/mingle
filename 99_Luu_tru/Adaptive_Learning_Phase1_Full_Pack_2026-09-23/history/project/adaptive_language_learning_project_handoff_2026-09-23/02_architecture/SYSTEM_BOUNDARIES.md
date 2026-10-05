# System Boundaries

## Learner client

Responsible for:

- user interaction;
- local/offline experience;
- durable local queuing;
- local rendering of version-pinned learning content;
- sending commands and telemetry.

Not authoritative for:

- final scoring;
- canonical progress;
- permissions;
- final content publication state.

## API/backend

Responsible for authoritative domain operations, validation, scoring, progress, permissions, command handling, and data access.

## Durable worker

Runs asynchronous/durable tasks from the same codebase as the API but as a separate process. It should support eventual processing without forcing premature external messaging infrastructure.

## Staff/admin web

Uses Flutter Web for content/staff/admin flows. Detailed capabilities are developed in later phases.
