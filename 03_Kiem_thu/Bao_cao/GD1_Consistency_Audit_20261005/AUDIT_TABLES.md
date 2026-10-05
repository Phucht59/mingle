# Consistency, traceability và decision tables — 05/10/2026

Labels: PROJECT SOURCE = artifact đã kiểm tra; EXECUTABLE EVIDENCE = actual run; EXTERNAL EVIDENCE = nguồn ngoài; INFERENCE = mapping có căn cứ; HYPOTHESIS = policy chưa validated; VALIDATION DEBT = external evidence chưa đủ. UNKNOWN/NOT FOUND/NOT EXECUTED không là PASS.

## Consistency Matrix

| Area | V3.2 | Workbook | Snapshot | Repo | Status | Finding IDs |
| --- | --- | --- | --- | --- | --- | --- |
| Architecture | docs01: frozen modular monolith | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | README, API/worker và stack khớp | PASS trong repo; workbook UNKNOWN | AUD-001,AUD-002 |
| Authority | docs01/02/07: server score/progress/permission | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Compatibility map; API health; UI sample disclosed | CONTRACT VERIFIED; domain runtime chưa chạy | AUD-001,AUD-011 |
| Content versioning | docs02/04: immutable/pinned release/revision | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | PRD14; staff draft/review/publish/new draft | SPEC CONSISTENT; permissions triển khai sau | AUD-001,AUD-004 |
| Learning evidence | Finalized attempt immutable; telemetry observational | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | PRD02–04/Evidence; first/hint/skip tests | SPEC+FIXTURE VERIFIED; chưa full domain | AUD-001,AUD-008,AUD-011 |
| Assessment | Full answer set; không offline canonical scoring | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Optional/provisional placement; retry new attempt theo mapping | SPEC CONSISTENT; metadata conditions triển khai sau | AUD-001,AUD-011 |
| Offline | docs03/04: durable IDs, receipts, grants, revision | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | UX states đúng; chưa durable mobile queues | CONTRACT VERIFIED / RUNTIME NOT YET VERIFIED | AUD-001,AUD-011 |
| Telemetry | Observation; server validates object context | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Purpose register; collection disabled | SPEC CONSISTENT; collection NOT RUN | AUD-006,AUD-011 |
| Analytics | docs05: exact captured membership/read view | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Compatibility map; không timestamp-only replay | CONTRACT VERIFIED; runtime capture chưa chạy | AUD-001,AUD-011 |
| Recommendation | docs09: Decision/Exposure/Execution/Outcome | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | PRD13/16; first Home/resume wiring gap | PARTIAL: spec đúng, fixture drift | AUD-010 |
| ML optionality | Optional risk; candidate model fixtures | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | PRD16/IV05; research datasets tách production | PASS principle/fixture; ML efficacy UNKNOWN | AUD-011 |
| Privacy | docs07/10: scope/generation/restore | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Purpose/minimization + new notes; account flow thiếu | PARTIAL; chưa thấy blocking legal contradiction | AUD-005,AUD-006 |
| Actor | docs07 object scopes | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | New role intent notes; assignment/segregation pending | FIXED repo intent; workbook UNKNOWN | AUD-004,AUD-001 |
| Account | Identity/delete/export technical boundaries | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Profile/preferences/reauth; chưa complete lifecycle BA | FAIL BA evidence completeness | AUD-005,AUD-001 |
| Staff/content | Content admin scope; immutable publish/access state | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | J-S01/02;S030–037; license/review test | SPEC+FIXTURE VERIFIED; actual server permissions sau | AUD-004,AUD-011 |
| NFR | Reliability/security/integrity/restore rules | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | Accessibility/performance/offline specs + checklist | FIXED consolidation; runtime pending | AUD-006 |
| Scope | Frozen types/action catalog; không new infra | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | 7 future staff routes; account scope chưa rõ | PARTIAL; không demonstrated architecture defect | AUD-003,AUD-005 |
| Traceability | Exact compatibility matrix có | NOT FOUND | 04/10 NOT FOUND; new05/10 records limit | 16PRD→screen/QA; workbook BR/UC/priorities chưa verified | FAIL full internal closure evidence | AUD-001,AUD-003 |

## Traceability Audit — toàn bộ16 repository PRDs

BR/Trigger/UC mappings dưới đây là INFERENCE dựa trên rule text và journey/flow có nguồn, không dựng workbook IDs. Text node phù hợp có thể đủ; không bắt buộc mọi node là artifact/screen riêng. P0 QA anchors được xếp trước PRD06 có P1 QA; **actual requirement priority UNKNOWN**, nên chưa certify toàn bộ workbook P0/P1.

