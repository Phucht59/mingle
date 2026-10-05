"""Run canonical P0 cases before P1, then supplemental accessibility/media tests."""
import os,subprocess,json,datetime
from pathlib import Path
root=Path(__file__).resolve().parents[2];out=root/'06_quality/phase2/evidence/codex';commands=[]
for priority in ['P0','P1']:
 env={**os.environ,'MINGO_QA_PRIORITY':priority}
 for command in [['python','-X','utf8','07_operations/scripts/verify_phase2_review.py'],['node','07_operations/scripts/verify_phase2_browser.cjs']]:
  start=datetime.datetime.now(datetime.timezone.utc).isoformat()
  result=subprocess.run(command,cwd=root,env=env,capture_output=True,text=True,encoding='utf-8',errors='replace')
  commands.append({'command':command,'priority':priority,'start':start,'end':datetime.datetime.now(datetime.timezone.utc).isoformat(),'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr});print(priority,result.stdout,flush=True)
for kind in ['review','browser']:
 runs=[json.loads((out/kind/f'run-{p}.json').read_text(encoding='utf-8')) for p in ['P0','P1']]
 combined={**runs[-1],'results':runs[0]['results']+runs[1]['results'],'execution_order':'P0 artifact + P0 browser; P1 artifact + P1 browser'}
 (out/kind/'run.json').write_text(json.dumps(combined,indent=2,ensure_ascii=False),encoding='utf-8')
cmd=['node','07_operations/scripts/verify_phase2_supplemental.cjs'];result=subprocess.run(cmd,cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
commands.append({'command':cmd,'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr});print(result.stdout)
(out/'ordered_execution_commands.json').write_text(json.dumps(commands,indent=2),encoding='utf-8')
raise SystemExit(any(c['exit_code'] for c in commands))
