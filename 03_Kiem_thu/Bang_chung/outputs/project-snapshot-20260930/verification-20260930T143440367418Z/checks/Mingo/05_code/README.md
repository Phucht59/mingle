# Code workspace

Executable source only.

- `backend/`: FastAPI API + durable worker in one Python codebase, PostgreSQL migrations, storage adapter, tests.
- `apps/learner/`: Flutter learner shell (Android-first; iOS-compatible direction).
- `apps/staff/`: Flutter Web staff/admin shell.
- `compose.yaml`: local PostgreSQL + migrate + API + worker stack.
- `.env.example`: local configuration template.

Flutter platform host files are intentionally generated with the pinned SDK rather than
stored as authored product source. Run `07_operations/scripts/bootstrap_clients.ps1` on
Windows or `bootstrap_clients.sh` on Linux before Flutter verification. The app manifests,
dependency locks, analyzer policy, `lib/`, and tests remain tracked.

Do not place research notes, decision records or evidence in this folder.
