# MINGO — GĐ1 FINAL CONSISTENCY AUDIT & CLOSURE

Ngày kiểm tra: **05/10/2026, Asia/Saigon**. Nguồn yêu cầu: bản chỉ đạo PO được lưu nguyên byte trong evidence. Audit kiểm tra nguồn thực tế, chạy bộ kiểm tra trước khi sửa và phân biệt specification với implementation/runtime.

## 1. Executive Verdict

**FAIL — chưa đủ điều kiện đóng internal consistency gate.** V3.2 tồn tại đúng bản gốc và đã chạy lại **115/115 contract checks, 22/22 SQL checks**. Trong các nguồn repo đã kiểm tra, không tìm thấy blocking contradiction cụ thể buộc thay V3.2.

Điểm chặn là thiếu actual BA workbook, chưa chứng minh đầy đủ traceability/P0–P1, và thiếu nguồn BA account lifecycle trong repo. Việc chưa có full product implementation là implementation debt riêng, không phải lý do tự động đánh trượt architecture baseline.

Sau sửa: **12 findings: 6 OPEN, 4 FIXED, 2 PASS**. Còn **1 BLOCKER và 2 HIGH chặn gate**: AUD-001/003/005. Customer validation remains **VALIDATION DEBT**.

## 2. GĐ1 Gate Recommendation

**Chưa chốt “GĐ1 — Internal BA Baseline Approved”.** Approval ngày **04/10/2026** được ghi nhận từ chỉ đạo trực tiếp của PO. Approval này giữ các nguyên tắc đã chốt, nhưng không thay thế internal consistency gate và không biến hypothesis thành customer evidence.

GĐ1 nghiệp vụ khác **engineering Phase1 — Implementation Foundation** trong repo. Gate foundation lịch sử vẫn giữ nguyên; Phase2 human/product gate vẫn pending và Phase3 HOLD. Xem [Gate Pack](GATE_PACK.md).

## 3. What Was Actually Inspected

Repo thực tế: `C:/Mingo`, branch `main`, HEAD `a112f762ab08f6fa688cc4857b21d95d1055ab5c`, có thay đổi staged/unstaged/untracked từ trước. Hai URL `Phucht59/mingo` và `Phucht59/mingle` trả cùng GitHub ID **1388925852**, tên canonical `Phucht59/mingle`; remote HEAD trùng commit local. Dirty working tree là source boundary của audit, không đồng nhất remote commit hoặc hosted CI.

Đã kiểm tra:

- README, START_HERE, PROJECT_MAP, REPO_RULES; không tìm thấy AGENTS.md trong workspace scan.
- Index/provenance V3.2, checksum của toàn bộ **102 file gốc**, master/invariants/receipt/offline/source-capture/ML/security/recommendation/delete-restore/acceptance docs, compatibility matrix; DDL/OpenAPI/schema/event contracts qua bộ verification gốc. Các bản copy trong archive/outputs được phân loại theo authority, không chọn canonical bằng timestamp.
- Charter, toàn bộ **16 PRD**, Evidence Model, Feed specification, Learning Experience Model, J-L01–15/J-S01–06, first-use/offline/accessibility specs, telemetry purpose register, wedge research plan, content rubric, Decision/CR/Implementation Issues, Project State và navigation snapshot.
- Toàn bộ **61 screen, 175 state**, PRD/state/scope CSV rows và **94 QA case definitions** để đối chiếu ID/priority/reference. Có **7 future staff placeholders** được ghi rõ.
- API/worker/migrations/tests/config, CI workflow và shared Flutter learner/staff/fixtures/audio/lesson. API hiện chỉ có health endpoints; các app dùng mẫu presentation, chưa có domain/auth/offline implementation hoàn chỉnh.
- Workbook **Quan_ly_du_an_Mingo.xlsx**, đọc toàn bộ ô có dữ liệu và công thức trong 7 sheet: 00_BAT_DAU, 01_TONG_QUAN, 02_SAN_PHAM, 03_ROADMAP, 04_CONG_VIEC, 05_VAN_DE_THAY_DOI, 06_BANG_CHUNG. Chỉ đọc, không lưu/export/render hoặc sửa workbook. Đây là workbook quản lý dự án khác với BA workbook được yêu cầu.

