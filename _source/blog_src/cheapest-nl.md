![Goedkoopste AI API 2026: API-prijzen vergelijken per 1 miljoen tokens](/goedkoopste-ai-api-nl.jpg)

**Kort:** de goedkoopste AI API in oktober 2026 is GPT-5 nano ($0,05 / $0,40 per 1 miljoen input- / outputtokens, zo'n $3 voor 10.000 gewone verzoeken). Begin wel liever met GPT-6 Luna: die kost maar een fractie meer.

Gaat het je alleen om de laagste rekening? Dan is **GPT-5 nano** de goedkoopste AI API, gevolgd door **GPT-6 Luna** en **Qwen 3.8 Flash**. Maar het goedkoopste model past zelden bij elke taak. Hieronder vergelijk je de API-prijzen van alle grote modellen op basis van wat een echt verzoek kost. Je ziet de kosten per 1 miljoen tokens, welke goedkope modellen de moeite waard zijn en wanneer een duurder model je juist geld bespaart.

## Hoe hebben we de API-prijzen vergeleken?

We keken naar de kosten van één gewoon verzoek, niet alleen naar de prijs per miljoen tokens. Die prijs alleen is om twee redenen misleidend:

- **Output is bij de meeste modellen 200% tot 700% duurder dan input.** Een model met goedkope input en dure output kan dus verliezen van een model waarbij het andersom is.
- **Tokenizers verschillen.** Dezelfde Engelse tekst levert bij Claude Opus en Sonnet ongeveer 30% meer tokens op dan bij GPT, en bij Gemini ongeveer 5% minder. Een Claude-model van "$2 per miljoen" kost per verzoek dus meer dan een GPT-model van "$2 per miljoen".

Daarom hebben we één gewoon verzoek doorgerekend: **2.000 inputtokens en 500 outputtokens Engelse tekst**, geteld zoals de tokenizer van elk model ze telt. We gebruikten de officiële prijslijsten, gecontroleerd op 1 oktober 2026. Zonder caching- of batchkorting.

## Wat zijn de goedkoopste AI API's?

![Wat zijn de goedkoopste AI API's?: Model, Maker, Input / output per 1 miljoen, 1 verzoek, 10.000 verzoeken](/goedkoopste-ai-api-wat-zijn-de-goedkoopste-ai-api-s-nl.jpg)

GPT-5 nano, GPT-6 Luna en Qwen 3.8 Flash. Alle drie kosten minder dan $6 per 10.000 verzoeken.

| Model | Maker | Input / output per 1 miljoen | 1 verzoek | 10.000 verzoeken |
|---|---|---|---:|---:|
| GPT-5 nano | OpenAI | $0,05 / $0,40 | $0,00030 | $3,00 |
| GPT-6 Luna | OpenAI | $0,10 / $0,50 | $0,00045 | $4,50 |
| Qwen 3.8 Flash | Qwen | $0,15 / $0,47 | $0,00053 | $5,35 |
| GPT-4o mini | OpenAI | $0,15 / $0,60 | $0,00060 | $6,00 |
| Mistral Small | Mistral | $0,15 / $0,60 | $0,00063 | $6,30 |
| Gemini 3.1 Flash-Lite | Google | $0,25 / $1,50 | $0,00119 | $11,88 |
| DeepSeek V4.1 Flash (piek) | DeepSeek | $0,30 / $1,20 | $0,00120 | $12,00 |
| GPT-5 mini | OpenAI | $0,25 / $2,00 | $0,00150 | $15,00 |
| GPT-4.1 mini | OpenAI | $0,40 / $1,60 | $0,00160 | $16,00 |
| Gemini 3.5 Flash-Lite | Google | $0,30 / $2,50 | $0,00176 | $17,57 |
| Mistral Large 3 | Mistral | $0,50 / $1,50 | $0,00184 | $18,38 |

Ter vergelijking: dezelfde 10.000 verzoeken kosten **$90** op GPT-6 Sol, **$117** op Claude Sonnet 5.5, **$234** op Claude Opus 5.5 en **$450** op GPT-6 Astra. Het goedkoopste model in de tabel kost minder dan 1% van wat GPT-6 Astra kost.

## Welk goedkoop model kies je?

![Welk goedkoop model kies je?: GPT-6 Luna probeer je als eerste. Het is het nieuwste kleine model van OpenAI (september 2026) en kost maar $1](/goedkoopste-ai-api-welk-goedkoop-model-kies-je-nl.jpg)

Begin met GPT-6 Luna. Voor het allersimpelste werk op grote schaal neem je GPT-5 nano.

- **GPT-6 Luna** probeer je als eerste. Het is het nieuwste kleine model van OpenAI (september 2026) en kost maar $1,50 per 10.000 verzoeken meer dan GPT-5 nano. Goed voor classificatie, gegevens uit tekst halen, routering, korte antwoorden en samenvattingen.
- **GPT-5 nano** voor het eenvoudigste werk in de grootste volumes, waar elke fractie van een cent telt: taggen, ja/nee-controles, spamfilters.
- **Qwen 3.8 Flash** en **Mistral Small** zijn de goedkoopste opties buiten OpenAI. Handig als je een tweede aanbieder wilt, of open-weight modellen die je later zelf kunt hosten.
- **Gemini 3.1 Flash-Lite** en **DeepSeek V4.1 Flash** zijn ruim 160% duurder dan Luna, maar een stap beter in schrijven en redeneren. Toch zijn ze per verzoek nog zo'n 87% goedkoper dan GPT-6 Sol. DeepSeek V4.1 Flash kost buiten de piekuren de helft ($0,15 / $0,60). Daarmee komt hij vlak achter GPT-6 Luna; zie [DeepSeek V4.1 Flash-prijzen](/blog/deepseek-v4-1-flash-api-pricing) (in het Engels).
- **Claude Haiku 4.5** is het goedkoopste Claude-model: $0,0047 per verzoek, ruim 900% duurder dan Luna. Kies het als je specifiek het gedrag van Claude nodig hebt, niet om de prijs.

## Wanneer kost het goedkoopste model juist meer?

Als het fouten maakt. Een goedkoop model dat faalt, betaal je twee keer: een keer voor het slechte antwoord en nog een keer voor de nieuwe poging op een beter model. Plus je eigen tijd. Twee aanpakken besparen meer dan overal het goedkoopste model kiezen:

1. **Verdeel op moeilijkheid.** Stuur alles eerst naar een klein model. Alleen de verzoeken die het fout doet (of die jij als lastig markeert) gaan door naar GPT-6 Sol, Claude Sonnet of Gemini 3.1 Pro. Blijft 80% van de verzoeken op GPT-6 Luna en gaat 20% naar GPT-6 Sol, dan dalen de gemiddelde kosten met ongeveer 75% vergeleken met alles naar Sol sturen.
2. **Snij in tokens, niet alleen in de prijs.** Met prompt caching betaal je bij de meeste aanbieders voor herhaalde instructies en documenten ongeveer een tiende van de inputprijs. Batch-API's rekenen ongeveer de helft voor werk dat kan wachten. Zie [prompt caching uitgelegd](/blog/prompt-caching-explained) en [batch-API's voor de halve prijs](/blog/batch-api-half-price) (beide in het Engels).

## Verandert je taal de ranglijst?

De ranglijst blijft gelijk, maar de rekening niet. Alle kosten hierboven gelden voor Engels. Andere talen gebruiken meer tokens voor dezelfde inhoud: op GPT Koreaans ongeveer 44% meer en Japans ongeveer 79% meer. Elke prijs in de tabel stijgt dan met hetzelfde percentage.

**Nederlandse tekst gebruikt op GPT (o200k) ongeveer 29% meer tokens dan Engels** ([meting](/nl/blog/tokens-nederlands-gpt)). Elk bedrag in de tabel ligt voor Nederlandse prompts dus zo'n 29% hoger. Wil je dat terugwinnen? Stuur je instructies in het Engels en vraag om een antwoord in het Nederlands. Zie ook [dezelfde prompt in 41 talen](/blog/token-cost-by-language) (in het Engels).

## Hoe check je de kosten van je eigen prompt?

Plak een echte prompt in de [tokenteller](/nl/). Je ziet dan het exacte aantal tokens en de kosten op elk model. Je kunt ook de teller voor [OpenAI](/openai-token-counter), [Claude](/claude-token-counter) of [Gemini](/gemini-token-counter) openen (in het Engels). Een volledig overzicht van kunnen tegenover prijs vind je bij [AI-modellen: prestaties vs. prijs](/compare/performance) (in het Engels).

Betaal je liever een vast bedrag per maand? Bekijk dan de [AI-abonnementen](/nl/plans) en het artikel over [AI-abonnement prijzen](/nl/blog/ai-abonnement-prijzen).

*Prijzen volgens de officiële prijslijsten, gecontroleerd op 1 oktober 2026. Prijzen veranderen vaak. Check de prijspagina van de aanbieder voordat je een model kiest.*

## Bronnen

- [OpenAI API-prijzen](https://developers.openai.com/api/docs/pricing)
- [OpenAI: GPT-5 nano-model](https://developers.openai.com/api/docs/models/gpt-5-nano)
- [Alibaba Cloud: prijs van qwen3.8-flash](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash)
- [Mistral AI: Mistral Large 3](https://docs.mistral.ai/models/mistral-large-3-25-12)
- [Gemini API-prijzen](https://ai.google.dev/gemini-api/docs/pricing)
- [DeepSeek API-modellen en prijzen](https://api-docs.deepseek.com/quick_start/pricing/)
- [Claude API-prijzen](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
