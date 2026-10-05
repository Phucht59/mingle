# Kế hoạch cập nhật artifact — GĐ1

## BA Excel: 16 sheet

Actual file **NOT FOUND**. Không sửa hoặc tạo replacement giả. Chỉ dẫn dưới đây theo sheet/semantic action; chưa có row/cell locator đáng tin. Khi file có trong boundary, giữ structure/format, tìm đúng record, kiểm tra P0/P1 thực, log before/after và verify affected dependencies.

| Sheet | Thay đổi cần áp dụng | Ràng buộc |
| --- | --- | --- |
| 00_Dashboard | Hiển thị GĐ1 internal gate FAIL, scoped approval04/10 và customer VALIDATION DEBT | Status dẫn từ register/gate, không static PASS |
| 01_Huong_dan | Ghi hierarchy, classifications và các mức evidence | GĐ1 nghiệp vụ khác engineering Phase1 |
| 02_Roadmap_8_GD | Giữ roadmap8GĐ; link roadmapPhase0–17 | Mapping chưa có: UNKNOWN, không tự quy đổi |
| 03_Yeu_cau_Nghiep_vu | Đọc actual P0 rồi P1; check account/learner/staff/NFR scope và AC | So16repoPRD; không tạo giả requirement priority |
| 04_Business_Rules | Map frozen principles tới exact V3.2/rule text | Numeric policies giữ HYPOTHESIS |
| 05_UseCase_Trigger | Trace actor/precondition/trigger/flow/alternative/failure | J-L/J-S có sẵn; account gap cần actual source |
| 06_User_Journey | Check first-use, return/resume/absence và offline flows | Goal/placement optional; Home priority chưa freeze |
| 07_RTM | Kiểm tra semantic chains, orphan/dangling/duplicate meaning | N-06→WF-10 chưa verified; không đổi sang L-010 bằng suy đoán |
| 08_Wireframe_Learner | Kiểm kê actual WF IDs và first-use/state meanings | Không bottom nav trước shell; không screen riêng cho mọi capability |
| 09_Wireframe_Staff | Check draft/review/license/publish/new revision và role intent | Published immutable; FUTURE placeholders giữ nguyên |
| 10_WBS | Đối chiếu item1.11 với actual traceability DoD | ACTIVE nếu incomplete; current row/status UNKNOWN |
| 11_RACI | Giữ project responsibility; link product actors riêng | RACI không cấp permission sản phẩm |
| 12_RAID | Ghi missing sources, account scope, validation/runtime/research debts | Phân biệt gate blocker với medium debt |
| 13_Research_Evidence | Tag PROJECT/EXECUTABLE/EXTERNAL/INFERENCE/HYPOTHESIS | Không fake customer validation; OULAD/UCI research only |
| 14_Decision_Log | Ghi scoped PO approval04/10 và candidate CR status | Không blanket-freeze hypotheses/deferred/FUTURE |
| 15_Test_Gate | Ghi115/22/9/232 và backend9/7 theo boundary | Contract/UI không là runtime PASS; internal gate FAIL |

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

| Section | Tên section | Nguồn đã có | Readiness / giới hạn |
| --- | --- | --- | --- |
| 1 | Executive Summary | Audit verdict, Charter, core promise | Draft có giới hạn; final gate FAIL |
| 2 | Research Method & Limitations | Evidence hierarchy, executed logs, missing artifacts | READY cho draft |
| 3 | Product / Problem Framing | Charter và approved direction | Internal framing; không claim measured prevalence |
| 4 | User Segmentation & JTBD | Initial Wedge Research Plan | HYPOTHESIS; chưa có validated ICP |
| 5 | Behavioral / Usage Context | Learning model, journeys, protocols | Conceptual context; actual customer behavior UNKNOWN |
| 6 | Learning-Science Synthesis | Scientific research resolution/evidence register | Dated synthesis; refresh citations cho official claims, không Mingo efficacy |
| 7 | Competitor / Market Context | Alternative research instrument/access limits | NOT READY cho current ranking/market validation |
| 8 | Business Capability Model | 16PRD, capability table, role intent | PARTIAL: actual workbook/account scope thiếu |
| 9 | Detailed Processes / Use Cases / Triggers / State | J-L/J-S và trace audit | PARTIAL: workbook IDs/priorities UNKNOWN |
| 10 | Staff / Content Operations | PRD14, J-S01/02, rubric, role intent | READY spec narrative; actual permission/publish runtime chưa có |
| 11 | Privacy / Accessibility / Trust | V3docs07/10, purpose register, NFR notes | READY intent/limits; không compliance/runtime certification |
| 12 | Requirements / Gaps / Priorities | Finding register và actual PRD | PARTIAL: requirement priority UNKNOWN |
| 13 | UX / Wireframe Implications | 61/175 catalog, selected232 tests | READY qualified; actual WF namespace chưa kiểm chứng |
| 14 | Metrics / Evidence Gates | Measurement framework, check results | READY definitions/observed checks; không efficacy results |
| 15 | Validation Plan | Wedge/usability/diary protocols | READY plan; execution vẫn VALIDATION DEBT |
| 16 | Decision / Change Register | Approval source, decision/CR records | READY với DRAFT/deferred rõ |
| 17 | GĐ1 Gate Conclusion | Gate Pack | NOT READY cho Approved; hiện phải ghi FAIL |
| 18 | Appendices / Traceability / Evidence Register | Audit tables/logs/hash ledger | READY audit appendices; BA workbook appendix thiếu |

Format khi soạn Word chính thức: A4; Times New Roman13pt body; H1 15pt bold uppercase centered; H2 14pt; H3 13pt; margins top/bottom3cm,left3.5cm,right2cm; spacing1.5; justified; first-line indent1cm; TOC/captions/page numbering/formal tables. Render/verify từng trang. Viết narrative từ evidence/implications, không copy toàn workbook. Customer validation phải ghi VALIDATION DEBT.

## Handoff GĐ1–GĐ8

| System | Source of truth | Nội dung bàn giao |
|---|---|---|
| Linear | Portfolio/product/project | AUD001/003/005, scope decisions, gate/debt và candidateCRs; link audit |
| GitHub | Code/PR/CI/engineering execution | HEAD+dirty candidate hash boundary; future fixture issue có link Linear, không duplicate task vô nghĩa |
| Google Sheets | Quantitative KPI/budget/numerical tracking | Metric definitions/results có nguồn; không fabricate learning/value data |
| Google Docs | Official report/customer/investor/thesis | Qualified draft; final approval conclusion blocked |

Đây là local handoff plan; không ghi/publish/tạo task vào external systems. Mapping GĐ1–GĐ8 với Phase0–17 còn UNKNOWN.