**NOT FOUND:** `Mingo GD1 — Quản lý Phân tích Nghiệp vụ.xlsx` với 16 sheet và `MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-04.md`. Workspace inventory có kiểm tra cả các ignored local candidate paths. Không tạo bản thay thế giả và không suy rằng những nội dung này vắng mặt ở mọi nơi ngoài workspace.

Inventory lưu SHA cho **324 file nguồn/config/workbook** hiện hành, loại generated/cache khỏi tập này. Hash inventory không có nghĩa cả 324 file đều được đọc sâu như nhau. Các QA workbook lịch sử được inventory để giữ provenance, không dùng thay BA source.

## 4. Executed Verification

| Check | Kết quả thực tế | Phạm vi |
|---|---|---|
| V3.2 nguyên bản | 115 passed / 0 failed; 22 passed / 0 failed; 102 hashes intact | Contract và SQL PGlite |
| Adapter guards | 9 passed / 0 failed | Additive tests, không cộng vào 115/22 |
| Backend | 9 passed / 7 skipped / 0 failed | Foundation unit tests; 6 PostgreSQL cases và 1 symlink case bị skip |
| Flutter: fixture + independent + presentation | 232 passed / 0 failed / 0 skipped; exit 0 | Widget/presentation/golden scope |
| Current evidence verifier | 19 checks PASS | Kiểm tra integrity và logs của prior candidate, không chạy lại prior 50/274/275 tests |
| Structural audit | 16 PRD, 61 screen, 175 state; zero dangling/missing/duplicate reference | Cấu trúc, không tự chứng minh semantics |

[Command, environment, expected/actual và logs](CHECK_RESULTS.md). Python 3.12.10, Node 24.19.0, Flutter 3.32.8/Dart 3.8.1, Windows/PowerShell. Run UTC 04/10/2026 18:11:05 tương ứng 05/10/2026 tại Asia/Saigon.

Không thực thi trong audit: hosted CI cho dirty candidate, native domain concurrency, durable mobile queues/process restart, real identity/assessment/offline APIs, physical TalkBack/performance và delete/restore drill. `docs/12_ACCEPTANCE_TESTS_V3.md` là kế hoạch acceptance, không phải mọi case đã PASS.

## 5. Critical Findings

| ID | Severity | Điểm chặn còn mở |
|---|---|---|
| AUD-001 | BLOCKER | Không có actual BA workbook để kiểm chứng 16 sheet, N-06→WF-10, WBS 1.11 và coverage |
| AUD-003 | HIGH | Chưa xác nhận đủ chuỗi requirement→BR→Trigger→UC→Screen/State→AC/Test và priority thực của toàn bộ workbook |
| AUD-005 | HIGH | Nguồn repo thiếu complete account lifecycle BA/scope; có thể được giải quyết khi đọc workbook thực |

AUD-004 và AUD-008 trước sửa là HIGH; đã FIXED ở phạm vi role intent/status trong repo. Không dùng kết quả này để tuyên bố workbook đã sửa hoặc đã verified.

## 6. Full Finding Register

Register giữ quan sát **trước sửa** và disposition **sau sửa**. [JSON đầy đủ](FINDING_REGISTER.json); bản trước sửa nằm ở `FINDINGS_BEFORE_FIXES.json` trong evidence.

### AUD-001 — BLOCKER / OPEN

