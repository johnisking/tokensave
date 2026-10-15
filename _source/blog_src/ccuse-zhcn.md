![如何查看 Claude Code、Codex 和 Cursor 的用量与费用](/claude-code-yongliang-zh-cn.jpg)

如何查看 Claude Code、Codex 和 Cursor 的用量与费用？Claude Code 本身会告诉你离套餐上限还有多远，却不太告诉你 token 都花在了哪里。在会话里输入 `/usage`，可以看到 5 小时额度和每周额度的百分比进度条；用 API 的话，还能看到当前会话的估算金额。但"上周二花了多少""这个月哪个项目用得最多""Max 套餐真的比按 token 付费划算吗"这类历史记录，它并不提供。

其实这些信息已经在你的电脑里了。Claude Code 会把每次对话都写进日志文件，每条回复都准确记录了模型名称和 token 数。ccusage、CodeBurn 这类命令行工具就是读取这些文件再求和。我想不装任何东西就看到同样的结果，于是做了一个在浏览器里读取日志的 [Claude Code 用量分析器](/zh-cn/claude-code-usage)，它也能读取 Codex 日志和 Cursor 的用量 CSV。

这篇文章整理了用量记录存在哪里、有哪些查看方法，以及我把自己的真实日志放进分析器后看到了什么。下面的数字都来自这些日志和 2026 年 10 月 15 日核对的官方价格表；人民币金额按 1 美元约 6.72 元换算，仅供参考。

## Claude Code 的用量记录在哪里？

Claude Code 会把每个会话的对话记录保存在 `~/.claude/projects/` 下。每个项目一个文件夹，每个会话是一个 `.jsonl` 文件（每行一个 JSON）。子代理的对话放在该会话旁边的 `subagents/` 文件夹里。

| 系统 | 文件夹 |
|---|---|
| Windows | `%USERPROFILE%\.claude\projects` |
| Mac | `~/.claude/projects` |
| Linux | `~/.claude/projects`（如果改了 CLAUDE_CONFIG_DIR，就是其中的 `projects/`） |

模型的每条回复都有一个 `usage` 字段，和费用有关的值有五个：

- **输入 token**：没有被缓存的新输入
- **缓存写入 token**：新写入提示词缓存的输入（分为 5 分钟和 1 小时两种）
- **缓存读取 token**：从缓存中重新读取的输入
- **输出 token**：模型写出的内容（包括思考过程）
- **模型**：例如 `claude-opus-5-5`

有两点容易出错。第一，同一条回复在流式输出时会被写成多行，继续会话时还可能再复制一次，直接相加会重复计算。分析器按消息 ID 和请求 ID 只计一次。第二，记录不会永久保留。根据 Claude Code 官方文档，超过 `cleanupPeriodDays` 的记录会被删除，**默认是 30 天**。想保留更久，就要在记录被删之前，在 `~/.claude/settings.json` 里调大这个值。

## 查看 Claude Code 用量的 4 种方法

![查看 Claude Code 用量的 4 种方法: 方法, 能看到什么, 安装, 按日期·项目的历史, 订阅 vs API, Codex·Cursor](/claude-code-yongliang-claude-code-4-zh-cn.jpg)

![查看 Claude Code 用量的 4 种方法: 方法, 能看到什么, 安装, 按日期·项目的历史, 订阅 vs API, Codex·Cursor](/claude-code-yongliang-claude-code-4-zh-cn.jpg)

| 方法 | 能看到什么 | 安装 | 按日期·项目的历史 | 订阅 vs API | Codex·Cursor |
|---|---|---|---|---|---|
| Claude Code 里的 `/usage` | 额度进度条、当前会话、占用额度的项目 | 不需要 | 无 | 无 | 无 |
| ccusage（`npx ccusage`） | 终端里的日报、月报、会话报告 | Node.js | 有 | 无 | 以 Claude Code 为主 |
| CodeBurn（`npx codeburn`） | 终端仪表盘，支持多种工具 | Node.js | 有 | 无 | 有（Cursor 为估算） |
| [TokenSave 用量分析器](/zh-cn/claude-code-usage) | 按日期、项目、模型、工具的费用，CSV | 不需要（浏览器） | 有 | 有 | 有 |

想知道会不会碰到额度上限，用 `/usage` 最合适。在 Pro、Max 套餐下，它还会显示子代理、MCP 服务器、缓存未命中等占用额度较多的项目。但它不是用来回顾几周用量的。习惯终端的话，ccusage 和 CodeBurn 都很好用，二者读取的是同样的 `.jsonl` 文件。浏览器分析器适合不想安装 Node.js、或者想在一个页面里同时看订阅和 API 对比的人。

