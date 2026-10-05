import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
const out='C:/Mingo/outputs/mingo-ui-v2';
const source=JSON.parse(await fs.readFile('C:/Mingo/outputs/mingo-ui-20260927/source.json','utf8'));
const src=source.map(s=>Object.fromEntries(s.data.flat()));
const w=Workbook.create(), manifest=[],links=[],audit=[];
const pal={ink:'#242927',muted:'#6D746F',green:'#285B47',line:'#E2E6E2',head:'#F3F5F2',soft:'#F8F9F7',white:'#FFFFFF'};
const names=['00_Tong_quan','01_Muc_luc','02_Cong_viec','03_Hanh_dong','04_Nghiem_thu','05_Blocker','06_Roadmap','07_Checklist_P1','08_San_pham','09_Luong_hoc','10_Quy_tac','11_Da_chot','12_Gia_thuyet','13_Baseline_V3_2','14_Van_de','15_Xu_ly_van_de','16_Thay_doi','17_Ghi_chu','18_Bang_chung','19_Pham_vi_test','20_Cach_lam_viec','21_Tu_dien'];
names.forEach(n=>w.worksheets.add(n));
function col(n){let a='';for(;n;n=Math.floor((n-1)/26))a=String.fromCharCode(65+(n-1)%26)+a;return a;}
function F(size=11,color=pal.ink,semibold=false){return {name:semibold?'Segoe UI Semibold':'Segoe UI',size:Math.round(size),color,bold:false};}
function set(s,addr,v){if(v===undefined||v===null)return;if(typeof v==='string'&&v.startsWith('='))s.getRange(addr).formulas=[[v]];else{s.getRange(addr).values=[[/^\d{4}-\d\d-\d\d 00:00:00$/.test(v)?new Date(v.replace(' ','T')+'Z'):v]];}}
function merge(s,range,value,size=11,color=pal.ink,bold=false){s.getRange(range).merge();set(s,range.split(':')[0],value);s.getRange(range).format={font:F(size,color,bold),wrapText:true,verticalAlignment:'center'};}
function take(si,addr,s,target){const v=src[si][addr];set(s,target,v);if(v!==undefined)audit.push({source:source[si].name,cell:addr,target:s.name,at:target,value:v});}
function formula(v){return v.replaceAll("'04_CONG_VIEC'!$A$5:$F$200,6,FALSE","'02_Cong_viec'!$B$9:$F$204,5,FALSE").replaceAll("'04_CONG_VIEC'!$B$5:$B$200","'02_Cong_viec'!$C$9:$C$204").replaceAll("'04_CONG_VIEC'!$F$5:$F$200","'02_Cong_viec'!$F$9:$F$204");}
function sheet(i,title,subtitle,widths,group){const s=w.worksheets.getItemAt(i),end=col(widths.length+1);s.showGridLines=false;s.getRange(`A1:${end}55`).format={font:F(),fill:pal.white,rowHeight:24,wrapText:true,verticalAlignment:'center'};s.getRange('A1:A55').format.columnWidthPx=28;widths.forEach((v,j)=>s.getRange(`${col(j+2)}1:${col(j+2)}55`).format.columnWidthPx=v);merge(s,`B2:${end}2`,`M I N G O    /    ${group}`,10,pal.green,true);merge(s,`B4:${end}4`,title,24,pal.ink,true);s.getRange(`B4:${end}4`).format.rowHeight=39;merge(s,`B5:${end}5`,subtitle,10.5,pal.muted);s.getRange(`B5:${end}5`).format.rowHeight=30;s.getRange(`B6:${end}6`).format={rowHeight:10,borders:{bottom:{style:'thin',color:pal.line}}};s.getRange(`B7:${end}7`).format.rowHeight=12;s.tabColor=i<2?pal.green:'#AEBDB2';manifest.push({name:s.name,title,group,end,last:26,kind:'table',width:widths.reduce((a,b)=>a+b,28)});if(i!==1){const last=col(widths.length+1);links.push({sheet:s.name,cell:`${last}1`,text:'← Mục lục',target:'01_Muc_luc'});}return s;}
function rows(s,headers,data,heights=40,tableName){const end=col(headers.length+1);s.getRange(`B8:${end}8`).values=[headers];s.getRange(`B8:${end}8`).format={fill:pal.head,font:F(10,pal.muted,true),rowHeight:31,verticalAlignment:'center',wrapText:true,borders:{bottom:{style:'thin',color:pal.line}}};data.forEach((row,j)=>{const r=j+9;row.forEach((v,k)=>set(s,`${col(k+2)}${r}`,v));s.getRange(`B${r}:${end}${r}`).format={font:F(),fill:pal.white,rowHeight:Array.isArray(heights)?heights[j]:heights,wrapText:true,verticalAlignment:'center',borders:{bottom:{style:'thin',color:pal.line}}};});if(tableName){const t=s.tables.add(`B8:${end}${8+data.length}`,true,tableName);t.style='TableStyleLight1';t.showFilterButton=true;}s.freezePanes.freezeRows(8);s.freezePanes.freezeColumns(2);manifest.find(x=>x.name===s.name).last=8+data.length;}
function mapTable(s,si,sourceRows,sourceCols,destCols){sourceRows.forEach((r,j)=>sourceCols.forEach((c,k)=>{if(c&&src[si][c+r]!==undefined)audit.push({source:source[si].name,cell:c+r,target:s.name,at:`${destCols?.[k]??col(k+2)}${j+9}`,value:src[si][c+r]});}));}
function stat(s,a){const states=[['ĐANG LÀM','#EAF1EB','#285B47'],['XONG','#EAF1EB','#285B47'],['PASS','#EAF1EB','#285B47'],['ĐÃ GIẢI QUYẾT','#EAF1EB','#285B47'],['BỊ CHẶN','#F8ECE9','#A64B3C'],['FAIL','#F8ECE9','#A64B3C'],['CHỜ','#F6F2E5','#867039'],['CHỜ CHẠY','#F6F2E5','#867039'],['MỞ','#F6F2E5','#867039'],['TẠM HOÃN','#F0F1F0','#777C78'],['CHƯA LÀM','#F0F1F0','#777C78'],['PASS LỊCH SỬ','#F0EDF5','#77658D'],['TÌM THẤY / CHỜ CHẠY LẠI','#F0EDF5','#77658D']];const r=s.getRange(a);for(const[v,bg,fg]of states)r.conditionalFormats.add('cellIs',{operator:'equal',formula:`"${v}"`,format:{fill:bg,font:{color:fg}}});r.format.horizontalAlignment='center';}
function listSheet(i,title,sub,si,a,b,group){const s=sheet(i,title,sub,[235,835],group);const data=Array.from({length:b-a+1},(_,j)=>[src[si]['A'+(a+j)],src[si]['B'+(a+j)]]);rows(s,['Chủ đề','Nội dung'],data,44);mapTable(s,si,Array.from({length:b-a+1},(_,j)=>a+j),['A','B']);return s;}
const taskRows=Array.from({length:13},(_,j)=>j+5);
{
const s=sheet(2,'Công việc','Cập nhật trạng thái, người phụ trách và hạn tại đây.',[98,55,325,68,128,135,105,115],'THỰC HIỆN');
const cs=['A','B','D','E','F','G','I','J'];rows(s,['Task ID','Phase','Công việc','Ưu tiên','Trạng thái','Phụ trách','Hạn','Cập nhật'],taskRows.map(r=>cs.map(c=>src[4][c+r])),45,'DailyTasksTable');mapTable(s,4,taskRows,cs);s.getRange('H9:I204').setNumberFormat('dd/mm/yy');s.getRange('E9:E204').dataValidation={rule:{type:'list',values:['P0','P1','P2','P3']}};s.getRange('F9:F204').dataValidation={rule:{type:'list',values:['CHƯA LÀM','CHỜ','ĐANG LÀM','BỊ CHẶN','XONG','TẠM HOÃN']}};stat(s,'F9:F204');
}
{
const s=sheet(3,'Hành động tiếp theo','Chi tiết theo Task ID · trạng thái cập nhật ở Công việc.',[98,130,165,360,350],'THỰC HIỆN');const cs=['A','C','K','L','N'];rows(s,['Task ID','Nhóm','Phụ thuộc','Việc tiếp theo','Ghi chú'],taskRows.map(r=>cs.map(c=>src[4][c+r])),51,'TaskActions');mapTable(s,4,taskRows,cs);
}
{
const s=sheet(4,'Nghiệm thu task','Người kiểm tra và bằng chứng hoàn thành.',[98,390,160,425],'THỰC HIỆN');rows(s,['Task ID','Công việc','Người kiểm tra','Bằng chứng'],taskRows.map((r,j)=>[src[4]['A'+r],`=VLOOKUP(B${9+j},'02_Cong_viec'!$B$9:$D$204,3,FALSE)`,src[4]['H'+r],src[4]['M'+r]]),43,'TaskAcceptance');mapTable(s,4,taskRows,['A',null,'H','M']);
}
{
const s=sheet(5,'Blocker','Trạng thái nhóm tự cập nhật từ công việc.',[190,140,535,205],'THỰC HIỆN');rows(s,['Nhóm','Trạng thái','Việc tiếp theo','Task nguồn'],Array.from({length:6},(_,j)=>{const r=j+6;return[src[1]['D'+r],formula(src[1]['E'+r]),src[1]['F'+r],src[1]['G'+r]]}),53,'BlockerGroups');stat(s,'C9:C14');mapTable(s,1,[6,7,8,9,10,11],['D',null,'F','G']);
}
{
const s=sheet(6,'Roadmap','Phase 0–17 · mỗi dòng là một giai đoạn.',[58,230,310,305,120,190],'KẾ HOẠCH');const cs=['A','B','C','D','E','F'];rows(s,['Phase','Giai đoạn','Mục tiêu','Điều kiện hoàn thành','Trạng thái','Ghi chú'],Array.from({length:18},(_,j)=>cs.map(c=>{const v=src[3][c+(5+j)];return typeof v==='string'&&v.startsWith('=')?formula(v):v;})),53,'RoadmapFixedTable');mapTable(s,3,Array.from({length:18},(_,j)=>j+5),cs);stat(s,'F9:F26');
}
{
const s=sheet(7,'Checklist Phase 1','Điều kiện nghiệm thu · trạng thái liên kết với Công việc.',[36,133,320,290,100,130,115],'KẾ HOẠCH');const cs=['A','B','C','D','E','F','G'];rows(s,['#','Nhóm','Việc cần làm','PASS khi','Task ID','Trạng thái','Phụ thuộc'],Array.from({length:12},(_,j)=>cs.map(c=>{const v=src[3][c+(27+j)];return typeof v==='string'&&v.startsWith('=')?formula(v):v;})),54,'Phase1Checklist');mapTable(s,3,Array.from({length:12},(_,j)=>j+27),cs);stat(s,'G9:G20');
}
{
const s=sheet(8,'Sản phẩm Mingo','Adaptive Language Learning & Early Intervention Platform',[40,275,755],'SẢN PHẨM');merge(s,'B8:D11',src[2].A11,12);s.getRange('B8:D11').format.rowHeight=24;merge(s,'B14:D14','Bốn nguyên tắc nền tảng',14,pal.ink,true);for(let j=0;j<4;j++){const r=16+j*3;merge(s,`B${r}:B${r+1}`,String(j+1).padStart(2,'0'),11,pal.green);merge(s,`C${r}:C${r+1}`,src[2]['B'+(5+j)],12,pal.ink,true);merge(s,`D${r}:D${r+1}`,src[2]['C'+(5+j)]);s.getRange(`B${r+1}:D${r+1}`).format.borders={bottom:{style:'thin',color:pal.line}};}manifest.find(x=>x.name===s.name).last=27;
}
{
const s=sheet(9,'Luồng học','Từ lúc mở app đến khi tích lũy bằng chứng học tập.',[60,290,720],'SẢN PHẨM');rows(s,['Bước','Nghiệp vụ','Hệ thống làm gì'],Array.from({length:11},(_,j)=>['A','B','C'].map(c=>src[2][c+(17+j)])),47,'LearnerFlowFixed');mapTable(s,2,Array.from({length:11},(_,j)=>j+17),['A','B','C']);
}
listSheet(10,'Quy tắc nghiệp vụ','Các nguyên tắc dễ hiểu sai khi triển khai.',2,32,42,'SẢN PHẨM');
listSheet(11,'Nội dung đã chốt','Muốn thay đổi nội dung ở đây: tạo đề nghị thay đổi.',2,47,60,'SẢN PHẨM');
listSheet(12,'Giả thuyết & chính sách','Các giả thuyết còn có thể thay đổi sau đo lường hoặc pilot.',2,65,73,'SẢN PHẨM');
listSheet(13,'Baseline V3.2','Nguồn chuẩn Phase 0 · phạm vi đã và chưa được chứng minh.',2,78,89,'SẢN PHẨM');
{
const s=sheet(14,'Vấn đề','Theo dõi issue, mức ưu tiên và người xử lý.',[90,280,250,90,155,205],'VẤN ĐỀ & THAY ĐỔI');const cs=['A','B','D','E','F','G'];rows(s,['Issue ID','Vấn đề','Trạng thái','Ưu tiên','Phụ trách','Task liên quan'],Array.from({length:9},(_,j)=>cs.map(c=>src[5][c+(6+j)])),43,'IssuesFixedTable');mapTable(s,5,Array.from({length:9},(_,j)=>j+6),cs);s.getRange('D9:D100').dataValidation={rule:{type:'list',values:['MỞ','BỊ CHẶN','TÌM THẤY / CHỜ CHẠY LẠI','ĐÃ GIẢI QUYẾT','TẠM HOÃN']}};stat(s,'D9:D100');
}
{
const s=sheet(15,'Xử lý vấn đề','Mô tả, hướng xử lý và bằng chứng theo Issue ID.',[85,325,345,180,135],'VẤN ĐỀ & THAY ĐỔI');const cs=['A','C','H','I','J'];rows(s,['Issue ID','Mô tả','Cách xử lý','Bằng chứng / commit','Cập nhật'],Array.from({length:9},(_,j)=>cs.map(c=>src[5][c+(6+j)])),62,'IssueDetails');mapTable(s,5,Array.from({length:9},(_,j)=>j+6),cs);s.getRange('F9:F100').setNumberFormat('dd/mm/yy');
}
{
const s=sheet(16,'Đề nghị thay đổi','Dành cho thay đổi nội dung đã chốt. Hiện chưa có đề nghị.',[80,95,125,245,160,155,230,120,120],'VẤN ĐỀ & THAY ĐỔI');rows(s,['CR ID','Ngày','Người đề nghị','Nội dung muốn đổi','Lý do','Ảnh hưởng','Test / migration','Trạng thái','Người duyệt'],Array.from({length:5},()=>Array(9).fill(null)),45,'ChangeRequests');s.getRange('C9:C100').setNumberFormat('dd/mm/yy');s.getRange('I9:I100').dataValidation={rule:{type:'list',values:['NHÁP','ĐANG XEM','ĐÃ DUYỆT','TỪ CHỐI','ĐÃ TRIỂN KHAI','HỦY']}};
}
{
const s=sheet(17,'Ghi chú & action','Thảo luận và hành động ngoài danh sách task.',[150,385,30,150,385],'VẤN ĐỀ & THAY ĐỔI');for(let j=0;j<2;j++){const a=j?'E':'B',b=j?'F':'C',r=28+j;merge(s,`${a}8:${b}8`,src[5]['A'+r],14,pal.ink,true);const fields=[['Ngày','B'],['Phase','C'],['Chủ đề','D'],['Nội dung','E'],['Việc cần làm','F'],['Phụ trách','G'],['Hạn','H'],['Trạng thái','I'],['Liên kết','J']];fields.forEach(([label,c],k)=>{const rr=10+k*2;merge(s,`${a}${rr}:${a}${rr+1}`,label,10.5,pal.muted);merge(s,`${b}${rr}:${b}${rr+1}`,src[5][c+r]);audit.push({source:source[5].name,cell:c+r,target:s.name,at:b+rr,value:src[5][c+r]});});s.getRange(`${b}10`).setNumberFormat('dd/mm/yy');s.getRange(`${b}22`).setNumberFormat('dd/mm/yy');s.getRange(`${b}24`).dataValidation={rule:{type:'list',values:['MỞ','ĐANG LÀM','BỊ CHẶN','XONG','HỦY']}};stat(s,`${b}24:${b}25`);}manifest.find(x=>x.name===s.name).last=28;
}
{
const s=sheet(18,'Bằng chứng','Trạng thái test / runtime / CI. Phạm vi và giới hạn ở sheet kế tiếp.',[70,165,380,150,115,190],'KIỂM CHỨNG');const cs=['A','B','C','E','F','G'];rows(s,['ID','Khu vực','Kiểm tra','Trạng thái','Ngày','Nguồn'],Array.from({length:15},(_,j)=>cs.map(c=>src[6][c+(5+j)])),39,'EvidenceFixedTable');mapTable(s,6,Array.from({length:15},(_,j)=>j+5),cs);s.getRange('F9:F204').setNumberFormat('dd/mm/yy');s.getRange('E9:E204').dataValidation={rule:{type:'list',values:['PASS','PASS LỊCH SỬ','CHỜ CHẠY','BỊ CHẶN','FAIL']}};stat(s,'E9:E204');
}
{
const s=sheet(19,'Phạm vi bằng chứng','Kết quả quan sát và giới hạn. Không đồng nhất PASS lịch sử với PASS hiện tại.',[70,500,500],'KIỂM CHỨNG');const cs=['A','D','H'];rows(s,['ID','Kết quả quan sát','Phạm vi / giới hạn'],Array.from({length:15},(_,j)=>cs.map(c=>src[6][c+(5+j)])),44,'EvidenceScope');mapTable(s,6,Array.from({length:15},(_,j)=>j+5),cs);
}
{
const s=sheet(20,'Cách làm việc','Năm quy tắc chung của dự án.',[55,360,655],'HƯỚNG DẪN');rows(s,['#','Quy tắc','Ý nghĩa'],Array.from({length:5},(_,j)=>['A','B','C'].map(c=>src[0][c+(15+j)])),65);mapTable(s,0,[15,16,17,18,19],['A','B','C']);merge(s,'B17:D17','Cập nhật theo thứ tự',14,pal.ink,true);merge(s,'B19:D21',src[4].A20,12);manifest.find(x=>x.name===s.name).last=22;
}
listSheet(21,'Từ điển dự án','Giải thích các thuật ngữ dùng trong workbook.',0,23,30,'HƯỚNG DẪN');
{
const s=sheet(0,'Tổng quan','Mingo · Adaptive Language Learning & Early Intervention Platform',[180,180,30,180,180,30,180,180],'DỰ ÁN');
merge(s,'B8:C8','Phase 1',21,pal.ink,true);merge(s,'E8:F8',formula(src[1].B10),21,pal.ink,true);s.getRange('E8').setNumberFormat('0%');merge(s,'H8:I8',`=COUNTIFS('02_Cong_viec'!$F$9:$F$204,"BỊ CHẶN")`,21,pal.ink,true);merge(s,'B9:C9','Nền tảng triển khai',10.5,pal.muted);merge(s,'E9:F9','Task Phase 1 đã hoàn tất',10.5,pal.muted);merge(s,'H9:I9','Task đang bị chặn',10.5,pal.muted);s.getRange('B11:I11').format.borders={bottom:{style:'thin',color:pal.line}};
merge(s,'B13:I13','Mục tiêu',10.5,pal.muted);merge(s,'B14:I16',src[1].B6,13);merge(s,'B19:C19','Trạng thái Phase 1',10.5,pal.muted);merge(s,'E19:I19',formula(src[1].B8),12,pal.green,true);merge(s,'B20:C20','Gate Phase 1',10.5,pal.muted);merge(s,'E20:I20',formula(src[1].B9),12,'#867039',true);merge(s,'B21:C21','Phase 2',10.5,pal.muted);merge(s,'E21:I21',src[1].B12.replace('B9','E20'),11,pal.muted);merge(s,'B22:C22','Phase 0',10.5,pal.muted);merge(s,'E22:I22',src[1].B11,11,pal.muted);s.getRange('B24:I24').format.borders={bottom:{style:'thin',color:pal.line}};
merge(s,'B26:I26','Đi tới',10.5,pal.muted);for(const [at,t,txt]of [['B28',2,'Công việc →'],['E28',5,'Blocker →'],['H28',1,'Tất cả sheet →']]){links.push({sheet:s.name,cell:at,target:names[t],text:txt});merge(s,`${at}:${col(at.charCodeAt(0)-64+1)}28`,txt,12,pal.green,true);}manifest.find(x=>x.name===s.name).last=30;
}
{
const s=sheet(1,'Mục lục','Chọn một sheet theo việc bạn đang cần làm.',[55,385,40,55,535],'ĐIỀU HƯỚNG');const groups=[['Thực hiện',[2,3,4,5,6,7]],['Sản phẩm',[8,9,10,11,12,13]],['Vấn đề & kiểm chứng',[14,15,16,17,18,19]],['Bắt đầu & hướng dẫn',[0,20,21]]];for(let g=0;g<4;g++){const c=g%2===0?'B':'E',last=g%2===0?'C':'F',start=g<2?8:24;merge(s,`${c}${start}:${last}${start}`,groups[g][0],14,pal.ink,true);groups[g][1].forEach((id,j)=>{const r=start+2+j*2;set(s,c+r,String(id).padStart(2,'0'));s.getRange(c+r).format.font=F(10.5,pal.muted);merge(s,`${last}${r}:${last}${r+1}`,manifest.find(x=>x.name===names[id]).title,12,pal.green);links.push({sheet:s.name,cell:last+r,target:names[id],text:manifest.find(x=>x.name===names[id]).title});});}manifest.find(x=>x.name===s.name).last=39;
}
// Restore source instructions as concise sheet-specific context, not large banners.
const phaseNext=w.worksheets.getItemAt(5);merge(phaseNext,'B17:E17','Thứ tự triển khai',14,pal.ink,true);for(let j=0;j<6;j++){const r=19+j;set(phaseNext,'B'+r,src[1]['A'+(17+j)]);merge(phaseNext,`C${r}:D${r}`,src[1]['B'+(17+j)],11);set(phaseNext,'E'+r,src[1]['C'+(17+j)]);phaseNext.getRange(`B${r}:E${r}`).format.rowHeight=45;}manifest.find(x=>x.name===phaseNext.name).last=25;
// Status is the only color-coded operational field; priorities remain understated text.
for(const m of manifest){const s=w.worksheets.getItem(m.name);s.getRange(`B8:${m.end}${m.last}`).format.wrapText=true;}
w.recalculate();
console.log((await w.inspect({kind:'match',searchTerm:'#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!',options:{useRegex:true,maxResults:30},maxChars:2000})).ndjson);
const file=await SpreadsheetFile.exportXlsx(w);await file.save(`${out}/Mingo - Workspace.xlsx`);
await fs.writeFile(`${out}/manifest.json`,JSON.stringify({sheets:manifest,links,audit},null,2));
console.log('Exported',manifest.length,'focused sheets.');