**Area:** Required BA evidence  
**Artifact:** Mingo GD1 — Quản lý Phân tích Nghiệp vụ.xlsx  
**Location:** All 16 requested sheets; workspace inventory  
**Observed:** NOT FOUND. Only a seven-sheet project-management workbook and dated Phase2 QA controls are available. N-06→WF-10, WBS 1.11, requirement priorities and workbook semantics cannot be verified.  
**Expected:** Inspect actual approved BA workbook, including all P0/P1 chains and known candidates.  
**Evidence:** artifact_candidates.txt; available_management_workbook_extract.json; supplied request  
**Source of truth:** User source hierarchy Levels 1–3  
**Impact:** Cannot certify workbook consistency or close GD1 internal gate.  
**Recommended action:** Bring the actual workbook into the audit boundary and rerun the workbook/RTM checks; do not fabricate a replacement.  
**Change Request required:** NO  
**Gate blocking:** YES  
**Status before fixes:** OPEN  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-002 — MEDIUM / FIXED

**Area:** Snapshot continuity  
**Artifact:** MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-04.md  
**Location:** Workspace inventory; PROJECT_PROGRESS_SNAPSHOT.md  
**Observed:** Requested dated snapshot NOT FOUND. Available snapshot is a navigation document, referencing 2026-10-02 authority and unsigned Phase2 gate. The new user instruction records GD1 conclusion approval on 2026-10-04.  
**Expected:** Preserve old history, record approved GD1 direction and distinguish business GD1 from engineering Phase1.  
**Evidence:** PROJECT_PROGRESS_SNAPSHOT.md paragraphs 1–2; PROJECT_STATE.md phase table; user approval record  
**Source of truth:** User approval dated 2026-10-04; V3.2  
**Impact:** Cross-chat continuation can confuse internal BA approval, foundation closure and human design acceptance.  
**Recommended action:** Create a new dated audit snapshot with explicit source limitation and phase distinction.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Created a new dated continuation snapshot; requested 2026-10-04 source remains NOT FOUND and no history is fabricated.  

### AUD-003 — HIGH / OPEN

**Area:** Traceability and priority  
**Artifact:** MVP_PRD.md; PRD_TRACEABILITY_V2.csv; SCREEN_STATE_TRACEABILITY.csv  
**Location:** All PRD-01..16; CSV headers and rows 2–17  
**Observed:** 16 PRDs map to existing screens/QA and 175 states, but PRD trace has no explicit BR/Trigger/UC relations or requirement P0/P1 field. Journeys provide semantic coverage for many rows. 27 routes lack a direct PRD mapping; several have clear inherited support/future rationale, so this is not 27 unauthorized features.  
**Expected:** A reviewable complete requirement→rule→trigger→flow→screen/state→acceptance/test chain, with accountable priority and justified support/future surfaces.  
**Evidence:** structural_audit.json (zero dangling references); PRD_TRACEABILITY_V2.csv headers; J-L01..15/J-S01..06  
**Source of truth:** User GD1 capability Definition of Done; V3.2 compatibility matrix  
**Impact:** P0-first completeness and orphan business-rule coverage cannot be certified across the missing workbook.  
**Recommended action:** Supply semantic trace audit for all 16 repo PRDs; reconcile it with actual workbook BR/UC/Trigger IDs and priorities. Do not infer requirement priority from QA priority.  
**Change Request required:** NO  
**Gate blocking:** YES  
**Status before fixes:** OPEN  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-004 — HIGH / FIXED

**Area:** Product actors and permission intent  
**Artifact:** MVP_PRD.md; V3.2 docs/07_SECURITY_PERMISSION_V3.md; Staff journeys  
**Location:** Actors paragraph; Object scopes; J-S01/J-S03/J-S06  
**Observed:** Learner, assigned instructor/advisor, content admin, platform admin and worker scopes exist. No complete canonical product model distinguishes Author, Reviewer, Publisher/Operator, Staff umbrella, conditional Advisor and FUTURE Guardian. A staff review fixture is not permission design.  
**Expected:** Business role boundaries and scope classification without inventing permission implementation or separation-of-duties rules.  
**Evidence:** V3.2 docs/07 object scopes; PHASE_2_SPEC.json staff entries; no actor register found in active product docs  
**Source of truth:** V3.2 security boundary; approved GD1 closure scope  
**Impact:** Content/support operations cannot be handed off with a complete role intent model.  
**Recommended action:** Record existing approved role intent and explicit undecided assignment/segregation questions; reconcile with workbook once available.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Approved role intent consolidated in GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md; detailed role assignment remains explicitly undecided. Missing-workbook verification remains AUD-001.  

