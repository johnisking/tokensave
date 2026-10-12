![Indie Game Development Cost: Solo Dev Budget, Fees, Real $20 Case](/indie-game-development-cost-en.jpg)

> **30-second summary**
> - Indie game development cost splits into four buckets: **engine, art and audio, code, and release**.
> - Engines are **free to start** (Unity Personal, Godot, Unreal Engine). Release fees are **$25 once for Google Play, $100 per game on Steam, and $99 a year for Apple**.
> - Outsourcing studios quote tens of thousands of dollars for a small game. **Building it yourself with AI** comes to about **$53–181** for a small 2D game (calculator estimate).
> - My own game was built for **$20**: one month of Claude Pro and nothing else. It launched on Google Play in September 2026, has about **200 downloads** so far, and has earned **$0**.

Search for "indie game development cost" and most of what you find is written by outsourcing studios, with budgets from $10,000 to $1,000,000. That is useful if you are hiring a team. It is not useful if you plan to build the game yourself. This guide is for the solo developer: what is free, what you really have to pay for, and what my own game cost, including what happened after launch. Prices were checked on official pages on October 12, 2026.

## The four costs of an indie game

![The four costs of an indie game: Bucket, What it covers, Cost range](/indie-game-development-cost-the-four-costs-of-an-indie-game-en.jpg)

| Bucket | What it covers | Cost range |
|---|---|---|
| Engine | Unity, Godot, Unreal Engine, GameMaker | Free to start |
| Art and audio | Characters, backgrounds, UI, music, sound effects | $0 with free assets, up to thousands of dollars for commissions |
| Code | Game logic, saves, ads and in-app purchases | Your time, or an AI subscription from $20 a month |
| Release | Store registration fees | Google Play $25 (once), Steam $100 (per game), Apple $99 (per year), web $0 |

For a solo developer the biggest cost is usually **time, not money**. That is why more and more indie developers use AI to cut the time spent on art, audio and code.

## Engine costs: free to start, with limits

![Engine costs: free to start, with limits: Engine, Price, The limit to know](/indie-game-development-cost-engine-costs-free-to-start-with-limits-en.jpg)

| Engine | Price | The limit to know |
|---|---|---|
| Unity Personal | Free | Revenue and funding combined must be $200,000 or less |
| Godot | Free | MIT open source license, no royalties |
| Unreal Engine | Free | 5% royalty on lifetime gross revenue above $1,000,000 per product |
| GameMaker | Free for non-commercial use | Professional license is $99.99 once, needed to sell your game |

A first-time solo developer can start with any of these at $0.

### Which engine fits a solo developer?

| Engine | Strengths | Weaknesses | Best for |
|---|---|---|---|
| Unity | Easy mobile and PC release, huge asset store and tutorials, C# | Above $200,000 you need Pro ($2,310 a year or $210 a month per seat); consoles also need Pro | 2D and 3D mobile games, learning from tutorials |
| Godot | Free forever, light and fast to install, GDScript (similar to Python) and C# | Console release goes through third-party porting companies; fewer assets than Unity | 2D games, keeping engine cost at $0 for good |
| Unreal Engine | High-end 3D graphics, Blueprint visual scripting without code | Heavy editor, needs a strong PC, 5% royalty above $1M | 3D and high-end PC games |
| GameMaker | Built for 2D, quick to learn | Selling requires a paid license | Small 2D games |

Unity canceled its per-install runtime fee in September 2024, and since Unity 6 the "Made with Unity" splash screen is optional on Personal. Unreal Engine does not charge its 5% royalty on revenue that Epic processes through the Epic Games Store.

## Release fees: what each store charges

| Platform | Registration fee | Store revenue share |
|---|---|---|
| Google Play | $25, once | Set by Google Play's service fee rules |
| Steam | $100 per game | Standard 30% |
| Apple App Store | $99 per year | Set by Apple's commission rules |
| Epic Games Store | – | 12%, and 100% of the first $1M per product each year when Epic processes the payment |
| itch.io and your own site | $0 | itch.io: 10% by default, and you can change it |

Steam's $100 is not refundable, but Valve pays it back once that game has made $1,000 in adjusted gross revenue. If you only want to test an idea, a free web release on itch.io costs nothing.

## Launch checklist: what you need besides money

### Steam

