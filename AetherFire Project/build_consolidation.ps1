# Compatibility entry point for current package maintenance (Python 3).
$ErrorActionPreference = 'Stop'
$pythonCommand = Get-Command python -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
if (-not $pythonCommand) {
    $pythonCommand = Get-Command python3 -CommandType Application -ErrorAction SilentlyContinue | Select-Object -First 1
}
if (-not $pythonCommand) {
    throw 'Python 3 is required. Run: python build_consolidation.py --check'
}
& $pythonCommand.Source (Join-Path $PSScriptRoot 'build_consolidation.py') @args
exit $LASTEXITCODE
