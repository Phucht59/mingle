// Runtime smoke/navigation on compiled Flutter Web, separate from widget goldens.
const {chromium}=require('playwright');
const fs=require('fs'),path=require('path');
const out=process.env.MINGO_V2_RUNTIME_OUTPUT||'03_Kiem_thu/QA_QC/phase2/rebaseline_v2_20261001/web_runtime_final';fs.mkdirSync(out,{recursive:true});
(async()=>{
 const browser=await chromium.launch({executablePath:process.env.MINGO_CHROME||'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const results=[];
 async function run(name,url,viewport,fn){
  const context=await browser.newContext({viewport});const page=await context.newPage();page.setDefaultTimeout(20000);const errors=[];page.on('pageerror',e=>errors.push(e.message));
  let result={name,url,viewport,status:'PASS',browser:browser.version()};
  try{
   await page.goto(url);await page.locator('flt-glass-pane').waitFor({state:'attached'});
   // Apps explicitly enable web semantics at boot; never click the offscreen engine placeholder.
   await page.locator('flt-semantics').first().waitFor({state:'attached'});
   const btn=n=>page.getByRole('button',{name:n,exact:true});
   const click=async n=>{await btn(n).scrollIntoViewIfNeeded();await btn(n).click();};
   await fn(page,click);
   if(errors.length)throw Error(errors.join(';'));
   result.documentWidth=await page.evaluate(()=>document.documentElement.scrollWidth);
   if(result.documentWidth>viewport.width+1)throw Error('Horizontal document overflow');
   await page.screenshot({path:path.join(out,name+'.png')});
   result.semantics=await page.locator('flt-semantics').allTextContents();
  }catch(e){result.status='FAIL';result.error=e.message;await page.screenshot({path:path.join(out,name+'_failure.png')}).catch(()=>{});}
  results.push(result);console.log(name,result.status);await context.close();
 }
 for(const width of [360,412,430])await run('learner-'+width,process.env.MINGO_LEARNER_URL||'http://127.0.0.1:8765/',{width,height:915},async(p,click)=>{
  await click('Khám phá trước');await click('Bắt đầu học');await click('Tiếp tục');
  await click('Good night!');await click('Kiểm tra câu trả lời');
  await p.getByText('Nhìn lại thời điểm trong ngày',{exact:false}).first().waitFor({state:'attached'});
  await click('Thử thêm một lần');await click('Good morning!');await click('Kiểm tra câu trả lời');
  await p.getByText('Phù hợp với buổi sáng!',{exact:false}).first().waitFor({state:'attached'});
  await click('Quay lại');
  await p.getByText('Mục tiêu: nhận biết và đáp lại một lời chào.',{exact:false}).first().waitFor({state:'attached'});
  await click('Quay lại');await p.getByRole('button',{name:'Bắt đầu học',exact:true}).waitFor({state:'attached'});
  await click('Học');
  await p.getByRole('button',{name:/Nghe lời chào/}).click();await click('Tiếp tục');
  const sampleResponse=p.waitForResponse(r=>r.url().endsWith('hello.ogg')&&r.status()===200);
  await click('Nghe mẫu');await (await sampleResponse).finished();
  await p.getByRole('button',{name:'Nghe mẫu',exact:true}).waitFor({state:'attached'});
  if(await p.getByText('Âm thanh chưa sẵn sàng',{exact:false}).count())throw Error('Licensed sample playback initialization failed');
  await click('Hello!');await click('Kiểm tra câu trả lời');
  await p.getByText('Phù hợp với câu này!',{exact:false}).first().waitFor({state:'attached'});
 });
 for(const width of [1280,1440,1920])await run('staff-'+width,process.env.MINGO_STAFF_URL||'http://127.0.0.1:8766/',{width,height:1000},async(p,click)=>{
  await click('Xem hàng chờ duyệt');await p.getByRole('button',{name:/Chào hỏi và làm quen/}).click();
  await click('Kiểm tra nguồn và giấy phép');
  await p.getByRole('checkbox').check();await click('Tiếp tục kiểm tra bài');await p.getByRole('checkbox').check();
  await click('Xem bước xác nhận');await click('Xem xác nhận mẫu');
  await p.getByRole('button',{name:'Xem bản mẫu',exact:true}).waitFor({state:'attached'});
  await p.keyboard.press('Escape');
  await p.getByRole('button',{name:'Xem bản mẫu',exact:true}).waitFor({state:'detached'});
  await click('Xem xác nhận mẫu');await click('Xem bản mẫu');
  await p.getByText('Bản đã xuất bản',{exact:false}).first().waitFor({state:'attached'});
  await p.keyboard.press('Tab');const focus=await p.evaluate(()=>document.activeElement?.tagName);if(!focus)throw Error('No keyboard focus');
 });
 await run('staff-600',process.env.MINGO_STAFF_URL||'http://127.0.0.1:8766/',{width:600,height:800},async(p,click)=>{
  await click('Mở danh mục');await click('Nội dung');
  await p.getByText('Nội dung học',{exact:true}).waitFor({state:'attached'});
  await p.getByRole('button',{name:'Mở danh mục',exact:true}).waitFor({state:'visible'});
  if(await p.getByRole('button',{name:'Hỗ trợ',exact:true}).count())throw Error('Drawer remains open after selection');
 });
 fs.writeFileSync(path.join(out,'run.json'),JSON.stringify({scope:'Runtime navigation/rendering, not TalkBack/human UAT',results},null,2));await browser.close();process.exitCode=results.some(r=>r.status!=='PASS')?1:0;
})();