## 分析器怎么用

![文件选择界面和 Claude Code、Codex、Cursor 日志位置说明](/claude-code-usage-analyzer-pick-zh-cn.jpg)

1. 打开 [tokensave.app/zh-cn/claude-code-usage](/zh-cn/claude-code-usage)。
2. 点击 **选择文件夹**，选中 `projects` 文件夹。Windows 上，在选择窗口顶部的地址栏粘贴 `%USERPROFILE%\.claude\projects` 并按 Enter；Mac 上按 ⌘ + Shift + G，粘贴 `~/.claude/projects`。
3. 需要的话，把 Codex 的 `~/.codex/sessions` 文件夹和 Cursor 用量 CSV（Cursor 控制台 → Usage → Export CSV）一起放进去。
4. 查看结果。时间范围可以切换为全部、7 天、30 天、本月；选择你的订阅后会显示对比。

选择文件夹时，Chrome 可能会询问"要将文件上传到此网站吗？"。这是浏览器打开文件夹时的固定提示。页面只是用浏览器的文件功能读取文件并把数字相加，提示词和代码不会离开这个标签页，也不会发送到服务器。

## 放进我自己的真实日志

![分析器结果：按 API 折算的费用、token、缓存节省、按工具的费用](/claude-code-usage-analyzer-result-zh-cn.jpg)

我放了三类记录：用来搭建和维护本网站的 Claude 代理会话（与 Claude Code 格式相同）、我电脑上的 Codex 会话，以及我账号的 Cursor 用量 CSV。

| 工具 | 回复 | Token | 按 API 折算 | 当时的套餐 |
|---|---|---|---|---|
| Claude Code（Opus 5.5） | 1,636 | 2.775 亿 | $145.90（约 ¥980） | Max 5× |
| Codex（GPT-5.6 Terra、GPT-6 Luna） | 108 | 650 万 | $1.98 | 免费 |
| Cursor（Grok 4.6） | 2 | 37.9 万 | $0.29 | 免费 |

Claude Code 的记录在 9 月 29 日到 10 月 15 日之间，实际使用了 10 天。用得最多的 10 月 8 日，按 API 价格约 39 美元。

最让我意外的是 token 的构成。2.775 亿 token 中，新输入只有约 3 千。缓存读取约 2.64 亿，缓存写入约 1,080 万，输出约 180 万。也就是说，**Claude Code"用掉"的 token 有 95% 以上是从缓存中重新读取的同一段上下文**。代理每一步都会重新发送之前的对话、打开过的文件和工具结果，而缓存让这部分变得便宜。

但便宜不等于免费。按 Opus 5.5 的价格，145.90 美元的构成如下：

| 项目 | 每 100 万 token | 费用占比 |
|---|---|---|
| 缓存读取 | $0.20 | 约 36% |
| 5 分钟缓存写入 | $5.00 | 约 34% |
| 输出 | $20.00 | 约 25% |
| 1 小时缓存写入 | $8.00 | 约 4% |
| 新输入 | $4.00 | 不到 1% |

Opus 5.5 的缓存读取比普通输入便宜 95%，但数量实在太多，所以费用占比反而最高。缓存写入也差不多，因为新文件、工具结果和长回答都要先写进缓存，之后才能便宜地读取。输出只有 180 万 token，但每 100 万 token 要 20 美元，占了总额的四分之一。

如果没有缓存，同样的缓存读取要按普通输入价格支付，会多花约 1,017 美元（约 ¥6,830）。界面上的"缓存节省"就是这个金额。

## Claude Max 划算吗？订阅与 API 对比

![订阅对比：Claude Max 5× 17 天的费用与同样用量的 API 费用](/claude-code-usage-analyzer-plan-zh-cn.jpg)

分析器会把你选的订阅，与同一时间段、同一工具的 API 费用进行比较。我的 Claude 记录跨了 17 天。Max 5× 不含税每月 100 美元，17 天约 56.67 美元（约 ¥381）。同样的 token 走 API 要 145.90 美元，所以 **我用掉了相当于订阅费约 257% 的 API 价值**。对于大量使用代理的工作，订阅明显比按 token 付费便宜。

看自己的结果时要注意两点：

- **订阅有上限。** Pro、Max 每 5 小时重置一次，还有每周上限。如果 API 折算金额是订阅费的好几倍，你很可能已经经常碰到上限，这时的选择是等待、升级套餐或购买额外用量。
- **用得少的话，订阅可能不划算。** 我的 Codex 和 Cursor 用的是免费套餐，分别是 1.98 美元和 0.29 美元。为这点 Codex 用量去付 ChatGPT Plus（每月 20 美元）的话，就是用量低于订阅费。分析器会用橙色显示这种情况。

