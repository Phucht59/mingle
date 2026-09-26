# Change Requests

**No Change Request is open as of 2026-09-26.** Research and runtime implementation did not prove a contradiction with available V3.2 summaries. The missing exact package is Implementation Issue II-01. Database naming and Windows/Flutter tooling fixes preserve architecture and business semantics.

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
