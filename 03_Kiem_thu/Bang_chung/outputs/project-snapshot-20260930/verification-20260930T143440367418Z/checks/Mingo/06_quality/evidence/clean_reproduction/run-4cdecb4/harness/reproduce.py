import os, pathlib, subprocess, secrets, json, time, urllib.request, sys
from datetime import datetime, timezone
import psycopg
from psycopg import sql

root=pathlib.Path(r'C:\Mingo\.local\clean-reproduction-20260926')
out=root/'06_quality/evidence/clean_reproduction'
out.mkdir(parents=True,exist_ok=True)
local=root/'.local'
local.mkdir(exist_ok=True)
env=os.environ.copy()
for key in ('DATABASE_URL','TEST_DATABASE_URL','MINGO_APP_PASSWORD','OBJECT_STORAGE_ROOT','PYTHONPATH','PYTHONHOME','VIRTUAL_ENV','JAVA_TOOL_OPTIONS','WORKER_ID','APP_ENV'):
    env.pop(key,None)
env.update(PYTHONUTF8='1', JAVA_HOME=r'C:\Program Files\Microsoft\jdk-17.0.20.101-hotspot', ANDROID_HOME=r'C:\Android\Sdk', ANDROID_SDK_ROOT=r'C:\Android\Sdk', GRADLE_USER_HOME=r'C:\Mingo\.local\clean-gradle',PUB_CACHE=r'C:\Mingo\.local\clean-pub',APP_ENV='clean-reproduction',WORKER_ID='clean-reproduction-worker',OBJECT_STORAGE_ROOT=str(local/'objects'))
env['PATH']=env['JAVA_HOME']+'\\bin;C:\\Dev\\flutter-3.32.8\\bin;'+env['PATH']
temp=local/'java-tmp';temp.mkdir(exist_ok=True)
env.update(TEMP=str(temp),TMP=str(temp),JAVA_TOOL_OPTIONS='-Djava.io.tmpdir='+str(temp))
py=str(root/'.venv/Scripts/python.exe')
pg=pathlib.Path(r'C:\Program Files\PostgreSQL\18\bin')
cluster=local/'pgdata'
def run(name,args,check=True):
    with (out/(name+'.log')).open('w',encoding='utf-8') as f:
        f.write('UTC: '+datetime.now(timezone.utc).isoformat()+'\nCommand: '+subprocess.list2cmdline(list(map(str,args)))+'\n');f.flush()
        p=subprocess.run(list(map(str,args)),cwd=root,env=env,stdout=f,stderr=subprocess.STDOUT)
        f.write('\nExit code: '+str(p.returncode)+'\n')
    print(name+': '+str(p.returncode),flush=True)
    if check and p.returncode: raise RuntimeError(name+' failed; inspect its log')
    return p.returncode

