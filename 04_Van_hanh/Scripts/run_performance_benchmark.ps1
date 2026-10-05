[CmdletBinding()]
param(
    [string]$Flutter = 'C:\Dev\flutter-3.32.8\bin\flutter.bat',
    [string]$Adb = 'C:\Android\Sdk\platform-tools\adb.exe',
    [string]$Device = '',
    [ValidateSet('Profile', 'Release')][string]$BuildMode = 'Profile',
    [ValidateSet('UNASSIGNED', 'LOW', 'MID', 'HIGH')][string]$DeviceTier = 'UNASSIGNED',
    [ValidateRange(3, 20)][int]$LaunchRepeats = 5,
    [switch]$BuildAab,
    [string]$EvidenceRoot = '',
    [string]$AppPackage = 'com.example.adaptive_learner'
)

$ErrorActionPreference = 'Stop'
$repoRoot = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\..'))
$learner = Join-Path $repoRoot '01_San_pham\apps\learner'
if (-not $EvidenceRoot) {
    $EvidenceRoot = Join-Path $repoRoot '03_Kiem_thu\QA_QC\phase2\evidence_gated_20261002\performance'
}
$resolvedEvidence = [IO.Path]::GetFullPath($EvidenceRoot)
if (-not $resolvedEvidence.StartsWith($repoRoot + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase)) {
    throw 'Evidence must stay within the Mingo workspace.'
}
$runId = [DateTime]::UtcNow.ToString('yyyyMMddTHHmmssZ') + '-' + [Guid]::NewGuid().ToString('N').Substring(0, 8)
$runRoot = Join-Path $resolvedEvidence $runId
New-Item -ItemType Directory -Path $runRoot | Out-Null
$commands = New-Object System.Collections.Generic.List[object]
$report = [ordered]@{
    schema = 'mingo.performance.host.v1'
    run_id = $runId
    capture_utc = [DateTime]::UtcNow.ToString('o')
    timezone_display = 'Asia/Saigon'
    build_mode = $BuildMode.ToLower()
    status = 'IN_PROGRESS'
    physical_device_performance = 'PENDING'
    device_tier = $DeviceTier
    tier_assignment = 'QA supplied; hardware evidence required, not inferred from emulator'
    scenarios = [ordered]@{}
    commands = $commands
    limits = @(
        'Emulator numbers cannot certify physical-device performance.',
        'FrameTiming violations are jank proxies, not exact compositor dropped frames.',
        'am start -W is Android activity-start reporting, not time to meaningful learning.',
        'Force-stop is process cold; filesystem cache/app data are not cleared.',
        'Warm launch is accepted only when the process PID is unchanged.',
        'Offline rendering is a fixture; durable offline runtime belongs to Phase6.',
        'dumpsys battery/thermal are snapshots, not battery-energy benchmarks.'
    )
}
$savedEnvironment = @{}
foreach ($name in @('TEMP', 'TMP', 'JAVA_TOOL_OPTIONS', 'MINGO_PERFORMANCE_OUT')) {
    $savedEnvironment[$name] = [Environment]::GetEnvironmentVariable($name, 'Process')
}

function Invoke-Observed {
    param([string]$Name, [string]$Tool, [string[]]$Arguments, [switch]$AllowFailure)
    $log = Join-Path $runRoot ($Name + '.log')
    if (Test-Path -LiteralPath $log) { throw 'Refusing to overwrite an observed-command log.' }
    Get-Command -Name $Tool -ErrorAction Stop | Out-Null
    Write-Host ('Running: ' + $Name)
    $start = [DateTime]::UtcNow
    $watch = [Diagnostics.Stopwatch]::StartNew()
    $previousPreference = $ErrorActionPreference
    try {
        # Native stderr includes informational Flutter/Java warnings on PS5.
        # Exit code, not a stderr stream label, determines command failure.
        $ErrorActionPreference = 'Continue'
        $captured = & $Tool @Arguments 2>&1 | ForEach-Object { $_.ToString() } | Tee-Object -FilePath $log
        $exitCode = $LASTEXITCODE
    }
    finally { $ErrorActionPreference = $previousPreference; $watch.Stop() }
    if (-not (Test-Path -LiteralPath $log)) { '' | Set-Content -LiteralPath $log -Encoding UTF8 }
    $commands.Add([ordered]@{
        name = $Name; tool = $Tool; arguments = $Arguments; started_utc = $start.ToString('o')
        elapsed_ms = $watch.Elapsed.TotalMilliseconds; exit_code = $exitCode
        log = [IO.Path]::GetFileName($log); sha256 = (Get-FileHash -LiteralPath $log -Algorithm SHA256).Hash.ToLower()
    })
    if ($exitCode -ne 0 -and -not $AllowFailure) { throw ($Name + ' failed; inspect the preserved command log.') }
    return ($captured -join [Environment]::NewLine)
}

