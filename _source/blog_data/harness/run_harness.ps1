$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\harness"
$mcp = "$env:USERPROFILE\Downloads\agent-test\empty_mcp.json"
$base = "-p --effort medium --output-format stream-json --verbose --mcp-config `"$mcp`" --strict-mcp-config"
$conds = @{
  "default"  = "--permission-mode acceptEdits";
  "safemode" = "--permission-mode acceptEdits --safe-mode";
  "minimal"  = "--permission-mode acceptEdits --system-prompt `"You are a coding agent. Use your tools to complete the user's task.`" --tools Write,Read";
  "subagent" = "--permission-mode acceptEdits";
  "skill"    = "--permission-mode acceptEdits";
  "hook"     = "--permission-mode acceptEdits --settings `"$root\settings_hook.json`"";
  "plan"     = "--permission-mode plan"
}
$order = "default", "safemode", "minimal", "subagent", "plan", "skill", "hook"
function Done($p) { (Test-Path $p) -and ((Get-Content $p -Raw -Encoding UTF8) -match '"type":"result"') }
foreach ($rep in 1, 2, 3, 4, 5) {
  foreach ($c in $order) {
    $d = "$root\runs\${c}_r$rep"
    $last = if ($c -eq "plan") { "$d\run2.jsonl" } else { "$d\run.jsonl" }
    if (-not (Done $last)) {
      New-Item -ItemType Directory -Force "$d\work" | Out-Null
      if ($c -eq "skill") { New-Item -ItemType Directory -Force "$d\work\.claude\skills" | Out-Null; Copy-Item -Recurse -Force "$root\skill\html-canvas-games" "$d\work\.claude\skills\" }
      $pf = if ($c -eq "subagent") { "$root\prompt_sub.txt" } else { "$root\prompt.txt" }
      Push-Location "$d\work"; $t0 = Get-Date
      cmd /c "type `"$pf`" | claude $base $($conds[$c]) > ..\run.jsonl 2>&1"
      if ($c -eq "plan") {
        cmd /c "type `"$root\prompt_go.txt`" | claude -c $base --permission-mode acceptEdits > ..\run2.jsonl 2>&1"
      }
      [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)"); Pop-Location
    }
    Write-Output "done $c r$rep $(Get-Date -Format HH:mm)"
  }
}
Write-Output "ALL DONE"
