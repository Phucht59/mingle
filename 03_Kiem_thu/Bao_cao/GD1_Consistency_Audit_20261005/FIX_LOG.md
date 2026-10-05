# Safe fix log — 05/10/2026

Findings được ghi trước sửa. Không sửa V3.2, API/worker/Flutter sources, tests, goldens, workbook, dated snapshots hoặc historical evidence. Trước/sau SHA và preservation checks nằm trong evidence. Không commit/push/PR hoặc ghi task ra external systems.

| Fix ID | Finding | File/Sheet | Before | After | Why Safe |
| --- | --- | --- | --- | --- | --- |
| FIX-01 | AUD-008 | PRODUCT_CHARTER.md | Exact source pending, name chưa freeze | Ghi exact V3.2 available/verified, Mingo và scoped PO approval | Chỉ sửa status/authority |
| FIX-02 | AUD-008 | MVP_PRD.md | Goal principle hypothesis; source pending | Optional/editable principle approved; categories hypothesis; GĐ1 gate pending | Không đổi threshold/score |
| FIX-03 | AUD-008 | LEARNER_EVIDENCE_MODEL.md | First response gọi unaided; matrix pending | First response có assistance condition; matrix hoàn tất được link | Khớp invariant assisted đã có |
| FIX-04 | AUD-008 | DECISION_REGISTER.md | Chưa ghi GĐ1 approval04/10 | Ghi approval nguồn direct user và 5 classifications | Không ký human/customer gates |
| FIX-05 | AUD-004/006 | GD1_INTERNAL_BA_CLOSURE_NOTES_20261005.md | Role/glossary/NFR/privacy phân tán | Tổng hợp intent và legal metadata; pending policies rõ | Không thêm enum/SLA/TTL/collection |
| FIX-06 | AUD-002 | New dated snapshot05/10 | Snapshot04/10 NOT FOUND | Tạo continuation snapshot có giới hạn | Không dựng lịch sử chưa đọc |
| FIX-07 | AUD-001/003/005 | PROJECT_STATE.md | Chưa có scoped GD1 audit status | GĐ1 FAIL riêng với engineering phases | Không đổi Phase2/Phase3 gates |
| FIX-08 | AUD-005/009/010 | CHANGE_REQUESTS.md | Gaps chưa được register | Hai candidate DRAFT; reconcile actual workbook trước | Không implement business/code |

AUD-002/004/006/008 FIXED ở phạm vi repo documentation. AUD-001/003/005 còn chặn gate; AUD-007/009/010 vẫn OPEN, non-blocking debt.