function Invoke-Adb {
    param([string]$Name, [string[]]$Arguments, [switch]$AllowFailure)
    return Invoke-Observed -Name $Name -Tool $Adb -Arguments (@('-s', $Device) + $Arguments) -AllowFailure:$AllowFailure
}

function Parse-Launch {
    param([string]$Text)
    $result = [ordered]@{ raw_report = $Text }
    foreach ($field in @('ThisTime', 'TotalTime', 'WaitTime')) {
        $match = [Regex]::Match($Text, '(?m)^' + $field + ':\s*(\d+)')
        $result[$field.ToLower() + '_ms'] = if ($match.Success) { [int]$match.Groups[1].Value } else { $null }
    }
    $result['status'] = if ($Text -match '(?m)^Status:\s*ok') { 'REPORTED_OK' } else { 'UNRESOLVED' }
    return $result
}

function Sample-Stats {
    param([object[]]$Samples, [string]$Field)
    $values = @($Samples | ForEach-Object { if ($null -ne $_[$Field]) { [double]$_[$Field] } } | Sort-Object)
    if ($values.Count -eq 0) { return @{ count = 0; median_ms = $null; p95_ms = $null } }
    return @{ count = $values.Count; median_ms = $values[[Math]::Ceiling($values.Count * .5) - 1]; p95_ms = $values[[Math]::Ceiling($values.Count * .95) - 1] }
}

