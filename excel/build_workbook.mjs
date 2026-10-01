import fs from 'node:fs/promises';
import {Workbook,SpreadsheetFile} from '@oai/artifact-tool';
import {fileURLToPath} from 'node:url';
const root=fileURLToPath(new URL('../',import.meta.url)).replace(/\/$/,'');
const d=JSON.parse(await fs.readFile(root+'/outputs/workbook_data.json','utf8'));
const w=Workbook.create();const s=w.worksheets.add('Campaign analysis');const data=w.worksheets.add('Clean data');
const fields=['date','campaign_id','channel','audience','spend','impressions','clicks','acquisitions','revenue','contribution_profit','month'];
data.getRange('A1:K1').values=[fields];data.getRange(`A2:K${d.clean.length+1}`).values=d.clean.map(r=>fields.map(f=>f==='date'?r[f].slice(0,10):r[f]));
data.tables.add(`A1:K${d.clean.length+1}`,true,'CampaignData');data.freezePanes.freezeRows(1);
s.mergeCells('A1:H1');s.getRange('A1').values=[['MARKETING CAMPAIGN & ROI ANALYTICS']];
s.mergeCells('A2:H2');s.getRange('A2').values=[['SYNTHETIC DATA | 2025 | INR | 55% assumed contribution margin']];
s.getRange('A4:M4').values=[['Channel','Spend','Impressions','Clicks','Acquisitions','Revenue','Contribution before marketing','Net contribution','CTR','Conversion rate','CPA','ROAS','ROI']];
const end=d.clean.length+1;const formulas=[];
for(let i=0;i<5;i++){const r=i+5;s.getRange(`A${r}`).values=[[d.channels[i]]];formulas.push(['E','F','G','H','I','J'].map(c=>`=SUMIF('Clean data'!$C$2:$C$${end},A${r},'Clean data'!$${c}$2:$${c}$${end})`).concat([`=G${r}-B${r}`,`=IFERROR(D${r}/C${r},"")`,`=IFERROR(E${r}/D${r},"")`,`=IFERROR(B${r}/E${r},"")`,`=IFERROR(F${r}/B${r},"")`,`=IFERROR(H${r}/B${r},"")`]));}
s.getRange('B5:M9').formulas=formulas;s.getRange('A10').values=[['TOTAL']];s.getRange('B10:H10').formulas=[['B','C','D','E','F','G','H'].map(c=>`=SUM(${c}5:${c}9)`)];s.getRange('I10:M10').formulas=[['=IFERROR(D10/C10,"")','=IFERROR(E10/D10,"")','=IFERROR(B10/E10,"")','=IFERROR(F10/B10,"")','=IFERROR(H10/B10,"")']];
for(const sh of [s,data]){sh.showGridLines=false;sh.getUsedRange().format.font={name:'Aptos',size:11};sh.getUsedRange().format.columnWidth=17;sh.getUsedRange().format.rowHeight=23;}
s.getRange('A1:M1').format={fill:'#10243A',font:{bold:true,color:'#FFFFFF',size:18},rowHeight:38};s.getRange('A4:M4').format={fill:'#0D9488',font:{bold:true,color:'#FFFFFF'},wrapText:true,rowHeight:48};s.getRange('A10:M10').format.fill='#DDECF1';s.getRange('B5:H10').setNumberFormat('#,##0');s.getRange('I5:J10').setNumberFormat('0.0%');s.getRange('K5:L10').setNumberFormat('0.00');s.getRange('M5:M10').setNumberFormat('0.0%');data.getRange(`E2:J${end}`).setNumberFormat('#,##0.00');data.getRange('A1:K1').format={fill:'#10243A',font:{bold:true,color:'#FFFFFF'}};
s.getRange('M5:M9').conditionalFormats.add('cellIs',{operator:'lessThan',formula:0,format:{fill:'#FEE2E2',font:{color:'#991B1B'}}});
const chart=s.charts.add('bar',[s.getRange('A4:A9'),s.getRange('M4:M9')]);chart.title='Profit-based ROI by channel';chart.setPosition('A13','G28');chart.yAxis={numberFormatCode:'0%',numberFormatSourceLinked:false};
s.mergeCells('A30:M30');s.getRange('A30').values=[['ROI = (contribution before marketing − spend) / spend. ROAS = revenue / spend. Totals use ratios of sums.']];
s.mergeCells('A31:M31');s.getRange('A31').values=[['Source: generated campaign-day simulation. Rejected records are provided separately. No causal or unique-customer claims.']];
w.recalculate();console.log((await w.inspect({kind:'region',sheetId:s.name,range:'A5:M10',maxChars:2500,tableMaxCols:13})).ndjson);
await fs.writeFile(root+'/outputs/excel_preview.png',new Uint8Array(await (await w.render({sheetName:s.name,range:'A1:M31',scale:1,format:'png'})).arrayBuffer()));
await (await SpreadsheetFile.exportXlsx(w)).save(root+'/excel/Marketing_ROI_Analysis.xlsx');
