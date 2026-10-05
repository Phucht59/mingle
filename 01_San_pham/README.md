# Code workspace

Executable source only.

- `backend`: FastAPI API + durable worker in one Python codebase, PostgreSQL migrations, storage adapter, tests.
- `apps/learner`: Flutter learner Phase2 presentation (Android-first; iOS-compatible direction).
- `apps/staff`: Flutter Web staff/admin Phase2 presentation.
- `cong_cu_phat_trien/mingo_ui`: shared design, assets, activity fixtures and presentation tests.
- `compose.yaml`: local PostgreSQL + migrate + API + worker stack.
- `.env.example`: local configuration template.

Flutter platform host files are intentionally generated with the pinned SDK rather than
stored as authored product source. Run `04_Van_hanh/Scripts/bootstrap_clients.ps1` on
Windows or `bootstrap_clients.sh` on Linux before Flutter verification. The app manifests,
dependency locks, analyzer policy, `lib/`, and tests remain tracked.

Do not place research notes, decision records or evidence in this folder.

Both apps use explicit sample data for Human Review. Auth, server scoring/progress,
durable offline queues and production services remain future approved phases.
See the current V2 design/handoff under `02_Tai_lieu_du_an/04_Thiet_ke_san_pham/ux_ui/phase2/rebaseline_v2`.
