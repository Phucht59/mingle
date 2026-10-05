# Change Requests

**No Change Request is open as of 2026-09-26.** Research, runtime verification and exact V3.2 source mapping did not demonstrate a frozen-contract contradiction. II-01 is resolved by verified original source intake; II-03 is resolved at the authority-mapping boundary. Database naming and Windows/Flutter tooling fixes preserve architecture and business semantics.

Create a CR only when a cited original frozen rule/business contract is demonstrably incompatible with a necessary behavior. Required template:

1. CR ID, status `DRAFT / OWNER APPROVED / REJECTED / IMPLEMENTED`.
2. Exact current V3.2 rule ID/file/version and reproduction of conflict.
3. Evidence and why preserving the rule cannot solve it.
4. Minimal proposed change and alternatives evaluated.
5. User behavior, security, offline, score, content-version and analytics impacts.
6. Schema/API/migration/backward compatibility plan.
7. Blocking vs deferrable decision, verification tests and rollout/rollback.
8. Explicit owner approval before altering the frozen rule.

Do not use a CR to rename modules, change formatting or optimize hypothetical scale. Record such work as normal tickets if semantics are preserved.

## Candidate CR-GD1-001 — Account lifecycle scope and business baseline

- **Problem:** Audit AUD-005 finds no complete BA chain for signup/login/logout/recovery/session/device change/account state/deletion/export. Engineering Phase3 deferral does not decide MVP business scope.
- **Current baseline:** V3.2 docs/07 fixes identity/object authorization; docs/10 fixes deletion/export/restore generation controls. PRD-10 covers goal/profile, not the complete account lifecycle. No demonstrated contradiction in V3.2 is asserted.
- **Requested change:** Resolve inclusion/defer status and record minimal actor/trigger/state/failure/acceptance for each lifecycle operation. Keep sensitive policy choices (recovery verification, session/device behavior, deletion/export timing) explicitly pending until decided. This is a candidate business-scope decision, not architecture redesign.
- **Reconciliation first:** Inspect the missing actual BA workbook before seeking a new decision. If it already contains approved lifecycle scope/rules, map those sources and close this candidate as NOT REQUIRED. Do not reopen approved decisions merely because they are absent from the current repository inspection.
- **Reason:** Internal BA handoff cannot leave identity and data-rights behavior undefined.
- **Affected artifacts:** Actual GĐ1 workbook sheets03/04/05/06/07/08/12/14/15 (currently NOT FOUND); PRD, account BA appendix, actor/privacy intent, traceability and new snapshot.
- **Affected contracts:** V3.2 docs/07/docs/10 and later identity API/schema versions if required. Existing originals remain unchanged.
- **Backward compatibility:** No implemented production account route exists in the inspected API. Any later schema/API change must be versioned and assessed; no compatibility waiver is approved here.
- **Risk:** Unknown lifecycle scope could permit inconsistent ownership, loss of pending work or unsafe export/deletion handling. Arbitrary retention/session rules must not be invented.
- **Decision owner:** Product Owner with Tech Lead and privacy reviewer for applicable policies.
- **Status:** **DRAFT / CHƯA QUYẾT ĐỊNH, 2026-10-05**. Not an approved V3.2 amendment. Gate blocking for missing BA specification, not for absent auth implementation.

## Candidate CR-GD1-002 — Optional goal and truthful first Home fixture

- **Problem:** AUD-009/AUD-010: the preview initializes a goal without learner selection; Goal has no explicit skip/missing state. Ordinary first Home passes due=true and does not wire hasResume to its reason/primary action.
- **Current baseline:** Approved optional/editable preference and truthful next action; J-L01/J-L12, PRD-10/13/16. Exact Home ranking and goal categories remain hypotheses. Fixture disclosure remains mandatory.
- **Requested change:** In a later targeted presentation task, represent missing/skipped/selected goal distinctly and show first-use/returning-valid-resume/due/no-eligible states with their truthful reason and action. Keep persistence of actual commands, eligibility and scoring on future server adapters. Do not change numerical policies or freeze candidate Home ranking.
- **Reason:** A passing helper test does not prove the named flow is represented by the UI.
- **Affected artifacts:** `fixtures.dart`, `learner.dart`, first-use/returning journey, goal/Home state catalogue, targeted tests, screenshots/goldens and BA trace once supplied.
- **Affected contracts:** No V3.2 change proposed. Review any future user-preference schema and source boundary separately.
- **Backward compatibility:** Current sample fixture only; no production preference data migration. Golden/technical candidate evidence must be regenerated after authorized UI work, preserving historical runs.
- **Risk:** A guessed goal or unsupported due claim may misrepresent user intent/evidence. Introducing a fixed ranking would prematurely freeze a hypothesis.
- **Decision owner:** Product Owner for product-state disposition; implementation owner/Tech Lead for targeted rework and verification.
- **Status:** **DRAFT / CHƯA QUYẾT ĐỊNH, 2026-10-05**. No code changed by this audit; non-blocking implementation debt for GĐ1 because approved business principles already exist.
