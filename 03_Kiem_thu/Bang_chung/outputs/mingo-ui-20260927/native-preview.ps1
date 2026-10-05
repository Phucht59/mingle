$ErrorActionPreference='Stop'
$dir='C:/Mingo/outputs/mingo-ui-20260927'
$app=New-Object -ComObject Excel.Application
$app.Visible=$false
$app.DisplayAlerts=$false
$app.EnableEvents=$false
$app.AutomationSecurity=3
try {
 $original=$app.Workbooks.Open('C:/Mingo/Manage Project.xlsx',0,$true)
 $sheet=$original.Worksheets.Item('01_TONG_QUAN')
 $sheet.PageSetup.PrintArea='$A$1:$G$22'
 $sheet.PageSetup.Orientation=2
 $sheet.PageSetup.Zoom=$false
 $sheet.PageSetup.FitToPagesWide=1
 $sheet.PageSetup.FitToPagesTall=1
 if(-not(Test-Path "$dir/before-native.pdf")){ $sheet.ExportAsFixedFormat(0,"$dir/before-native.pdf") }
 $original.Close($false)
 Write-Output 'Original preview exported'
 $book=$app.Workbooks.Open("$dir/Manage Project - Redesigned.xlsx",0,$true)
 $app.CalculateFullRebuild()
 $specs=@(
 @('00_BAT_DAU','A1:S38','cover'),
 @('01_TONG_QUAN','A1:S26','overview'),
 @('01_TONG_QUAN','B28:R39','overview-actions'),
 @('02_SAN_PHAM','A1:D28','product1'),
 @('02_SAN_PHAM','A30:C60','product2'),
 @('02_SAN_PHAM','A63:C89','product3'),
 @('03_ROADMAP','A1:G22','roadmap'),
 @('03_ROADMAP','A25:G38','checklist'),
 @('04_CONG_VIEC','A1:N20','tasks'),
 @('05_VAN_DE_THAY_DOI','A1:J14','issues'),
 @('05_VAN_DE_THAY_DOI','A17:J34','changes'),
 @('06_BANG_CHUNG','A1:H19','evidence'),
 @('00_BAT_DAU','B40:R80','coverdetails'))
 foreach($spec in $specs){
   $sheet=$book.Worksheets.Item($spec[0])
   $sheet.PageSetup.PrintArea=$spec[1]
   $sheet.PageSetup.Orientation=2
   $sheet.PageSetup.PaperSize=8
   $sheet.PageSetup.Zoom=$false
   $sheet.PageSetup.FitToPagesWide=1
   $sheet.PageSetup.FitToPagesTall=1
   $sheet.PageSetup.LeftMargin=12
   $sheet.PageSetup.RightMargin=12
   $sheet.PageSetup.TopMargin=12
   $sheet.PageSetup.BottomMargin=12
   $sheet.ExportAsFixedFormat(0,"$dir/$($spec[2])-native.pdf")
   Write-Output "Rendered $($spec[2])"
 }
 Write-Output "Native results: progress=$($book.Worksheets.Item('01_TONG_QUAN').Range('G7').Value2); blockers=$($book.Worksheets.Item('01_TONG_QUAN').Range('L7').Value2); doing=$($book.Worksheets.Item('01_TONG_QUAN').Range('P7').Value2)"
 $book.Worksheets.Item('04_CONG_VIEC').Range('F5').Value2='XONG'
 $app.CalculateFullRebuild()
 Write-Output "Reaction test: progress=$($book.Worksheets.Item('01_TONG_QUAN').Range('G7').Value2); doing=$($book.Worksheets.Item('01_TONG_QUAN').Range('P7').Value2); checklist=$($book.Worksheets.Item('03_ROADMAP').Range('F27').Value2)"
 $book.Close($false)
} finally { $app.Quit(); [System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($app) | Out-Null }
