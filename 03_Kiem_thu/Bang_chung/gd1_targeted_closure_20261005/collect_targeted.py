from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, hashlib, shutil, re, zipfile, warnings
import openpyxl

R = Path('C:/Mingo')
E = R/'03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005'
O = R/'03_Kiem_thu/Bao_cao/GD1_Targeted_Closure_20261005'
REQUEST = Path('C:/Users/Phúc/.codex/attachments/defe1d0c-f1d5-46b6-a21e-e636b8064dfe/Pasted text.txt')
ANCHOR='0878ee84d20283dc90bd8881c8a8b3f9ea91e150fbf86803b8e54a2aff85251e'
SANCHOR='795252dbf8e9cc26ae5f319a9121121e4b5d4bd60d8e3d801773c43a43c4b148'
EXPECTED=['00_Dashboard','01_Huong_dan','02_Roadmap_8_GD','03_Yeu_cau_Nghiep_vu','04_Business_Rules','05_UseCase_Trigger','06_User_Journey','07_RTM','08_Wireframe_Learner','09_Wireframe_Staff','10_WBS','11_RACI','12_RAID','13_Research_Evidence','14_Decision_Log','15_Test_Gate']
def write(n,v): (E/n).write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def run(a): return subprocess.check_output(a,cwd=R,text=True,encoding='utf-8',errors='replace')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
shutil.copyfile(REQUEST,E/'PO_TARGETED_REQUEST.txt')
write('audit_paths.json',{'report':str(O),'evidence':str(E),'business_date':'2026-10-05','timezone':'Asia/Ho_Chi_Minh','request_sha256':sha(REQUEST),'request_end':'Input ends at Mermaid TEST node; no further instructions present.'})
for n,a in [('git_status_before.txt',['git','status','--porcelain=v1','--untracked-files=all']),('git_diff_stat_before.txt',['git','diff','--stat']),('git_cached_stat_before.txt',['git','diff','--cached','--stat'])]: (E/n).write_text(run(a),encoding='utf-8')
write('git_identity.json',{'root':run(['git','rev-parse','--show-toplevel']).strip(),'branch':run(['git','branch','--show-current']).strip(),'head':run(['git','rev-parse','HEAD']).strip(),'remotes':run(['git','remote','-v']).splitlines(),'captured_utc':datetime.now(timezone.utc).isoformat()})
instructions=run(['rg','--files','--hidden','--no-ignore','-g','AGENTS.md','-g','AGENTS.override.md','-g','!.git/**']) if False else subprocess.run(['rg','--files','--hidden','--no-ignore','-g','AGENTS.md','-g','AGENTS.override.md','-g','!.git/**'],cwd=R,capture_output=True,text=True,encoding='utf-8')
write('instruction_discovery.json',{'recursive_command':'rg --files --hidden --no-ignore -g AGENTS.md -g AGENTS.override.md -g !.git/**','exit':instructions.returncode,'paths':instructions.stdout.splitlines(),'ancestor_paths':{str(p):p.exists() for p in [Path('C:/AGENTS.md'),Path('C:/AGENTS.override.md'),R/'AGENTS.md',R/'AGENTS.override.md']},'read':['README.md','START_HERE.md','REPO_RULES.md'],'applicable_precedence':'Targeted user write restrictions override generic repo evidence placement and governance write rules.'})
before=json.loads((R/'03_Kiem_thu/Bao_cao/GD1_Consistency_Audit_20261005/FINDING_REGISTER.json').read_text(encoding='utf-8'))
write('FINDINGS_BEFORE_FIXES.json',before)
files=run(['rg','--files','--hidden','--no-ignore','-g','*.xlsx','-g','*.xlsm','-g','*.xls','-g','*.ods','-g','*MINGO_PROJECT_PROGRESS_SNAPSHOT*','-g','!.git/**']).splitlines()
(E/'artifact_candidates.txt').write_text('\n'.join(files)+'\n',encoding='utf-8')
cache={}; candidates=[]; snapshots=[]
for name in files:
 p=R/name; st=p.stat(); digest=sha(p)
 base={'path':str(p),'sha256':digest,'size':st.st_size,'modified_utc':datetime.fromtimestamp(st.st_mtime,timezone.utc).isoformat()}
 if p.suffix.lower() not in {'.xlsx','.xlsm','.xls','.ods'}:
  base.update(identity='EXACT MATCH' if digest==SANCHOR else 'DIFFERENT VERSION', authority='Historical continuity' if '2026-10-04' in name else 'Repository continuity; not BA authority'); snapshots.append(base); continue
 if digest not in cache:
  d={'openable':False,'sheets':[],'expected_sheet_overlap':0,'fingerprint_ids':{}}
  try:
   with warnings.catch_warnings():
    warnings.simplefilter('ignore'); w=openpyxl.load_workbook(p,read_only=True,data_only=False)
   d['openable']=True
   all_ids={}
   for s in w:
    d['sheets'].append({'name':s.title,'state':s.sheet_state,'range':s.calculate_dimension(),'rows':s.max_row,'columns':s.max_column})
    # Inspect bounded populated workbook content, not only title/sheet count.
    for row in s.iter_rows():
     for c in row:
      if isinstance(c.value,str):
       for x in re.findall(r'\b(?:PRD|BR|TRG|TRIGGER|UC|WF|N)-\d{1,3}\b',c.value): all_ids.setdefault(x,[]).append(f'{s.title}!{c.coordinate}')
   d['fingerprint_ids']=all_ids
   d['expected_sheet_overlap']=len(set(w.sheetnames)&set(EXPECTED)); w.close()
  except Exception as ex: d['error']=str(ex)
  cache[digest]=d
 d=cache[digest]; base.update(d)
 base['identity']='EXACT MATCH' if digest==ANCHOR else 'DIFFERENT VERSION'
 base['selection']='REVIEW BA CANDIDATE' if digest==ANCHOR or d['expected_sheet_overlap']>=5 else 'REJECTED AS BA WORKBOOK'
 base['reason']='Identity or content matches expected BA family; inspect actual version' if base['selection'].startswith('REVIEW') else ('Unreadable Excel owner/lock file; not workbook' if not d['openable'] else f"Different artifact content: {len(d['sheets'])} sheets; {d['expected_sheet_overlap']}/16 expected sheets; management/UX-QA/dashboard template, not GD1 BA inventory")
 candidates.append(base)