### AUD-005 — HIGH / OPEN

**Area:** Account lifecycle BA  
**Artifact:** MVP_PRD.md; learner journeys; roadmap  
**Location:** PRD-01..16; J-L01..15; /reauth L-064; engineering Phase3  
**Observed:** No canonical BA flow and acceptance chain for signup/login/logout/recovery/session/device change/account state/deletion/export. Profile/preferences and reauth design exist. Auth implementation is legitimately held for Phase3, which does not establish business requirements or MVP scope.  
**Expected:** Explicit inclusion/defer decisions and minimal business states, failure paths and acceptance references for account lifecycle.  
**Evidence:** MVP_PRD functional table; J-L journeys; SCREEN_CATALOG L-050..054/L-064; V3.2 deletion/export controls  
**Source of truth:** User account capability audit; V3.2 identity/object/deletion contracts  
**Impact:** Identity and data-rights behavior remains insufficiently specified for a GD1 business handoff.  
**Recommended action:** Create a candidate scope CR to resolve unrecorded account inclusion and minimum lifecycle behavior; do not implement auth or invent policies.  
**Change Request required:** YES  
**Gate blocking:** YES  
**Status before fixes:** OPEN  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-006 — MEDIUM / FIXED

**Area:** NFR/privacy consolidation  
**Artifact:** Telemetry purpose register; Evidence model; V3.2 retention controls  
**Location:** Collection gate/lifecycle; Evidence model §5; V3.2 docs/10  
**Observed:** Telemetry purpose/minimization and delete/restore races are specified; collection disabled and TTL/access approval pending. Active artifacts do not record Law 91/2025/QH15 or Decree 356/2025/NĐ-CP. No obsolete Decree13 primary reference found in inspected active docs. NFR rules are scattered, rather than a GD1 checklist.  
**Expected:** Record verified 2026 legal source context and purpose→collection→access→use→retention→deletion/export→audit intent; no invented legal TTL/SLA.  
**Evidence:** Telemetry register; Evidence model §5; official government law/decree metadata, both effective 2026-01-01  
**Source of truth:** V3.2; recorded project privacy baseline; official government metadata  
**Impact:** Pre-pilot governance dependency is difficult to track. No observed unauthorized collection or proven blocking privacy contradiction.  
**Recommended action:** Add source-backed privacy/NFR closure notes and keep numeric retention/SLO and collection approval pending.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Source-backed legal-context metadata, NFR checklist and governance intent consolidated. TTL/SLO and collection approval remain later prerequisites, not completed runtime.  

### AUD-007 — MEDIUM / OPEN

**Area:** Stale management workbook  
**Artifact:** Quan_ly_du_an_Mingo.xlsx  
**Location:** 00_BAT_DAU!B17; 01_TONG_QUAN!B7; 02_SAN_PHAM!B86; 03_ROADMAP!F6; 04_CONG_VIEC!F5:F7; 05_VAN_DE_THAY_DOI!C6:D6; 06_BANG_CHUNG!E8:E9  
**Observed:** Workbook calls Phase1 current, Phase2 not started, original import/rerun pending. Actual original source and reruns exist and PROJECT_STATE says Phase2 review pending. This is a different workbook from requested GD1 BA artifact.  
**Expected:** Consistent dated authority or clearly historical classification; task evidence drives statuses.  
**Evidence:** Read-only cell extraction with source hash; PROJECT_STATE current table; fresh 115+22 run  
**Source of truth:** V3.2 executed evidence; scoped PROJECT_STATE; preserved historical gate evidence  
**Impact:** A reader may act on stale blocker/status. Not evidence of premature GD1 DONE.  
**Recommended action:** Provide exact correction plan for this workbook separately; do not substitute it for BA workbook or blindly mark all foundation tasks done.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-008 — HIGH / FIXED

