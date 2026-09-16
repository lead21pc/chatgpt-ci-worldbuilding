[CmdletBinding()]
param(
    [Parameter(Mandatory, Position = 0)]
    [string]$ProjectRoot,

    [string[]]$ExpectedExcludedSource = @(
        'aetherfire_chat_anti_drift.md',
        'modular_engine_concept_anti_drift_revised.md'
    )
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function Get-ManifestRows {
    param([Parameter(Mandatory)][string]$Text)

    $rows = @()
    foreach ($match in [regex]::Matches($Text, '(?m)^\| `([^`]+)` \| `([A-Fa-f0-9]{64})` \|$')) {
        $rows += [pscustomobject]@{
            Name = $match.Groups[1].Value
            Hash = $match.Groups[2].Value.ToUpperInvariant()
        }
    }
    return $rows
}

function Get-Section {
    param(
        [Parameter(Mandatory)][string]$Text,
        [Parameter(Mandatory)][string]$Start,
        [Parameter(Mandatory)][string]$End
    )

    $startIndex = $Text.IndexOf($Start, [StringComparison]::Ordinal)
    $endIndex = $Text.IndexOf($End, $startIndex + $Start.Length, [StringComparison]::Ordinal)
    if ($startIndex -lt 0 -or $endIndex -lt 0) {
        throw "Manifest section missing: $Start"
    }
    return $Text.Substring($startIndex, $endIndex - $startIndex)
}

$root = (Resolve-Path -LiteralPath $ProjectRoot).Path
$required = @(
    '00_AETHERFIRE_CONSOLIDATION_INDEX.md',
    '91_RECONCILIATION_RECORD.md',
    'MANIFEST.md',
    'build_consolidation.ps1',
    'Source_Archive'
)
foreach ($name in $required) {
    if (-not (Test-Path -LiteralPath (Join-Path $root $name))) {
        throw "Required package item missing: $name"
    }
}

$manifestPath = Join-Path $root 'MANIFEST.md'
$manifestText = [IO.File]::ReadAllText($manifestPath)
$generatedRows = Get-ManifestRows (Get-Section $manifestText '## Generated outputs' '## Archived source snapshot')
$archiveRows = Get-ManifestRows (Get-Section $manifestText '## Archived source snapshot' '## Build')
if ($generatedRows.Count -eq 0 -or $archiveRows.Count -eq 0) {
    throw 'Manifest contains no generated or archived rows.'
}

$issues = [Collections.Generic.List[string]]::new()
foreach ($row in $generatedRows) {
    $path = Join-Path $root $row.Name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        $issues.Add("Missing generated output: $($row.Name)")
        continue
    }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
    if ($actual -ne $row.Hash) {
        $issues.Add("Generated hash mismatch: $($row.Name)")
    }
}

$archiveRoot = Join-Path $root 'Source_Archive'
foreach ($row in $archiveRows) {
    $path = Join-Path $archiveRoot $row.Name
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        $issues.Add("Missing archived source: $($row.Name)")
        continue
    }
    $actual = (Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash
    if ($actual -ne $row.Hash) {
        $issues.Add("Archived hash mismatch: $($row.Name)")
    }
}

$listedArchive = @($archiveRows.Name | Sort-Object)
$actualArchive = @(Get-ChildItem -LiteralPath $archiveRoot -File -Filter '*.md' | ForEach-Object Name | Sort-Object)
$inventoryDiff = @(Compare-Object -ReferenceObject $listedArchive -DifferenceObject $actualArchive)
foreach ($difference in $inventoryDiff) {
    $issues.Add("Archive inventory mismatch: $($difference.InputObject) [$($difference.SideIndicator)]")
}

$buildText = [IO.File]::ReadAllText((Join-Path $root 'build_consolidation.ps1'))
foreach ($name in $ExpectedExcludedSource) {
    $escaped = [regex]::Escape($name)
    if ($buildText -match "(?m)^\s*\$\w+\s*=\s*Read-MarkdownSource\s+'$escaped'\s*$") {
        $issues.Add("Expected excluded source is read by build: $name")
    }
}

$tempBase = [IO.Path]::GetTempPath()
$tempRoot = Join-Path $tempBase ('aetherfire-package-verify-' + [Guid]::NewGuid().ToString('N'))
New-Item -ItemType Directory -Path $tempRoot | Out-Null
try {
    foreach ($child in Get-ChildItem -LiteralPath $root -Force) {
        Copy-Item -LiteralPath $child.FullName -Destination $tempRoot -Recurse -Force
    }

    $buildLog = & (Join-Path $tempRoot 'build_consolidation.ps1') | Out-String
    foreach ($row in $generatedRows) {
        $livePath = Join-Path $root $row.Name
        $rebuiltPath = Join-Path $tempRoot $row.Name
        if (-not (Test-Path -LiteralPath $rebuiltPath -PathType Leaf)) {
            $issues.Add("Rebuild did not create: $($row.Name)")
            continue
        }
        if ((Get-FileHash -LiteralPath $livePath -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath $rebuiltPath -Algorithm SHA256).Hash) {
            $issues.Add("Rebuild differs from live output: $($row.Name)")
        }
    }

    if ((Get-FileHash -LiteralPath $manifestPath -Algorithm SHA256).Hash -ne (Get-FileHash -LiteralPath (Join-Path $tempRoot 'MANIFEST.md') -Algorithm SHA256).Hash) {
        $issues.Add('Rebuilt MANIFEST.md differs from live manifest.')
    }
}
finally {
    if ($tempRoot.StartsWith($tempBase, [StringComparison]::OrdinalIgnoreCase) -and (Test-Path -LiteralPath $tempRoot)) {
        Remove-Item -LiteralPath $tempRoot -Recurse -Force
    }
}

$result = [pscustomobject]@{
    Status = if ($issues.Count -eq 0) { 'PASS' } else { 'FAIL' }
    ProjectRoot = $root
    GeneratedFiles = $generatedRows.Count
    ArchivedSources = $archiveRows.Count
    ExcludedSourcesChecked = $ExpectedExcludedSource.Count
    BuildOutput = $buildLog.Trim()
    Issues = @($issues)
}
$result | ConvertTo-Json -Depth 4

if ($issues.Count -gt 0) {
    throw "AetherFire package verification failed with $($issues.Count) issue(s)."
}