write('workbook_discovery.json',{'root':str(R),'includes_hidden_ignored_archive_outputs_local':True,'excluded_only':'.git internals','patterns':['*.xlsx','*.xlsm','*.xls','*.ods','*MINGO_PROJECT_PROGRESS_SNAPSHOT*','exact expected title and underscore variant checked against inventory'],'expected_zone':str(R/'02_Tai_lieu_du_an/**/Mingo GD1 — Quản lý Phân tích Nghiệp vụ.xlsx'),'expected_sheets':EXPECTED,'workbook_anchor':ANCHOR,'snapshot_anchor':SANCHOR,'candidate_count':len(candidates),'unique_hash_count':len(cache),'ba_candidates':[x['path'] for x in candidates if x['selection'].startswith('REVIEW')],'result':'FOUND' if any(x['selection'].startswith('REVIEW') for x in candidates) else 'NOT FOUND','candidates':candidates,'snapshots':snapshots})
active=run(['rg','--files','--hidden','-g','!.git/**','-g','!.local/**','-g','!.venv/**','-g','!99_Luu_tru/**','-g','!03_Kiem_thu/Bang_chung/outputs/**','-g','!**/node_modules/**','-g','!**/build/**','-g','!**/.dart_tool/**']).splitlines()
protected=[]
for name in active:
 p=R/name
 if p.is_file() and not p.is_relative_to(E) and not p.is_relative_to(O): protected.append({'path':name,'sha256':sha(p),'size':p.stat().st_size})
write('protected_files_before.json',protected)
commands=[('.local/v32-venv/Scripts/python.exe',None),('.venv/Scripts/python.exe',None),('04_Van_hanh/Scripts/check_original_contracts.py',None),('04_Van_hanh/tests',None),('01_San_pham/backend/tests',None),('04_Van_hanh/Scripts/verify_phase2_artifacts.py',None),('01_San_pham/cong_cu_phat_trien/mingo_ui/test/fixture_test.dart',None),('01_San_pham/cong_cu_phat_trien/mingo_ui/test/independent_test.dart',None),('01_San_pham/cong_cu_phat_trien/mingo_ui/test/presentation_test.dart',None)]
write('command_preflight.json',{'paths':[{'path':str(R/n),'exists':(R/n).exists()} for n,_ in commands],'flutter':shutil.which('flutter'),'node':shutil.which('node'),'npm':shutil.which('npm.cmd')})
print(json.dumps({'workbooks':len(candidates),'unique':len(cache),'ba_candidates':[x['path'] for x in candidates if x['selection'].startswith('REVIEW')],'protected_files':len(protected),'snapshots':len(snapshots)},ensure_ascii=False))
