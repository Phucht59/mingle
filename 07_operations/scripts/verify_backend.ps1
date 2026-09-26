param(
    [string]$Python = "python",
    [switch]$RunPostgres
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$evidenceRoot = Join-Path $repoRoot "06_quality\evidence"
$runId = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
New-Item -ItemType Directory -Path $evidenceRoot -Force | Out-Null

if ($RunPostgres -and [string]::IsNullOrWhiteSpace($env:TEST_DATABASE_URL)) {
    throw "Set TEST_DATABASE_URL to a disposable PostgreSQL database ending in _test."
}

function Invoke-LoggedCheck {
    param(
        [string]$Name,
        [string[]]$Arguments
    )

    $logPath = Join-Path $evidenceRoot "$Name-$runId.log"
    "Command: $Python $($Arguments -join ' ')" | Set-Content -LiteralPath $logPath
    Push-Location $repoRoot
    try {
        & $Python @Arguments *>&1 | Tee-Object -FilePath $logPath -Append
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

Invoke-LoggedCheck "backend-lint" @("-m", "ruff", "check", "05_code/backend")

$unitXml = Join-Path $evidenceRoot "backend-unit-$runId.xml"
Invoke-LoggedCheck "backend-unit" @(
    "-m", "pytest", "05_code/backend", "--junitxml=$unitXml"
)

if ($RunPostgres) {
    $postgresXml = Join-Path $evidenceRoot "postgres-$runId.xml"
    Invoke-LoggedCheck "postgres" @(
        "-m", "pytest", "05_code/backend", "--run-postgres", "-m", "postgres",
        "--junitxml=$postgresXml"
    )
}

Invoke-LoggedCheck "api-smoke" @("07_operations/scripts/smoke_api.py")
