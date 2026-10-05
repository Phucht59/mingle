from pathlib import Path
import json,csv,re,sys,hashlib
root=Path(__file__).resolve().parents[2]
p2=root/'02_Tai_lieu_du_an/04_Thiet_ke_san_pham'/'ux_ui'/'phase2'; q=root/'03_Kiem_thu/QA_QC/phase2'
required=[
 p2/'01_PHASE_2_CONTRACT.md',p2/'PHASE_2_SPEC.json',p2/'SCREEN_INVENTORY.csv',p2/'15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md',
 p2/'16_ACCESSIBILITY_FOCUS_LIVE_REGION_SPEC.md',p2/'17_SCREEN_STATE_QA_TRACEABILITY.md',p2/'SCREEN_STATE_QA_TRACEABILITY.csv',
 p2/'prototype'/'index.html',p2/'prototype'/'styles.css',p2/'prototype'/'app.js',q/'PHASE2_REWORK_R1_FIX_REGISTER.md',q/'QA_TEST_CASES.csv'
]
errors=[]
for f in required:
    if not f.is_file() or f.stat().st_size==0:errors.append(f'missing/empty: {f.relative_to(root)}')
spec=json.loads((p2/'PHASE_2_SPEC.json').read_text(encoding='utf-8'))
ids=[s['id'] for s in spec['screens']]
if len(ids)!=57:errors.append(f'expected 57 screens, got {len(ids)}')
if len(ids)!=len(set(ids)):errors.append('duplicate screen ids')
if len(spec['components'])<18:errors.append('component catalog unexpectedly smaller than 18')
if spec.get('gate')!='NOT_PASSED_UNTIL_QC_QA_SIGNOFF':errors.append('gate must remain not-passed before QA signoff')
js=(p2/'prototype'/'app.js').read_text(encoding='utf-8');html=(p2/'prototype'/'index.html').read_text(encoding='utf-8');css=(p2/'prototype'/'styles.css').read_text(encoding='utf-8')
combined=js+'\n'+html+'\n'+css
if re.search(r'https?://|//cdn\.|@import\s+url',combined,re.I):errors.append('prototype has external dependency')
# Regression-static assertions for independent audit defects.
checks={
 'data-driven correct answer': "answer:'good'" in js and "selected==='go'" not in js,
 'blank submit validation': "Choose an answer before submitting" in js and "disabled" in js,
 'persistent assisted state': 'response.assisted=true' in js and 'assisted:response.assisted' in js,
 'network not sync ack': "syncState='local_queued'" in js and 'simulateAck' in js,
 'bounded retry': 'response.retryCount>=1' in js and 'retry-exhausted' in (p2/'PHASE_2_SPEC.json').read_text(encoding='utf-8'),
 'offline recovery states': all(x in js for x in ['failed_retryable','partial','reauth','canonical_refresh']),
 'onboarding executable': all(x in js for x in ['welcome()','placementOffer()','placementQuestion()','placementResult()']),
 'listening executable': "listening:{" in js and 'audioControl' in js and 'play-limit-reached' in (p2/'PHASE_2_SPEC.json').read_text(encoding='utf-8'),
 'staff publication executable': all(x in js for x in ['contentPreview()','sourceLicense()','openPublishDialog()','confirmPublish()','newDraftFromPublished()']),
 'accessible labels': 'label for="content-prompt"' in js and 'id="content-prompt"' in js,
 'complex interaction contracts': (p2/'15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md').is_file(),
 'screen state traceability': (p2/'SCREEN_STATE_QA_TRACEABILITY.csv').is_file(),
 'locked preview handler': 'openLockedPreview()' in js and 'closeLockedPreview()' in js,
 'targeted live region': 'id="liveStatus"' in html and 'aria-live="polite"' not in re.search(r'<main[^>]*>',html,re.I).group(0),
 'focus token consumed': 'outline:3px solid var(--focus)' in css and 'outline:3px solid #C4B5FD' not in css,
 'grammar executable': "grammar:{" in js and "Present simple: be" in js,
}
for name,ok in checks.items():
    if not ok:errors.append(f'rework regression static check failed: {name}')
with (q/'QA_TEST_CASES.csv').open(encoding='utf-8-sig') as f:cases=list(csv.DictReader(f))
if len(cases)!=94:errors.append(f'expected 94 QA cases, got {len(cases)}')
for cid in ['QA-LRN-021','QA-LRN-022','QA-LRN-023','QA-STF-011','QA-ACC-013','QA-HO-006','QA-OFF-007']:
    if not any(c['id']==cid for c in cases):errors.append(f'missing audit-added QA case {cid}')
with (p2/'SCREEN_STATE_QA_TRACEABILITY.csv').open(encoding='utf-8-sig') as f:trace=list(csv.DictReader(f))
covered={r['screen_id'] for r in trace}
missing=set(ids)-covered
if missing:errors.append('traceability missing screens: '+','.join(sorted(missing)))
if any(not r['qa_cases'].strip() for r in trace):errors.append('traceability row without QA case')
secret=re.compile(r'(?i)(password\s*[:=]\s*[^<\s]+|postgresql://[^\s]+:[^@\s]+@|ghp_[A-Za-z0-9]+)')
for f in list(p2.rglob('*'))+list(q.rglob('*.md')):
    if f.is_file() and f.suffix.lower() in {'.md','.json','.csv','.html','.js','.css'}:
        if secret.search(f.read_text(encoding='utf-8',errors='ignore')):errors.append(f'possible secret: {f.relative_to(root)}')
result={'status':'PASS' if not errors else 'FAIL','screens':len(ids),'components':len(spec['components']),'qa_cases':len(cases),'traceability_rows':len(trace),'rework_static_checks':checks,'errors':errors}
output = Path(__import__('os').environ.get('MINGO_QA_OUTPUT', str(q/'evidence'/'verification_runs'/'rework')))
output.mkdir(parents=True,exist_ok=True)
(output/'rework_r1_static_checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2));sys.exit(0 if not errors else 1)
