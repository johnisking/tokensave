$null = [Console]::In.ReadToEnd()
Write-Output '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"Hook check: the file was saved. Before you finish, confirm that the game has 2 levels, a score display, 3 lives, and works with both the keyboard and the mouse."}}'
