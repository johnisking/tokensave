I had zero coding experience. I didn't even know what a "game engine" was. Still, by describing what I wanted to an AI in plain words, I made a game in 3 days, and getting it to launch cost **$45**.

![Sperm Race Google Play feature graphic](/blog-spermrace-feature-en.jpg)

This is part 1 of the dev log for Sperm Race, a silly sperm-racing game.

- **Google Play**: [Sperm Race](https://play.google.com/store/apps/details?id=com.spermrace.game&hl=en)
- **Web version (itch.io)**: [Sperm Race](https://johnisking.itch.io/sperm-race) — it came out on itch.io first, then on Google Play.

## "Let's make an easy game" took me all the way back to sperm

My goal at the start was simple: **"Just make an easy game."**

But the more I thought about what "easy" means, the more primal my ideas got. A game with one rule. A game that needs no explanation. A game everyone already knows. Following that line all the way back, I ended up at **sperm**. Swim forward, reach the egg, done. When you think about it, it's the one race every one of us has already won once.

The moment that thought hit me, I laughed out loud. **"Wait, this is funny."**

That one reaction set the direction. Not a serious game, but a goofy one that makes you smirk the second you see it.

## I didn't know what a game engine was

I had never written code. I didn't know engines like Unity or Godot existed, let alone what they do.

So I started without one. I told Claude (Sonnet) in Korean, "I want to make a game like this," and what came back was a single HTML file that ran right in the browser. Later I wrapped that same file into an Android app and put it on Google Play. Building by describing what you want to an AI instead of writing code yourself has a name now: **vibe coding**. Looking back, starting without knowing anything was actually faster. No engine to install, nothing to study, and I could play it on day one.

## The first prompt: "I want to make a game where a sperm swims to meet the egg"

That one sentence produced the first version. A sperm appeared on screen, and I could move it with my finger.

The problem was the tail. It was stiff as a stick, more matchstick than sperm. So the second thing I said was:

**"Add a wave to the tail."**

![Left: the first version with a stiff tail. Right: the next version with a wave](/blog-spermrace-tail.gif)

On the left is the stiff tail from the first version; on the right is the next version with the wave. Just making the tail wiggle finally made it look like a living sperm. That's how the main character was born.

## Three days of adding, cutting and adding again

After that I couldn't stop. Every time I played a build, the next idea showed up. If it came to mind, I added it. If it didn't work, I cut it. Then I added again.

1. **"Make a map."** Now there was somewhere to swim.
2. **"Add obstacles too."** Once there was something to dodge, it became a game. This is today's Adventure mode.
3. **"Add sperm racing, like real car racing."** A Racing mode with 3 laps around a track.
4. **"Make a mode where they run on their own like horse racing, and I place obstacles."** Pick a sperm to root for and help it win with obstacles. This is Derby mode.
5. **"Make a survival mode where you run away, with cancer as the motif."** Dodge cancer cells in a maze and survive for 1 minute 30 seconds.

The file dates left in my Downloads folder show how fast it went. I got the first HTML file in the early hours of August 19, and by the next afternoon I had downloaded a new version **16 times**. That's "fix this → download the new file → play" four or five times every half day. Meanwhile the code grew from 47 KB to 149 KB. By August 21 I was already taking screenshots for the store.

![Sperm Race main menu (current version — the Play with friends button was added after launch)](/blog-spermrace-menu-en.jpg)

## Graphics and sound effects, all in code

There isn't a single image file in this game. The character, backgrounds, tracks and mazes were all drawn in code by Sonnet.

![Four modes drawn entirely in code: Adventure, Racing, Derby, Survival](/blog-spermrace-modes.jpg)

From left: Adventure, Racing, Derby, Survival. The sperm is one ellipse and a wiggling line, the track is a thick curve, and the maze is glowing straight lines. For a silly game, that simplicity actually worked.

Same with sound effects. There are no sound files; Sonnet synthesized the sounds in code. The only audio file in the game folder is free background music from Pixabay.

## The testers' first reaction: "That's so original"

Before launch I showed it to testers. What came back was: **"That's so original."**

The idea that started with "wait, this is funny" wasn't funny only to me.

Here's what was in the game at launch:

- 4 modes: Adventure (120 stages), Racing (3 laps), Derby, Survival (last 1 minute 30 seconds)
- 13 languages
- Controls: drag, arrow keys/WASD, gamepad

Multiplayer with friends (up to 10 players in Derby, 4 in the other modes) came later, in an update after launch.

## So what did it cost? $45

| Item | What I used | Cost |
|---|---|---|
| Code | Claude Pro subscription (Sonnet) | $20 (one month) |
| Graphics | Drawn in code | $0 |
| Background music | Free tracks from Pixabay | $0 |
| Sound effects | Made in code | $0 |
| Launch | Google Play developer registration | $25 (one-time) |
| **Total** | | **$45** |

I use Claude Max 20× now, but Sperm Race was built **entirely on the Pro plan.** It was done within a month, so I only paid for one month.

For comparison, if you run a small game through the [AI game cost calculator](/ai-game-cost-calculator), the standard stack (image and music AI plus Claude Max) comes out at $128–181. Sperm Race came in at about 25–35% of that.

## Next time

So far it looks like "AI made a game in 3 days, easy." But the real struggle came after. Building took 3 days; fixing bugs took 14.

**Next: 3 days to build, 14 days to fix bugs** — why AI pokes at the wrong code when you ask it to "find the bug," and how I ended up finding bugs myself and having the AI fix them.
