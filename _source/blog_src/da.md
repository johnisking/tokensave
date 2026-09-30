Jeg oversatte den samme kundeserviceprompt til 41 sprog og talte tokens med o200k_base, OpenAI's nuværende tokenizer (GPT-4o og nyere). Engelsk kræver 34 tokens, dansk **46 – altså 1,35× så mange**, plads 16 af 41 (1 = billigst).

Den danske version:

> Opsummer kundens e-mail nedenfor i tre punkter, og foreslå et høfligt svar. Kunden skriver, at ordren kom to dage for sent, og at der manglede en vare i kassen.

## Resultater

| Sprog | Tokens | I forhold til engelsk | Gammel GPT-4-tokenizer |
|---|---:|---:|---:|
| English | 34 | 1,00× | 1,00× |
| 简体中文 | 35 | 1,03× | 1,53× |
| Español | 40 | 1,18× | 1,29× |
| Deutsch | 43 | 1,26× | 1,50× |
| **Dansk** | **46** | **1,35×** | **1,59×** |
| 한국어 | 49 | 1,44× | 2,50× |
| हिन्दी | 51 | 1,50× | 4,59× |
| 日本語 | 61 | 1,79× | 2,21× |
| Čeština | 68 | 2,00× | 2,59× |
| Ελληνικά | 70 | 2,06× | 4,94× |
| ਪੰਜਾਬੀ | 83 | 2,44× | 7,41× |

![Resultater](/blog-language-tax-chart-v4.png)

## Hvorfor

Tokenizeren lærer mest af engelsk tekst: ord som " polite" eller " customer" er ét token, mens mange danske ord – især sammensatte ord – deles op:

- manglede → `m | angle | de` · 3
- høfligt → `hø | fl | igt` · 3
- Opsummer → `Ops | ummer` · 2

## I forhold til den gamle tokenizer

Med tokenizeren fra GPT-4-tiden (cl100k) kostede den samme prompt **1,59×**, i dag **1,35×**.

## I penge

Med en model til 2 $ pr. million input-tokens koster det 68 $ på engelsk og 92 $ på dansk at sende prompten en million gange. Svarer modellen også på dansk, gælder den samme faktor for output-tokens, som typisk er 4–5× dyrere.

## Sådan sparer du

- Skriv systemprompten og faste instruktioner på engelsk; lad kun brugerens input være på dansk.
- Bed om mellemtrin (klassificering, udtræk, værktøjskald) på engelsk eller som JSON, og kun det endelige svar på dansk.
- Brug prompt caching til den faste del af prompten.

## Begrænsninger

- Der er målt én prompt; for andre tekster kan forholdet variere ±0,1–0,2.
- Claude og Gemini bruger andre tokenizere – tallene gælder kun OpenAI-modeller.
- Oversættelsen bygger på en gennemgået maskinoversættelse.

Alle resultater for 41 sprog (på engelsk): [sammenligning af 41 sprog](/blog/token-cost-by-language)
