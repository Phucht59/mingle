param([string]$Flutter = "flutter")

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
Push-Location $repoRoot
try {
    & $Flutter create --no-pub --platforms=android,web --project-name adaptive_learner 01_San_pham/apps/learner
    if ($LASTEXITCODE -ne 0) { throw "Learner platform bootstrap failed" }
    & $Flutter create --no-pub --platforms=web --project-name adaptive_staff 01_San_pham/apps/staff
    if ($LASTEXITCODE -ne 0) { throw "Staff platform bootstrap failed" }
}
finally {
    Pop-Location
}
