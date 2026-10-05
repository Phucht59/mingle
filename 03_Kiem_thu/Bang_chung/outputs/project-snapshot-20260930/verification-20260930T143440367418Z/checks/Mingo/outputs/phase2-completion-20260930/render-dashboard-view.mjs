import fs from 'node:fs/promises';
import { Workbook } from '@oai/artifact-tool';
const dir='C:/Mingo/outputs/phase2-completion-20260930';
const source=JSON.parse(await fs.readFile('C:/Mingo/outputs/final-gate-20260930/workbook_rows.json','utf8'))['00_Dashboard'];
const edits=JSON.parse(await fs.readFile(`${dir}/dashboard-edits.json`,'utf8'));
const wb=Workbook.create(),s=wb.worksheets.add('Dashboard');
const rows=[];
for(let row=4;row<=11;row++){
 const original=source.find(r=>r.row===row)?.values??[];
 rows.push(Array.from({length:7},(_,col)=>{
  const cell=String.fromCharCode(68+col)+row;
  if(edits[cell])return edits[cell].value;
  const value=original[col+3]??null;
  return typeof value==='string'&&value.startsWith('=')?0:value;
 }));
}
s.getRange('A1:G8').values=rows;
s.showGridLines=false;
s.getRange('A1:G8').format.font={name:'Arial',size:10,color:'#172033'};
s.getRange('A1:G8').format.wrapText=true;
s.getRange('A1:G8').format.rowHeight=28;
s.getRange('A1:G8').format.verticalAlignment='center';
s.getRange('A1:G1').format={fill:'#1E293B',font:{name:'Arial',size:10,bold:true,color:'#FFFFFF'},rowHeight:30};
for(const [col,width] of Object.entries({A:26,B:16,C:13,D:34,E:18,F:18,G:18}))s.getRange(`${col}:${col}`).format.columnWidth=width;
s.getRange('C1:C8').format.fill='#FFFFFF';
s.getRange('B2:B8').setNumberFormat('0');
wb.recalculate();
const p=await wb.render({sheetName:'Dashboard',range:'A1:G8',scale:1,format:'png'});
await fs.writeFile(`${dir}/dashboard-corrected-view.png`,new Uint8Array(await p.arrayBuffer()));
console.log('Rendered corrected Dashboard display view (formula values authored/calculated separately).');
