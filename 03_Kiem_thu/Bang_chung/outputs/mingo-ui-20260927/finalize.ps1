$ErrorActionPreference='Stop'
$dir='C:/Mingo/outputs/mingo-ui-20260927'
$app=New-Object -ComObject Excel.Application
$app.Visible=$false
$app.DisplayAlerts=$false
$app.EnableEvents=$false
$app.AutomationSecurity=3
try{
 $book=$app.Workbooks.Open("$dir/Manage Project - Redesigned.xlsx",0,$false)
 foreach($sheet in $book.Worksheets){
  $sheet.Activate()
  $app.ActiveWindow.DisplayGridlines=$false
  $app.ActiveWindow.Zoom=90
  $app.ActiveWindow.ScrollRow=1
  $app.ActiveWindow.ScrollColumn=1
  foreach($table in $sheet.ListObjects){$table.ShowAutoFilter=$true}
  $sheet.Range('A1').Select()
 }
 $cover=$book.Worksheets.Item('00_BAT_DAU')
 $cover.Range('A1:S82').RowHeight=20
 $cover.Range('A2:S3').RowHeight=27
 $cover.Range('A9:S9').RowHeight=30
 $cover.Range('A17:S17').RowHeight=30
 $overview=$book.Worksheets.Item('01_TONG_QUAN')
 $overview.Range('A1:S41').RowHeight=22
 $overview.Range('A2:S3').RowHeight=27
 $overview.Range('A15:S16').RowHeight=35
 $overview.Range('A19:S19').RowHeight=30
 $overview.Range('A20:S25').RowHeight=36
 $overview.Range('A29:S29').RowHeight=30
 $overview.Range('A30:S35').RowHeight=34
 foreach($r in @('G7:J8','L7:N8','P7:R8')){$overview.Range($r).HorizontalAlignment=-4131}
 $product=$book.Worksheets.Item('02_SAN_PHAM')
 $product.Columns.Item('A').ColumnWidth=42
 $issues=$book.Worksheets.Item('05_VAN_DE_THAY_DOI')
 $issues.Columns.Item('D').ColumnWidth=40
 $issues.Range('D6:D14').WrapText=$true
 $issues.Range('E6:E14').HorizontalAlignment=-4108
 $issues.Range('J6:J14').HorizontalAlignment=-4108
 $book.Worksheets.Item('04_CONG_VIEC').Range('I5:J200').HorizontalAlignment=-4108
 $book.Worksheets.Item('06_BANG_CHUNG').Range('F5:F200').HorizontalAlignment=-4108
 $app.CalculateFullRebuild()
 $cover.Activate()
 $cover.Range('A1').Select()
 $book.Save()
 Write-Output 'Saved native Excel workbook with filters and final view settings.'
 foreach($spec in @(@('00_BAT_DAU','A1:S38','cover-final'),@('01_TONG_QUAN','A1:S26','overview-final'),@('02_SAN_PHAM','A63:C89','product-final'),@('05_VAN_DE_THAY_DOI','A1:J14','issues-final'))){
  $sheet=$book.Worksheets.Item($spec[0]);$sheet.PageSetup.PrintArea=$spec[1];$sheet.PageSetup.Orientation=2;$sheet.PageSetup.PaperSize=8;$sheet.PageSetup.Zoom=$false;$sheet.PageSetup.FitToPagesWide=1;$sheet.PageSetup.FitToPagesTall=1;$sheet.PageSetup.LeftMargin=12;$sheet.PageSetup.RightMargin=12;$sheet.PageSetup.TopMargin=12;$sheet.PageSetup.BottomMargin=12;$sheet.ExportAsFixedFormat(0,"$dir/$($spec[2])-native.pdf")
 }
 $book.Close($false)
 $test=$app.Workbooks.Open("$dir/Manage Project - Redesigned.xlsx",0,$true)
 Write-Output "Reopen OK. Worksheets=$($test.Worksheets.Count); task filter=$($test.Worksheets.Item('04_CONG_VIEC').ListObjects.Item(1).ShowAutoFilter); progress=$($test.Worksheets.Item('01_TONG_QUAN').Range('G7').Text); link label=$($test.Worksheets.Item('00_BAT_DAU').Range('B14').Text)"
 $test.Close($false)
}finally{$app.Quit();[System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)|Out-Null}