**Area:** Current documentation status drift  
**Artifact:** PRODUCT_CHARTER.md; MVP_PRD.md; LEARNER_EVIDENCE_MODEL.md; DECISION_REGISTER.md  
**Location:** Charter opening and acceptance; PRD final paragraph/PRD-10 status; Evidence model opening/footer; current Decision register  
**Observed:** Charter says exact V3.2 pending and brand not frozen; PRD says exact V3.2 unavailable/pending; Evidence footer requires completing a matrix already completed 2026-09-26. PRD-10 still labels optional goal principle as hypothesis. No scoped 2026-10-04 GD1 approval record.  
**Expected:** Current docs acknowledge supplied/verified originals and approved optional/editable goal principle; exact goal categories stay hypothesis; GD1 approval is not Phase2 human signoff or customer validation.  
**Evidence:** Charter first/final paragraphs; PRD-10 and Out of scope; compatibility matrix; user approval record  
**Source of truth:** Verified V3.2; user 2026-10-04 approval  
**Impact:** Implementation may treat resolved authority mapping as blocked or infer approval beyond its scope.  
**Recommended action:** Correct stale status/terminology only, preserving versioned policies and historical decisions.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Stale availability/mapping/status wording corrected; approved optional goal principle distinguished from hypothesis categories; scoped approval recorded.  

### AUD-009 — MEDIUM / OPEN

**Area:** Optional goal presentation drift  
**Artifact:** fixtures.dart; learner.dart; J-L01  
**Location:** ReviewPreferences.goal line53; L-003 content lines383–410  
**Observed:** Goal initializes to Giao tiếp hằng ngày, is non-null, and L-003 only offers Continue; no explicit skip/missing-goal state. Welcome can bypass the whole flow, but the default preference still exists. The proposed optional goal is not faithfully represented in this fixture.  
**Expected:** Optional explicit intent remains distinct from missing/skipped intent; editing remains allowed and never creates evidence or bypasses prerequisites.  
**Evidence:** Source code and J-L01; PRD-10; supplied approved goal decision  
**Source of truth:** Approved first-use direction; V3.2 evidence/eligibility boundaries  
**Impact:** Preview may suggest a goal selected by the learner when it was a default. No production collection exists.  
**Recommended action:** Record candidate presentation behavior CR; retain code and goldens until authorized targeted implementation/retest.  
**Change Request required:** YES  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-010 — MEDIUM / OPEN

**Area:** First Home/resume explanation drift  
**Artifact:** learner.dart; fixtures.dart; PHASE_2_SPEC.json  
**Location:** L-010 content lines447–485; nextLessonReason lines89–98; Home actions/rules  
**Observed:** Home passes due=true for ordinary first-use state and never supplies hasResume to its helper; primary action is always Start. Helper unit tests cover hasResume but the Home wiring does not. Stateless sample mode is disclosed.  
**Expected:** First-use explanation reflects missing/provisional evidence; returning valid unfinished work has resume semantics. Exact ranking remains hypothesis unless separately approved.  
**Evidence:** learner.dart nextLessonReason call; helper/test; J-L01/J-L12; Home spec reason/actions  
**Source of truth:** Approved truthful reason/resume direction; no new ranking invariant  
**Impact:** UI tests can pass while a named business scenario is not represented. Does not prove broken durable production sync.  
**Recommended action:** Add to candidate presentation CR and require first-use/returning/resume scenario evidence; do not silently freeze candidate priority.  
**Change Request required:** YES  
**Gate blocking:** NO  
**Status before fixes:** OPEN  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-011 — INFO / PASS

