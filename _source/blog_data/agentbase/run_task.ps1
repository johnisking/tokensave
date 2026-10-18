$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test"
$codex = "$env:USERPROFILE\.codex\plugins\.plugin-appserver\codex.exe"
$prompt = "Make a brick-breaker game that runs in the browser as a single file named index.html in the current folder. It needs 2 levels, a score display and 3 lives, and it must be playable with the keyboard and the mouse. Write the file and finish."
foreach ($rep in 1, 2) {
  # ---- Claude Code (medium effort) ----
  $d = "$root\task_claude_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
  '{"mcpServers":{}}' | Out-File -Encoding ascii "$root\empty_mcp.json"
  $t0 = Get-Date
  cmd /c "claude -p `"$prompt`" --effort medium --permission-mode acceptEdits --output-format json --mcp-config `"$root\empty_mcp.json`" --strict-mcp-config < NUL > ..\task_claude_r$rep.json 2>&1"
  $s = [int]((Get-Date) - $t0).TotalSeconds
  Pop-Location
  Write-Output "claude r$rep seconds=$s"
  # ---- Codex (medium effort) ----
  $d = "$root\task_codex_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
  $t0 = Get-Date
  cmd /c "`"$codex`" exec --json --skip-git-repo-check -s workspace-write -c model_reasoning_effort=`"medium`" `"$prompt`" < NUL > ..\task_codex_r$rep.jsonl 2>&1"
  $s = [int]((Get-Date) - $t0).TotalSeconds
  Pop-Location
  Write-Output "codex r$rep seconds=$s"
}
Write-Output "ALL DONE"