| Requirement | BR | Trigger | UC/Flow | Screen/State | Acceptance/Test | Result | Gap |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PRD-01; req priority UNKNOWN; QA P0,P1 | Finite cycle, closure, opt-in; PRD01/Feed§3,7 | Start/continue lesson | J-L01/J-L03;Feed§3–7 | L-020,L-021,L-022,L-023,L-024,L-025,L-026,L-027,L-032 | Không infinite feed/forced timer; presentation tests; QA-LRN-001,QA-LRN-002,QA-LRN-012,QA-LRN-021 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Workbook/priority UNKNOWN; valid content runtime triển khai sau |
| PRD-02; req priority UNKNOWN; QA P0,P1 | Giữ first response; retry sau finalize dùng new attempt; V3docs02§5 | Wrong→feedback→retry | J-L04 | L-024,L-029 | First wrong còn nguyên sau correct retry; fixture test/IV01; QA-LRN-006,QA-LRN-007 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Condition schema/runtime deferred; không overwrite first response |
| PRD-03; req priority UNKNOWN; QA P0 | Assisted!=unaided; Check không pre-submit hint; Evidence§2/4 | Request hint / enter Check | J-L05/J-L07 | L-024,L-027,L-030 | Hint context giữ; fixture Check từ chối hint/retry/skip; QA-LRN-008,QA-LRN-013 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Missing context vẫn unknown; không certify từ thiếu telemetry |
| PRD-04; req priority UNKNOWN; QA P0 | Skip không completion/mastery; V3 không partial submit | Explicit practice skip | J-L06/J-L13 | L-022,L-024,L-031 | Không first response/completion; fixture test/IV02; QA-LRN-009,QA-BIZ-003 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Threshold vẫn hypothesis; skip không gửi scored completion |
| PRD-05; req priority UNKNOWN; QA P0,P1 | Play policy khác physical listens/score; V3docs07/mapping | Replay / media unavailable | J-L07/J-L15 | L-005,L-023,L-027 | Budget/error tests; unavailable media chặn Check; QA-LRN-014,QA-BIZ-005,QA-LRN-023 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Cap/accessibility comparability hypothesis; native listening chưa verified |
| PRD-07; req priority UNKNOWN; QA P0 | Hai distinct unaided first responses, gồm Check; bounded challenge; PRD07/Feed§5 | Eligible provisional evidence predicate | Feed§5; eligible/locked objective flow | L-010,L-041 | Sample challenge/locked start; QA-BIZ006 inherited; QA-BIZ-006 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Predicate hypothesis; chưa native evidence computation |
| PRD-08; req priority UNKNOWN; QA P0 | Focus trong eligibility; bounded due/prerequisite insertion; PRD08/Feed§4,6 | Choose focus; due/prerequisite available | J-L03;Feed§4–6 | L-010,L-021,L-022,L-041 | Reason/locked/current states; QA-BIZ007 inherited; QA-BIZ-007 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Cap/ranking hypothesis; server scheduler deferred |
| PRD-09; req priority UNKNOWN; QA P0,P1 | Placement optional, skip valid, result provisional; PRD09 | First-use choose/skip offer | J-L01/J-L02 | L-004,L-005,L-006 | L004 skip; L006 insufficient evidence; không certification; QA-LRN-015,QA-LRN-016 | SPEC CONSISTENT / WORKBOOK UNKNOWN | 6–9 configurable; one sample item không là final placement |
| PRD-10; req priority UNKNOWN; QA P0,P1 | Goal optional/editable preference, không bypass; qualitative profile; PRD10 | Choose/skip/edit goal; view evidence | J-L01/J-L02/J-L11;L052 | L-003,L-050,L-051,L-052 | Missing evidence/no mastery%; actual goal fixture gap; QA-LRN-017,QA-BIZ-008 | SPEC CONSISTENT / WORKBOOK UNKNOWN | AUD009 default/no missing state; categories hypothesis |
| PRD-11; req priority UNKNOWN; QA P0 | Habit khác mastery; idempotent day policy; PRD11 | Qualifying retrieval+feedback per day | Feed engagement; PRD11 acceptance | L-010,L-050 | Habit copy tách learning; QA-BIZ009 inherited; QA-BIZ-009 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Mechanics/timezone hypothesis; reward runtime chưa có |
| PRD-12; req priority UNKNOWN; QA P0 | Reward không đổi mastery/eligibility; PRD12 | Milestone theo versioned policy | Feed engagement; summary/profile flow | L-032,L-050 | Không XP/shop; QA-BIZ010 inherited; QA-BIZ-010 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Mechanics hypothesis; chưa production awards |
| PRD-13; req priority UNKNOWN; QA P0,P1 | Locked preview không unlock; reason auditable; PRD13/V3docs09 | Open course/preview/next action | J-L08/J-L10 | L-010,L-040,L-041,L-042 | Locked recovery; IV05 fallback; Home gap; QA-LRN-018,QA-BIZ-011 | SPEC CONSISTENT / WORKBOOK UNKNOWN | AUD010 first Home/resume wiring; priority chưa frozen |
| PRD-14; req priority UNKNOWN; QA P0,P1 | License/review blocking; published immutable; V3docs02/04 | Draft→review→publish→new revision | J-S01/J-S02; role intent notes | S-030,S-033,S-035,S-036,S-037,L-041 | IV03 direct confirmation blocked; sample license/review flow; QA-STF-006,QA-STF-007,QA-BIZ-012,QA-STF-011 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Assignment policies pending; access status khác editorial states |
| PRD-15; req priority UNKNOWN; QA P0,P1 | Command!=telemetry; receipt/revision/source capture; V3docs03–05 | Offline/network restore/retry/late arrival | J-L09/J-L12; offline UX table | L-011,L-012,L-060,L-061,S-050 | Original115+22; 175 states; pending khác ack; QA-OFF-001,QA-OFF-002,QA-OFF-004,QA-BIZ-013,QA-OFF-007 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Durable queues/native concurrency/process restart NOT EXECUTED |
| PRD-16; req priority UNKNOWN; QA P0 | ML/recommendation OFF fallback; no content→honest empty; V3docs01/06 | Service/model unavailable | J-L10; Feed fallback | L-010,L-020,L-063 | IV05/fixture fallback; L063 empty state; QA-LRN-019,QA-BIZ-014 | SPEC CONSISTENT / WORKBOOK UNKNOWN | Real server eligibility/scheduler triển khai sau |
| PRD-06; req priority UNKNOWN; QA P1 | Teaching/retrieval/transfer/check tách; PRD06/Feed§3 | Choose objective/modality | J-L14/J-L15;Feed§3 | L-023,L-024,L-025,L-027 | Task-specific answer/explanation và changed contexts; QA-LRN-004,QA-LRN-005,QA-LRN-022,QA-LRN-023 | SPEC CONSISTENT / WORKBOOK UNKNOWN | QA anchors P1; formal requirement priority UNKNOWN; content review pending |

