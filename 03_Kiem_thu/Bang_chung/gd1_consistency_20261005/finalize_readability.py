"""Final Vietnamese editorial pass on text deliverables; no source/test/workbook mutation."""
from pathlib import Path
import json
R=Path('C:/Mingo'); E=R/'03_Kiem_thu/Bang_chung/gd1_consistency_20261005'; O=R/'03_Kiem_thu/Bao_cao/GD1_Consistency_Audit_20261005'
def put(n,s):(O/n).write_text(s.strip()+'\n',encoding='utf-8')
def tab(h,rows):
 return '| '+' | '.join(h)+' |\n| '+' | '.join('---' for _ in h)+' |\n'+'\n'.join('| '+' | '.join(str(v).replace('|','/') for v in row)+' |' for row in rows)+'\n'
f=json.loads((O/'FINDING_REGISTER.json').read_text(encoding='utf-8'))['findings']
register='\n\n'.join('### '+x['ID']+' — '+x['Severity']+' / '+x['Status']+'\n\n'+'\n'.join('**'+k+':** '+x[k]+'  ' for k in ['Area','Artifact','Location','Observed','Expected','Evidence','Source of truth','Impact','Recommended action','Change Request required','Gate blocking','Status before fixes','After audit']) for x in f)
put('EXECUTIVE_AUDIT.md','''# MINGO — GĐ1 FINAL CONSISTENCY AUDIT & CLOSURE

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

'''+register+'''

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
''')

put('GATE_PACK.md','''# MINGO — GĐ1 Internal BA Baseline

Ngày 05/10/2026, Asia/Saigon. **Overall: FAIL. Gate: chưa đóng.**

| Gate field | Kết quả |
|---|---|
| Architecture source | Exact V3.2.0; 102 original hashes intact |
| PO approval | Approved current GĐ1 conclusions/principles ngày 04/10/2026 theo supplied user instruction |
| Customer validation | **VALIDATION DEBT** |
| Critical open | AUD-001 BLOCKER; AUD-003 HIGH; AUD-005 HIGH |
| Candidate CR | CR-GD1-001 account scope; CR-GD1-002 goal/Home/resume fixture; cả hai DRAFT |
| Fresh verification | 115 contracts +22 SQL; guard9; backend9pass/7skip; Flutter232; structural16/61/175 |
| Runtime limitation | Chưa chạy domain/offline/auth/restore/physical/human/hosted CI cho candidate này |
| Gate recommendation | **FAIL — chưa được gọi Internal BA Baseline Approved** |

PO approval không phải customer validation hoặc chữ ký các Phase2 visual/content/TalkBack/physical gates. Business GĐ1 khác engineering Phase1 foundation; Phase3 vẫn HOLD.

Giữ hypotheses: exact duration, candidate customer/segment, placement/goal categories, thresholds, reward/streak/pricing và exact Home priority. Giữ deferred: final mastery/risk, production ML weights, advanced intervention/speaking, child/guardian. OULAD/UCI research only; 7 staff future routes là placeholders.

Điều kiện đóng tiếp theo:

1. Đọc actual 16-sheet BA workbook; xác nhận authority/hash và kiểm tra N-06→WF-10, WBS 1.11 cùng actual P0/P1 inventory.
2. Xác nhận mỗi requirement/rule có semantic chain đúng, AC/test và scope/priority; orphan/support surface cần resolve hoặc justify.
3. Map account lifecycle scope/flows đã approved nếu có; chỉ quyết định mới khi actual sources còn thiếu, theo CR-GD1-001.
4. Reconcile safe updates vào actual workbook, retest affected references/status và bảo toàn hypotheses/customer debt.

Khi không còn BLOCKER/HIGH ảnh hưởng gate mới đề xuất **GĐ1 — INTERNAL BA BASELINE APPROVED**, kèm customer **VALIDATION DEBT**. Xem [audit](EXECUTIVE_AUDIT.md), [tables](AUDIT_TABLES.md), [checks](CHECK_RESULTS.md), [update plan](ARTIFACT_UPDATE_PLAN.md).
''')

fixrows=[
['FIX-01','AUD-008','PRODUCT_CHARTER.md','Exact source pending, name chưa freeze','Ghi exact V3.2 available/verified, Mingo và scoped PO approval','Chỉ sửa status/authority'],
['FIX-02','AUD-008','MVP_PRD.md','Goal principle hypothesis; source pending','Optional/editable principle approved; categories hypothesis; GĐ1 gate pending','Không đổi threshold/score'],
['FIX-03','AUD-008','LEARNER_EVIDENCE_MODEL.md','First response gọi unaided; matrix pending','First response có assistance condition; matrix hoàn tất được link','Khớp invariant assisted đã có'],
['FIX-04','AUD-008','DECISION_REGISTER.md','Chưa ghi GĐ1 approval04/10','Ghi approval nguồn direct user và 5 classifications','Không ký human/customer gates'],
['FIX-05','AUD-004/006','GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md','Role/glossary/NFR/privacy phân tán','Tổng hợp intent và legal metadata; pending policies rõ','Không thêm enum/SLA/TTL/collection'],
['FIX-06','AUD-002','New dated snapshot05/10','Snapshot04/10 NOT FOUND','Tạo continuation snapshot có giới hạn','Không dựng lịch sử chưa đọc'],
['FIX-07','AUD-001/003/005','PROJECT_STATE.md','Chưa có scoped GD1 audit status','GĐ1 FAIL riêng với engineering phases','Không đổi Phase2/Phase3 gates'],
['FIX-08','AUD-005/009/010','CHANGE_REQUESTS.md','Gaps chưa được register','Hai candidate DRAFT; reconcile actual workbook trước','Không implement business/code'],
]
put('FIX_LOG.md','# Safe fix log — 05/10/2026\n\nFindings được ghi trước sửa. Không sửa V3.2, API/worker/Flutter sources, tests, goldens, workbook, dated snapshots hoặc historical evidence. Trước/sau SHA và preservation checks nằm trong evidence. Không commit/push/PR hoặc ghi task ra external systems.\n\n'+tab(['Fix ID','Finding','File/Sheet','Before','After','Why Safe'],fixrows)+'\nAUD-002/004/006/008 FIXED ở phạm vi repo documentation. AUD-001/003/005 còn chặn gate; AUD-007/009/010 vẫn OPEN, non-blocking debt.\n')

