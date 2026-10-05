const {chromium}=require('playwright');
const fs=require('fs');
const out='C:/Mingo/outputs/d021-fix-20260930';
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 const results=[];
 for(const route of ['Home','Learn','Course','Profile']){
  const context=await browser.newContext({viewport:{width:320,height:1000}});
  const page=await context.newPage();await page.goto('http://127.0.0.1:8765/');
  for(const name of ['Start learning','Skip for now','Start without it','Go to Home'])await page.getByRole('button',{name,exact:true}).click();
  if(route!=='Home')await page.getByRole('button',{name:route,exact:true}).click();
  await page.evaluate(()=>{const els=[...document.querySelectorAll('body,body *')];const sizes=els.map(e=>parseFloat(getComputedStyle(e).fontSize));els.forEach((e,i)=>e.style.fontSize=sizes[i]*2+'px');});
  const metrics=await page.evaluate(()=>{
   const measure=e=>{const r=e.getBoundingClientRect();return {tag:e.tagName,classes:e.className,id:e.id,text:e.textContent.trim().slice(0,130),left:r.left,right:r.right,width:r.width,scrollWidth:e.scrollWidth}};
   const overflow=selector=>[...document.querySelectorAll(selector)].filter(e=>e.getClientRects().length&&(e.getBoundingClientRect().right>innerWidth+1||e.getBoundingClientRect().left < -1)).map(measure);
   return {viewport:innerWidth,document:document.documentElement.scrollWidth,app:measure(document.querySelector('#app')),phone:measure(document.querySelector('.phone')),allOverflow:overflow('body *'),learnerOverflow:overflow('#app *'),toolbarOverflow:overflow('.prototype-bar *'),bottomNav:[...document.querySelectorAll('.bottom-nav button')].map(measure)};
  });
  await page.screenshot({path:out+'/D021-'+route+'.png',fullPage:true});results.push({route,...metrics});await context.close();
 }
 fs.writeFileSync(out+'/D021-runtime.json',JSON.stringify({platform:process.platform,browser:browser.version(),method:'Original R1 assets; 320px viewport; each computed font size doubled (same text-scale proxy as canonical supplemental test). No source change. This is not interactive assistive technology.',results},null,2));
 console.log(JSON.stringify(results.map(r=>({route:r.route,document:r.document,app:r.app.width,learnerOverflow:r.learnerOverflow.length,toolbarOverflow:r.toolbarOverflow.length}))));
 await browser.close();
})().catch(e=>{console.error(e);process.exitCode=1});
