from pathlib import Path
import json, csv, re, hashlib, sys
root=Path(__file__).resolve().parents[2]
p2=root/'02_Tai_lieu_du_an/04_Thiet_ke_san_pham'/'ux_ui'/'phase2'
q=root/'03_Kiem_thu/QA_QC/phase2'
required=[
 p2/'01_PHASE_2_CONTRACT.md',p2/'02_INFORMATION_ARCHITECTURE.md',p2/'03_LEARNER_JOURNEYS.md',p2/'04_STAFF_JOURNEYS.md',
 p2/'05_NAVIGATION_ROUTING_SPEC.md',p2/'06_SCREEN_SPECIFICATIONS.md',p2/'07_UI_STATE_CATALOG.md',p2/'08_DESIGN_SYSTEM_SPEC.md',
 p2/'DESIGN_TOKENS.json',p2/'09_ACCESSIBILITY_RESPONSIVE_SPEC.md',p2/'10_CONTENT_MICROCOPY_GUIDE.md',p2/'11_OFFLINE_SYNC_UX_SPEC.md',
 p2/'12_UX_REQUIREMENT_TRACEABILITY.md',p2/'13_DEVELOPER_HANDOFF.md',p2/'PHASE_2_SPEC.json',p2/'prototype'/'index.html',p2/'prototype'/'styles.css',p2/'prototype'/'app.js',
 q/'PHASE_2_GATE.md',q/'QA_TEST_PLAN.md',q/'QC_REVIEW_CHECKLIST.md',q/'UAT_SCENARIOS.md',q/'ACCESSIBILITY_TEST_PLAN.md',q/'QA_DEFECT_SEVERITY.md',q/'QA_TEST_CASES.csv'
]
errors=[]
for f in required:
    if not f.is_file() or f.stat().st_size==0: errors.append(f'missing/empty: {f.relative_to(root)}')
spec=json.loads((p2/'PHASE_2_SPEC.json').read_text(encoding='utf-8'))
tokens=json.loads((p2/'DESIGN_TOKENS.json').read_text(encoding='utf-8'))
ids=[s['id'] for s in spec['screens']]
if len(ids)!=len(set(ids)): errors.append('duplicate screen ids')
if len(spec['screens'])<50: errors.append('screen inventory unexpectedly small')
prds=[x['prd'] for x in spec['prd_traceability']]
expected=[f'PRD-{i:02d}' for i in range(1,17)]
if sorted(prds)!=expected: errors.append(f'PRD mapping mismatch: {prds}')
if spec.get('gate')!='NOT_PASSED_UNTIL_QC_QA_SIGNOFF': errors.append('phase2 gate state incorrect')
if tokens.get('meta',{}).get('brand_lock') is not False: errors.append('reference theme incorrectly brand-locked')
html=(p2/'prototype'/'index.html').read_text(encoding='utf-8')
css=(p2/'prototype'/'styles.css').read_text(encoding='utf-8')
js=(p2/'prototype'/'app.js').read_text(encoding='utf-8')
combined=html+'\n'+css+'\n'+js
if re.search(r'https?://|//cdn\.|@import\s+url', combined, flags=re.I): errors.append('prototype contains external network dependency')
if 'mastery 83' in combined.lower(): errors.append('prototype contains fake mastery percentage')
with (q/'QA_TEST_CASES.csv').open(encoding='utf-8-sig') as f:
    cases=list(csv.DictReader(f))
if len(cases)<80: errors.append('QA case count unexpectedly small')
if not any(c['priority']=='P0' for c in cases): errors.append('no P0 QA cases')
# Check no phase2 secret-ish strings
secret_pattern=re.compile(r'(?i)(password\s*[:=]\s*[^<\s]+|postgresql://[^\s]+:[^@\s]+@|ghp_[A-Za-z0-9]+)')
for f in list(p2.rglob('*'))+list(q.rglob('*.md')):
    if f.is_file() and f.suffix.lower() in {'.md','.json','.csv','.html','.js','.css'}:
        txt=f.read_text(encoding='utf-8', errors='ignore')
        if secret_pattern.search(txt): errors.append(f'possible secret pattern: {f.relative_to(root)}')
result={'status':'PASS' if not errors else 'FAIL','screens':len(ids),'components':len(spec['components']),'prd_coverage':len(prds),'qa_cases':len(cases),'errors':errors}
print(json.dumps(result,indent=2))
output = Path(__import__('os').environ.get('MINGO_QA_OUTPUT', str(q/'evidence'/'verification_runs'/'artifacts')))
output.mkdir(parents=True, exist_ok=True)
(output/'internal_static_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
sys.exit(0 if not errors else 1)
