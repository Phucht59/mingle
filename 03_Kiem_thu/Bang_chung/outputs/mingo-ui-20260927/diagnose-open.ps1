$app=New-Object -ComObject Excel.Application
$app.Visible=$false
$app.DisplayAlerts=$false
$app.AutomationSecurity=3
try {
 $m=[Type]::Missing
 $p='C:\Mingo\outputs\mingo-ui-20260927\Manage Project - Redesigned.xlsx'
 $book=$app.Workbooks.Open($p,0,$false,5,'','',$true,2,'',$false,$false,0,$false,$true,1)
 Write-Output "Repair open success: $($book.Name)"
 $book.SaveAs('C:\Mingo\outputs\mingo-ui-20260927\native-repaired.xlsx',51)
 $book.Close($false)
} finally { $app.Quit();[System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)|Out-Null }
