![How to Make a Roblox Game in 2026: Step by Step with Roblox AI](/how-to-make-a-roblox-game-with-ai-en.jpg)

Most guides on how to make a Roblox game start with "you don't need to know how to code," and then drop you into Roblox Studio, a window with dozens of buttons and no obvious first move. This guide follows one real first session instead. I installed Roblox Studio for the first time on Windows, made a block, got stuck putting a script in the wrong place, and then had Roblox's built-in AI build a disappearing stepping-stone course. Along the way I dropped in a free car from the Creator Store. Every screenshot is from that session. Anything that can change, like system requirements, publishing rules and payouts, was checked against Roblox's official documentation on October 13, 2026.

![Roblox Creator Hub landing page with the Start Creating button](/how-to-make-a-roblox-game-with-ai-hub-en.jpg)

## What you need to make a Roblox game

Roblox games are made in **Roblox Studio**, a free app. Roblox's official requirements:

| | Minimum | Recommended |
|---|---|---|
| Operating system | Windows 10, macOS 10.14 | Windows 11, macOS 14+ |
| Memory (RAM) | 3 GB | 8 GB |
| Screen resolution | 1600×900 or higher | 1600×900 or higher |
| Price | Free | Free |

You also need a Roblox account. Your normal player account works, and if you don't have one you can create it during setup. Studio runs **only on Windows and Mac**. If you want to make a game on a phone or iPad, see "Making a Roblox game on mobile" further down.

## Step 1: Install Roblox Studio and sign in

1. On the Creator Hub (create.roblox.com), click **Start Creating**, then **Download Studio**.
2. Run the installer: `RobloxStudioInstaller.exe` on Windows, `RobloxStudio.dmg` on Mac. Windows shows a security prompt; check that the publisher is Roblox Corporation and click Run.
3. When the install finishes, Studio opens on a sign-in screen.

![Roblox Studio sign-in screen](/how-to-make-a-roblox-game-with-ai-login-en.jpg)

Click **Log In** and a browser opens. If you're new, choose **Create account**, then enter a birthday, username and password. The username field itself warns you not to use your real name.

![Roblox account sign-up screen](/how-to-make-a-roblox-game-with-ai-signup-en.jpg)

After that you'll see a "Continue to Roblox Studio" screen and the Terms of Service. Accept them and Studio opens on its start page. It offers a guided tour, which you can skip.

## Step 2: Pick a template

Click **New Experience** or **Templates** to see starting maps. My list had 15:

![Roblox Studio template list](/how-to-make-a-roblox-game-with-ai-templates-en.jpg)

| Type | Templates |
|---|---|
| Empty maps | Baseplate, Classic Baseplate, Flat Terrain |
| Game genres | Platformer, Laser Tag, FPS System, Racing, Classic Obby |
| Worlds | Village, Castle, Suburban, Pirate Island, Starting Place, Modern City |
| Other | UGC Homestore |

For a first project, **Baseplate** is the easiest. It's just a floor and a SpawnLocation (where your character appears), so you can see exactly what you add. If you already know you want an obby or a racing game, starting from Classic Obby or Racing and editing it is faster.

## Step 3: Add a block and change its color

![Baseplate with the SpawnLocation recolored](/how-to-make-a-roblox-game-with-ai-editor-en.jpg)

The Studio window has four areas you'll use constantly:

- **3D viewport (center):** your map. Hold the right mouse button and drag to turn the camera; move with W, A, S and D.
- **Home tab (top):** Part, Move, Scale, Rotate, Color and Anchor.
- **Explorer (right):** every object in the game as a tree. Anything under **Workspace** is physically in the map.
- **Properties (bottom right):** values of the selected object, such as Color, Material and Transparency.

Click **Part** on the Home tab and a gray block appears. Click Color in Properties to open the color picker; I tried it on the SpawnLocation and turned it lime green. Click **Anchor** so the block can't roll or be pushed. Press the blue ▶ (Play) to test with your own character.

## Step 4: Add a script, and where I got stuck

To make a block *do* something you need a **script**, written in Luau, Roblox's version of Lua. This one makes a block go see-through when a player steps on it, then disappear a second later:

```lua
local part = script.Parent
local touched = false

part.Touched:Connect(function(hit)
	if touched then return end
	local humanoid = hit.Parent:FindFirstChildOfClass("Humanoid")
	if humanoid then
		touched = true
		part.Transparency = 0.5
		task.wait(1)
		part:Destroy()
	end
end)
```

To add it, hover over your Part in the Explorer, click **+ → Script**, delete the `print("Hello world!")` line in the editor and paste the code.

That sounds simple. It wasn't. I pressed Play, stepped on the block, and nothing happened. The Output window showed this in red:

