$ErrorActionPreference='Stop'
$dir='C:/Mingo/outputs/mingo-ui-v2'
$manifest=Get-Content -Raw -LiteralPath "$dir/manifest.json" | ConvertFrom-Json
$app=New-Object -ComObject Excel.Application
$app.Visible=$false;$app.DisplayAlerts=$false;$app.EnableEvents=$false;$app.AutomationSecurity=3
try{
 $b=$app.Workbooks.Open("$dir/Mingo - Workspace.xlsx",0,$false)
 foreach($m in $manifest.sheets){
  $s=$b.Worksheets.Item($m.name)
  if($m.name -notin @('00_Tong_quan','01_Muc_luc','08_San_pham','17_Ghi_chu','20_Cach_lam_viec')){
   for($r=9;$r -le $m.last;$r++){
    $row=$s.Rows.Item($r)
    if($row.RowHeight -gt 31){$row.RowHeight=[Math]::Max(33,$row.RowHeight-8)}
   }
  }
  foreach($cell in $s.UsedRange.Cells){
   if(-not $cell.HasFormula -and $cell.Value2 -is [string]){
    $v=$cell.Value2.Replace('04_CONG_VIEC','02_Cong_viec').Replace('02_SAN_PHAM','08_San_pham')
    if($v -ne $cell.Value2){$cell.Value2=$v}
   }
  }
 }
 $s=$b.Worksheets.Item('00_Tong_quan')
 $s.Range('A1:I30').RowHeight=20
 $s.Rows.Item(4).RowHeight=39
 $s.Rows.Item(5).RowHeight=28
 $s.Rows.Item(8).RowHeight=30
 foreach($r in @(3,7,10,11,12,17,18,23,24,25,27,29,30)){$s.Rows.Item($r).RowHeight=10}
 $s.Range('E8:F8').HorizontalAlignment=-4131
 $s.Range('H8:I8').HorizontalAlignment=-4131
 $s=$b.Worksheets.Item('01_Muc_luc')
 $s.Range('A9:F39').RowHeight=18
 foreach($c in @('B','E')){foreach($start in @(10,26)){for($j=0;$j -lt 6;$j++){ $r=$start+$j*2;if($s.Range("$c$r").Value2){$s.Range("$c${r}:$c$($r+1)").Merge();$s.Range("$c${r}:$c$($r+1)").VerticalAlignment=-4108}}}}
 foreach($n in @('06_Roadmap','07_Checklist_P1','09_Luong_hoc','20_Cach_lam_viec')){$b.Worksheets.Item($n).Range('B9:B30').HorizontalAlignment=-4108}
 $s=$b.Worksheets.Item('05_Blocker')
 $s.Range('B19:B24').HorizontalAlignment=-4108
 $b.Worksheets.Item('02_Cong_viec').Range('H9:I204').HorizontalAlignment=-4108
 $b.Worksheets.Item('18_Bang_chung').Range('F9:F204').HorizontalAlignment=-4108
 $app.CalculateFullRebuild()
 $b.Worksheets.Item('00_Tong_quan').Activate()
 $b.Save()
 foreach($m in $manifest.sheets){$b.Worksheets.Item($m.name).ExportAsFixedFormat(0,"$dir/$($m.name).pdf")}
 $b.Close($false)
 Write-Output 'Final typography and spacing saved; all previews refreshed.'
}finally{$app.Quit();[System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)|Out-Null}
