# Mingo — gói nguồn và evidence ngày 2026-09-30

Đây là bản snapshot bàn giao theo yêu cầu đóng gói dự án. Không phải biên bản chốt Phase 2/3.

| Phase | Trạng thái đã có evidence |
|---|---|
| Phase 0 | DONE |
| Phase 1 | DONE / GATE PASSED |
| Phase 2 | ACTIVE / TECHNICAL RETEST PASS / GATE HOLD |
| Phase 3 — Identity/Auth/Authorization | DEFERRED; chưa triển khai; chưa đủ điều kiện bắt đầu |

Phase 2 là UX/UI, đặc tả, prototype mô phỏng, traceability và developer handoff. Production app/web/backend được triển khai ở các phase sau. Các shell Flutter và nền tảng backend Phase 1 có trong `05_code/`.

Independent R1: canonical 94/94 PASS, P0 44/44 PASS, D001–D020 CLOSED. D021 đã được chủ dự án chọn FIX NOW: chỉ sửa CSS toolbar QA; Windows browser 74/74, supplemental 30/30 và 320px/200% PASS. Linux/independent closure còn chờ. D022 có workbook derivative sửa 19 ô Dashboard; data/preservation PASS; final visual/independent confirmation còn chờ.

| Gate item | Trạng thái |
|---|---|
| Objective verification | Core PASS; report follow-up PENDING |
| Interactive TalkBack | BLOCKED BY ENVIRONMENT / NOT RUN |
| Tech Lead decision | PENDING |
| Product Owner UAT | PENDING |
| P2-D021 | FIX IMPLEMENTED; independent retest PENDING |
| P2-D022 | FIX IMPLEMENTED; confirmation PENDING |
| Phase 2 gate | HOLD / NOT PASSED |
| Phase 3 | DEFERRED |

## Đọc và kiểm tra gói

1. Đọc `06_quality/phase2/final_gate/2026-09-30/FINAL_GATE_STATUS.md`, `PHASE2_SCOPE_RECONCILIATION.md` và `FINAL_GATE_OBJECTIVE_VERIFICATION.md`.
2. Original independent report/JSON/workbook nằm trong `06_quality/phase2/final_gate/2026-09-30/inputs/`; corrected derivative nằm trong `outputs/phase2-completion-20260930/`.
3. TalkBack runbook, evidence template, Tech Lead packet và Owner UAT packet ở cùng thư mục final gate. Những trường quyết định/chữ ký còn trống.
4. Phase 1 closure: `08_handoff/PHASE1_CLOSURE_20260926.md`; nguồn ứng dụng: `05_code/README.md`.
5. Từ thư mục `Mingo`, chạy `python 07_operations/scripts/verify_phase2_package_manifest.py` để kiểm tra hash toàn bộ file. Kiểm tra này không ghi file.
6. Xem prototype: `python -m http.server 8765 --bind 127.0.0.1 --directory 02_product/ux_ui/phase2/prototype`, rồi mở `http://127.0.0.1:8765`. Đây là prototype UX mô phỏng.
7. Xem `START_HERE.md` và `07_operations/` để dựng môi trường Phase 1; dependency/runtime cài riêng. Chạy verifier có ghi evidence trên một bản sao để giữ bản bàn giao nguyên trạng.

`01_governance/` và hồ sơ cũ được giữ nguyên như lịch sử R1; một số dòng vẫn mô tả independent retest đang chờ. Evidence mới ngày 2026-09-29/30 ở final gate và `08_handoff/project_snapshot_20260930/PACKAGE_STATE.json` xác nhận technical retest đã PASS, nhưng không phê duyệt gate thay chủ dự án.

Toàn bộ 780 file tracked của R1 được xuất từ ZIP đã xác minh; chỉ overlay CSS đã kiểm thử và tái tạo package manifest. V3.2 originals, Phase 1 code/evidence và các workbook signoff gốc giữ nguyên byte từ R1. ZIP R1 gốc, companion manifest/checksum/handoff và manifest/CSS gốc được giữ trong `08_handoff/project_snapshot_20260930/provenance/`.

Không đóng gói `.git`, môi trường ảo, SDK cài trên máy, cache/build/node_modules, các bản giải nén tạm trùng lặp hoặc workbook local `Manage Project.xlsx` không thuộc candidate. Không ghi ACCEPTED, không ký tên, không đổi Phase 2/3 thành DONE.