sheet_actions=[
('00_Dashboard','Hiển thị GĐ1 internal gate FAIL, scoped approval04/10 và customer VALIDATION DEBT','Status dẫn từ register/gate, không static PASS'),
('01_Huong_dan','Ghi hierarchy, classifications và các mức evidence','GĐ1 nghiệp vụ khác engineering Phase1'),
('02_Roadmap_8_GD','Giữ roadmap8GĐ; link roadmapPhase0–17','Mapping chưa có: UNKNOWN, không tự quy đổi'),
('03_Yeu_cau_Nghiep_vu','Đọc actual P0 rồi P1; check account/learner/staff/NFR scope và AC','So16repoPRD; không tạo giả requirement priority'),
('04_Business_Rules','Map frozen principles tới exact V3.2/rule text','Numeric policies giữ HYPOTHESIS'),
('05_UseCase_Trigger','Trace actor/precondition/trigger/flow/alternative/failure','J-L/J-S có sẵn; account gap cần actual source'),
('06_User_Journey','Check first-use, return/resume/absence và offline flows','Goal/placement optional; Home priority chưa freeze'),
('07_RTM','Kiểm tra semantic chains, orphan/dangling/duplicate meaning','N-06→WF-10 chưa verified; không đổi sang L-010 bằng suy đoán'),
('08_Wireframe_Learner','Kiểm kê actual WF IDs và first-use/state meanings','Không bottom nav trước shell; không screen riêng cho mọi capability'),
('09_Wireframe_Staff','Check draft/review/license/publish/new revision và role intent','Published immutable; FUTURE placeholders giữ nguyên'),
('10_WBS','Đối chiếu item1.11 với actual traceability DoD','ACTIVE nếu incomplete; current row/status UNKNOWN'),
('11_RACI','Giữ project responsibility; link product actors riêng','RACI không cấp permission sản phẩm'),
('12_RAID','Ghi missing sources, account scope, validation/runtime/research debts','Phân biệt gate blocker với medium debt'),
('13_Research_Evidence','Tag PROJECT/EXECUTABLE/EXTERNAL/INFERENCE/HYPOTHESIS','Không fake customer validation; OULAD/UCI research only'),
('14_Decision_Log','Ghi scoped PO approval04/10 và candidate CR status','Không blanket-freeze hypotheses/deferred/FUTURE'),
('15_Test_Gate','Ghi115/22/9/232 và backend9/7 theo boundary','Contract/UI không là runtime PASS; internal gate FAIL'),
]
word_sections=[
('Executive Summary','Audit verdict, Charter, core promise','Draft có giới hạn; final gate FAIL'),
('Research Method & Limitations','Evidence hierarchy, executed logs, missing artifacts','READY cho draft'),
('Product / Problem Framing','Charter và approved direction','Internal framing; không claim measured prevalence'),
('User Segmentation & JTBD','Initial Wedge Research Plan','HYPOTHESIS; chưa có validated ICP'),
('Behavioral / Usage Context','Learning model, journeys, protocols','Conceptual context; actual customer behavior UNKNOWN'),
('Learning-Science Synthesis','Scientific research resolution/evidence register','Dated synthesis; refresh citations cho official claims, không Mingo efficacy'),
('Competitor / Market Context','Alternative research instrument/access limits','NOT READY cho current ranking/market validation'),
('Business Capability Model','16PRD, capability table, role intent','PARTIAL: actual workbook/account scope thiếu'),
('Detailed Processes / Use Cases / Triggers / State','J-L/J-S và trace audit','PARTIAL: workbook IDs/priorities UNKNOWN'),
('Staff / Content Operations','PRD14, J-S01/02, rubric, role intent','READY spec narrative; actual permission/publish runtime chưa có'),
('Privacy / Accessibility / Trust','V3docs07/10, purpose register, NFR notes','READY intent/limits; không compliance/runtime certification'),
('Requirements / Gaps / Priorities','Finding register và actual PRD','PARTIAL: requirement priority UNKNOWN'),
('UX / Wireframe Implications','61/175 catalog, selected232 tests','READY qualified; actual WF namespace chưa kiểm chứng'),
('Metrics / Evidence Gates','Measurement framework, check results','READY definitions/observed checks; không efficacy results'),
('Validation Plan','Wedge/usability/diary protocols','READY plan; execution vẫn VALIDATION DEBT'),
('Decision / Change Register','Approval source, decision/CR records','READY với DRAFT/deferred rõ'),
('GĐ1 Gate Conclusion','Gate Pack','NOT READY cho Approved; hiện phải ghi FAIL'),
('Appendices / Traceability / Evidence Register','Audit tables/logs/hash ledger','READY audit appendices; BA workbook appendix thiếu'),
]
put('ARTIFACT_UPDATE_PLAN.md','''# Kế hoạch cập nhật artifact — GĐ1

## BA Excel: 16 sheet

Actual file **NOT FOUND**. Không sửa hoặc tạo replacement giả. Chỉ dẫn dưới đây theo sheet/semantic action; chưa có row/cell locator đáng tin. Khi file có trong boundary, giữ structure/format, tìm đúng record, kiểm tra P0/P1 thực, log before/after và verify affected dependencies.

'''+tab(['Sheet','Thay đổi cần áp dụng','Ràng buộc'],sheet_actions)+'''
## Workbook quản lý dự án hiện có: các ô stale

File này khác BA workbook. Toàn bộ populated cells/formulas được đọc, không lưu hoặc sửa. Các action cụ thể:

| Sheet/Cell | Before | Action |
|---|---|---|
| 00_BAT_DAU!B17 | Phase2 chưa bắt đầu | Ghi current status có ngày/source hoặc phân loại historical |
| 01_TONG_QUAN!B7 | Phase1 là current phase | Đối chiếu Project State. B8/B9/B12 là formulas: cập nhật owning tasks/evidence trước, không hardcode dashboard |
| 02_SAN_PHAM!B86 | Original import/rerun pending | Map exact source/compatibility/fresh115+22, giữ domain runtime limit |
| 03_ROADMAP!F6 | Gate chưa pass | Phân biệt historical foundation gate, current regression và GĐ1 internal gate |
| 04_CONG_VIEC!F5:F7 | Import/rerun CHỜ/ĐANG LÀM | Map P1-T001..003 tới source/logs; không hàng loạt đánh các task DB/CI khác XONG |
| 05_VAN_DE_THAY_DOI!C6:D6 | II-01 chờ import/rerun | Record resolved source/mapping và AUD/CR mới theo scope; giữ lịch sử |
| 06_BANG_CHUNG!E8:E9 | CHỜ CHẠY | Thêm fresh run05/10 với115/22passed và boundary, không ghi đè packaged history |

Review dependencies/cached results/visual/native features sau khi sửa owning rows. Audit này giữ workbook nguyên checksum.

## Project Snapshot

Đã tạo snapshot05/10. Snapshot04/10 vẫn NOT FOUND; không tái tạo nội dung chưa đọc. Navigation snapshot cũ giữ nguyên; PROJECT_STATE thêm scoped GD1 FAIL, giữ engineering gates riêng.

## Final Word Report readiness

**NOT READY để phát hành Final GĐ1 Approved report.** Có thể viết qualified narrative draft, chưa được giả lập customer findings hoặc kết luận Approved. Audit cung cấp content/readiness plan; không tạo final DOCX giả.

'''+tab(['Section','Tên section','Nguồn đã có','Readiness / giới hạn'],[(i+1,*x) for i,x in enumerate(word_sections)])+'''
Format khi soạn Word chính thức: A4; Times New Roman13pt body; H1 15pt bold uppercase centered; H2 14pt; H3 13pt; margins top/bottom3cm,left3.5cm,right2cm; spacing1.5; justified; first-line indent1cm; TOC/captions/page numbering/formal tables. Render/verify từng trang. Viết narrative từ evidence/implications, không copy toàn workbook. Customer validation phải ghi VALIDATION DEBT.

## Handoff GĐ1–GĐ8

| System | Source of truth | Nội dung bàn giao |
|---|---|---|
| Linear | Portfolio/product/project | AUD001/003/005, scope decisions, gate/debt và candidateCRs; link audit |
| GitHub | Code/PR/CI/engineering execution | HEAD+dirty candidate hash boundary; future fixture issue có link Linear, không duplicate task vô nghĩa |
| Google Sheets | Quantitative KPI/budget/numerical tracking | Metric definitions/results có nguồn; không fabricate learning/value data |
| Google Docs | Official report/customer/investor/thesis | Qualified draft; final approval conclusion blocked |

Đây là local handoff plan; không ghi/publish/tạo task vào external systems. Mapping GĐ1–GĐ8 với Phase0–17 còn UNKNOWN.
''')