Semantic conclusions: full-answer submit tương thích với skip vì skip không tạo scored completion. Retry sau finalized attempt dùng new attempt ID. Assistance/replay context không thay score formula. Offline Check không có canonical offline scoring; client playback không chứng minh physical listens. Historical analytics phải dùng exact SourceCapture membership/read view, không query current data bằng wall-clock cutoff cũ. Editorial lifecycle và ReleaseAccessStatus là hai lớp khác nhau.

Không orphan repo PRD trong16-row map; zero dangling screen/QA ID. 27 routes không direct-map ở PRD CSV là diagnostic, không phải27 unauthorized features: feedback/resume/settings/search/staff substeps có supporting sources và7future routes explicit placeholders. Tập ID đầy đủ nằm ở structural_audit.json. Actual BR orphan và priorities của missing workbook vẫn UNKNOWN.

## Decision/Hypothesis Audit

| Decision | Expected Status | Artifact Status | Consistent? | Action |
| --- | --- | --- | --- | --- |
| V3.2/stack/server authority | ĐÃ CHỐT | README/V3.2/hashes và fresh115+22 | YES | Không architecture change |
| Finite cycle/no infinite feed/no forced timer | ĐÃ CHỐT | PRD01/Feed/EG05–06 | YES | Duration tách hypothesis |
| First response/assistance/skip | ĐÃ CHỐT | PRD02–04/Evidence/tests | YES sau terminology fix | Retry sau finalize new attempt |
| Qualitative progress/no fake precision | ĐÃ CHỐT | PRD10/Evidence/EG16 | YES | Không validated mastery% giả |
| Short onboarding/no early bottom nav | ĐÃ CHỐT direction | L001–006 không thuộc main navigation list | YES source/presentation | Termination durability chưa verified |
| Optional/editable goal | ĐÃ CHỐT principle | PRD10 status corrected; fixture còn default/no skip | PARTIAL | CR-GD1-002; categories hypothesis |
| Optional/provisional placement | ĐÃ CHỐT principle | J-L01/02;L004/L006 | YES | Count/cutoff configurable |
| Exact5m/placement6–9 | GIẢ THUYẾT CẦN KIỂM CHỨNG | PRD01/09/config/EG06 | YES | Không timer hoặc production invariant |
| Vietnam18–35/beginner-rebuilder | GIẢ THUYẾT CẦN KIỂM CHỨNG | Initial wedge E0 pending; Charter candidate | YES | Không customer-validated claim |
| Retry/replay/skip/challenge/focus thresholds | GIẢ THUYẾT CẦN KIỂM CHỨNG | PRD02/04/05/07/08, Feed/rubric | YES | Defaults versioned/configurable |
| Exact Home priority | Approved direction / GIẢ THUYẾT CẦN KIỂM CHỨNG | Spec/helper, actual default due/no resume wiring | PARTIAL | CR-GD1-002; không freeze order |
| Streak/rewards/pricing | GIẢ THUYẾT CẦN KIỂM CHỨNG | PRD11/12; free-first/future pricing | YES | Không engagement→mastery |
| Rule-based core/ML OFF | ĐÃ CHỐT | PRD16/EG17/IV05 | YES fixture/spec | Runtime eligibility sau |
| Final mastery/risk/weights/intervention | ĐỂ GIAI ĐOẠN SAU | PRD scope/INTEL001–005 | YES | Không spec weights/algorithm |
| OULAD/UCI production use | RESEARCH ONLY / ĐỂ GIAI ĐOẠN SAU | EG21/model fixtures candidate | YES | Không promote research fixture |
| Child/Guardian/advanced speaking | ĐỂ GIAI ĐOẠN SAU / FUTURE | Closure role intent/PRD scope | YES | Separate future privacy/safety domain |
| Account MVP inclusion/policies | CHƯA QUYẾT ĐỊNH ở nguồn có; UNKNOWN trong workbook thiếu | Phase3HOLD; profile/reauth only | NOT VERIFIABLE | CR001; reconcile approved workbook trước |
| PO approval04/10 | ĐÃ CHỐT scoped conclusions | Direct user instruction/Decision Register | YES scoped | Không ký Phase2/customer/physical gates |
| Customer/learning/value validation | VALIDATION DEBT | E0–E3 pending; không actual dataset | YES | Actual consented discovery/pilot cần thực hiện |

