from pathlib import Path
from datetime import datetime, timezone
import subprocess, os, sys, json, shutil
R=Path('C:/Mingo'); E=R/'03_Kiem_thu/Bang_chung/gd1_targeted_closure_20261005'
env=os.environ.copy(); env.update(PYTHONUTF8='1',PYTHONDONTWRITEBYTECODE='1')
V=str(R/'.local/v32-venv/Scripts/python.exe'); B=str(R/'.venv/Scripts/python.exe')
def run(name,command,cwd=R,extra=None):
 e=env.copy(); e.update(extra or {})
 start=datetime.now(timezone.utc).isoformat(); log=E/(name+'.log')
 shell=Path(command[0]).suffix.lower() in {'.bat','.cmd'}
 with log.open('w',encoding='utf-8') as out:
  out.write('CWD: '+str(cwd)+'\nCommand: '+subprocess.list2cmdline(command)+'\n'); out.flush()
  p=subprocess.run(subprocess.list2cmdline(command) if shell else command,cwd=cwd,env=e,stdout=out,stderr=subprocess.STDOUT,shell=shell)
 meta={'name':name,'cwd':str(cwd),'exact_command':subprocess.list2cmdline(command),'start_utc':start,'end_utc':datetime.now(timezone.utc).isoformat(),'exit_code':p.returncode,'status':'EXECUTED','log':str(log),'generated_artifacts':[],'result':'PASS' if p.returncode==0 else 'FAIL','boundary':'Existing checks; no runtime/product/customer gate inferred'}
 (E/(name+'_command.json')).write_text(json.dumps(meta,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 print(name,p.returncode,flush=True)
 return p.returncode
group=sys.argv[1]
if group=='v3':
 run('v3_versions',[V,'--version']); run('node_version',[shutil.which('node'),'--version'])
 run('original_contracts',[V,'-X','utf8',str(E/'run_v3_redirect.py')])
elif group=='fast':
 run('pip_check',[V,'-m','pip','check'])
 run('adapter_guards',[V,'-m','unittest','discover','-s','04_Van_hanh/tests','-v'])
 run('backend_version',[B,'--version'])
 run('backend',[B,'-m','pytest','01_San_pham/backend/tests','-q','-p','no:cacheprovider','--junitxml='+str(E/'backend.xml')])
 run('phase2_artifacts',[V,'-X','utf8','04_Van_hanh/Scripts/verify_phase2_artifacts.py'],extra={'MINGO_QA_OUTPUT':str(E/'phase2_static')})
elif group=='flutter':
 f=shutil.which('flutter'); assert f
 run('flutter_version',[f,'--version'])
 run('flutter_selected',[f,'test','test/fixture_test.dart','test/independent_test.dart','test/presentation_test.dart','--reporter','json','--no-pub'],R/'01_San_pham/cong_cu_phat_trien/mingo_ui')