put('CHECK_RESULTS.md','''# Executed verification — 05/10/2026

Windows/PowerShell; V3.2 và backend Python3.12.10; Node24.19.0; Flutter3.32.8/Dart3.8.1. Bundled Python chỉ dùng đọc workbook/evidence. Repo main/HEADa112f762..., dirty candidate. Baseline checks chạy trước corrections, không sửa test hoặc original files.

| Check | Command | Expected | Actual | Result |
|---|---|---|---|---|
| Original V3.2 | `.local/v32-venv/Scripts/python.exe -X utf8 04_Van_hanh/Scripts/check_original_contracts.py` | 115 contract +22 SQL, hashes intact | 115/0failed,22/0failed,102hashes; npm/contract/sql exits0 | PASS — SQL PGlite |
| Dependencies | `.local/v32-venv/Scripts/python.exe -m pip check` | Không broken requirements | Không broken requirements | PASS |
| Adapter guards | `.local/v32-venv/Scripts/python.exe -m unittest discover -s 04_Van_hanh/tests -v` | 9 additive guards | 9passed,0failed,0skip | PASS; không cộng vào115/22 |
| Backend | `.venv/Scripts/python.exe -m pytest 01_San_pham/backend/tests -q --junitxml=03_Kiem_thu/Bang_chung/gd1_consistency_20261005/backend.xml` | Environment-supported cases | 9passed,7skipped,0failed | PARTIAL EXECUTION |
| Flutter shared package | `flutter test test/fixture_test.dart test/independent_test.dart test/presentation_test.dart --reporter json` | 3 unchanged test files | 232passed,0failed,0skipped; exit0 | PASS presentation/widget/golden |
| Legacy static | `MINGO_QA_OUTPUT=<audit>/legacy_static`; `python -X utf8 04_Van_hanh/Scripts/verify_phase2_artifacts.py` | Inherited spec metadata | 57screens,18components,16PRD,94QA,0errors | PASS at legacy spec scope |
| Current evidence verifier | `python -X utf8 <audit>/run_current_verifier.py` | Existing conditions, preserve historical report | 19checksPASS,0errors | PASS integrity of recorded evidence |
| Fresh structural extraction | Bundled Python `-X utf8 <audit>/collect_evidence.py` | Exact ID/set consistency | 16PRD/61screens/175states; zero dangling/missing/duplicate | PASS structure |
| Native PostgreSQL | NOT EXECUTED with --run-postgres | Disposable native DB cases | 6 foundation PG cases skipped | NOT EXECUTED |
| Mobile/domain fault scenarios, real auth/offline/deletion/restore | NOT EXECUTED | Runtime acceptance | Handlers/queues not implemented in current source | NOT EXECUTED |
| Physical device/TalkBack/human studies | NOT EXECUTED | Device/human evidence | No run in this audit | NOT EXECUTED |
| Hosted CI for dirty candidate | NOT EXECUTED | Exact candidate CI | Workflow inspected, no dispatch/push | NOT EXECUTED |
| Actual BA workbook checks | NOT EXECUTED | Full P0/P1/RTM/WBS semantics | NOT FOUND | BLOCKED |

Backend7skip gồm6 PostgreSQL và1 Windows symlink privilege. XML/log giữ reasons. Historical foundation6/6 không thay fresh native evidence. Selected Flutter232 khác prior full275 do test subset; không phải drift115/22. Legacy57 và current61 là hai source boundaries, không ép số khớp.

Original run: `03_Kiem_thu/Bang_chung/v3_2/20261004T181105665514Z/`, package3.2.0. ManifestSHA `617245605096b3b9cc5f141dda352abc180d97f11738297949c3195711cc0e6d`. UTC04/10 18:11:05 tương ứng05/10 Asia/Saigon.

Current verifier wrapper không đổi conditions/input; chỉ redirect sole report write sang audit evidence. Các số50/274/275 trong output được đọc từ runs20261003, không chạy lại ở audit này. Prior report nguyên byte. `docs/12_ACCEPTANCE_TESTS_V3.md` là acceptance plan, không phải toàn bộ scenarios executed.

Logs/XML/JSON, source hash ledger và post-fix validation nằm trong `03_Kiem_thu/Bang_chung/gd1_consistency_20261005/`. Post-fix checks không rerun runtime suites vì corrections chỉ ở documentation, nhưng kiểm chứng originals/protected source, expected edits, navigation links và report counts.
''')