![Output window showing "Touched is not a valid member of Workspace"](/how-to-make-a-roblox-game-with-ai-error-en.jpg)

Three things had gone wrong at once:

| What you see | Why | Fix |
|---|---|---|
| `Touched is not a valid member of Workspace` | The script sits directly under Workspace, not inside the Part, so `script.Parent` is Workspace | Drag the Script onto the Part in the Explorer |
| Nothing runs at all | One stray character (`s`) pasted on the last line; a single typo stops the whole script | Delete it |
| Your fixes vanish | You edited while Play mode was running | Press the red ■ (Stop) first, then edit |

The parent-child tree in the Explorer is the most confusing part for a beginner. On my next try the script landed under the Baseplate and the new blocks ended up nested under a Texture. At that point I switched to the easier route: Roblox's AI.

## Step 5: Make the game with Roblox Assistant (AI)

Roblox Studio has a built-in AI called **Assistant**. According to Roblox's docs it answers questions, creates and edits objects and scripts, inserts Creator Store assets and generates 3D models. Click **Assistant** at the right end of the top bar and a chat panel opens.

![Roblox Studio with the Assistant panel open](/how-to-make-a-roblox-game-with-ai-assistant-en.jpg)

You just describe what you want. I sent four requests:

1. "Make a red block, put it in front of the spawn point, and when a player steps on it make it go half-transparent and disappear after 1 second."
2. Edit: add a respawn so the block comes back after it disappears.
3. Make 10 of them in a line as stepping stones.
4. Edit: give all 10 the same behavior as the first block, including the respawn.

![The red block Assistant created](/how-to-make-a-roblox-game-with-ai-redblock-en.jpg)

Each request took **15 to 30 seconds**. The disappearing block I'd failed to wire up by hand came out right on the first request, with the script already inside the block.

After the third request Assistant summarized what it built: 3×1×3 pads, 4 studs apart so you can jump between them, ten in a row starting in front of the spawn, grouped in a folder called RedSteppingStones. Then it asked whether it should give the stepping stones the same disappear-and-respawn behavior.

![Ten red stepping stones built by Assistant](/how-to-make-a-roblox-game-with-ai-stones-en.jpg)

After the fourth request the course worked as asked. Each stone turns see-through when you land on it, disappears a second later, and comes back three seconds after that.

![Stepping stones disappearing as the character crosses them](/how-to-make-a-roblox-game-with-ai-stones-en.gif)

![Playtesting the stepping-stone course](/how-to-make-a-roblox-game-with-ai-stones-play-en.jpg)

By the screenshot timestamps, it took about 15 minutes from opening Assistant to running across all ten stones. That was less than the time I'd spent fighting with one script by hand.

**How to write requests that work.** Roblox's own Build guide says to be specific about how the game plays. A request like the first one above, with the color, position, trigger and timing in one sentence, needs fewer corrections than "make a fun obby."

## Step 6: Save your game

There are two ways to save:

- **File → Save As:** saves a `.rbxl` file on your computer. That's what I did.
- **File → Publish:** uploads the game to Roblox's cloud and ties it to your account, so you can keep working from any computer. A published game is still private: only you and people with edit access can join until you release it.

## Add a free car from the Creator Store

The **Toolbox** on the left searches the Creator Store, where people share models. Plenty are free and some are paid. I searched for a car, inserted the free "Drift Car mobile", and it drove straight away, speedometer included.

![Inserting a free car model from the Creator Store](/how-to-make-a-roblox-game-with-ai-car-store-en.jpg)

![Driving the free car in a playtest](/how-to-make-a-roblox-game-with-ai-car-drive-en.jpg)

Models made by other people often come with scripts inside. After inserting one, look in the Explorer to see what came with it.

## Is Roblox's AI free? Usage, API keys and MCP

Open the **…** menu at the top right of the Assistant panel to get to Assistant settings. It has four tabs: Usage, API key, MCP servers and Skills.

![Assistant usage screen showing 6% of the free allowance used](/how-to-make-a-roblox-game-with-ai-usage-en.jpg)

**Usage.** There is a free allowance bar. After all four requests above it read **6% used**, **resets in 6 days**. You can switch on buying extra usage with Robux and set a daily spending cap. On my screen that switch was off and the cap field showed 500 Robux. Roblox's docs don't publish the exact size of the free allowance, so treat the 6% as a rough measure of what a small feature costs.

![Assistant API key settings](/how-to-make-a-roblox-game-with-ai-apikey-en.jpg)

**API key.** The default model is "Roblox default" and follows a daily limit. You can instead plug in your own Anthropic (Claude), OpenAI or Google API key. Then you pay that company's API rates, and Studio warns that your data goes to that provider. To estimate what that costs, run your prompts through the [token cost calculator](/).

