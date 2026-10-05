param(
    [string]$Python = "python",
    [switch]$RunPostgres
)

$ErrorActionPreference = "Stop"
$repoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..")).Path
$evidenceRoot = Join-Path $repoRoot "03_Kiem_thu\Bang_chung"
$backendEvidence = Join-Path $evidenceRoot "backend"
$postgresEvidence = Join-Path $evidenceRoot "postgres"
$workerEvidence = Join-Path $evidenceRoot "worker"
$runId = [DateTime]::UtcNow.ToString("yyyyMMddTHHmmssZ")
$commit = (git -C $repoRoot rev-parse HEAD).Trim()
New-Item -ItemType Directory -Path $backendEvidence -Force | Out-Null
New-Item -ItemType Directory -Path $postgresEvidence -Force | Out-Null
New-Item -ItemType Directory -Path $workerEvidence -Force | Out-Null

$envFile = Join-Path $repoRoot "01_San_pham\.env"
if (Test-Path -LiteralPath $envFile) {
    foreach ($line in Get-Content -LiteralPath $envFile) {
        if ($line -match '^([^#=]+)=(.*)$' -and [string]::IsNullOrWhiteSpace([Environment]::GetEnvironmentVariable($Matches[1]))) {
            [Environment]::SetEnvironmentVariable($Matches[1], $Matches[2], 'Process')
        }
    }
}

if ($RunPostgres -and [string]::IsNullOrWhiteSpace($env:TEST_DATABASE_URL)) {
    throw "Set TEST_DATABASE_URL to a disposable PostgreSQL database ending in _test."
}

function Invoke-LoggedCheck {
    param(
        [string]$Name,
        [string[]]$Arguments,
        [string]$Directory = $backendEvidence
    )

    $logPath = Join-Path $Directory "$Name-$runId.log"
    "Commit: $commit`nCommand: $Python $($Arguments -join ' ')" | Set-Content -LiteralPath $logPath
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

Invoke-LoggedCheck "backend-lint" @("-m", "ruff", "check", "01_San_pham/backend")

$unitXml = Join-Path $backendEvidence "backend-unit-$runId.xml"
Invoke-LoggedCheck "backend-unit" @(
    "-m", "pytest", "01_San_pham/backend", "--junitxml=$unitXml"
)

if ($RunPostgres) {
    $postgresXml = Join-Path $postgresEvidence "postgres-$runId.xml"
    Invoke-LoggedCheck "postgres" @(
        "-m", "pytest", "01_San_pham/backend", "--run-postgres", "-m", "postgres",
        "--junitxml=$postgresXml"
    ) $postgresEvidence
    Invoke-LoggedCheck "postgres-migrate" @(
        "-m", "all_foundation.cli", "migrate"
    ) $postgresEvidence
    Invoke-LoggedCheck "worker-enqueue" @(
        "-m", "all_foundation.cli", "enqueue-probe", "--key", "verify-$runId"
    ) $workerEvidence
    Invoke-LoggedCheck "worker-once" @(
        "-m", "all_foundation.worker", "--once"
    ) $workerEvidence
    Invoke-LoggedCheck "worker-healthcheck" @(
        "-m", "all_foundation.worker", "--healthcheck"
    ) $workerEvidence
}

if ($RunPostgres) {
    Invoke-LoggedCheck "api-ready-smoke" @("04_Van_hanh/Scripts/smoke_api.py", "--expect-ready")
}
else {
    Invoke-LoggedCheck "api-degraded-smoke" @("04_Van_hanh/Scripts/smoke_api.py")
}

# Storage does not connect to PostgreSQL, but Settings requires a URI.
if ([string]::IsNullOrWhiteSpace($env:DATABASE_URL)) {
    $env:DATABASE_URL = "postgresql://unused:unused@127.0.0.1:1/mingo"
}
Invoke-LoggedCheck "storage-smoke" @("-m", "all_foundation.cli", "storage-smoke")