snap='''# MINGO PROJECT PROGRESS SNAPSHOT — 2026-10-05

Ngày05/10/2026,Asia/Saigon. Snapshot có ngày để tiếp tục công việc; current phase authority vẫn PROJECT_STATE và architecture authority là V3.2. Requested snapshot04/10 NOT FOUND, không tái dựng nội dung chưa đọc.

- Mingo dùng finite meaningful cycle và truthful next action; ML optional. Server quyết định score/progress/permission; command tách telemetry; published content immutable/pinned; event/knowledge time và exact source capture tách biệt.
- Repo C:/Mingo, main, HEADa112f762ab08f6fa688cc4857b21d95d1055ab5c, dirty từ trước. URLmingo/mingle cùng GitHubID1388925852, canonicalPhucht59/mingle. Không commit/push/PR.
- Fresh evidence:102originalhashes intact;115/115contracts+22/22PGliteSQL;guard9/9;backend9pass/7skip;Flutterselected232pass;structural16PRD/61screen/175state,zero dangling. Không native domain/offline/auth/restore/physical/human/hosted CI run cho candidate này.
- PO approve current GĐ1 conclusions/principles ngày04/10/2026 theo supplied instruction, đã ghi scope trong Decision Register. Hypotheses/deferred/FUTURE/research giữ nguyên; không ký Phase2 human/physical/content gates.
- **GĐ1 Internal BA gate: FAIL — chưa đóng.** AUD001BLOCKER: actual16-sheetBAworkbook thiếu. AUD003HIGH: full workbook P0/P1 semantic trace/priority chưa verified. AUD005HIGH: account lifecycle BA/scope thiếu trong repo, có thể đã có trong workbook cần đọc.
- Safe docs fixes: Charter/PRD/Evidence/Decision status, actor/glossary/NFR/privacy intent, scoped Project State. AUD002/004/006/008 FIXED ở phạm vi repo docs. Code/tests/goldens/V3.2/workbook/lịch sử nguyên byte.
- CR-GD1-001 account lifecycle DRAFT: reconcile actual approved workbook trước khi xin quyết định mới. CR-GD1-002 optional goal/first Home/resume fixture DRAFT, non-blocking implementation debt. Không đề xuất V3.2 amendment.
- Customer discovery **VALIDATION DEBT**. SegmentVietnam18–35/beginner,exact5m,placement6–9,goal categories/thresholds/streak/rewards/pricing/Home ranking vẫn hypotheses. Không claim customer/market validation hoặc learning/ML efficacy.
- Deferred: final mastery/risk/production weights, advanced intervention/speaking, child/guardian;7futurestaff placeholders;OULAD/UCIresearch only.
- EngineeringPhase1 foundation đã có closure riêng;Phase2 human/product gate pending;Phase3HOLD. Mapping businessGĐ1–GĐ8↔Phase0–17 UNKNOWN.
- Tiếp theo: đọc actual BA workbook, N06→WF10/WBS1.11, toàn bộ actualP0/P1 và account flows; áp dụng safe updates có locator thực; đóng3criticalitems rồi xét InternalBAApproved kèm customerVALIDATIONDEBT. Final Word Approved report NOT READY; qualified draft plan đã có.

[Full audit](../../03_Kiem_thu/Bao_cao/GD1_Consistency_Audit_20261005/EXECUTIVE_AUDIT.md) · [Gate Pack](../../03_Kiem_thu/Bao_cao/GD1_Consistency_Audit_20261005/GATE_PACK.md) · [Update plan](../../03_Kiem_thu/Bao_cao/GD1_Consistency_Audit_20261005/ARTIFACT_UPDATE_PLAN.md). Evidence: `03_Kiem_thu/Bang_chung/gd1_consistency_20261005/` và original run`20261004T181105665514Z`.
'''
(R/'02_Tai_lieu_du_an/07_Tien_do_du_an/MINGO_PROJECT_PROGRESS_SNAPSHOT_2026-10-05.md').write_text(snap,encoding='utf-8')
print('Final report, gate, fix log, check results, update plan and snapshot edited for readability.')

