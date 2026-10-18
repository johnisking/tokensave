$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\agentmd"
$codex = "$env:USERPROFILE\.codex\plugins\.plugin-appserver\codex.exe"
$mcp = "$env:USERPROFILE\Downloads\agent-test\search\empty_mcp.json"
$enc = New-Object System.Text.UTF8Encoding($false)
$body = [IO.File]::ReadAllText("$root\files\50kb\guide.md")
$line = "`n## Release`n- The release codename for this project is BLUE-HERON-47.`n"
$q = "Without opening or reading any files, answer from the instructions you were given: what is the release codename for this project? If you were not given one, say NONE."
foreach ($pos in "start", "end") {
  if ($pos -eq "start") { $txt = $line + $body } else { $txt = $body + $line }
  foreach ($rep in 1, 2) {
    $d = "$root\sentinel\claude_${pos}_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
    [IO.File]::WriteAllText("$d\CLAUDE.md", $txt, $enc)
    cmd /c "claude -p `"$q`" --effort medium --output-format json --tools `"`" --mcp-config `"$mcp`" --strict-mcp-config < NUL > out.json 2>&1"
    Pop-Location
    $d = "$root\sentinel\codex_${pos}_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
    [IO.File]::WriteAllText("$d\AGENTS.md", $txt, $enc)
    cmd /c "`"$codex`" exec --json --skip-git-repo-check -s read-only -c model_reasoning_effort=`"medium`" `"$q`" < NUL > out.jsonl 2>&1"
    Pop-Location
    Write-Output "done $pos r$rep"
  }
}
Write-Output "ALL DONE"
