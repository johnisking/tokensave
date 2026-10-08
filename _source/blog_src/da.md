![Dansk bruger 35 % flere tokens end engelsk i GPT](/tokens-dansk-gpt-da.jpg)

Jeg oversatte den samme kundeserviceprompt til 41 sprog og talte tokens med o200k_base, OpenAI's nuværende tokenizer (GPT-4o og nyere). Engelsk kræver 34 tokens, dansk **46 – altså 35% flere**, plads 16 af 41 (1 = billigst).

Den danske version:

> Opsummer kundens e-mail nedenfor i tre punkter, og foreslå et høfligt svar. Kunden skriver, at ordren kom to dage for sent, og at der manglede en vare i kassen.

## Resultater

| Sprog | Tokens | I forhold til engelsk | Sparet ved afsendelse på engelsk |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| **Dansk** | **46** | **+35%** | **26%** |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Diagram: ekstra tokens pr. sprog sammenlignet med engelsk i GPT](/blog-language-tax-chart-v5.png)

## Hvorfor

![Hvorfor: manglede → m | angle | de · 3; høfligt → hø | fl | igt · 3; Opsummer → Ops | ummer · 2](/tokens-dansk-gpt-hvorfor-da.jpg)

Tokenizeren lærer mest af engelsk tekst: ord som " polite" eller " customer" er ét token, mens mange danske ord – især sammensatte ord – deles op:

- manglede → `m | angle | de` · 3
- høfligt → `hø | fl | igt` · 3
- Opsummer → `Ops | ummer` · 2

## Skift til engelsk med én knap

Den største besparelse får du ved at sende din prompt på engelsk: ca. 26 % færre tokens for dansk. Nutidens modeller forstår engelske instruktioner fint og svarer på dansk, hvis du beder om det. I TokenSaves token-tæller indsætter du din prompt og trykker på **💸 Spar tokens**: den rydder op i mellemrum, oversætter til engelsk, fjerner fyldord og tilføjer "Reply in Danish.", så svaret forbliver på dit sprog. Den bruger oversætteren, der er indbygget i Chrome 138+ / Edge 148+ på computer; oversættelsen sker på din egen enhed, og din tekst uploades aldrig. Tryk på **↩ Original** for at få originalen tilbage.

## I penge

Med en model til 2 $ pr. million input-tokens koster det 68 $ på engelsk og 92 $ på dansk at sende prompten en million gange. Svarer modellen også på dansk, gælder den samme faktor for output-tokens, som typisk er 300–400% dyrere.

## Sådan sparer du

![Sådan sparer du: Skriv systemprompten og faste instruktioner på engelsk; lad kun brugerens input være på dansk.; Bed om mellemt](/tokens-dansk-gpt-sadan-sparer-du-da.jpg)

- Skriv systemprompten og faste instruktioner på engelsk; lad kun brugerens input være på dansk.
- Bed om mellemtrin (klassificering, udtræk, værktøjskald) på engelsk eller som JSON, og kun det endelige svar på dansk.
- Brug prompt caching til den faste del af prompten.

## Begrænsninger

- Der er målt én prompt; for andre tekster kan forholdet variere ±0,1–0,2.
- Claude og Gemini bruger andre tokenizere – tallene gælder kun OpenAI-modeller.
- Oversættelsen bygger på en gennemgået maskinoversættelse.

Prøv med din egen tekst i [tokentælleren](/da/); alle sprog side om side finder du i [sprogtabellen](/languages).

Alle resultater for 41 sprog (på engelsk): [sammenligning af 41 sprog](/blog/token-cost-by-language)

## Kilder

- [tiktoken: OpenAIs tokenizer (o200k_base) på GitHub](https://github.com/openai/tiktoken)
- [Priser for OpenAI API](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