matrix=[
('Architecture','docs01: frozen modular monolith','README, API/worker và stack khớp','PASS trong repo; workbook UNKNOWN','001/002'),
('Authority','docs01/02/07: server score/progress/permission','Compatibility map; API health; UI sample disclosed','CONTRACT VERIFIED; domain runtime chưa chạy','001/011'),
('Content versioning','docs02/04: immutable/pinned release/revision','PRD14; staff draft/review/publish/new draft','SPEC CONSISTENT; permissions triển khai sau','001/004'),
('Learning evidence','Finalized attempt immutable; telemetry observational','PRD02–04/Evidence; first/hint/skip tests','SPEC+FIXTURE VERIFIED; chưa full domain','001/008/011'),
('Assessment','Full answer set; không offline canonical scoring','Optional/provisional placement; retry new attempt theo mapping','SPEC CONSISTENT; metadata conditions triển khai sau','001/011'),
('Offline','docs03/04: durable IDs, receipts, grants, revision','UX states đúng; chưa durable mobile queues','CONTRACT VERIFIED / RUNTIME NOT YET VERIFIED','001/011'),
('Telemetry','Observation; server validates object context','Purpose register; collection disabled','SPEC CONSISTENT; collection NOT RUN','006/011'),
('Analytics','docs05: exact captured membership/read view','Compatibility map; không timestamp-only replay','CONTRACT VERIFIED; runtime capture chưa chạy','001/011'),
('Recommendation','docs09: Decision/Exposure/Execution/Outcome','PRD13/16; first Home/resume wiring gap','PARTIAL: spec đúng, fixture drift','010'),
('ML optionality','Optional risk; candidate model fixtures','PRD16/IV05; research datasets tách production','PASS principle/fixture; ML efficacy UNKNOWN','011'),
('Privacy','docs07/10: scope/generation/restore','Purpose/minimization + new notes; account flow thiếu','PARTIAL; chưa thấy blocking legal contradiction','005/006'),
('Actor','docs07 object scopes','New role intent notes; assignment/segregation pending','FIXED repo intent; workbook UNKNOWN','004/001'),
('Account','Identity/delete/export technical boundaries','Profile/preferences/reauth; chưa complete lifecycle BA','FAIL BA evidence completeness','005/001'),
('Staff/content','Content admin scope; immutable publish/access state','J-S01/02;S030–037; license/review test','SPEC+FIXTURE VERIFIED; actual server permissions sau','004/011'),
('NFR','Reliability/security/integrity/restore rules','Accessibility/performance/offline specs + checklist','FIXED consolidation; runtime pending','006'),
('Scope','Frozen types/action catalog; không new infra','7 future staff routes; account scope chưa rõ','PARTIAL; không demonstrated architecture defect','003/005'),
('Traceability','Exact compatibility matrix có','16PRD→screen/QA; workbook BR/UC/priorities chưa verified','FAIL full internal closure evidence','001/003'),
]
matrixrows=[(a,v,'NOT FOUND','04/10 NOT FOUND; new05/10 records limit',repo,status,','.join('AUD-'+x.zfill(3) for x in ids.split('/'))) for a,v,repo,status,ids in matrix]
tr=[
('PRD-01','Finite cycle, closure, opt-in; PRD01/Feed§3,7','Start/continue lesson','J-L01/J-L03;Feed§3–7','Không infinite feed/forced timer; presentation tests','Workbook/priority UNKNOWN; valid content runtime triển khai sau'),
('PRD-02','Giữ first response; retry sau finalize dùng new attempt; V3docs02§5','Wrong→feedback→retry','J-L04','First wrong còn nguyên sau correct retry; fixture test/IV01','Condition schema/runtime deferred; không overwrite first response'),
('PRD-03','Assisted!=unaided; Check không pre-submit hint; Evidence§2/4','Request hint / enter Check','J-L05/J-L07','Hint context giữ; fixture Check từ chối hint/retry/skip','Missing context vẫn unknown; không certify từ thiếu telemetry'),
('PRD-04','Skip không completion/mastery; V3 không partial submit','Explicit practice skip','J-L06/J-L13','Không first response/completion; fixture test/IV02','Threshold vẫn hypothesis; skip không gửi scored completion'),
('PRD-05','Play policy khác physical listens/score; V3docs07/mapping','Replay / media unavailable','J-L07/J-L15','Budget/error tests; unavailable media chặn Check','Cap/accessibility comparability hypothesis; native listening chưa verified'),
('PRD-06','Teaching/retrieval/transfer/check tách; PRD06/Feed§3','Choose objective/modality','J-L14/J-L15;Feed§3','Task-specific answer/explanation và changed contexts','QA anchors P1; formal requirement priority UNKNOWN; content review pending'),
('PRD-07','Hai distinct unaided first responses, gồm Check; bounded challenge; PRD07/Feed§5','Eligible provisional evidence predicate','Feed§5; eligible/locked objective flow','Sample challenge/locked start; QA-BIZ006 inherited','Predicate hypothesis; chưa native evidence computation'),
('PRD-08','Focus trong eligibility; bounded due/prerequisite insertion; PRD08/Feed§4,6','Choose focus; due/prerequisite available','J-L03;Feed§4–6','Reason/locked/current states; QA-BIZ007 inherited','Cap/ranking hypothesis; server scheduler deferred'),
('PRD-09','Placement optional, skip valid, result provisional; PRD09','First-use choose/skip offer','J-L01/J-L02','L004 skip; L006 insufficient evidence; không certification','6–9 configurable; one sample item không là final placement'),
('PRD-10','Goal optional/editable preference, không bypass; qualitative profile; PRD10','Choose/skip/edit goal; view evidence','J-L01/J-L02/J-L11;L052','Missing evidence/no mastery%; actual goal fixture gap','AUD009 default/no missing state; categories hypothesis'),
('PRD-11','Habit khác mastery; idempotent day policy; PRD11','Qualifying retrieval+feedback per day','Feed engagement; PRD11 acceptance','Habit copy tách learning; QA-BIZ009 inherited','Mechanics/timezone hypothesis; reward runtime chưa có'),
('PRD-12','Reward không đổi mastery/eligibility; PRD12','Milestone theo versioned policy','Feed engagement; summary/profile flow','Không XP/shop; QA-BIZ010 inherited','Mechanics hypothesis; chưa production awards'),
('PRD-13','Locked preview không unlock; reason auditable; PRD13/V3docs09','Open course/preview/next action','J-L08/J-L10','Locked recovery; IV05 fallback; Home gap','AUD010 first Home/resume wiring; priority chưa frozen'),
('PRD-14','License/review blocking; published immutable; V3docs02/04','Draft→review→publish→new revision','J-S01/J-S02; role intent notes','IV03 direct confirmation blocked; sample license/review flow','Assignment policies pending; access status khác editorial states'),
('PRD-15','Command!=telemetry; receipt/revision/source capture; V3docs03–05','Offline/network restore/retry/late arrival','J-L09/J-L12; offline UX table','Original115+22; 175 states; pending khác ack','Durable queues/native concurrency/process restart NOT EXECUTED'),
('PRD-16','ML/recommendation OFF fallback; no content→honest empty; V3docs01/06','Service/model unavailable','J-L10; Feed fallback','IV05/fixture fallback; L063 empty state','Real server eligibility/scheduler triển khai sau'),
]
sources={x['prd']:x for x in json.loads((E/'prd_trace_source.json').read_text(encoding='utf-8'))}
struct=json.loads((E/'structural_audit.json').read_text(encoding='utf-8'))
trace=[]
for id,rule,trigger,uc,ac,gap in sorted(tr,key=lambda x:(x[0]=='PRD-06',x[0])):
 s=sources[id]; p=','.join(sorted({q['priority'] for q in struct['qa_priority_by_requirement'][id]}))
 trace.append((id+'; req priority UNKNOWN; QA '+p,rule,trigger,uc,s['screens'],ac+'; '+s['qa'],'SPEC CONSISTENT / WORKBOOK UNKNOWN',gap))
