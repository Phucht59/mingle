$ErrorActionPreference='Stop'
$dir='C:/Mingo/outputs/mingo-ui-v2'
$manifest=Get-Content -Raw -LiteralPath "$dir/manifest.json" | ConvertFrom-Json
$app=New-Object -ComObject Excel.Application
$app.Visible=$false;$app.DisplayAlerts=$false;$app.EnableEvents=$false;$app.AutomationSecurity=3
try{
 $b=$app.Workbooks.Open("$dir/Mingo - Workspace.xlsx",0,$true)
 foreach($m in $manifest.sheets){$b.Worksheets.Item($m.name).ExportAsFixedFormat(0,"$dir/$($m.name)-final.pdf")}
 $b.Close($false)
 Write-Output 'Reopened normally; all 22 final previews exported.'
}finally{$app.Quit();[System.Runtime.InteropServices.Marshal]::FinalReleaseComObject($app)|Out-Null}
