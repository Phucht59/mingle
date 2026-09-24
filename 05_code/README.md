# Code workspace

Executable source only.

- `backend/`: FastAPI API + durable worker in one Python codebase, PostgreSQL migrations, storage adapter, tests.
- `apps/learner/`: Flutter learner shell (Android-first; iOS-compatible direction).
- `apps/staff/`: Flutter Web staff/admin shell.
- `compose.yaml`: local PostgreSQL + migrate + API + worker stack.
- `.env.example`: local configuration template.

Do not place research notes, decision records or evidence in this folder.