decisions=[
('V3.2/stack/server authority','ĐÃ CHỐT','README/V3.2/hashes và fresh115+22','YES','Không architecture change'),
('Finite cycle/no infinite feed/no forced timer','ĐÃ CHỐT','PRD01/Feed/EG05–06','YES','Duration tách hypothesis'),
('First response/assistance/skip','ĐÃ CHỐT','PRD02–04/Evidence/tests','YES sau terminology fix','Retry sau finalize new attempt'),
('Qualitative progress/no fake precision','ĐÃ CHỐT','PRD10/Evidence/EG16','YES','Không validated mastery% giả'),
('Short onboarding/no early bottom nav','ĐÃ CHỐT direction','L001–006 không thuộc main navigation list','YES source/presentation','Termination durability chưa verified'),
('Optional/editable goal','ĐÃ CHỐT principle','PRD10 status corrected; fixture còn default/no skip','PARTIAL','CR-GD1-002; categories hypothesis'),
('Optional/provisional placement','ĐÃ CHỐT principle','J-L01/02;L004/L006','YES','Count/cutoff configurable'),
('Exact5m/placement6–9','GIẢ THUYẾT CẦN KIỂM CHỨNG','PRD01/09/config/EG06','YES','Không timer hoặc production invariant'),
('Vietnam18–35/beginner-rebuilder','GIẢ THUYẾT CẦN KIỂM CHỨNG','Initial wedge E0 pending; Charter candidate','YES','Không customer-validated claim'),
('Retry/replay/skip/challenge/focus thresholds','GIẢ THUYẾT CẦN KIỂM CHỨNG','PRD02/04/05/07/08, Feed/rubric','YES','Defaults versioned/configurable'),
('Exact Home priority','Approved direction / GIẢ THUYẾT CẦN KIỂM CHỨNG','Spec/helper, actual default due/no resume wiring','PARTIAL','CR-GD1-002; không freeze order'),
('Streak/rewards/pricing','GIẢ THUYẾT CẦN KIỂM CHỨNG','PRD11/12; free-first/future pricing','YES','Không engagement→mastery'),
('Rule-based core/ML OFF','ĐÃ CHỐT','PRD16/EG17/IV05','YES fixture/spec','Runtime eligibility sau'),
('Final mastery/risk/weights/intervention','ĐỂ GIAI ĐOẠN SAU','PRD scope/INTEL001–005','YES','Không spec weights/algorithm'),
('OULAD/UCI production use','RESEARCH ONLY / ĐỂ GIAI ĐOẠN SAU','EG21/model fixtures candidate','YES','Không promote research fixture'),
('Child/Guardian/advanced speaking','ĐỂ GIAI ĐOẠN SAU / FUTURE','Closure role intent/PRD scope','YES','Separate future privacy/safety domain'),
('Account MVP inclusion/policies','CHƯA QUYẾT ĐỊNH ở nguồn có; UNKNOWN trong workbook thiếu','Phase3HOLD; profile/reauth only','NOT VERIFIABLE','CR001; reconcile approved workbook trước'),
('PO approval04/10','ĐÃ CHỐT scoped conclusions','Direct user instruction/Decision Register','YES scoped','Không ký Phase2/customer/physical gates'),
('Customer/learning/value validation','VALIDATION DEBT','E0–E3 pending; không actual dataset','YES','Actual consented discovery/pilot cần thực hiện'),
]
coverage=[
('First launch/onboarding','IN MVP direction','L001/002;J-L01','Short CTA/no bottom nav; termination durability chưa verified'),
('Account/restore/signup/login/logout/recovery/session/device/state','DEFERRED implementationPhase3; MVP scope UNKNOWN','L064;V3docs07;roadmap','AUD005: complete business lifecycle chưa có'),
('Goal/edit/skip','IN MVP principle; categories HYPOTHESIS','PRD10;L003/L052','AUD009: default/no explicit missing goal state'),
('Optional placement','IN MVP direction; count HYPOTHESIS','L004–006;J-L01/02','Skip/provisional đúng; sample không final placement'),
('Recommendation/ML OFF/fallback','IN MVP; exact ranking HYPOTHESIS','PRD13/16;L010/L063;IV05','AUD010 wiring; server scheduler chưa có'),
('Resume/pause/exit/interruption','IN MVP baseline','L033;J-L12;history/back tests','In-memory state; app termination/durability chưa verified'),
('Browse/search/course/map/preview','IN MVP direction','L020/L040–042/L071;PRD13','Preview không unlock; không new domain API'),
('Start/answer/hint/replay/skip/explanation/retry','IN MVP principles; limits HYPOTHESIS','PRD01–06;L021–025/L028–031','Fixtures giữ first/assistance/skip; server domain sau'),
('Independent Check/result/closure','IN MVP principles','L026/027/L032;J-L07','Không hint/skip/retry Check; summary không mastery'),
('Review/spaced return/after absence','IN MVP direction; cadence HYPOTHESIS','J-L03;Feed due policy','Long absence exact policy chưa complete'),
('Progress','IN MVP principle','L050/051/L070;PRD10','Qualitative evidence/uncertainty'),
('Offline/download/sync/download management','IN MVP contract; Phase6 implementation DEFERRED','L011/012/L054/L060/061;V3docs03/04','Actual durable queues/package fault tests chưa chạy'),
('Settings/preferences/accessibility/context','IN MVP direction','L053/L072; accessibility specs','Voluntary context; no diagnosis; TalkBack pending'),
('Content issue/disagreement','CHƯA QUYẾT ĐỊNH / UNKNOWN scope','Không tìm canonical issue-report BA chain','Không tự thêm screen'),
('Deletion/export','DEFERRED implementation; MVP boundary UNKNOWN','V3docs10','AUD005 business request/status/failure missing'),
('Notification fatigue/preferences','HYPOTHESIS; delivery DEFERRED','L073; notifications=false fixture','Toggle có; actual delivery/fatigue policy UNKNOWN'),
('Author/preview/review/return/approve/publish/new revision','IN MVP planned content operations','S030–037;J-S01/02;PRD14','Role intent có; permission runtime sau'),
('Advisor/intervention/analytics/admin','DEFERRED / FUTURE','7 explicit staff placeholders','Không production features'),
('Advanced speaking/child/ML/intervention','FUTURE / DEFERRED; datasets RESEARCH ONLY','PRD/Decision Register','Không detailed weights/algorithm mới'),
('Infinite feed/XP farm/leaderboard/learning-style profiling','OUT','PRD12/EG07/product principles','Không thêm implementation'),
]
edges=[
('Interruption/app termination','IN MVP recovery intent','J-L12/L033','Back state verified; process restart/durable queue NOT EXECUTED'),
('Return after long absence','IN MVP direction; exact policy UNKNOWN','Feed/J-L03','Không infer psychology; cần valid eligible next action'),
('Offline during learning/assessment','IN MVP contract; implementation DEFERRED','V3docs04/J-L09/J-L15','Pending canonical score; essential media missing blocks Check'),
('Network restored but commands pending / sync retry','IN MVP contract','V3docs03/offline UX','Network!=ack; same ID/payload retry'),
('Duplicate replay / ordering','IN MVP contract','V3docs02/03','Immutable receipt, progress anti-rollback, batch order explicit'),
('Stale/partial/corrupt download','IN MVP contract','V3docs04;L054','Checksums/pinning; actual faults NOT EXECUTED'),
('Insufficient storage','IN MVP contract','V3docs04 media/queue budgets','Không evict pending commands; halt new work khi queue full; runtime chưa chạy'),
('Device change','DEFERRED implementation; MVP scope UNKNOWN','Session/installation binding','Account flow missing; AUD005'),
('No eligible content','IN MVP direction','PRD16/L063','Honest empty; không fake completion'),
('Revision changed / retire / revoke','IN MVP contract','V3docs02/04','Old attempt pinned; no silent denominator change'),
('Learner rejects recommendation','IN MVP direction; full rejection policy UNKNOWN','Dismissed execution/browse alternative','Giữ eligibility; không causal outcome claim'),
('Goal changes','IN MVP principle','PRD10/L052','Không rewrite ability/bypass prerequisite'),
('Content issue/disagreement','CHƯA QUYẾT ĐỊNH scope','BA chain NOT FOUND trong nguồn có','Record gap; không tự thêm capability'),
('ML/recommendation unavailable','IN MVP baseline','PRD16/J-L10/IV05','Deterministic eligible fallback hoặc empty'),
('Deletion/export','DEFERRED implementation; MVP scope UNKNOWN','V3docs10','Generation/restore lock rules có; business front flow thiếu'),
('Notification fatigue/preferences','HYPOTHESIS / DEFERRED delivery','L073/preference toggle','Không implemented delivery policy; không forced reminder'),
]
known=[('N-06→WF-10','UNKNOWN / NOT VERIFIED','Actual workbook NOT FOUND; WF namespace khác L namespace'),('WBS1.11 DONE','UNKNOWN / NOT VERIFIED','Không có actual row/status; không gọi FIXED'),('Repo dangling reference','PASS structure','16PRD/61screens/175states; zero dangling refs'),('Full workbook P0/P1 semantics','FAIL evidence completeness','Requirement priority UNKNOWN; không thay bằng QA priority'),('Actor model','FIXED repo intent','Assignment details pending; workbook chưa verified'),('Account lifecycle','FAIL available BA coverage','Có thể đã có trong missing workbook; reconcile trước new decision'),('Staff lifecycle','PASS spec/fixture boundary','J-S01/02; license/review/direct confirmation checks'),('NFR/privacy','FIXED consolidation; runtime pending','Không arbitrary SLA/TTL; collection disabled')]
put('AUDIT_TABLES.md','''# Consistency, traceability và decision tables — 05/10/2026

Labels: PROJECT SOURCE = artifact đã kiểm tra; EXECUTABLE EVIDENCE = actual run; EXTERNAL EVIDENCE = nguồn ngoài; INFERENCE = mapping có căn cứ; HYPOTHESIS = policy chưa validated; VALIDATION DEBT = external evidence chưa đủ. UNKNOWN/NOT FOUND/NOT EXECUTED không là PASS.

## Consistency Matrix

'''+tab(['Area','V3.2','Workbook','Snapshot','Repo','Status','Finding IDs'],matrixrows)+'''
## Traceability Audit — toàn bộ16 repository PRDs

BR/Trigger/UC mappings dưới đây là INFERENCE dựa trên rule text và journey/flow có nguồn, không dựng workbook IDs. Text node phù hợp có thể đủ; không bắt buộc mọi node là artifact/screen riêng. P0 QA anchors được xếp trước PRD06 có P1 QA; **actual requirement priority UNKNOWN**, nên chưa certify toàn bộ workbook P0/P1.

'''+tab(['Requirement','BR','Trigger','UC/Flow','Screen/State','Acceptance/Test','Result','Gap'],trace)+'''
Semantic conclusions: full-answer submit tương thích với skip vì skip không tạo scored completion. Retry sau finalized attempt dùng new attempt ID. Assistance/replay context không thay score formula. Offline Check không có canonical offline scoring; client playback không chứng minh physical listens. Historical analytics phải dùng exact SourceCapture membership/read view, không query current data bằng wall-clock cutoff cũ. Editorial lifecycle và ReleaseAccessStatus là hai lớp khác nhau.

Không orphan repo PRD trong16-row map; zero dangling screen/QA ID. 27 routes không direct-map ở PRD CSV là diagnostic, không phải27 unauthorized features: feedback/resume/settings/search/staff substeps có supporting sources và7future routes explicit placeholders. Tập ID đầy đủ nằm ở structural_audit.json. Actual BR orphan và priorities của missing workbook vẫn UNKNOWN.

## Decision/Hypothesis Audit

'''+tab(['Decision','Expected Status','Artifact Status','Consistent?','Action'],decisions)+'''
## Known prior audit candidates

'''+tab(['Candidate','Result','Evidence / limitation'],known)+'''
## Capability Coverage

DEFERRED implementation không tự quyết định capability OUT of MVP. Nếu source không đủ thì ghi scope UNKNOWN/CHƯA QUYẾT ĐỊNH; không invent inclusion để lấp bảng.

'''+tab(['Capability','Scope','Source','Coverage / gap'],coverage)+'''
## Edge Cases

'''+tab(['Case','Scope','Source','Coverage / gap'],edges))
print('All matrix/trace/decision/coverage tables rewritten with readable labels.')