**Area:** Validation and runtime boundaries  
**Artifact:** Initial wedge plan; V3.2 docs/12; API and UI sources  
**Location:** E0 status; implementation acceptance plan; api.py routes; ReviewLabel/fixtures  
**Observed:** Customer discovery and efficacy remain pending; no positive customer/market validation claim found in inspected active sources. API exposes health only; Flutter sample logic is labelled presentation. Full native domain/offline/auth/restore scenarios not run.  
**Expected:** Customer validation remains VALIDATION DEBT; contract/schema/UI PASS never becomes production/runtime/efficacy PASS.  
**Evidence:** Initial wedge plan; docs/12 first paragraph; source API/UI; current phase state  
**Source of truth:** User evidence hierarchy and V3.2  
**Impact:** No defect in separating evidence layers; later gates remain necessary.  
**Recommended action:** Preserve boundary in report, debt register and snapshot.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** PASS  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

### AUD-012 — INFO / PASS

**Area:** Repository identity  
**Artifact:** Git origin and GitHub repository metadata  
**Location:** origin Phucht59/mingo vs requested Phucht59/mingle  
**Observed:** Two requested URL spellings resolve through GitHub API to the same repository ID 1388925852/full_name Phucht59/mingle. ls-remote HEAD equals local a112f762ab08f6fa688cc4857b21d95d1055ab5c. Working tree is dirty; remote commit is not this full candidate.  
**Expected:** Use verified repo identity and disclose dirty source boundary.  
**Evidence:** GitHub API read-only responses; git ls-remote; git_identity.json; git_status_before.txt  
**Source of truth:** Actual repository metadata and Git state  
**Impact:** Name mismatch resolved; dirty candidate is still not hosted CI evidence.  
**Recommended action:** Record both URLs and common identity; do not switch/reset/commit/push.  
**Change Request required:** NO  
**Gate blocking:** NO  
**Status before fixes:** PASS  
**After audit:** Unchanged; see recommended action and the scoped audit limits.  

## 7. Consistency Matrix

[Ma trận đủ 17 area](AUDIT_TABLES.md) đối chiếu V3.2, workbook, snapshot và repo. Architecture/authority/content/evidence tương thích trong phạm vi nguồn đã đọc. Workbook vẫn UNKNOWN; recommendation fixture có medium drift; account BA và full traceability chưa đóng.

Không tìm thấy căn cứ cần thêm Kafka/Kubernetes/microservices/warehouse/feature store hoặc đổi scoring/progress/permission authority. Không thêm thuật toán mastery/risk/ML, production weights hay learning-style personalization.

## 8. Traceability Audit

[Bảng đầy đủ 16 PRD](AUDIT_TABLES.md) chỉ rõ rule text/source hiện có, trigger, journey/flow, screen/state, acceptance/test và gap. Không dựng BR/Trigger/UC IDs của workbook chưa đọc. Existing text nodes có thể đủ để trace ở mức phù hợp; không cần một screen riêng cho mọi capability.

Các P0 QA anchors được kiểm tra trước PRD-06 có P1 QA anchors. **Requirement priority vẫn UNKNOWN**, không suy từ QA priority. Vì thiếu workbook, không thể certify đã audit toàn bộ P0 rồi P1 của BA baseline.

Repo có zero dangling screen/QA reference và không thiếu PRD row trong 16-row map. **27 routes** không nằm trực tiếp trong cột PRD screens là diagnostic: nhiều route có basis từ feedback/resume/settings/search/staff substeps, owner presentation direction hoặc FUTURE scope. Không gọi cả 27 là unauthorized features. Orphan BR, N-06→WF-10 và WBS 1.11 của actual workbook: **UNKNOWN / NOT VERIFIED**, không ghi PASS, FIXED hay NOT APPLICABLE.

## 9. Decision/Hypothesis Audit

[Decision table](AUDIT_TABLES.md) phân biệt ĐÃ CHỐT, GIẢ THUYẾT CẦN KIỂM CHỨNG, CHƯA QUYẾT ĐỊNH, ĐỂ GIAI ĐOẠN SAU và VALIDATION DEBT. Optional/editable goal và optional/provisional placement là approved principles. Exact categories/counts vẫn hypothesis.

Không freeze exact 5 phút, Vietnam 18–35/beginner wedge, placement 6–9, retry/replay/skip/challenge/focus thresholds, streak/reward/pricing hoặc exact Home ranking. Final mastery/risk, weights, advanced intervention/speaking và child/guardian vẫn deferred; OULAD/UCI chỉ research.

