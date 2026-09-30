Ik vertaalde dezelfde klantenservice-prompt naar 34 talen en telde de tokens met o200k_base, de huidige tokenizer van OpenAI (GPT-4o en nieuwer). Engels heeft 34 tokens nodig, Nederlands **44 — 1,29× zoveel**, plaats 10 van 34 (1 = goedkoopst).

De Nederlandse versie:

> Vat de onderstaande e-mail van de klant samen in drie punten en stel een beleefd antwoord voor. De klant zegt dat de bestelling twee dagen te laat aankwam en dat er één artikel in de doos ontbrak.

## Resultaten

| Taal | Tokens | Ten opzichte van Engels | Oude GPT-4-tokenizer |
|---|---:|---:|---:|
| English | 34 | 1,00× | 1,00× |
| 简体中文 | 35 | 1,03× | 1,53× |
| Español | 40 | 1,18× | 1,29× |
| Deutsch | 43 | 1,26× | 1,50× |
| **Nederlands** | **44** | **1,29×** | **1,74×** |
| 한국어 | 49 | 1,44× | 2,50× |
| 日本語 | 61 | 1,79× | 2,21× |
| Čeština | 68 | 2,00× | 2,59× |
| Ελληνικά | 70 | 2,06× | 4,94× |

![Resultaten](/blog-language-tax-chart-v3.png)

## Waarom

De tokenizer leert vooral van Engelse tekst: woorden als " polite" of " customer" zijn één token, terwijl veel Nederlandse woorden in stukken worden gehakt:

- ontbrak → `ont | br | ak` · 3
- beleefd → `bele | efd` · 2
- aankwam → `aank | wam` · 2

## Vergeleken met de oude tokenizer

Met de tokenizer uit het GPT-4-tijdperk (cl100k) kostte dezelfde prompt **1,74×**, nu **1,29×**.

## In geld

Bij een model van $2 per miljoen inputtokens kost het 68 dollar in het Engels en 88 dollar in het Nederlands om deze prompt een miljoen keer te versturen. Antwoordt het model ook in het Nederlands, dan geldt dezelfde factor voor de outputtokens, die meestal 4–5× duurder zijn.

## Zo bespaar je

- Schrijf de systeemprompt en vaste instructies in het Engels; houd alleen de invoer van gebruikers in het Nederlands.
- Laat tussenstappen (classificatie, extractie, tool-aanroepen) in het Engels of als JSON teruggeven, en alleen het eindantwoord in het Nederlands.
- Gebruik prompt caching voor het vaste deel van de prompt.

## Beperkingen

- Er is één prompt gemeten; bij andere teksten kan de verhouding ±0,1–0,2 afwijken.
- Claude en Gemini gebruiken andere tokenizers; deze cijfers gelden alleen voor OpenAI-modellen.
- De vertaling is gebaseerd op een gecontroleerde machinevertaling.

Alle resultaten voor 34 talen (in het Engels): [vergelijking van 34 talen](/blog/token-cost-by-language)
