$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\agentmd"
$codex = "$env:USERPROFILE\.codex\plugins\.plugin-appserver\codex.exe"
$mcp = "$env:USERPROFILE\Downloads\agent-test\search\empty_mcp.json"
cmd /c "node `"$root\gen.js`" `"$root\files`""
$p1 = "Reply with the single word OK."
$p2 = "Reply with the single word OK again."
foreach ($rep in 1, 2) {
  foreach ($kb in 0, 1, 5, 10, 25, 50) {
    # ---- Claude Code: CLAUDE.md ----
    $d = "$root\runs\claude_${kb}kb_r$rep"
    if (-not (Test-Path "$d\turn2.json")) {
      Remove-Item -Recurse -Force $d -ErrorAction SilentlyContinue
      New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
      if ($kb -gt 0) { Copy-Item "$root\files\${kb}kb\guide.md" "$d\CLAUDE.md" }
      cmd /c "claude -p `"$p1`" --effort medium --output-format json --mcp-config `"$mcp`" --strict-mcp-config < NUL > turn1.json 2>&1"
      cmd /c "claude -c -p `"$p2`" --effort medium --output-format json --mcp-config `"$mcp`" --strict-mcp-config < NUL > turn2.json 2>&1"
      Pop-Location
    }
    # ---- Codex: AGENTS.md ----
    $d = "$root\runs\codex_${kb}kb_r$rep"
    if (-not (Test-Path "$d\turn2.jsonl")) {
      Remove-Item -Recurse -Force $d -ErrorAction SilentlyContinue
      New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
      if ($kb -gt 0) { Copy-Item "$root\files\${kb}kb\guide.md" "$d\AGENTS.md" }
      cmd /c "`"$codex`" exec --json --skip-git-repo-check -s read-only -c model_reasoning_effort=`"medium`" `"$p1`" < NUL > turn1.jsonl 2>&1"
      cmd /c "`"$codex`" exec resume --last --json --skip-git-repo-check -c model_reasoning_effort=`"medium`" `"$p2`" < NUL > turn2.jsonl 2>&1"
      Pop-Location
    }
    Write-Output "done ${kb}kb r$rep"
  }
}
Write-Output "ALL DONE"
