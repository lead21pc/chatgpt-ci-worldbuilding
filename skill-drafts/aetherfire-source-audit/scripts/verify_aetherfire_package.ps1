[CmdletBinding()]
param(
    [Parameter(Mandatory, Position = 0)]
    [string]$ProjectRoot,

    [string]$PythonExecutable = 'python'
)

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

$root = (Resolve-Path -LiteralPath $ProjectRoot).Path
$builder = Join-Path $root 'build_consolidation.py'
if (-not (Test-Path -LiteralPath $builder -PathType Leaf)) {
    throw 'Required package item missing: build_consolidation.py'
}

# Delegate current-package checks to its maintained, read-only validator.
& $PythonExecutable -B $builder --check
if ($LASTEXITCODE -ne 0) {
    throw "Project Feather Core package verification failed (exit code $LASTEXITCODE)."
}