## Known prior audit candidates

| Candidate | Result | Evidence / limitation |
| --- | --- | --- |
| N-06→WF-10 | UNKNOWN / NOT VERIFIED | Actual workbook NOT FOUND; WF namespace khác L namespace |
| WBS1.11 DONE | UNKNOWN / NOT VERIFIED | Không có actual row/status; không gọi FIXED |
| Repo dangling reference | PASS structure | 16PRD/61screens/175states; zero dangling refs |
| Full workbook P0/P1 semantics | FAIL evidence completeness | Requirement priority UNKNOWN; không thay bằng QA priority |
| Actor model | FIXED repo intent | Assignment details pending; workbook chưa verified |
| Account lifecycle | FAIL available BA coverage | Có thể đã có trong missing workbook; reconcile trước new decision |
| Staff lifecycle | PASS spec/fixture boundary | J-S01/02; license/review/direct confirmation checks |
| NFR/privacy | FIXED consolidation; runtime pending | Không arbitrary SLA/TTL; collection disabled |

## Capability Coverage

DEFERRED implementation không tự quyết định capability OUT of MVP. Nếu source không đủ thì ghi scope UNKNOWN/CHƯA QUYẾT ĐỊNH; không invent inclusion để lấp bảng.

| Capability | Scope | Source | Coverage / gap |
| --- | --- | --- | --- |
| First launch/onboarding | IN MVP direction | L001/002;J-L01 | Short CTA/no bottom nav; termination durability chưa verified |
| Account/restore/signup/login/logout/recovery/session/device/state | DEFERRED implementationPhase3; MVP scope UNKNOWN | L064;V3docs07;roadmap | AUD005: complete business lifecycle chưa có |
| Goal/edit/skip | IN MVP principle; categories HYPOTHESIS | PRD10;L003/L052 | AUD009: default/no explicit missing goal state |
| Optional placement | IN MVP direction; count HYPOTHESIS | L004–006;J-L01/02 | Skip/provisional đúng; sample không final placement |
| Recommendation/ML OFF/fallback | IN MVP; exact ranking HYPOTHESIS | PRD13/16;L010/L063;IV05 | AUD010 wiring; server scheduler chưa có |
| Resume/pause/exit/interruption | IN MVP baseline | L033;J-L12;history/back tests | In-memory state; app termination/durability chưa verified |
| Browse/search/course/map/preview | IN MVP direction | L020/L040–042/L071;PRD13 | Preview không unlock; không new domain API |
| Start/answer/hint/replay/skip/explanation/retry | IN MVP principles; limits HYPOTHESIS | PRD01–06;L021–025/L028–031 | Fixtures giữ first/assistance/skip; server domain sau |
| Independent Check/result/closure | IN MVP principles | L026/027/L032;J-L07 | Không hint/skip/retry Check; summary không mastery |
| Review/spaced return/after absence | IN MVP direction; cadence HYPOTHESIS | J-L03;Feed due policy | Long absence exact policy chưa complete |
| Progress | IN MVP principle | L050/051/L070;PRD10 | Qualitative evidence/uncertainty |
| Offline/download/sync/download management | IN MVP contract; Phase6 implementation DEFERRED | L011/012/L054/L060/061;V3docs03/04 | Actual durable queues/package fault tests chưa chạy |
| Settings/preferences/accessibility/context | IN MVP direction | L053/L072; accessibility specs | Voluntary context; no diagnosis; TalkBack pending |
| Content issue/disagreement | CHƯA QUYẾT ĐỊNH / UNKNOWN scope | Không tìm canonical issue-report BA chain | Không tự thêm screen |
| Deletion/export | DEFERRED implementation; MVP boundary UNKNOWN | V3docs10 | AUD005 business request/status/failure missing |
| Notification fatigue/preferences | HYPOTHESIS; delivery DEFERRED | L073; notifications=false fixture | Toggle có; actual delivery/fatigue policy UNKNOWN |
| Author/preview/review/return/approve/publish/new revision | IN MVP planned content operations | S030–037;J-S01/02;PRD14 | Role intent có; permission runtime sau |
| Advisor/intervention/analytics/admin | DEFERRED / FUTURE | 7 explicit staff placeholders | Không production features |
| Advanced speaking/child/ML/intervention | FUTURE / DEFERRED; datasets RESEARCH ONLY | PRD/Decision Register | Không detailed weights/algorithm mới |
| Infinite feed/XP farm/leaderboard/learning-style profiling | OUT | PRD12/EG07/product principles | Không thêm implementation |

