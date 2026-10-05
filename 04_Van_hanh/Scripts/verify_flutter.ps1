param([string]$Flutter = "flutter")

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$javaTemp = Join-Path $repoRoot ".local\java-tmp"
New-Item -ItemType Directory -Force -Path $javaTemp | Out-Null
$env:TEMP = $javaTemp
$env:TMP = $javaTemp
$env:JAVA_TOOL_OPTIONS = "-Djava.io.tmpdir=$javaTemp"
$evidenceRoot = Join-Path $repoRoot "03_Kiem_thu\Bang_chung\flutter"
$learnerEvidence = Join-Path $evidenceRoot "learner"
$staffEvidence = Join-Path $evidenceRoot "staff"
$runId = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
$commit = (git -C $repoRoot rev-parse HEAD).Trim()
New-Item -ItemType Directory -Force -Path $learnerEvidence, $staffEvidence | Out-Null

function Invoke-FlutterCheck {
    param(
        [string]$Name,
        [string]$WorkingDirectory,
        [string[]]$Arguments,
        [string]$EvidenceDirectory
    )

    $logPath = Join-Path $EvidenceDirectory "$Name-$runId.log"
    "Commit: $commit`nCommand: flutter $($Arguments -join ' ')" | Set-Content -LiteralPath $logPath
    Push-Location $WorkingDirectory
    try {
        & $Flutter @Arguments *>&1 | Tee-Object -FilePath $logPath -Append
        $exitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }
    "Exit code: $exitCode" | Add-Content -LiteralPath $logPath
    if ($exitCode -ne 0) {
        throw "$Name failed with exit code $exitCode. See $logPath"
    }
}

Invoke-FlutterCheck "flutter-version" $repoRoot @("--version") $evidenceRoot
Invoke-FlutterCheck "flutter-doctor" $repoRoot @("doctor", "-v") $evidenceRoot

$learner = Join-Path $repoRoot "01_San_pham\apps\learner"
Invoke-FlutterCheck "pub-get" $learner @("pub", "get") $learnerEvidence
Invoke-FlutterCheck "analyze" $learner @("analyze") $learnerEvidence
Invoke-FlutterCheck "test" $learner @("test") $learnerEvidence
Invoke-FlutterCheck "build-apk-debug" $learner @("build", "apk", "--debug") $learnerEvidence

$staff = Join-Path $repoRoot "01_San_pham\apps\staff"
Invoke-FlutterCheck "pub-get" $staff @("pub", "get") $staffEvidence
Invoke-FlutterCheck "analyze" $staff @("analyze") $staffEvidence
Invoke-FlutterCheck "test" $staff @("test") $staffEvidence
Invoke-FlutterCheck "build-web" $staff @("build", "web") $staffEvidence
