from reproduce import root,out,env,py,run
import subprocess,time,json,urllib.request,pathlib,sys
adb=r'C:\Android\Sdk\platform-tools\adb.exe'
def a(*args):
    return subprocess.check_output([adb,'-s','emulator-5554',*args],text=True,encoding='utf-8',errors='replace',timeout=60).strip()
if sys.argv[1]=='android':
    for _ in range(120):
        try:
            if a('shell','getprop','sys.boot_completed')=='1': break
        except Exception: pass
        time.sleep(2)
    else: raise RuntimeError('Fresh emulator boot timeout')
    apk=root/'05_code/apps/learner/build/app/outputs/flutter-apk/app-debug.apk'
    assert apk.is_file()
    package='com.example.adaptive_learner'
    assert not a('shell','pm','list','packages',package), 'Expected fresh AVD without learner installed'
    run('android-install',[adb,'-s','emulator-5554','install',str(apk)])
    a('logcat','-c')
    run('android-start',[adb,'-s','emulator-5554','shell','am','start','-W','-n',package+'/.MainActivity'])
    time.sleep(20)
    pid=a('shell','pidof',package); assert pid
    run('android-ui-dump',[adb,'-s','emulator-5554','shell','uiautomator','dump','/sdcard/mingo-ui.xml'])
    run('android-ui-pull',[adb,'-s','emulator-5554','pull','/sdcard/mingo-ui.xml',str(out/'android-ui.xml')])
    xml=(out/'android-ui.xml').read_text(encoding='utf-8')
    assert 'Your learning space' in xml and 'Your next learning session will appear here.' in xml
    a('shell','screencap','-p','/sdcard/mingo-runtime.png')
    run('android-screenshot',[adb,'-s','emulator-5554','pull','/sdcard/mingo-runtime.png',str(out/'android-runtime.png')])
    log=a('logcat','-d','--pid='+pid)
    (out/'android-app-logcat.log').write_text(log,encoding='utf-8')
    assert 'FATAL EXCEPTION' not in log and 'E/flutter' not in log
    import hashlib
    (out/'android-runtime.json').write_text(json.dumps({'commit':subprocess.check_output(['git','rev-parse','HEAD'],cwd=root,text=True).strip(),'fresh_avd':'mingo_clean_20260926','package_absent_before_install':True,'boot_completed':1,'pid':pid,'ui_assertions':'PASS','startup_crash':'none in captured app log','apk_sha256':hashlib.sha256(apk.read_bytes()).hexdigest()},indent=2),encoding='utf-8')
    print('Fresh Android runtime PASS',flush=True)
elif sys.argv[1]=='web':
    web=root/'05_code/apps/staff/build/web';assert (web/'index.html').is_file()
    log=(out/'web-server.log').open('w',encoding='utf-8')
    server=subprocess.Popen([py,'-m','http.server','8132','--bind','127.0.0.1','--directory',str(web)],env=env,stdout=log,stderr=subprocess.STDOUT)
    try:
        for _ in range(30):
            try:
                status=urllib.request.urlopen('http://127.0.0.1:8132').status
                if status==200:break
            except Exception:pass
            time.sleep(1)
        else:raise RuntimeError('Web server not ready')
        profile=root/'.local/clean-chrome';assert not profile.exists()
        run('chrome-render',[r'C:\Program Files\Google\Chrome\Application\chrome.exe','--headless=new','--disable-gpu','--no-sandbox','--no-first-run','--user-data-dir='+str(profile),'--window-size=1440,900','--virtual-time-budget=15000','--screenshot='+str(out/'staff-web-runtime.png'),'--dump-dom','http://127.0.0.1:8132'])
        assert (out/'staff-web-runtime.png').is_file()
        (out/'web-runtime.json').write_text(json.dumps({'http_status':status,'fresh_browser_profile':True,'built_from_fresh_clone':True,'screenshot':'staff-web-runtime.png','visual_inspection':'required separately'},indent=2),encoding='utf-8')
        print('Web screenshot captured; inspect image',flush=True)
    finally:server.terminate();server.wait();log.close()
