$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\search"
$codex = "$env:USERPROFILE\.codex\plugins\.plugin-appserver\codex.exe"
$enc = New-Object System.Text.UTF8Encoding($false)
$qs = [ordered]@{
  "en_q1_fact"    = "What is the current monthly price of the Claude Pro plan in the United States? Answer in one sentence and cite your source.";
  "en_q2_news"    = "Summarize the three most important AI model releases announced in the past 7 days, one sentence each, with a source link for each.";
  "en_q3_compare" = "Compare the current API prices per million input and output tokens of the flagship models from Anthropic, OpenAI and Google. Use official pricing pages and cite them.";
  "en_q4_geo"     = "How many more tokens does Korean text need than the same English text on OpenAI and Claude tokenizers? Give numbers and cite your sources."
}
foreach ($rep in 1, 2) {
  foreach ($k in $qs.Keys) {
    $d = "$root\claude_${k}_notools_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
    [IO.File]::WriteAllText("$d\prompt.txt", $qs[$k], $enc); $t0 = Get-Date
    cmd /c "type prompt.txt | claude -p --effort medium --output-format stream-json --verbose --tools `"`" --mcp-config `"$root\empty_mcp.json`" --strict-mcp-config > run.jsonl 2>&1"
    [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)"); Pop-Location
    $d = "$root\codex_${k}_notools_r$rep"; New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
    [IO.File]::WriteAllText("$d\prompt.txt", $qs[$k], $enc); $t0 = Get-Date
    cmd /c "type prompt.txt | `"$codex`" exec --json --skip-git-repo-check -s read-only -c web_search=`"disabled`" --disable apps --disable plugins --disable in_app_browser --disable skill_search -c model_reasoning_effort=`"medium`" - > run.jsonl 2>&1"
    [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)"); Pop-Location
    Write-Output "done $k r$rep"
  }
}
Write-Output "ALL DONE"