if sys.argv[1]=='backend':
    assert not (root/'.venv').exists()
    assert not cluster.exists()
    baseline={'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'utc':datetime.now(timezone.utc).isoformat(),'initial_git_status':subprocess.check_output(['git','status','--porcelain'],cwd=root,text=True),'fresh_venv':True,'fresh_database_cluster':True,'fresh_object_store':True,'database_port':55432,'application_role':'mingo_app','databases':['mingo','mingo_test'],'toolchains_reused':'Python 3.12.10, Flutter 3.32.8, JDK17, installed Android SDK; all explicitly configured','fresh_pub_cache':env['PUB_CACHE'],'fresh_gradle_cache':env['GRADLE_USER_HOME']}
    (out/'environment.json').write_text(json.dumps(baseline,indent=2),encoding='utf-8')
    run('python-version',[r'C:\Users\Phúc\AppData\Local\Programs\Python\Python312\python.exe','--version'])
    run('venv-create',[r'C:\Users\Phúc\AppData\Local\Programs\Python\Python312\python.exe','-m','venv','.venv'])
    run('locked-install',[py,'-m','pip','install','-r','05_code/backend/requirements.lock'])
    run('package-install',[py,'-m','pip','install','--no-deps','./05_code/backend'])
    run('pip-check',[py,'-m','pip','check'])
    # First prove the no-database documented path has no dependency on a local .env.
    run('backend-without-env',['pwsh','-NoProfile','-File','07_operations/scripts/verify_backend.ps1','-Python',py])
    admin=secrets.token_urlsafe(32); app=secrets.token_urlsafe(32)
    pwfile=local/'pg-init-password';pwfile.write_text(admin,encoding='utf-8')
    run('postgres-initdb',[pg/'initdb.exe','-D',cluster,'-U','postgres','--auth=scram-sha-256','--encoding=UTF8','--locale=C','--pwfile='+str(pwfile)])
    pwfile.unlink()
    run('postgres-start',[pg/'pg_ctl.exe','-D',cluster,'-l',local/'postgres.log','-o','-p 55432 -h 127.0.0.1','-w','start'])
    try:
        with psycopg.connect(host='127.0.0.1',port=55432,user='postgres',password=admin,dbname='postgres',autocommit=True) as c:
            c.execute(sql.SQL('CREATE ROLE mingo_app LOGIN PASSWORD {}').format(sql.Literal(app)))
            for db in ('mingo','mingo_test'): c.execute(sql.SQL('CREATE DATABASE {} OWNER mingo_app').format(sql.Identifier(db)))
        env['DATABASE_URL']=f'postgresql://mingo_app:{app}@127.0.0.1:55432/mingo'
        env['TEST_DATABASE_URL']=env['DATABASE_URL']+'_test'
        (root/'05_code/.env').write_text('\n'.join(k+'='+env[k] for k in ('DATABASE_URL','TEST_DATABASE_URL','OBJECT_STORAGE_ROOT','WORKER_ID','APP_ENV'))+'\n',encoding='utf-8')
        with psycopg.connect(env['DATABASE_URL']) as c:
            assert c.execute("SELECT to_regnamespace('foundation')").fetchone()[0] is None
            assert not c.execute('SELECT rolsuper FROM pg_roles WHERE rolname=current_user').fetchone()[0]
        (out/'fresh-database.txt').write_text('Fresh initdb; no foundation schema before migration; mingo_app is not superuser.\n',encoding='utf-8')
        run('backend-postgres',['pwsh','-NoProfile','-File','07_operations/scripts/verify_backend.ps1','-Python',py,'-RunPostgres'])
        run('migration-repeat',[py,'-m','all_foundation.cli','migrate'])
        api_log=(out/'api-live-process.log').open('w',encoding='utf-8'); worker_log=(out/'worker-live-process.log').open('w',encoding='utf-8')
        api=subprocess.Popen([py,'-m','uvicorn','all_foundation.api:create_app','--factory','--host','127.0.0.1','--port','8131'],cwd=root,env=env,stdout=api_log,stderr=subprocess.STDOUT)
        worker=subprocess.Popen([py,'-m','all_foundation.worker'],cwd=root,env=env,stdout=worker_log,stderr=subprocess.STDOUT)
        try:
            for _ in range(60):
                try:
                    ready=urllib.request.urlopen('http://127.0.0.1:8131/health/ready',timeout=2).status
                    if ready==200: break
                except Exception: pass
                time.sleep(1)
            else: raise RuntimeError('API not ready')
            run('enqueue-concurrent',[py,'-m','all_foundation.cli','enqueue-probe','--key','clean-concurrent'])
            for _ in range(30):
                with psycopg.connect(env['DATABASE_URL']) as c:
                    row=c.execute("SELECT j.state,count(e.job_id) FROM foundation.jobs j LEFT JOIN foundation.probe_effects e ON e.job_id=j.id WHERE dedupe_key='clean-concurrent' GROUP BY j.state").fetchone()
                if row==('done',1): break
                time.sleep(1)
            else: raise RuntimeError('durable effect not confirmed')
            run('worker-health-live',[py,'-m','all_foundation.worker','--healthcheck'])
            live=urllib.request.urlopen('http://127.0.0.1:8131/health/live').status
            assert live==200 and api.poll() is None and worker.poll() is None
            (out/'simultaneous-runtime.json').write_text(json.dumps({'live':live,'ready':ready,'api_pid':api.pid,'worker_pid':worker.pid,'both_running':True,'probe_state':row[0],'durable_effect_count':row[1]},indent=2),encoding='utf-8')
        finally:
            api.terminate();worker.terminate();api.wait();worker.wait();api_log.close();worker_log.close()
        run('original-v3-2',[py,'07_operations/scripts/check_original_contracts.py'],check=False)
    finally: run('postgres-stop',[pg/'pg_ctl.exe','-D',cluster,'-m','fast','-w','stop'])
elif sys.argv[1]=='flutter':
    for app in ('learner','staff'):
        for directory in ('.dart_tool','build'):
            assert not (root/'05_code/apps'/app/directory).exists()
    assert not pathlib.Path(env['PUB_CACHE']).exists()
    assert not pathlib.Path(env['GRADLE_USER_HOME']).exists()
    run('flutter-bootstrap',['pwsh','-NoProfile','-File','07_operations/scripts/bootstrap_clients.ps1','-Flutter',r'C:\Dev\flutter-3.32.8\bin\flutter.bat'])
    run('flutter-verify',['pwsh','-NoProfile','-File','07_operations/scripts/verify_flutter.ps1','-Flutter',r'C:\Dev\flutter-3.32.8\bin\flutter.bat'])
