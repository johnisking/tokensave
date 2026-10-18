$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test"
$server = "$root\mcp_dummy.js"
$codex = "$env:USERPROFILE\.codex\plugins\.plugin-appserver\codex.exe"
$cursor = "$env:LOCALAPPDATA\cursor-agent\cursor-agent.cmd"
$prompt = "Reply with the single word OK."
$counts = @(0, 1, 10, 30)
$results = @()
foreach ($rep in 1, 2) {
  foreach ($n in $counts) {
    # ---- Claude Code ----
    $d = "$root\claude_n${n}_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
    if ($n -eq 0) { '{"mcpServers":{}}' | Out-File -Encoding ascii mcp.json }
    else { ('{"mcpServers":{"tracker":{"command":"node","args":["' + ($server -replace '\\','\\') + '","' + $n + '"]}}}') | Out-File -Encoding ascii mcp.json }
    cmd /c "claude -p `"$prompt`" --output-format json --mcp-config mcp.json --strict-mcp-config < NUL > run.json 2>&1"
    Pop-Location
    $results += "claude n=$n r=$rep"
    # ---- Codex ----
    $d = "$root\codex_n${n}_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
    if ($n -eq 0) { cmd /c "`"$codex`" exec --json --skip-git-repo-check -s read-only -c model_reasoning_effort=`"low`" `"$prompt`" < NUL > run.jsonl 2>&1" }
    else { cmd /c "`"$codex`" exec --json --skip-git-repo-check -s read-only -c model_reasoning_effort=`"low`" -c `"mcp_servers.tracker.command='node'`" -c `"mcp_servers.tracker.args=['$server','$n']`" `"$prompt`" < NUL > run.jsonl 2>&1" }
    Pop-Location
    $results += "codex n=$n r=$rep"
    # ---- Cursor ----
    $d = "$root\cursor_n${n}_r$rep"; New-Item -ItemType Directory -Force "$d\.cursor" | Out-Null; Push-Location $d
    if ($n -gt 0) { ('{"mcpServers":{"tracker":{"command":"node","args":["' + ($server -replace '\\','\\') + '","' + $n + '"]}}}') | Out-File -Encoding ascii .cursor\mcp.json }
    cmd /c "`"$cursor`" -p --output-format stream-json --trust --approve-mcps `"$prompt`" < NUL > run.jsonl 2>&1"
    Pop-Location
    $results += "cursor n=$n r=$rep"
    Write-Output "done n=$n rep=$rep"
  }
}
Write-Output "ALL DONE"
