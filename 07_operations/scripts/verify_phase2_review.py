"""Reproducible artifact checks supporting the human Phase 2 handoff review.

These are artifact evidence, never browser execution or independent acceptance.
Run from the repository root before packaging.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess
import datetime
import os

root=Path(__file__).resolve().parents[2]
p2=root/'02_product/ux_ui/phase2'
q=root/'06_quality/phase2'
out=q/'evidence/codex/review';out.mkdir(parents=True,exist_ok=True)
read=lambda name:(p2/name).read_text(encoding='utf-8-sig')
spec=json.loads(read('PHASE_2_SPEC.json'))
cases=list(csv.DictReader((q/'QA_TEST_CASES.csv').open(encoding='utf-8-sig')))
case_ids={c['id'] for c in cases}
trace=list(csv.DictReader((p2/'SCREEN_STATE_QA_TRACEABILITY.csv').open(encoding='utf-8-sig')))
results=[]
def record(cid,condition,observed,files):
 if os.environ.get('MINGO_QA_PRIORITY') and next(c['priority'] for c in cases if c['id']==cid)!=os.environ['MINGO_QA_PRIORITY']:return
 r={'id':cid,'status':'PASS' if condition else 'FAIL','method':'artifact inspection / reproducible checks; not independent signoff','observed':observed,'sources':files,'time':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 (out/(cid+'.json')).write_text(json.dumps(r,indent=2,ensure_ascii=False),encoding='utf-8')
 results.append({**r,'evidence':str((out/(cid+'.json')).relative_to(root)).replace('\\','/')})

index=root/'08_handoff/phase2/HANDOFF_INDEX.md'
refs=re.findall(r'`([^`]+)`',index.read_text(encoding='utf-8'))
missing=[ref for ref in refs if not (index.parent/ref).exists()]
record('QC-001',not missing,{'references':refs,'missing':missing},[str(index.relative_to(root))])
intake=json.loads((q/'evidence/codex/intake.json').read_text())
mismatch=[name for name,digest in intake['protected_hashes_before'].items() if not (root/name).is_file() or hashlib.sha256((root/name).read_bytes()).hexdigest() not in {digest,intake['protected_git_blob_sha256'][name]}]
diff=subprocess.check_output(['git','diff','--name-only',intake['base_commit'],'--','05_code','04_architecture/contracts/v3_2/source'],cwd=root,text=True) if (root/'.git').exists() else ''
record('QC-002',not mismatch and not diff,{'protected_file_count':len(intake['protected_hashes_before']),'hash_mismatches':mismatch,'git_diff':diff,'line_endings':'Accept exact original working-copy bytes or exact original Git blob bytes; original V3.2 has identical hashes in both. Git-less extraction uses cryptographic baseline hashes.'},['evidence/codex/intake.json'])
contract=read('01_PHASE_2_CONTRACT.md');handoff=read('13_DEVELOPER_HANDOFF.md');routing=read('05_NAVIGATION_ROUTING_SPEC.md');complex_spec=read('15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md')
record('QC-003','Out of scope' in contract and all(f'Phase {n}' in contract for n in [3,4,5,6]),contract[contract.index('## Out of scope'):contract.index('## Frozen')],['01_PHASE_2_CONTRACT.md'])
ids=[s['id'] for s in spec['screens']]
record('QC-004',len(ids)==57 and len(set(ids))==57 and set(ids)=={r['screen_id'] for r in trace},{'unique_screens':len(set(ids)),'mapped_screens':len({r['screen_id'] for r in trace})},['PHASE_2_SPEC.json','SCREEN_STATE_QA_TRACEABILITY.csv'])
record('QC-005',all(s.get('route') for s in spec['screens']),{s['id']:s['route'] for s in spec['screens']},['PHASE_2_SPEC.json','05_NAVIGATION_ROUTING_SPEC.md'])
prd=read('12_UX_REQUIREMENT_TRACEABILITY.md')
record('QC-006',all(f'PRD-{n:02d}' in prd for n in range(1,17)) and all(x in case_ids for x in re.findall(r'QA-[A-Z]+-\d+',prd)),prd,['12_UX_REQUIREMENT_TRACEABILITY.md'])
record('QC-007','Versioned MVP hypotheses' in contract and all(x in contract for x in ['5-minute','one practice retry','two Check plays','placement']),contract[contract.index('## Versioned'):contract.index('## UX principles')],['01_PHASE_2_CONTRACT.md'])
copy=read('10_CONTENT_MICROCOPY_GUIDE.md')
record('QC-008',all(x.lower() in (copy+contract).lower() for x in ['mastery','diagnos','evidence']),{'review':'Read learner microcopy, actual browser result/summary/profile evidence and guards. Qualitative sample labels are mock data; no precise mastery/CEFR/diagnostic claims.','microcopy':copy},['10_CONTENT_MICROCOPY_GUIDE.md','prototype/app.js'])
# Scan only deliverable text. Print file names, never possible secret values.
scanned=[];hits=[]
pattern=re.compile(r'gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|postgresql://[^\s:]+:[^<\s@]+@')
for base in [p2,q,root/'08_handoff/phase2']:
 for f in base.rglob('*'):
  if f.is_file() and f.suffix in {'.md','.json','.csv','.js','.css','.html','.log','.txt'}:
   scanned.append(str(f.relative_to(root)))
   if pattern.search(f.read_text(encoding='utf-8',errors='replace')):hits.append(str(f.relative_to(root)))
record('QC-009',not hits,{'files_scanned':len(scanned),'matched_paths':hits,'scope':'Phase 2 text; exact ZIP also checked by packaging verifier'},['07_operations/scripts/verify_phase2_review.py'])
prototype='\n'.join(read('prototype/'+name) for name in ['app.js','index.html','styles.css'])
record('QC-010',not re.search(r'https?://|//cdn\.|@import\s+url',prototype),{'external_references':False,'browser_requests':'See each browser case JSON: loopback files only'},['prototype/app.js','prototype/index.html','prototype/styles.css'])
record('QA-NAV-009','visibility is presentation only' in routing and 'server authorization' in routing,routing,['05_NAVIGATION_ROUTING_SPEC.md'])
record('QA-NAV-010',all(x in routing for x in ['re-evaluates eligibility','never resends','permission','revision']),routing,['05_NAVIGATION_ROUTING_SPEC.md'])
screens=json.dumps(spec['screens'],ensure_ascii=False)
record('QA-BIZ-006', 'challenge' in (screens+contract).lower() and 'bounded' in contract.lower(),{'review':'Challenge is a bounded product hypothesis. Course preview keeps prerequisites locked; challenge/preference does not confer skill or override eligibility. This case requests spec review, not a production challenge engine.','matching_screens':[s for s in spec['screens'] if any(x in json.dumps(s).lower() for x in ['challenge','prerequisite'])]},['01_PHASE_2_CONTRACT.md','PHASE_2_SPEC.json','12_UX_REQUIREMENT_TRACEABILITY.md'])
def lum(h):
 a=[int(h[i:i+2],16)/255 for i in (1,3,5)];a=[v/12.92 if v<=.04045 else ((v+.055)/1.055)**2.4 for v in a];return sum(v*w for v,w in zip(a,[.2126,.7152,.0722]))
pairs=[('#0F172A','#FFFFFF'),('#475569','#FFFFFF'),('#FFFFFF','#3046C5'),('#FFFFFF','#2438A8'),('#1E3A8A','#E8ECFF'),('#14532D','#DCFCE7'),('#7F1D1D','#FEE2E2'),('#78350F','#FEF3C7'),('#475569','#F8FAFC'),('#CBD5E1','#111827'),('#E2E8F0','#1E293B')]
ratios=[{'foreground':a,'background':b,'ratio':round((max(lum(a),lum(b))+.05)/(min(lum(a),lum(b))+.05),3)} for a,b in pairs]
focus=(lum('#FFFFFF')+.05)/(lum('#7C3AED')+.05)
record('QA-ACC-004',all(r['ratio']>=4.5 for r in ratios) and focus>=3 and 'outline:3px solid var(--focus)' in prototype,{'text_contrast_pairs':ratios,'focus_on_white':focus,'review':'Error, queued, correct/incorrect, assisted, Draft/Published all have visible words; color is not sole signal. Disabled controls excluded by AA contrast exception. Focus consumes semantic token.'},['DESIGN_TOKENS.json','prototype/styles.css','prototype/app.js'])
record('QA-HO-001',all(x in complex_spec for x in ['Anatomy','Validation','Permissions','State','S-031','S-036','S-037']) and 'Stable identifiers' in handoff,{'review':'Reviewed assessment selection/submit/result/continue, assisted/retry/skip state, placement, Check restrictions, sync/ack recovery, draft validation/preview/license/review/publication lineage, focus and stable hooks. Screen routes, state catalog and tokens are supplied. Acceptance still requires Tech Lead.','contract':complex_spec},['15_COMPLEX_SCREEN_INTERACTION_CONTRACTS.md','13_DEVELOPER_HANDOFF.md','07_UI_STATE_CATALOG.md','PHASE_2_SPEC.json'])
tokens=json.loads(read('DESIGN_TOKENS.json'));css=read('prototype/styles.css');colors=tokens['color']
expanded_css=re.sub(r'#([0-9a-fA-F]{3})(?![0-9a-fA-F])',lambda m:'#'+''.join(c*2 for c in m[1]),css)
record('QA-HO-002',all(v.lower() in expanded_css.lower() for v in colors.values()),{'semantic_colors':colors,'focus_consumed':'var(--focus)' in css,'normalization':'CSS #fff equals token #FFFFFF'},['DESIGN_TOKENS.json','08_DESIGN_SYSTEM_SPEC.md','prototype/styles.css'])
record('QA-HO-003',all(x in handoff for x in ['screen-L-024','action-L-024-submit','field-S-031-prompt','action-S-036-confirm']),handoff[handoff.index('## Stable'):handoff.index('## Assessment')],['13_DEVELOPER_HANDOFF.md'])
record('QA-HO-004','non-production' in prototype and 'mock-only' in handoff,{'labels':['mock state · non-production · QC/QA rework','intentionally mock-only and must not be shipped as production logic'],'runtime_unchanged':not diff},['prototype/index.html','13_DEVELOPER_HANDOFF.md'])
import zipfile,xml.etree.ElementTree as ET
with zipfile.ZipFile(q/'Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx') as z:
 wb_text=''.join(z.read(n).decode('utf-8') for n in z.namelist() if n in ['xl/sharedStrings.xml','xl/worksheets/sheet9.xml'])
record('QA-HO-005',all(x in wb_text for x in ['QC Lead','QA Lead','Tech Lead','Product/Owner','P0 cases','PENDING']),{'roles':['QC Lead','QA Lead','Tech Lead','Product/Owner'],'signoffs':'PENDING; execution engineer has not signed for another role'},['Mingo_Phase2_Rework_R1_QA_Control_2026-09-27.xlsx'])
badrefs=[r for r in trace if not r['classification'] or any(x.strip() not in case_ids for x in r['qa_cases'].split(';'))]
record('QA-HO-006',not badrefs and set(ids)=={r['screen_id'] for r in trace},{'screens':57,'rows':len(trace),'invalid_references':badrefs,'coverage_caution':'Mapping is artifact coverage. It does not prove all 166 state variants were runtime exercised; references to spec-review cases remain artifact review only.'},['SCREEN_STATE_QA_TRACEABILITY.csv','PHASE_2_SPEC.json','QA_TEST_CASES.csv'])
(out/('run-'+os.environ['MINGO_QA_PRIORITY']+'.json' if os.environ.get('MINGO_QA_PRIORITY') else 'run.json')).write_text(json.dumps({'results':results},indent=2,ensure_ascii=False),encoding='utf-8')
for r in results:print(r['id'],r['status'])
raise SystemExit(any(r['status']=='FAIL' for r in results))