| Step | What it involves | Time |
|---|---|---|
| Identity | Sign up with your legal name or company name and verify it | – |
| Bank details | The account holder must match the sign-up name | – |
| US tax information | Fill in the tax interview (W-8BEN for most non-US developers) | 10–15 business days to verify |
| App fee | $100 per game | – |
| Waiting period | Minimum wait after paying before you can release | 21 days |
| Coming soon page | Your first games need a public "coming soon" page for at least 2 weeks | 2 weeks |
| Review | Store page and build review | 1–5 days |

If you skip the tax information, Valve withholds **30% of your earnings** under US rules. With a tax treaty country, the rate can be lower. To ship a Mac version on Steam, the game must be notarized by Apple, which needs a Developer ID from the Apple Developer Program ($99 a year).

### Google Play

| Step | What it involves |
|---|---|
| Developer account | $25 once, identity verification |
| Closed test (personal accounts) | Personal accounts created after November 13, 2023 need **at least 12 testers for 14 days in a row** before going to production |
| Paid apps and in-app purchases | A payments profile with seller details and a bank account |

I went through the 14-day closed test myself and wrote down every bug it caught in [Google Play's 14-day closed test](/blog/google-play-closed-testing-14-days).

### Apple App Store

| Step | What it involves |
|---|---|
| Apple Account | Two-factor authentication on, legal name (no nicknames or company names for individuals) |
| Individual sign-up | Legal name, email, phone, street address (no P.O. box) |
| Organization sign-up | A D-U-N-S number, a legal entity, and a website and email on the organization's domain |
| Annual fee | $99 per year |
| Paid apps and in-app purchases | Paid Apps Agreement, US tax forms, bank account |

Once a game earns money, your own country's tax rules apply too. Check with a local tax professional.

## Outsourcing vs building it yourself with AI

Outsourcing studios publish their own budgets. According to their blogs, a small 2D indie game costs about **$20,000–$100,000** (Prolific Studio), and a prototype starts at about **$5,000** (Pixune). These are quotes for hiring a team, and they vary with scope, platform and art style.

If you build it yourself with AI, your money goes to **AI subscriptions and store fees**. Here is a small 2D merge game in the [AI game cost calculator](/ai-game-cost-calculator):

| Stack | Time (estimate) | Cost |
|---|---|---|
| Best value (Gemini images + free music + Google AI Pro) | 14–22 days | $53–75 |
| Typical (Midjourney + Suno + ElevenLabs + Claude Max 5×) | 14–22 days | $128–181 |

The tradeoff: a studio costs you money but little time. Building it yourself costs little money, but **planning, testing and fixing take your own hours.** The full breakdown by size and genre is in [AI game development cost by size and genre](/blog/ai-game-development-cost).

## Real case: a game built for $20

I had zero coding experience. I made **Sperm Race**, a silly racing game, by describing what I wanted to an AI in plain words. Here is everything it cost to build:

| Item | What I used | Cost |
|---|---|---|
| Code | Claude Pro subscription | $20 (one month) |
| Graphics | Drawn in code by the AI | $0 |
| Music | Free tracks from Pixabay | $0 |
| Sound effects | Generated in code | $0 |
| **Cost to build** | | **$20** |

The first playable version took 3 days. Fixing bugs through Google Play's closed test took another 14. To publish, I paid the one-time **$25** Google Play fee on top. That fee is a release cost, not a build cost, and it covers every future game on the same account. The web version on itch.io was free to publish. How the first 3 days went is in [a beginner who vibe-coded a game](/blog/vibe-coding-a-game-beginner).

Later I fed the same specs into my calculator to see if it was right. It predicted $47–102, and the real number came in below that. The comparison is in [I checked the calculator against my released game](/blog/ai-game-cost-calculator-review).

### What happened after launch

| | Result |
|---|---|
| Released | September 2026 (Google Play, plus a free web version) |
| Downloads | About 200 so far |
| Revenue | $0 so far |

Building the game was the cheap part. **Getting players is the hard part.** A $20 game can be finished in weeks, but it will not find players on its own. If you budget for an indie game, budget for being found, either in money or in time spent on short clips, communities and store pages.

My time per game varies a lot. Besides Sperm Race (about 2 weeks), a gold-rush tycoon game took me about 4 weeks and a merge-and-decorate game about 6 weeks. The detail you want matters more than the genre.

## Hidden costs people forget

![Hidden costs people forget: Marketing; Servers; iOS](/indie-game-development-cost-hidden-costs-people-forget-en.jpg)

- **Marketing:** often bigger than the development cost. My game cost $20 to build and has about 200 downloads so far.
- **Servers:** online multiplayer or leaderboards need a backend such as Photon or Firebase.
- **iOS:** the $99 yearly fee, plus a real device for testing and time for App Review.
- **Languages:** every added language means translation and checking.
- **Your time:** every extra month of development is another month of subscriptions.
- **Taxes:** once money comes in, your country's tax and business registration rules apply.

## How to cut costs without cutting quality

1. **Start on a free engine.** Unity Personal, Godot and Unreal Engine all cost $0 to start.
2. **Make art with AI, only as much as you need.** Compare per-image prices in the [AI image cost calculator](/image).
3. **Start with free audio.** Pixabay, Kenney and Freesound have free music and sound effects. Check each license.
4. **Ship small, then grow.** Finish within one month and you only pay one month of subscriptions.
5. **Release where it is cheap first.** Put a web build on itch.io ($0) or Google Play ($25), see how players react, then move to Steam.

## FAQ

**How much does it cost to make an indie game?**
Done yourself, it can be very little: my game cost $20 to build. With paid AI tools for art and music, a small 2D game comes to about $53–181. Hiring a studio starts in the thousands and often reaches tens of thousands of dollars.

**Can one person make an indie game for free?**
Almost. The engines are free, free assets exist, and a web release on itch.io costs $0. In practice most solo developers pay for at least one AI or tool subscription to save time.

**How much does it cost to release a game on Steam, Google Play and the App Store?**
Steam charges $100 per game (paid back after $1,000 in revenue), Google Play $25 once, and Apple $99 every year.

**Is Godot really free? Do Unity and Unreal charge royalties?**
Godot is free under the MIT license. Unity Personal is free up to $200,000 in revenue and funding and charges no runtime fee. Unreal Engine charges 5% on lifetime gross revenue above $1,000,000 per product.

**What is the biggest cost of solo indie game development?**
Your time, then marketing. My build cost was $20, but getting past 200 downloads needs time or money spent on being found.

**Is it cheaper to make a game yourself or hire a studio?**
In money, doing it yourself is far cheaper. In time, a studio is faster for you. Use the [AI game cost calculator](/ai-game-cost-calculator) to estimate your own project.

**How long does it take to make an indie game alone?**
There is no single answer. It depends on scope, experience and how many hours a day you put in. My small mobile game took about 2 weeks including bug fixing.

## Sources

- [Unity pricing](https://unity.com/products)
- [Unity pricing updates](https://unity.com/products/pricing-updates)
- [Unity: canceling the runtime fee](https://unity.com/blog/unity-is-canceling-the-runtime-fee)
- [Unreal Engine FAQ](https://www.unrealengine.com/en-US/faq)
- [Godot license](https://godotengine.org/license/)
- [GameMaker: upgrading your licence](https://gamemaker.io/en/help/articles/how-to-upgrade-your-gamemaker-licence)
- [Steamworks: Steam Direct fee](https://partner.steamgames.com/doc/gettingstarted/appfee)
- [Steamworks: onboarding](https://partner.steamgames.com/doc/gettingstarted/onboarding)
- [Steamworks: tax FAQ](https://partner.steamgames.com/doc/finance/taxfaq)
- [Steamworks: platforms (macOS notarization)](https://partner.steamgames.com/doc/store/application/platforms)
- [Google Play Console: get started](https://support.google.com/googleplay/android-developer/answer/6112435?hl=en)
- [Google Play: testing requirements for new personal accounts](https://support.google.com/googleplay/android-developer/answer/14151465?hl=en)
- [Apple Developer Program](https://developer.apple.com/programs/)
- [Apple Developer Program enrollment](https://developer.apple.com/programs/enroll/)
- [itch.io: payments](https://itch.io/docs/creators/payments)
- [Epic Games Store: 100% of the first $1M per product per year](https://store.epicgames.com/en-US/news/epic-games-store-updates-revenue-share-keep-100-of-the-first-1m-per-product-per-year)
- [Claude pricing](https://claude.com/pricing)
- [Prolific Studio: indie game development cost](https://blog.prolificstudio.co/blog/indie-game-development-cost/)
- [Pixune: how much does it cost to make a game](https://pixune.com/blog/how-much-does-it-cost-to-make-a-game/)
<!-- autoimg -->
