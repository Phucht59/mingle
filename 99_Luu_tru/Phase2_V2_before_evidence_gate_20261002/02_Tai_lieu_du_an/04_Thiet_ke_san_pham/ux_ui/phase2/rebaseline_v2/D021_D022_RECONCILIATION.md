# Independent R1 findings retained

| Finding | Old status | New evidence / applicability | Current status / next action |
|---|---|---|---|
| D021 QA-toolbar overflow320px/200% Linux | Owner FIX NOW; Windows fix/retest passed; Linux independent closure pending | V2 Flutter has no product QA toolbar; V2 responsive evidence applies only to V2 | R1 historical finding remains independent retest pending. Do not infer Linux closure. Test V2 separately and obtain reviewer disposition |
| D022 independent workbook dashboard | Corrected derivative only;94/44/94 counts and13other sheets preserved; final visual/independent confirmation pending | Original/derivative preserved; no workbook edited in V2. Hashes checked separately in V2 preservation evidence | R1 workbook visual and independent closure pending; report maintainer/QA must confirm. No new fabricated signoff |

Original supplied workbook hash6c3792d76628e894c46e814db933714a63b6669fd6bd936f1ac3b4d575438222. Corrected derivative hash e4fefc2f813c3b549d4f7263d974b157b1a17c537828519403c64f4e1758ad31. See preserved final_gate/2026-09-30 packets and original correction evidence. D001–D020 closure history is not reopened or rewritten by V2. Updated design requires a new independent technical/visual review before acceptance.

V2 final evidence2026-10-02: four Home/Learn/Course/Profile320px/200% cases PASS with captured goldens. D022 original and corrected derivative SHA256 both match (d022_preservation.json). No workbook was edited. R1 D021 Linux closure and D022 visual/independent acceptance remain PENDING; reviewer disposition is still required.