## 10. Safe Fixes Applied

[Fix log](FIX_LOG.md) ghi 8 actions: sửa status/terminology Charter/PRD/Evidence/Decision; tổng hợp actor/glossary/NFR/privacy intent; scoped Project State; snapshot mới; DRAFT CR register. Findings được lưu trước sửa. V3.2, code, tests, goldens, workbook và lịch sử không sửa; preservation ledger kiểm chứng riêng.

## 11. Change Requests Required

**CR-GD1-001 — account lifecycle scope/business baseline:** DRAFT. Trước tiên đọc actual approved workbook; nếu đã có policy/flow approved thì map lại và đóng candidate là NOT REQUIRED, không hỏi lại PO các quyết định đã chốt.

**CR-GD1-002 — optional goal, first Home/resume fixture:** DRAFT, non-blocking implementation debt cho GĐ1. Cần trạng thái missing/skipped/selected goal và reason/action khớp first-use/returning/resume; không freeze ranking hoặc sửa V3.2. Đủ các trường CR nằm trong CHANGE_REQUESTS.md. Chưa đổi code hay goldens.

## 12. Remaining Validation Debt

- **Validation debt:** discovery, target circumstance/JTBD, current alternatives, value/adoption/usability/trust chưa có actual participant evidence đủ để close. Five-user pilot chỉ qualitative.
- **Implementation debt:** identity/permissions/domain scoring/content publication, durable queues, source capture, deletion/export/restore, native concurrency, physical accessibility/performance và current hosted CI chưa chứng minh.
- **Research debt:** delayed learning gain/transfer, mastery/risk calibration, scientific/model validity chưa proven.
- **Deferred product scope:** advanced ML/speaking/intervention, child/guardian và các future staff layers; không ép vào MVP.

Legal project context được kiểm tra bằng metadata chính thức: [Luật 91/2025/QH15](https://chinhphu.vn/?classid=1&docid=214590&pageid=27160), [Nghị định 356/2025/NĐ-CP](https://vanban.chinhphu.vn/?docid=216387&pageid=27160&typegroupid=4), đều hiệu lực **01/01/2026**. Không tìm thấy active primary reference tới Decree 13 trong tập nguồn đã scan. Đây là kiểm tra source identity/ngày hiệu lực, không tự phát minh legal requirement hoặc chứng nhận tuân thủ. Collection disabled; TTL/access/consent còn cần quyết định trước thu dữ liệu.

## 13. Excel Update Instructions

[Update plan](ARTIFACT_UPDATE_PLAN.md) nêu đủ 16 sheet BA và cell-specific instructions cho workbook quản lý dự án khác. Chưa thể final-update actual BA Excel khi file chưa có. Không invent row/cell IDs. WBS 1.11 phải ACTIVE nếu DoD traceability chưa đạt, sau khi đọc đúng record thực.

## 14. Final Word Report Readiness

**NOT READY để phát hành Final GĐ1 Approved report.** Có thể bắt đầu qualified narrative draft từ các facts/plans/limitations đã kiểm tra. [Kế hoạch 18 section](ARTIFACT_UPDATE_PLAN.md) nêu readiness, nguồn và format A4/Times New Roman theo yêu cầu. Không tạo final DOCX giả hoặc đưa customer discovery vào report như đã hoàn tất.

## 15. New Project Progress Snapshot

Đã tạo `02_Tai_lieu_du_an/07_Tien_do_du_an/MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-05.md`: PO approval scope, V3.2 results, source boundary, 3 critical open findings, hypotheses/deferred/debt và bước tiếp theo. Snapshot 04/10 vẫn NOT FOUND; navigation snapshot và lịch sử giữ nguyên.

Audit đã trả lời stop conditions bằng evidence hoặc UNKNOWN có lý do. Kết luận này hoàn tất **audit trong phạm vi nguồn hiện có**; chưa hoàn tất **GĐ1 closure** vì các source/gap chặn gate còn mở.
