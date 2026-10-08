![How Much Does One Minute of AI Video Cost?](/ai-video-cost-per-minute-en.jpg)

AI video models are priced per second of output, and the prices look small: ten cents here, forty cents there. Multiply by sixty and by the number of attempts it takes to get a usable shot, and a one-minute video can cost anywhere from a few dollars to well over a hundred. Here is what one minute costs on the main video APIs, and how to keep the number down.

## One minute of 1080p video with audio

![One minute of 1080p video with audio: Model, Maker, $/second, 1 minute](/ai-video-cost-per-minute-one-minute-of-1080p-video-with-audio-en.jpg)

API list prices checked September 30, 2026, multiplied out to 60 seconds:

| Model | Maker | $/second | 1 minute |
|---|---|---|---|
| Veo 3.1 Lite | Google | 0.08 | $4.80 |
| Veo 3.1 Fast | Google | 0.12 | $7.20 |
| Kling 3.0 Turbo | Kuaishou | 0.14 | $8.40 |
| Hailuo 3 (2K)* | MiniMax | 0.15 | $9.00 |
| Gemini Omni Flash* | Google | 0.15 | $9.00 |
| Kling 3.0 | Kuaishou | 0.168 | $10.08 |
| Wan 3.0* | Alibaba | 0.20 | $12.00 |
| Grok Imagine Video 1.5 | xAI | 0.25 | $15.00 |
| FLUX 3 Video | Black Forest Labs | 0.29 | $17.40 |
| Veo 3.1 | Google | 0.40 | $24.00 |
| Seedance 2.0* | ByteDance | 0.40 | $24.00 |

\* No public per-second price from the maker; the rate shown is Runway's API price for that model.

## Cheaper at 720p, or without sound

![Cheaper at 720p, or without sound: Model, 720p, 1 minute](/ai-video-cost-per-minute-cheaper-at-720p-or-without-sound-en.jpg)

Dropping to 720p, or turning audio off where a model charges for it, cuts the price a lot:

| Model | 720p, 1 minute |
|---|---|
| Runway Gen-4 Turbo (no audio) | $3.00 |
| Veo 3.1 Lite | $3.00 |
| FLUX 3 Video Draft | $3.60 |
| Grok Imagine Video | $4.20 |
| Kling 3.0 (no audio) | $5.04 |

Kling 3.0, for example, charges $0.112 per second at 1080p without audio and $0.168 with it: sound adds 50%.

## The number that actually matters: attempts

Nobody gets a usable one-minute video from one generation. Most models produce clips of 5 to 10 seconds, so a minute is 6 to 12 clips, and each clip often takes 2 to 4 tries before the motion, faces and timing look right. A realistic budget is the list price **times three**.

On Veo 3.1 at 1080p, that turns $24 into roughly $72 for one finished minute. On Veo 3.1 Fast, $7.20 becomes about $22.

## How to spend less

![How to spend less: Draft cheap, finish expensive. Find the right prompt and framing on a draft or lite model at 720p, then render](/ai-video-cost-per-minute-how-to-spend-less-en.jpg)

1. **Draft cheap, finish expensive.** Find the right prompt and framing on a draft or lite model at 720p, then render only the final take on the premium model.
2. **Generate short.** A 5-second test clip shows whether a prompt works for half the cost of a 10-second one.
3. **Skip audio you will replace.** If music and voice-over are added in editing anyway, use a silent mode where the model offers one.
4. **Use image-to-video.** Starting from a still you already like gives far more predictable results than text alone, which means fewer retries.
5. **Check resolution needs.** Social feeds compress video heavily. 720p is often indistinguishable from 1080p on a phone.

## Price your own project

The [AI video cost calculator](/video) lets you set clip length, number of clips, resolution and audio, and ranks every model by total cost.

*Prices change often. Confirm on the provider's pricing page before a large job.*
<!-- autoimg -->