## Edge Cases

| Case | Scope | Source | Coverage / gap |
| --- | --- | --- | --- |
| Interruption/app termination | IN MVP recovery intent | J-L12/L033 | Back state verified; process restart/durable queue NOT EXECUTED |
| Return after long absence | IN MVP direction; exact policy UNKNOWN | Feed/J-L03 | Không infer psychology; cần valid eligible next action |
| Offline during learning/assessment | IN MVP contract; implementation DEFERRED | V3docs04/J-L09/J-L15 | Pending canonical score; essential media missing blocks Check |
| Network restored but commands pending / sync retry | IN MVP contract | V3docs03/offline UX | Network!=ack; same ID/payload retry |
| Duplicate replay / ordering | IN MVP contract | V3docs02/03 | Immutable receipt, progress anti-rollback, batch order explicit |
| Stale/partial/corrupt download | IN MVP contract | V3docs04;L054 | Checksums/pinning; actual faults NOT EXECUTED |
| Insufficient storage | IN MVP contract | V3docs04 media/queue budgets | Không evict pending commands; halt new work khi queue full; runtime chưa chạy |
| Device change | DEFERRED implementation; MVP scope UNKNOWN | Session/installation binding | Account flow missing; AUD005 |
| No eligible content | IN MVP direction | PRD16/L063 | Honest empty; không fake completion |
| Revision changed / retire / revoke | IN MVP contract | V3docs02/04 | Old attempt pinned; no silent denominator change |
| Learner rejects recommendation | IN MVP direction; full rejection policy UNKNOWN | Dismissed execution/browse alternative | Giữ eligibility; không causal outcome claim |
| Goal changes | IN MVP principle | PRD10/L052 | Không rewrite ability/bypass prerequisite |
| Content issue/disagreement | CHƯA QUYẾT ĐỊNH scope | BA chain NOT FOUND trong nguồn có | Record gap; không tự thêm capability |
| ML/recommendation unavailable | IN MVP baseline | PRD16/J-L10/IV05 | Deterministic eligible fallback hoặc empty |
| Deletion/export | DEFERRED implementation; MVP scope UNKNOWN | V3docs10 | Generation/restore lock rules có; business front flow thiếu |
| Notification fatigue/preferences | HYPOTHESIS / DEFERRED delivery | L073/preference toggle | Không implemented delivery policy; không forced reminder |