![Assistant MCP server settings](/how-to-make-a-roblox-game-with-ai-mcp-en.jpg)

**MCP server.** Turn on "Use Studio as MCP server" and an outside AI coding tool can drive your open Studio session. Per Roblox's docs it can read and edit scripts, run Luau code, start and stop playtests, move the character, simulate keyboard and mouse input and capture the viewport. Quick connect supports Antigravity, Codex CLI, Claude Code, Claude Desktop, Cursor, Gemini CLI and Visual Studio Code. My screen only listed the four I had installed. For costs, see [Claude Code pricing](/blog/claude-code-cost-per-month) and [Codex pricing](/blog/codex-pricing). How the tools compare on the same task is in [Claude Code vs Codex vs Cursor](/blog/claude-code-vs-codex-vs-cursor-cost).

## Making a Roblox game on mobile: Build

Studio is desktop-only, but in July 2026 Roblox added **Build** to the mobile app. According to Roblox's docs, you describe a game in the Build tab and the AI generates gameplay, characters, environment, sound and achievements, and you can publish with one tap. For now it focuses on **2D and 2.5D games** such as clickers, arcade games and side-scrollers. You get a set number of free prompts per day and can buy more with Robux.

## Releasing your game and earning from it

I didn't release this test game, but here is what Roblox's docs require:

- **Release to ages 16+:** your account must be at least 2 days old and you must complete an age check (facial age estimation or government ID). Answer the content-maturity question in the Publish window and the game goes live.
- **Release to all ages:** everything above, plus verifying your account, turning on 2FA, and either 2 consecutive months of Roblox Plus or Premium or a refundable 1,000 Robux publishing fee. You get the fee back if the game keeps 25 highly engaged players for 60 days.
- **Earning:** you earn Robux from passes, developer products, subscriptions, paid private servers and more, and turn it into money through the Developer Exchange (DevEx). The standard rate is $0.0038 per Robux, so 30,000 Robux = $114. You need to be at least 13 and have at least 30,000 earned Robux to cash out.

## What it was actually like

With Assistant, a first-timer can go from installing Studio to a working disappearing stepping-stone course in a little over an hour. My honest take after the session:

> To make a proper game, the free allowance probably isn't enough. The Assistant panel is narrower than I expected. It doesn't cover the game view, but it would have been nice to pop just the Assistant out into its own window. With free assets and templates, plus paid ones, there's a lot of variety, so building looks easy.

One small feature used 6% of the free allowance. A game with a full map, a shop and saved progress will likely need more than the free tier through Assistant alone. For bigger builds, plan on buying extra usage with Robux or connecting Claude Code or Codex over MCP.

## How long will your game take, and what will it cost?

A stepping-stone course is a starting point. A real game's time and cost depend on genre and size. In the [AI game cost calculator](/ai-game-cost-calculator), choose Roblox as the platform and enter your genre and scope. It returns the expected build time, AI tool costs and a ready-to-paste kickoff prompt. If you don't have an idea yet, start from [what's trending on Roblox right now](/blog/roblox-trending-games). Real numbers from games I built solo with AI are in [indie game development cost](/blog/indie-game-development-cost).

## FAQ

**Is it free to make a Roblox game?**
Installing Studio, building and publishing to the cloud are free. Assistant has a free allowance; past it you buy more with Robux. Releasing to all ages requires a Plus or Premium subscription or a refundable 1,000 Robux fee.

**Do I need to know how to code?**
Not for simple games. The stepping-stone course here was built without writing a line of code, just by describing it to Assistant. Knowing how to read the Explorer tree (what sits inside what) saves a lot of time when something breaks.

**Can I make a Roblox game on my phone or iPad?**
Roblox Studio is Windows and Mac only. On a phone, the Build feature in the Roblox app makes 2D and 2.5D games with AI.

**How do I show my game to friends before releasing it?**
Use File → Invite early testers to invite up to 10 similar-aged friends to a preview.

*Sources: Roblox Creator Hub, [Studio setup](https://create.roblox.com/docs/studio/setup), [Create and publish games and places](https://create.roblox.com/docs/production/publishing/publish-experiences-and-places), [Assistant for Studio](https://create.roblox.com/docs/assistant/guide), [Connect to the Studio MCP server](https://create.roblox.com/docs/studio/mcp), [Create games with Build](https://create.roblox.com/docs/ai/build) and [Developer Exchange](https://create.roblox.com/docs/production/monetization/developer-exchange), checked October 13, 2026. Screenshots taken October 13, 2026 on Windows 11.*
<!-- autoimg -->