如果还没用过 Claude Code、想看的是预估而不是历史，可以用根据任务大小和每天任务数估算月费的 [Claude Code 月费计算器](/zh-cn/agents)。

## Codex 和 Cursor 的用量

**Codex** 在 `~/.codex/sessions/年/月/日/` 下为每个会话留下一个 `rollout-….jsonl` 文件。它不是每条回复写一次用量，而是在每一步写下整个会话的累计值。分析器计算两步之间增加的部分，按 OpenAI API 价格计费，缓存输入按缓存价格计算。我记录里的 GPT-5.6 Terra 每 100 万 token 输入 2 美元、缓存输入 0.20 美元、输出 12 美元；GPT-6 Luna 分别是 0.10、0.01 和 0.50 美元。归档的会话会以同样的文件名移到 `archived_sessions/`，所以同名文件只计一次。

**Cursor** 的情况不同。我打开自己电脑上 Cursor 的本地数据库，发现每个对话的 token 数都是 0。新版 Cursor 不在本地保存 token 数，所以命令行工具也只能按字数估算。准确的数据来自 Cursor 控制台的用量导出：在 Usage 页面点击 **Export CSV**，每个请求都会列出时间、模型、含/不含缓存写入的输入、缓存读取、输出以及 Cursor 收取的金额。分析器直接使用这个金额。

## 怎么把费用降下来

知道大部分费用来自缓存和输出，降低费用的方法也就清楚了：

- **新任务开新会话。** 用 `/clear` 清掉旧上下文，之后的步骤就不会再读取它。会话越长，之前所有内容都会一直产生缓存读取费用。
- **日常工作用 Sonnet。** Sonnet 5.5 每 100 万 token 为 2/10 美元，Opus 5.5 为 4/20 美元，同样的会话按 API 计算约便宜 50%。
- **看看哪天最贵。** 每日图表能直接看出哪一天、哪类任务让费用上升。
- **清理不用的工具。** 用订阅的话，可以在 `/usage` 里看到哪些 MCP 服务器和子代理在占用额度。

## 常见问题

**怎么查看 Claude Code 的使用历史？**
在 [用量分析器](/zh-cn/claude-code-usage) 中打开 `~/.claude/projects` 文件夹，或在终端运行 `npx ccusage`。Claude Code 里的 `/usage` 显示的是当前额度，而不是历史。

**分析器会上传我的代码吗？**
不会。它在浏览器标签页里读取文件，只汇总 token 数字，不会发送到任何地方。

**为什么 API 折算费用比订阅高这么多？**
代理每一步都会重新读取完整上下文，缓存 token 因此非常多。订阅是固定费用，这个数字表示同样的 token 按 token 计费时的金额。

**为什么只显示最近一个月？**
Claude Code 默认会删除 30 天以前的记录。在 `settings.json` 里调大 `cleanupPeriodDays` 就能保留更久。

**支持 Gemini CLI、Copilot 或 Windsurf 吗？**
暂时不支持。目前可以读取 Claude Code、Codex 和 Cursor 的 CSV。

## 总结

Claude Code 其实把用掉的每个 token 都记录下来了，难的是读懂它。`/usage` 告诉你离上限有多近，`~/.claude/projects` 里的记录告诉你钱花到了哪里。在我 17 天的代理工作中，大部分 token 是缓存读取，缓存相关费用约占 API 折算费用的四分之三，Max 5× 的价值约为订阅费的 257%。用免费套餐的 Codex 和 Cursor 加起来也只有几美元。想看看自己的数字，就把文件夹放进 [用量分析器](/zh-cn/claude-code-usage)，和你的订阅比一比。

## 参考来源

- [Claude Code 文档：.claude 目录（记录位置与 30 天清理）](https://code.claude.com/docs/en/claude-directory)
- [Claude Code 文档：成本管理（/usage）](https://code.claude.com/docs/en/costs)
- [Anthropic API 价格（提示词缓存单价）](https://platform.claude.com/docs/en/about-claude/pricing)
- [OpenAI API 价格](https://developers.openai.com/api/docs/pricing)
- [Claude 套餐](https://claude.com/pricing) · [Cursor 价格](https://cursor.com/pricing)
- [ccusage](https://github.com/ryoppippi/ccusage) · [CodeBurn](https://github.com/getagentseal/codeburn)
<!-- autoimg -->
