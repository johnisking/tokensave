$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\vibe"
$mcp = "$env:USERPROFILE\Downloads\agent-test\empty_mcp.json"
$base = "-p --effort medium --output-format stream-json --verbose --mcp-config `"$mcp`" --strict-mcp-config --permission-mode acceptEdits"
$models = "claude-haiku-5-5", "claude-sonnet-5-5", "claude-opus-5-5"
$tasks = $args
if (-not $tasks) { $tasks = "brick", "2048" }
function Done($p) { (Test-Path $p) -and ((Get-Content $p -Raw -Encoding UTF8) -match '"type":"result"') }
foreach ($rep in 1, 2, 3, 4, 5) {
  foreach ($t in $tasks) {
    foreach ($m in $models) {
      $short = $m -replace 'claude-', ''
      $d = "$root\runs\${t}_${short}_r$rep"
      if (-not (Done "$d\run.jsonl")) {
        New-Item -ItemType Directory -Force "$d\work" | Out-Null
        Push-Location "$d\work"; $t0 = Get-Date
        cmd /c "type `"$root\prompt_$t.txt`" | claude $base --model $m > ..\run.jsonl 2>&1"
        [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)"); Pop-Location
      }
      Write-Output "done $t $short r$rep $(Get-Date -Format HH:mm)"
    }
  }
}
Write-Output "ALL DONE"
