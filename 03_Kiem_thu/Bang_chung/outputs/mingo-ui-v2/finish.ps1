$ErrorActionPreference='Stop'
$dir='C:/Mingo/outputs/mingo-ui-v2'
$manifest=Get-Content -Raw -LiteralPath "$dir/manifest.json" | ConvertFrom-Json
$app=New-Object -ComObject Excel.Application
$app.Visible=$false
$app.DisplayAlerts=$false
$app.EnableEvents=$false
$app.AutomationSecurity=3
try{
 $book=$app.Workbooks.Open("$dir/Mingo - Workspace.xlsx",0,$false)
 foreach($m in $manifest.sheets){
  $s=$book.Worksheets.Item($m.name)
  $s.Activate()
  $app.ActiveWindow.DisplayGridlines=$false
  $app.ActiveWindow.DisplayHeadings=$false
  $app.ActiveWindow.Zoom=100
  $app.ActiveWindow.ScrollRow=1
  $app.ActiveWindow.ScrollColumn=1
  if($m.name -in @('00_Tong_quan','01_Muc_luc','08_San_pham','17_Ghi_chu','20_Cach_lam_viec')){$app.ActiveWindow.FreezePanes=$false}
  foreach($t in $s.ListObjects){$t.ShowAutoFilter=$true;$t.ShowTableStyleRowStripes=$false;$t.ShowTableStyleColumnStripes=$false}
  $s.Range('A1').Select() | Out-Null
  $s.PageSetup.PrintArea="A1:$($m.end)$($m.last)"
  $s.PageSetup.Orientation=2
  $s.PageSetup.PaperSize=8
  $s.PageSetup.Zoom=$false
  $s.PageSetup.FitToPagesWide=1
  $s.PageSetup.FitToPagesTall=1
  $s.PageSetup.LeftMargin=22
  $s.PageSetup.RightMargin=22
  $s.PageSetup.TopMargin=22
  $s.PageSetup.BottomMargin=22
 }
 foreach($l in $manifest.links){
  $s=$book.Worksheets.Item($l.sheet)
  $r=$s.Range($l.cell)
  $s.Hyperlinks.Add($r,'',"'$($l.target)'!A1",'',$l.text) | Out-Null
  $r.Font.Name='Segoe UI'
  $r.Font.Size=11
  $r.Font.Color=4676392
  $r.Font.Underline=-4142
  if($l.cell -match '1$'){$r.HorizontalAlignment=-4152;$r.WrapText=$false}
 }
 $app.CalculateFullRebuild()
 $book.Worksheets.Item('00_Tong_quan').Activate()
 $book.Save()
 Write-Output 'Saved 22-sheet workbook in native Excel.'
 foreach($m in $manifest.sheets){
  $book.Worksheets.Item($m.name).ExportAsFixedFormat(0,"$dir/$($m.name).pdf")
  Write-Output "Preview $($m.name)"
 }
 Write-Output "Before test: progress=$($book.Worksheets.Item('00_Tong_quan').Range('E8').Value2), blocked=$($book.Worksheets.Item('00_Tong_quan').Range('H8').Value2), checklist=$($book.Worksheets.Item('07_Checklist_P1').Range('G9').Value2)"
 $book.Worksheets.Item('02_Cong_viec').Range('F9').Value2='XONG'
 $app.CalculateFullRebuild()
 if([Math]::Abs($book.Worksheets.Item('00_Tong_quan').Range('E8').Value2-1.0/12.0) -gt 0.000001){throw 'Progress reaction failed'}
 if($book.Worksheets.Item('07_Checklist_P1').Range('G9').Value2 -ne 'XONG'){throw 'Checklist reaction failed'}
 Write-Output 'PASS: task status updates progress and checklist.'
 $book.Close($false)
 $book=$app.Workbooks.Open("$dir/Mingo - Workspace.xlsx",0,$true)
 if($book.Worksheets.Item('02_Cong_viec').Range('F9').Value2 -ne 'ĐANG LÀM'){throw 'Test input leaked'}
 Write-Output "Reopen OK. Sheets=$($book.Worksheets.Count), hyperlinks=$($book.Worksheets.Item('01_Muc_luc').Hyperlinks.Count)"
 $book.Close($false)
}finally{$app.Quit();[System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)|Out-Null}
