# 07 — Security & Permission V3

## Server authority

Derived from verified auth:
- learner identity;
- role;
- object scope.

Client never authoritatively sets:
- learner ownership;
- score;
- progress;
- mastery;
- risk;
- server receive/availability timestamps.

## Object scopes

- learner: own enrollment/attempt/receipt/grant only;
- instructor/advisor: specifically assigned learners only;
- content admin: content operations, no default raw risk access;
- platform admin: privileged audited actions;
- worker: least privilege by job class.

## Offline grant authorization

Grant lookup checks:
- authenticated learner owner;
- enrollment;
- device installation/package;
- release hash;
- deadlines/revoke state.

A client-provided grant ID alone grants nothing.

## Receipt authorization

Receipt lookup:
- requires same authenticated learner;
- staff access only through staff-specific audited endpoint if later added.

## Telemetry context

Server validates context references:
- enrollment belongs to learner;
- activity revision belongs to enrollment's pinned release;
- media/hint belongs to referenced activity revision;
- recommendation exposure decision belongs to learner and is active/known.

Typed payload validation alone is insufficient.

## Supabase

- service-role/secret never in Flutter;
- authoritative business tables written through FastAPI;
- any direct Data API table requires explicit grants/RLS + tests.
