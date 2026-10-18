$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\tasklang"
$codex = "$env:USERPROFILE\.codex\plugins\.plugin-appserver\codex.exe"
$mcp = "$env:USERPROFILE\Downloads\agent-test\empty_mcp.json"
$enc = New-Object System.Text.UTF8Encoding($false)
$qs = [IO.File]::ReadAllText("$root\prompts.json", [Text.Encoding]::UTF8) | ConvertFrom-Json
foreach ($rep in 1, 2) {
  foreach ($k in $qs.PSObject.Properties.Name) {
    $d = "$root\claude_${k}_r$rep"
    if (-not (Test-Path "$d\run.json")) {
      New-Item -ItemType Directory -Force "$d\work" | Out-Null
      [IO.File]::WriteAllText("$d\prompt.txt", $qs.$k, $enc)
      Push-Location "$d\work"; $t0 = Get-Date
      cmd /c "type ..\prompt.txt | claude -p --effort medium --permission-mode acceptEdits --output-format json --mcp-config `"$mcp`" --strict-mcp-config > ..\run.json 2>&1"
      [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)"); Pop-Location
    }
    $d = "$root\codex_${k}_r$rep"
    if (-not (Test-Path "$d\run.jsonl")) {
      New-Item -ItemType Directory -Force "$d\work" | Out-Null
      [IO.File]::WriteAllText("$d\prompt.txt", $qs.$k, $enc)
      Push-Location "$d\work"; $t0 = Get-Date
      cmd /c "type ..\prompt.txt | `"$codex`" exec --json --skip-git-repo-check -s workspace-write -c model_reasoning_effort=`"medium`" - > ..\run.jsonl 2>&1"
      [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)"); Pop-Location
    }
    Write-Output "done $k r$rep"
  }
}
Write-Output "ALL DONE"
