![AI Image Generation Cost per Image, Compared](/ai-image-cost-per-image-en.jpg)

AI image prices are quoted per image, and the range is wider than most people expect: from about one cent to forty cents for a single picture. For a one-off that hardly matters. For a product catalog, a game's art pipeline or an app that generates images for users, it is the difference between a rounding error and a real line in the budget.

## Price per 1024px image

![Price per 1024px image: Model, Maker, 1 image, 1,000 images](/ai-image-cost-per-image-price-per-1024px-image-en.jpg)

API prices checked September 30, 2026:

| Model | Maker | 1 image | 1,000 images |
|---|---|---|---|
| GPT Image 2.5 · low* | OpenAI | $0.010 | $10 |
| FLUX.2 [klein] 4B | Black Forest Labs | $0.014 | $14 |
| Grok Imagine Image | xAI | $0.020 | $20 |
| Runway Gen-4 Image Turbo | Runway | $0.020 | $20 |
| FLUX.2 [pro] | Black Forest Labs | $0.030 | $30 |
| Nano Banana 2 Lite | Google | $0.034 | $34 |
| Seedream 5 Lite* | ByteDance | $0.040 | $40 |
| GPT Image 2.5 · medium* | OpenAI | $0.050 | $50 |
| Nano Banana 2 | Google | $0.067 | $67 |
| FLUX.2 [max] | Black Forest Labs | $0.070 | $70 |
| GPT Image 2.5 · high* | OpenAI | $0.160 | $160 |
| Nano Banana Pro* | Google | $0.200 | $200 |

\* Rate from Runway's API for that model.

## Resolution changes the price

![Resolution changes the price: Nano Banana 2 goes from $0.067 at 1K to $0.101 at 2K and $0.151 at 4K.; FLUX.2 bills per megapixel; GPT Image ](/ai-image-cost-per-image-resolution-changes-the-price-en.jpg)

Most models charge more for larger images, but not in the same way:

- **Nano Banana 2** goes from $0.067 at 1K to $0.101 at 2K and $0.151 at 4K.
- **FLUX.2** bills per megapixel: the first megapixel at one price, each additional one cheaper. A 2048px image is 4 MP.
- **GPT Image 2.5 · medium** costs the same $0.05 at 1K and 2K, then $0.11 at 4K.

If you only need images for the web or social media, 1K is usually enough, and upscaling a good 1K image can be cheaper than generating at 4K.

## Quality tiers are the biggest lever

The same model can cost very different amounts depending on the quality setting. GPT Image 2.5 is 16 times more expensive at *high* than at *low*. Use the low or draft tier to find a composition that works, then regenerate only the keepers at higher quality.

## Plan for retries

As with video, the list price is the cost of one attempt. Hands, text inside images, and consistent characters often need several tries. Budget **two to four generations per usable image** for anything detailed.

## Which one to pick

![Which one to pick: Bulk and drafts; Good quality at a fair price; Hardest prompts, text in images, final assets](/ai-image-cost-per-image-which-one-to-pick-en.jpg)

- **Bulk and drafts:** GPT Image 2.5 low, FLUX.2 [klein], Grok Imagine Image.
- **Good quality at a fair price:** FLUX.2 [pro], Nano Banana 2, Seedream 5.
- **Hardest prompts, text in images, final assets:** Nano Banana Pro, GPT Image 2.5 high, FLUX.2 [max].

Quality is subjective, so test your own prompts on two or three models before you commit to one for a large batch.

## Price your batch

The [AI image cost calculator](/image) compares every model above for your resolution and number of images.

*Prices change often. Confirm on the provider's pricing page before a large job.*
<!-- autoimg -->
