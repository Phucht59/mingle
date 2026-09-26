# Implementation Issues — 2026-09-26

| ID | Issue | Status / resolution |
|---|---|---|
| II-01 | Exact V3.2 package, original DDL/OpenAPI and 115+22 verification source absent | **OPEN / BLOCKING exact mapping and gate**. Exhaustive active/archive/nested-ZIP/history/bundle search found historical claims and placeholders only. Do not recreate or substitute the original suite |
| II-02 | MVP learning hypotheses could be mistaken for frozen scoring/architecture | **OPEN / NON-BLOCKING**. Keep domain/scoring implementation contract-driven |
| II-03 | Offline Check/placement audio replay authority | **OPEN / depends on II-01**. Playback telemetry is not canonical score evidence and cannot prove listens |
| II-04 | PostgreSQL/container runtime not evidenced | **RESOLVED 2026-09-26 locally**. `mingo_app`, `mingo`, and `mingo_test` provisioned with SCRAM; 6/6 PostgreSQL tests, migrations, worker probe and API readiness pass |
| II-05 | Flutter runtime not evidenced | **RESOLVED 2026-09-26 locally**. Flutter 3.32.8 analyze/test/build plus actual Android emulator and Chrome boot pass. Hosted Linux build remains part of II-06 |
| II-06 | No hosted Git CI evidence | **FOUNDATION CI RESOLVED 2026-09-26**. Run `36250667211` passes backend and both Flutter jobs. Overall CI remains blocked solely by II-01; clean reproduction is recorded separately |
| II-07 | Previous delivery split active source outside the Full Pack while its index referred to `source/` inside the pack | **RESOLVED 2026-09-24** by canonical repository layout + preserved archive/provenance |
| II-08 | Previous source bundle exported only `HEAD`, causing detached-HEAD clone behavior | **RESOLVED 2026-09-24** in the canonical handoff bundle with named `main` |
| II-09 | Local immutable storage adapter used POSIX-only directory flags and mishandled Windows resolved paths | **RESOLVED 2026-09-26**; 9 focused tests pass. Windows symlink privilege skip remains covered by capable hosted Linux CI |
| II-10 | Supplied `Mingo (2).zip` packages `.git`, `.venv`, `.local`, caches/builds and duplicate nested history | **RESOLVED 2026-09-26**. `git archive` export inspected: no runtime/cache/secret directories; ZIP integrity passes. Historical supplied ZIP retained unchanged |
| II-11 | Flutter bootstrap preserved authored manifests while generated analyzer policy required undeclared `flutter_lints` | **RESOLVED 2026-09-26** by pinning template-compatible `flutter_lints` 5.x and committing application locks/analyzer policy |
| II-12 | Windows user profile with Unicode characters broke Java Unix-domain temp sockets and AVD file handling | **RESOLVED 2026-09-26 locally** with repository-local ASCII Java temp and ASCII Android SDK/AVD paths; documented for reproduction |
| II-13 | GitHub runner split single-quoted PostgreSQL Docker health command into flags | **RESOLVED 2026-09-26** in `4cdecb4`: double-quoted health command; hosted backend rerun passes with all assertions retained |
| II-14 | Backend-only clean setup required an undocumented DATABASE_URL for storage smoke | **RESOLVED 2026-09-26** in `6cf9a1b`: verifier supplies a non-connecting placeholder only for storage; fresh clone without `.env` passes |

No demonstrated V3.2 business-rule conflict. **No Change Request is open.**