try {
    $javaTemp = Join-Path $repoRoot '.local\java-tmp'
    New-Item -ItemType Directory -Path $javaTemp -Force | Out-Null
    $env:TEMP = $javaTemp; $env:TMP = $javaTemp
    $env:JAVA_TOOL_OPTIONS = '-Djava.io.tmpdir=' + $javaTemp.Replace('\', '/')
    $env:MINGO_PERFORMANCE_OUT = $runRoot
    $deviceList = Invoke-Observed -Name 'adb-devices' -Tool $Adb -Arguments @('devices', '-l')
    $online = @([Regex]::Matches($deviceList, '(?m)^([^\s]+)\s+device(?:\s|$)') | ForEach-Object { $_.Groups[1].Value })
    if (-not $Device -and $online.Count -eq 1) { $Device = $online[0] }
    if (-not $Device -or $online -notcontains $Device) {
        $report.status = 'BLOCKED_BY_ENVIRONMENT'
        $report.blocker = 'No unambiguously selected online Android device. Connect a device or supply -Device.'
        $report.scenarios.frame_timings = 'NOT_RUN'
        throw $report.blocker
    }
    $qemu = (Invoke-Adb 'device-qemu' @('shell', 'getprop', 'ro.kernel.qemu')).Trim()
    $isEmulator = $qemu -eq '1' -or $Device.StartsWith('emulator-')
    $report['is_emulator'] = $isEmulator
    $report['device_alias'] = if ($isEmulator) { $Device } else { 'physical-device-' + $runId }
    $report['manufacturer'] = (Invoke-Adb 'device-manufacturer' @('shell', 'getprop', 'ro.product.manufacturer')).Trim()
    $report['model'] = (Invoke-Adb 'device-model' @('shell', 'getprop', 'ro.product.model')).Trim()
    $report['android_sdk'] = (Invoke-Adb 'device-sdk' @('shell', 'getprop', 'ro.build.version.sdk')).Trim()
    $report['abi'] = (Invoke-Adb 'device-abi' @('shell', 'getprop', 'ro.product.cpu.abi')).Trim()
    $report['display_raw'] = Invoke-Adb 'display-before' @('shell', 'dumpsys', 'display')
    $gles = Invoke-Adb 'renderer-context' @('shell', 'dumpsys', 'SurfaceFlinger') -AllowFailure
    $report['renderer_context'] = (@($gles -split "`n" | Where-Object { $_ -match 'GLES:' }) -join '').Trim()
    $report['engine_override'] = 'NONE; Android engine default'
    $report['memory_hardware_raw'] = Invoke-Adb 'hardware-memory' @('shell', 'cat', '/proc/meminfo')
    Invoke-Adb 'battery-before' @('shell', 'dumpsys', 'battery') -AllowFailure | Out-Null
    Invoke-Adb 'thermal-before' @('shell', 'dumpsys', 'thermalservice') -AllowFailure | Out-Null
    $report['flutter_version'] = Invoke-Observed -Name 'flutter-version' -Tool $Flutter -Arguments @('--version')
    $report['source_sha256'] = @(
        Get-ChildItem -LiteralPath (Join-Path $repoRoot '01_San_pham\cong_cu_phat_trien\mingo_ui\lib') -Recurse -File
        Get-ChildItem -LiteralPath (Join-Path $learner 'lib') -Recurse -File
    ) | ForEach-Object { @{ path = $_.FullName.Substring($repoRoot.Length + 1).Replace('\', '/'); sha256 = (Get-FileHash -LiteralPath $_.FullName -Algorithm SHA256).Hash.ToLower() } }
    $report['instrumentation_sha256'] = @(
        (Join-Path $learner 'integration_test\performance_test.dart'),
        (Join-Path $learner 'test_driver\performance_driver.dart'),
        $PSCommandPath
    ) | ForEach-Object { @{ path = $_.Substring($repoRoot.Length + 1).Replace('\', '/'); sha256 = (Get-FileHash -LiteralPath $_ -Algorithm SHA256).Hash.ToLower() } }
    Push-Location $learner
    try {
        if ($BuildMode -eq 'Profile') {
            Invoke-Observed -Name 'profile-frame-journey' -Tool $Flutter -Arguments @(
                'drive', '--profile', '--no-pub', '--no-dds', '-d', $Device,
                '--driver=test_driver/performance_driver.dart', '--target=integration_test/performance_test.dart'
            ) | Out-Null
            if (-not (Test-Path -LiteralPath (Join-Path $runRoot 'frame_timings.json'))) { throw 'Profile command produced no FrameTiming artifact.' }
            $report.scenarios.frame_timings = 'MEASURED_PROFILE_ENGINEERING'
            $benchmarkApk = Join-Path $learner 'build\app\outputs\flutter-apk\app-profile.apk'
            $report['benchmark_apk'] = @{ bytes = (Get-Item -LiteralPath $benchmarkApk).Length; sha256 = (Get-FileHash -LiteralPath $benchmarkApk -Algorithm SHA256).Hash.ToLower(); entrypoint = 'integration_test/performance_test.dart'; deliverable_app = $false }
        } else {
            $report.scenarios.frame_timings = 'NOT_RUN_RELEASE_HAS_NO_VM_SERVICE'
        }
        # Restore the normal app entrypoint before host launch/memory sampling.
        # The integration APK must never be labelled a normal deliverable build.
        # Pub/build verification refreshes the generated native registrant for
        # release (dev-only integration plugin must not survive a profile run).
        Invoke-Observed -Name 'normal-app-build' -Tool $Flutter -Arguments @('build', 'apk', ('--' + $BuildMode.ToLower()), '--target=lib/main.dart') | Out-Null
        $apk = Join-Path $learner ('build\app\outputs\flutter-apk\app-' + $BuildMode.ToLower() + '.apk')
        $apkItem = Get-Item -LiteralPath $apk
        $report['apk'] = @{ bytes = $apkItem.Length; sha256 = (Get-FileHash -LiteralPath $apk -Algorithm SHA256).Hash.ToLower(); mode = $BuildMode.ToLower(); entrypoint = 'lib/main.dart'; release_signing = 'Generated local debug signing; not production release' }
        if ($BuildAab) {
            Invoke-Observed -Name 'release-aab-build' -Tool $Flutter -Arguments @('build', 'appbundle', '--release', '--target=lib/main.dart') | Out-Null
            $aab = Join-Path $learner 'build\app\outputs\bundle\release\app-release.aab'
            $report['aab'] = @{ bytes = (Get-Item -LiteralPath $aab).Length; sha256 = (Get-FileHash -LiteralPath $aab -Algorithm SHA256).Hash.ToLower(); note = 'Bundle size is not Play delivery size; local generated signing only' }
        }
    } finally { Pop-Location }
    Invoke-Adb 'normal-app-install' @('install', '-r', $apk) | Out-Null
    $component = (Invoke-Adb 'resolve-activity' @('shell', 'cmd', 'package', 'resolve-activity', '--brief', $AppPackage)).Trim().Split([Environment]::NewLine) | Select-Object -Last 1
    if ($component -notmatch '^[\w.]+/[\w.]+$') { throw 'Cannot resolve the installed launcher activity.' }
    $cold = New-Object System.Collections.Generic.List[object]
    $report.scenarios['cold_launch'] = @{ samples = $cold; status = 'PARTIAL_UNTIL_COMPLETE' }
    for ($i = 1; $i -le $LaunchRepeats; $i++) {
        Invoke-Adb ('cold-force-stop-' + $i) @('shell', 'am', 'force-stop', $AppPackage) | Out-Null
        $sample = Parse-Launch (Invoke-Adb ('cold-launch-' + $i) @('shell', 'am', 'start', '-W', '-n', $component))
        $sample['classification'] = 'PROCESS_COLD_NO_DATA_OR_FILESYSTEM_CACHE_CLEAR'
        $cold.Add($sample)
        Start-Sleep -Milliseconds 1200
        $sample['process_after_launch'] = (Invoke-Adb ('cold-pid-after-' + $i) @('shell', 'pidof', $AppPackage) -AllowFailure).Trim()
        if (-not $sample['process_after_launch'] -or $null -eq $sample['totaltime_ms']) {
            Invoke-Adb ('cold-runtime-diagnostic-' + $i) @('logcat', '-d', '-s', 'flutter', 'AndroidRuntime') -AllowFailure | Out-Null
            throw 'Cold start did not retain a running app with a reported activity duration.'
        }
    }
    $warm = New-Object System.Collections.Generic.List[object]
    $report.scenarios['warm_launch_and_background_return'] = @{ samples = $warm; status = 'PARTIAL_UNTIL_COMPLETE' }
    for ($i = 1; $i -le $LaunchRepeats; $i++) {
        $beforePid = (Invoke-Adb ('warm-pid-before-' + $i) @('shell', 'pidof', $AppPackage)).Trim()
        Invoke-Adb ('warm-background-' + $i) @('shell', 'input', 'keyevent', 'KEYCODE_HOME') | Out-Null
        Start-Sleep -Milliseconds 1200
        $sample = Parse-Launch (Invoke-Adb ('warm-launch-' + $i) @('shell', 'am', 'start', '-W', '-n', $component))
        $afterPid = (Invoke-Adb ('warm-pid-after-' + $i) @('shell', 'pidof', $AppPackage)).Trim()
        $sample['same_process'] = $beforePid -ne '' -and $beforePid -eq $afterPid
        $sample['classification'] = if ($sample['same_process']) { 'WARM_BACKGROUND_RETURN' } else { 'PROCESS_CHANGED_NOT_VALID_WARM_SAMPLE' }
        $warm.Add($sample)
    }
    $report.scenarios['cold_launch'] = @{ samples = $cold; this_time = Sample-Stats $cold 'thistime_ms'; total_time = Sample-Stats $cold 'totaltime_ms'; metric = 'Android am start -W reported activity time, not meaningful-learning latency' }
    $report.scenarios['warm_launch_and_background_return'] = @{ samples = $warm; wait_time = Sample-Stats @($warm | Where-Object { $_['same_process'] }) 'waittime_ms'; note = 'WaitTime is command completion, not an equivalent to cold ThisTime/TotalTime' }
    $memory = Invoke-Adb 'normal-app-memory' @('shell', 'dumpsys', 'meminfo', $AppPackage)
    $match = [Regex]::Match($memory, '(?m)^\s*TOTAL PSS:\s*(\d+)')
    $report['total_pss_kib_after_launch'] = if ($match.Success) { [int]$match.Groups[1].Value } else { $null }
    Invoke-Adb 'battery-after' @('shell', 'dumpsys', 'battery') -AllowFailure | Out-Null
    Invoke-Adb 'thermal-after' @('shell', 'dumpsys', 'thermalservice') -AllowFailure | Out-Null
    Invoke-Adb 'display-after' @('shell', 'dumpsys', 'display') -AllowFailure | Out-Null
    $report.status = 'ENGINEERING_MEASUREMENT_COMPLETE'
    $report.physical_device_performance = if ($isEmulator) { 'PENDING_EMULATOR_NOT_CERTIFICATION' } else { 'MEASURED_CANDIDATE_REQUIRES_INDEPENDENT_REVIEW' }
} catch {
    if ($report.status -eq 'IN_PROGRESS') { $report.status = 'FAILED_OR_BLOCKED'; $report['failure'] = $_.Exception.Message }
    Write-Warning $_.Exception.Message
} finally {
    foreach ($name in $savedEnvironment.Keys) { [Environment]::SetEnvironmentVariable($name, $savedEnvironment[$name], 'Process') }
    $report | ConvertTo-Json -Depth 30 | Set-Content -LiteralPath (Join-Path $runRoot 'host_report.json') -Encoding UTF8
    Write-Output ('Evidence: ' + $runRoot)
    Write-Output ('Status: ' + $report.status)
}
if ($report.status -ne 'ENGINEERING_MEASUREMENT_COMPLETE') { exit 2 }
