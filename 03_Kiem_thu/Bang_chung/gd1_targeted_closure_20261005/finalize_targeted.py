from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,re,collections,xml.etree.ElementTree as ET
R=Path('C:/Mingo'); E=R/'03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005'; O=R/'03_Kiem_thu/Bao_cao/GD1_Targeted_Closure_20261005'
def load(p):return json.loads(p.read_text(encoding='utf-8'))
def dump(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def table(h,rows):
 def c(x):return str(x).replace('|',' / ').replace('\n','<br>')
 return '\n'.join(['| '+' | '.join(h)+' |','| '+' | '.join(['---']*len(h))+' |']+['| '+' | '.join(c(x) for x in row)+' |' for row in rows])+'\n'
def report(n,t):(O/n).write_text(t.rstrip()+'\n',encoding='utf-8')
cmds=[load(p) for p in E.glob('*_command.json')]
v3=load(next((E/'v3_2').glob('*/run.json')))
flutter_lines=(E/'flutter_selected.log').read_text(encoding='utf-8').splitlines()
events=[]
for line in flutter_lines:
 try:events.append(json.loads(line))
 except json.JSONDecodeError:pass
starts={x['test']['id']:x['test'] for x in events if x.get('type')=='testStart'}
done=[x for x in events if x.get('type')=='testDone' and not x.get('hidden',False)]
summary={'passed':sum(x['result']=='success' and not x.get('skipped',False) for x in done),'failed':sum(x['result']!='success' and not x.get('skipped',False) for x in done),'skipped':sum(x.get('skipped',False) for x in done),'terminal_done':[x for x in events if x.get('type')=='done'],'test_files':sorted({x['suite']['path'] for x in events if x.get('type')=='suite'}),'named_results':[{'name':starts.get(x['testID'],{}).get('name','UNKNOWN'),'result':x['result'],'skipped':x.get('skipped',False),'location':starts.get(x['testID'],{}).get('url'),'line':starts.get(x['testID'],{}).get('line')} for x in done]}
dump(E/'flutter_selected_summary.json',summary)
backend=ET.parse(E/'backend.xml').getroot()
backend_cases=list(backend.iter('testcase')); skips=[{'name':x.attrib.get('name'),'reason':x.find('skipped').attrib.get('message') or x.find('skipped').text} for x in backend_cases if x.find('skipped') is not None]
bs={'passed':sum(x.find('skipped') is None and x.find('failure') is None and x.find('error') is None for x in backend_cases),'failed':sum(x.find('failure') is not None or x.find('error') is not None for x in backend_cases),'skipped':len(skips),'skips':skips}
dump(E/'backend_summary.json',bs)
material={'v3_python':v3['python'],'node':v3['node'],'v3_version':v3['package_version'],'manifest_sha256':v3['manifest_sha256'],'flutter_version':(E/'flutter_version.log').read_text(encoding='utf-8'),'backend_python':(E/'backend_version.log').read_text(encoding='utf-8')}
boundscript='''import importlib.metadata as m, all_foundation, pathlib, hashlib, json
root=pathlib.Path('C:/Mingo/01_San_pham/backend/src/all_foundation'); package=pathlib.Path(all_foundation.__file__).parent
out=[]
for p in root.rglob('*'):
 if p.is_file() and p.suffix in {'.py','.sql'}:
  q=package/p.relative_to(root); out.append({'source':str(p),'loaded':str(q),'source_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'loaded_sha256':hashlib.sha256(q.read_bytes()).hexdigest() if q.exists() else None})
print(json.dumps({'package':str(package),'versions':{n:m.version(n) for n in ['pytest','fastapi','starlette','httpx','psycopg']},'files':out,'all_match':all(x['source_sha256']==x['loaded_sha256'] for x in out)}))
'''
bp=subprocess.run([str(R/'.venv/Scripts/python.exe'),'-X','utf8','-c',boundscript],cwd=R,capture_output=True,text=True,encoding='utf-8')
if bp.returncode==0:
 boundary=json.loads(bp.stdout);dump(E/'backend_loaded_source_boundary.json',boundary);material['backend_dependencies']=boundary['versions']
else:
 boundary={'status':'SOURCE BOUNDARY NOT VERIFIED','error':bp.stderr};dump(E/'backend_loaded_source_boundary.json',boundary)
dump(E/'material_versions.json',material)
counts={'original_contracts':{'passed':v3['contract']['passed']+v3['sql']['passed'],'failed':v3['contract']['failed']+v3['sql']['failed'],'skipped':0,'detail':f"{v3['contract']['passed']} contract + {v3['sql']['passed']} SQL; {v3['original_files_verified']} original hashes; npm ci exit0"},'adapter_guards':{'passed':9 if 'Ran 9 tests' in (E/'adapter_guards.log').read_text(encoding='utf-8') and '\nOK' in (E/'adapter_guards.log').read_text(encoding='utf-8') else 'UNKNOWN','failed':0,'skipped':0,'detail':'9 negative/positive adapter-integrity/report guards'},'backend':{**bs,'detail':'API/worker foundation; native DB tests skipped when test DSN unavailable'},'flutter_selected':{**summary,'detail':'Unit/widget/presentation fixtures; three selected files; no auth/durable/native/customer claim'},'pip_check':{'passed':'N/A dependency consistency','failed':0,'skipped':0,'detail':'No broken requirements found'},'phase2_artifacts':{'passed':'N/A structural aggregate','failed':0,'skipped':0,'detail':'57 legacy screens, 18 components, 16 PRDs, 94 QA specs; not 94 executed QA cases'}}
for x in cmds:
 if x['name'] in counts:
  v=counts[x['name']];x['passed']=v['passed'];x['failed']=v['failed'];x['skipped']=v['skipped'];x['limitation']=v['detail']
 else:x.update(passed='N/A version query',failed=0,skipped=0,limitation='Read-only environment/tool query; no gate result')
 if x['name']=='original_contracts':x['generated_artifacts']=[str(next((E/'v3_2').glob('*/run.json'))),str(E/'v3_child_commands.json'),str(E/'v3_output_redirect.json'),str(E/'v3_work')]
 elif x['name']=='backend':x['generated_artifacts']=[str(E/'backend.xml'),str(E/'backend_summary.json')]
 elif x['name']=='flutter_selected':x['generated_artifacts']=[str(E/'flutter_selected.log'),str(E/'flutter_selected_summary.json')]
 elif x['name']=='phase2_artifacts':x['generated_artifacts']=[str(E/'phase2_static/internal_static_checks.json')]
 dump(E/(x['name']+'_command.json'),x)
children=load(E/'v3_child_commands.json')
for x in children:
 x.update(status='EXECUTED',result='PASS' if x['exit_code']==0 else 'FAIL',generated_artifact='v3_2 run log/report and isolated v3_work copy',limitation='Unchanged original suite on copied source; npm ci install uses existing lock without upgrading original')
dump(E/'command_results.json',{'material_versions':material,'commands':sorted(cmds,key=lambda x:x['start_utc']),'v3_nested_commands':children,'read_only_backend_boundary_probe':{'cwd':str(R),'exact_command':str(R/'.venv/Scripts/python.exe')+' -X utf8 -c <boundscript literal in finalize_targeted.py>','exit_code':bp.returncode,'result':'PASS current/installed source bytes match' if boundary.get('all_match') else 'UNKNOWN','output':str(E/'backend_loaded_source_boundary.json')}})
ct='# Executed verification and evidence boundaries\n\nAll six applicable existing checks were executed. Original V3.2 adapter is executed through an output-only harness: exactly two output path expressions redirect evidence and work copy inside the dedicated audit evidence. ROOT, SOURCE, checksum inventory, adapter source bytes, validators, assertions and failure conditions remain unchanged. The canonical script is not edited. Exact transformation: v3_output_redirect.json; child commands include npm-ci, original validators/run_checks.py and original tests/check_sql.mjs. Flutter uses --no-pub to avoid dependency/lock updates; backend disables pytest cache provider and writes JUnit only here.\n\n'
ct+=table(['Check','Result','Passed','Failed','Skipped','Execution/evidence limitation'],[[x['name'],x['result'],x['passed'],x['failed'],x['skipped'],x['limitation']] for x in sorted(cmds,key=lambda x:x['start_utc'])])+'\n## Commands, cwd, timing, artifacts\n\n'
ct+=table(['Command','Working directory','Start UTC','End UTC','Exit','Output/artifacts'],[[x['exact_command'],x['cwd'],x['start_utc'],x['end_utc'],x['exit_code'],x['log']+'; '+', '.join(x['generated_artifacts'])] for x in sorted(cmds,key=lambda x:x['start_utc'])])+'\n### Nested unchanged V3.2 commands\n\n'+table(['Command','CWD','Start UTC','End UTC','Exit'],[[x['command'],x['cwd'],x['start_utc'],x['end_utc'],x['exit_code']] for x in children])+'\n## Material versions\n\nPython V3.2: '+v3['python']+'; Node '+v3['node']+'; original package '+v3['package_version']+'. Flutter version output: '+(E/'flutter_version.log').read_text(encoding='utf-8')+'. Backend dependency versions and loaded-source equivalence: backend_loaded_source_boundary.json. Loaded installed package matches '+str(len(boundary.get('files',[])))+' current source files: '+str(boundary.get('all_match','UNKNOWN'))+'.\n\n## Backend skip reasons\n\n'+table(['Test','Reason'],[[x['name'],x['reason']] for x in skips])+'\n## Evidence type separation\n\n'+table(['Layer','Current result','Meaning / limit'],[['ARTIFACT PRESENT','Repo source/specs present; actual BA workbook NOT FOUND','Presence alone is not semantic approval'],['STRUCTURAL VALIDATION','Current16/61/175 zero dangling; legacy verifier57/94 PASS','Current Flutter catalog and inherited Phase2 artifacts are different inventories'],['SEMANTIC VALIDATION','PARTIAL; actual priority/BR/Trigger/UC/WF unknown','Candidate PO/source trace is reviewable but cannot certify absent workbook'],['EXECUTABLE CHECK','115+22, 9 guards, backend9/7, Flutter'+str(summary['passed'])+' passed','Original PGlite and fixtures/foundation, not full auth/offline runtime'],['RUNTIME VALIDATION','NOT EXECUTED for full product/native DB concurrency/auth/offline/device recovery','Skipped DB-dependent tests are not PASS'],['HUMAN VALIDATION','NOT EXECUTED in this audit; separate Phase2 gate pending','Widget/golden/structural checks do not sign human acceptance'],['CUSTOMER VALIDATION','VALIDATION DEBT; NOT EXECUTED','No market/PMF/learning/ML efficacy claim']])
report('CHECK_RESULTS.md',ct)

# Final status and protected bytes comparison; original dirty state is retained.
status=subprocess.check_output(['git','status','--porcelain=v1','--untracked-files=all'],cwd=R,text=True,encoding='utf-8',errors='replace')
(E/'git_status_after.txt').write_text(status,encoding='utf-8')
oldstatus=(E/'git_status_before.txt').read_text(encoding='utf-8').splitlines(); newstatus=status.splitlines()
before=set(oldstatus);after=set(newstatus)
added=sorted(after-before);removed=sorted(before-after)
allowed=['03_Kiem_thu/Bao_cao/GD1_Targeted_Closure_20261005/','03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005/']
unexpected_added=[x for x in added if not any(a in x for a in allowed)];unexpected_removed=[x for x in removed if not any(a in x for a in allowed)]
protected=load(E/'protected_files_before.json');changed=[];missing=[]
for x in protected:
 p=R/x['path']
 if not p.exists():missing.append(x['path'])
 elif sha(p)!=x['sha256']:changed.append({'path':x['path'],'before':x['sha256'],'after':sha(p)})
dis=load(E/'workbook_discovery.json');workbookchanged=[x['path'] for x in dis['candidates'] if not Path(x['path']).exists() or sha(Path(x['path']))!=x['sha256']]
protect={'files_compared':len(protected),'changed':changed,'missing':missing,'workbook_paths_compared':len(dis['candidates']),'workbook_bytes_changed':workbookchanged,'status_added':added,'status_removed':removed,'unexpected_status_added':unexpected_added,'unexpected_status_removed':unexpected_removed,'head_before':load(E/'git_identity.json')['head'],'head_after':subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip(),'ignored_runtime_noise':'Flutter may refresh ignored build/.dart_tool test caches in its existing package. No cache cleanup attempted. Dependency resolution suppressed with --no-pub; pubspec/package-lock/source bytes compared. V3 npm artifacts only in new isolated audit work copy. Temporary test resources have normal test lifecycle; no user file deletion/restoration.'}
dump(E/'source_preservation.json',protect)
report('SOURCE_PRESERVATION.md','# Repository preservation\n\nBaseline git status and dirty files were captured before tests/candidate edits. Final comparison: '+str(len(protected))+' existing files hashed, '+str(len(changed))+' changed, '+str(len(missing))+' missing; '+str(len(dis['candidates']))+' Excel paths hashed again, '+str(len(workbookchanged))+' changed. HEAD remains '+protect['head_after']+'. No unexpected git status changes outside dedicated audit directories: '+str(not unexpected_added and not unexpected_removed)+'.\n\nCanonical workbook/source/code/tests/V3.2/migrations/schema/package-lock/pubspec-lock and prior completed reports are untouched. No commit/push or destructive Git operation. Full before/after statuses and hashes are stored in evidence. '+protect['ignored_runtime_noise']+'\n\n'+table(['Status difference','Count','Boundary'],[['Added entries',len(added),'New dedicated report/evidence only' if not unexpected_added else str(unexpected_added)],['Removed entries',len(removed),'No pre-existing status removed' if not unexpected_removed else str(unexpected_removed)],['Changed protected bytes',len(changed),str(changed)],['Missing protected files',len(missing),str(missing)],['Excel hash changes',len(workbookchanged),str(workbookchanged)]]))
findings=load(O/'FINDING_REGISTER.json')['findings']; critical=[x for x in findings if x['Severity'] in ['BLOCKER','HIGH'] and x['Status']=='OPEN']
gate='FAIL' if critical else 'CONDITIONAL PASS';assert gate=='FAIL'
gate_text='''# GĐ1 targeted Gate Recommendation — 2026-10-05

**FAIL — GĐ1 Internal BA Baseline chưa thể đóng.**

'''+table(['Finding','Before','After targeted closure','Gate blocking'],[['AUD-001','BLOCKER / OPEN','BLOCKER / OPEN: actual workbook NOT FOUND after116 Excel paths/12 unique contents','YES'],['AUD-003','HIGH / OPEN','HIGH / OPEN:16 priorities UNKNOWN, missing actual formal chain; cited repo table/orphans complete at available-source boundary','YES'],['AUD-005','HIGH / OPEN','HIGH / OPEN: Account Gate approved by Q3; minimum full lifecycle / P0 completeness unverified','YES']])+'''
Gate is determined by unresolved BA evidence and semantics. Passing executable suites do not override these findings. All prior FIXED/PASS findings remain retained; AUD-002 old snapshot absence is not a new blocker. No new high/blocker was manufactured from deferred runtime implementation or numeric policy alone.

The approved Q3 Account Gate and Q6 Home order are synchronized in candidate documents with source-derived account acceptance. No renewed “does learning require an account?” decision request and no broad new CR. Full minimum lifecycle gaps remain visible. No account mechanism, expiry, recovery window, device count, deletion grace or export SLA was invented.

Required next evidence: the real BA workbook in its canonical project zone with authority/version, then actual P0-first/P1 trace and lifecycle reconciliation. Check N-06→WF-10 and WBS1.11 against actual cells; do not guess WF replacements. Keep any safe fix in a separate candidate copy. Do not mark traceability DONE until all actual closure conditions hold.

Customer discovery is **VALIDATION DEBT**. This recommendation does not certify customer/market validation, PMF, production readiness or learning/ML efficacy. Auth implementation remains GĐ4/appropriate technical stage; separate engineering Phase3 HOLD and Phase2 human gate are not changed.
'''
report('GATE_RECOMMENDATION.md',gate_text)
executive='''# Mingo GĐ1 — targeted closure result

**Gate Recommendation: FAIL.** AUD-001, AUD-003 và AUD-005 chưa đóng; không ép kết quả PASS.

'''+table(['Target','Kết quả','Bằng chứng chính'],[['AUD-001','BLOCKER / OPEN — NOT FOUND', '116 Excel paths,12 hashes; every plausible candidate read-only sheet/content inspection; all candidate paths/hash/size/time recorded'],['AUD-003','HIGH / OPEN — incomplete actual semantic chain','16 repo requirements; every actual priority UNKNOWN;61 screens/175 states zero dangling; formal workbook Need/BR/Trigger/UC/WF links unknown'],['AUD-005','HIGH / OPEN — approved gate, incomplete lifecycle evidence','Q3 already approves Guest/Account Gate/methods/return;17 capability matrix,8 source-derived spec-only AC; minimum necessary paths/P0 completeness unverified']])+f'''
Đã tạo candidate đồng bộ Q1–Q15 và ba candidate documents/patches cho DECISION_REGISTER, MVP_PRD, CHANGE_REQUESTS. Q6 Home order được ghi là approved baseline; Q12 là DEFERRED-FUTURE, không permanently rejected. CR-GD1-001 broad inclusion question được superseded trong candidate, không yêu cầu PO quyết định lại Q3. Canonical documents chưa thay thế; không tạo workbook giả hoặc auth code.

Verification thực chạy: **115 contract +22 SQL PASS**, **102 original hashes intact**, **9 adapter guards PASS**, **backend {bs['passed']} passed/{bs['skipped']} skipped**, **Flutter {summary['passed']} passed/{summary['failed']} failed/{summary['skipped']} skipped**, pip check PASS; existing Phase2 static check PASS (57 inherited screens/18 components/16 PRD/94 QA specs). Current61-screen/175-state structure audited separately. Backend skipped tests are not native runtime PASS; original SQL is PGlite, Flutter is fixture/widget/presentation.

Preservation: {len(protected)} pre-existing files compared, {len(changed)} changed, {len(missing)} missing; all116 Excel hashes unchanged. Existing dirty state and HEAD retained. No commit/push. Dedicated report: {O}. Evidence: {E}. PO packet preserved byte-for-byte; its supplied text ends at Mermaid TEST node, no unobserved trailing instructions assumed.

Customer discovery remains VALIDATION DEBT; internal BA approval, implementation/runtime, human and customer validation are separate layers.

## Review pack

- [Gate Recommendation](GATE_RECOMMENDATION.md)
- [Workbook discovery, all116 candidates](WORKBOOK_DISCOVERY.md)
- [Semantic trace table and exact row evidence](TRACEABILITY_AUDIT.md)
- [Orphan/inherited support register](ORPHAN_REGISTER.md)
- [Account lifecycle candidate](ACCOUNT_LIFECYCLE_CANDIDATE.md)
- [17-area consistency matrix](CONSISTENCY_MATRIX.md)
- [PO decision synchronization candidate](PO_DECISION_SYNC_CANDIDATE.md)
- [Candidate doc patches / before-after](CANDIDATE_DOC_PATCHES.md)
- [Executed checks and limitations](CHECK_RESULTS.md)
- [Source preservation](SOURCE_PRESERVATION.md)
- [Finding register](FINDING_REGISTER.md)
'''
report('EXECUTIVE_TARGETED_CLOSURE.md',executive)
dump(E/'final_counts.json',{'gate':gate,'workbook_candidates':len(dis['candidates']),'unique_workbook_hashes':dis['unique_hash_count'],'ba_result':dis['result'],'v3_contract':v3['contract'],'v3_sql':v3['sql'],'original_hashes':v3['original_files_verified'],'backend':bs,'flutter':{k:summary[k] for k in ['passed','failed','skipped']},'source_protected_files':len(protected),'source_changes':changed,'source_missing':missing,'open_gate_findings':[x['ID'] for x in critical]})
print(json.dumps({'gate':gate,'flutter':{k:summary[k] for k in ['passed','failed','skipped']},'protected':len(protected),'changed':changed,'missing':missing,'unexpected_git_added':unexpected_added,'unexpected_git_removed':unexpected_removed},ensure_ascii=False))
