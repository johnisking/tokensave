I'm a solo developer from Korea with zero coding background. I make games by describing them to an AI. My first one, **Sperm Race** (a silly sperm racing game), is live on Google Play. People kept asking me "how much does it cost to make a game with AI?", so I built a free calculator.

But I didn't actually know if my own calculator was right. So I fed it the exact specs of the game I had already shipped.

![Sperm Race screenshots](/spermrace-screens.jpg)

## What I entered

- **Genre:** racing · **Size:** small · **Art:** simple vector · **2D**
- **Content:** 3 characters, 3 music tracks, 13 languages
- **Features:** ads, in-app purchase, save data · **Platform:** Android · **Engine:** Phaser (in reality, plain HTML5)
- **Tools:** Claude Pro, Pixabay (free music), free sound effect libraries

It's all buttons. The only thing I typed was the game's name.

![The calculator's input form](/gamecalc-form-en.jpg)

## Prediction vs reality

| | Calculator | Actual |
|---|---|---|
| Cost | $47–102 | **$45** (1 month of Claude Pro $20 + Google Play fee $25) |
| Time | 19–31 days | **~17 days** (3 days to build + 14 days of bug fixing) |
| Code | ~5,400 lines | ~3,100 lines at launch → 13,800 now (after adding multiplayer) |
| Art | $10 (Midjourney) | **$0** (the AI drew characters and backgrounds in code) |
| Music & SFX | $0 | $0 (music from Pixabay, sound effects generated in code) |

![The calculator's result for Sperm Race](/gamecalc-spermrace-en.jpg)

## What it got right

The cost was right almost to the dollar. The only gap was the $10 for art, and that's because I had the AI draw everything in code instead of generating images.

## What it got wrong

- **Time:** the calculator was too pessimistic. The game itself took 3 days. The other 14 days were almost all bug fixing during Google Play's closed test. When I asked the AI to find a bug, it often "fixed" something unrelated, so I ended up hunting most bugs down myself. ([The 14 bugs, one by one](/blog/google-play-closed-testing-14-days))
- **Lines of code:** too high for the first version. But counting updates after launch, I've blown way past it.
- **"This plan's usage limit is likely too low" warning:** in my case, Claude Pro was enough to get to launch.

## How it calculates (roughly)

- **Size** is anchored to real games built solo with AI coding agents: small about 2 weeks, medium about 4, large about 6. Genre, features and number of languages move it up or down.
- **Images** = characters × animation frames + backgrounds + items + UI. It assumes you keep 1 of every 3 images you generate, so it plans for 3× as many generations.
- **Coding tokens** assume about 20 million tokens read per working day (mostly cached context) for 70% of the schedule. The 343M here is that estimate. I was on a subscription, so I never measured my real token count.

## What I learned

1. **With AI subscriptions, money goes out by the month, not by the token.** Every month you slip is another bill.
2. **Plan more time for fixing than for building.** For me it was more than four times as long.

The calculator is free, no sign-up. Pick a genre and size and you get the list of images and sounds you'll need, a cost and time estimate, and a ready-to-use starter prompt. It also handles 3D and Roblox games now.

If you've shipped something, try your own project and see how far off it is. I'd love to know.
