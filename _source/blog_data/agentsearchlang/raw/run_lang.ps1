$ErrorActionPreference = "Continue"
$root = "$env:USERPROFILE\Downloads\agent-test\searchlang"
$mcp = "$env:USERPROFILE\Downloads\agent-test\search\empty_mcp.json"
$enc = New-Object System.Text.UTF8Encoding($false)
$qs = [IO.File]::ReadAllText("$root\questions.json", [Text.Encoding]::UTF8) | ConvertFrom-Json
$keys = $qs.PSObject.Properties.Name
function Done($p) { (Test-Path "$p\run.jsonl") -and ((Get-Content "$p\run.jsonl" -Raw -Encoding UTF8) -match '"type":"result"') }
foreach ($rep in 1, 2) {
  foreach ($k in $keys) {
    $d = "$root\claude_${k}_on_r$rep"
    if (-not (Done $d)) {
      New-Item -ItemType Directory -Force $d | Out-Null; Push-Location $d
      [IO.File]::WriteAllText("$d\prompt.txt", $qs.$k, $enc)
      $t0 = Get-Date
      cmd /c "type prompt.txt | claude -p --effort medium --output-format stream-json --verbose --allowedTools WebSearch WebFetch --mcp-config `"$mcp`" --strict-mcp-config > run.jsonl 2>&1"
      [IO.File]::WriteAllText("$d\seconds.txt", "$([int]((Get-Date) - $t0).TotalSeconds)")
      Pop-Location
    }
    Write-Output "done $k r$rep"
  }
}
Write-Output "ALL DONE"
