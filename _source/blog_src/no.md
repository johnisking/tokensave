![Norsk bruker 32 % flere tokens enn engelsk i GPT](/tokens-norsk-gpt-no.jpg)

Jeg oversatte den samme kundeserviceprompten til 41 språk og talte tokens med o200k_base, OpenAIs nåværende tokenizer (GPT-4o og nyere). Engelsk trenger 34 tokens, norsk **45 – altså 32% flere**, plass 13 av 41 (1 = billigst).

Den norske versjonen:

> Oppsummer kundens e-post nedenfor i tre punkter, og foreslå et høflig svar. Kunden sier at bestillingen kom to dager for sent, og at det manglet en vare i esken.

## Resultater

| Språk | Tokens | Sammenlignet med engelsk | Spart hvis sendt på engelsk |
|---|---:|---:|---:|
| English | 34 | ±0% | – |
| 简体中文 | 35 | +3% | 3% |
| Español | 40 | +18% | 15% |
| Deutsch | 43 | +26% | 21% |
| **Norsk** | **45** | **+32%** | **24%** |
| 한국어 | 49 | +44% | 31% |
| हिन्दी | 51 | +50% | 33% |
| 日本語 | 61 | +79% | 44% |
| Čeština | 68 | +100% | 50% |
| Ελληνικά | 70 | +106% | 51% |
| ਪੰਜਾਬੀ | 83 | +144% | 59% |

![Diagram: ekstra tokens per språk sammenlignet med engelsk i GPT (41 språk)](/blog-language-tax-chart-v5.png)

## Hvorfor

![Hvorfor: bestillingen → best | ill | ingen · 3; høflig → hø | fl | ig · 3; Oppsummer → Opp | summer · 2](/tokens-norsk-gpt-hvorfor-no.jpg)

Tokenizeren lærer mest av engelsk tekst: ord som " polite" eller " customer" er ett token, mens mange norske ord – særlig sammensatte ord – deles opp:

- bestillingen → `best | ill | ingen` · 3
- høflig → `hø | fl | ig` · 3
- Oppsummer → `Opp | summer` · 2

## Bytt til engelsk med én knapp

Den største besparelsen får du ved å sende prompten på engelsk: omtrent 24 % færre tokens for norsk. Dagens modeller forstår engelske instruksjoner svært godt og svarer på norsk hvis du ber om det. I [TokenSaves token-teller](/no/) limer du inn prompten og trykker på **💸 Spar tokens**: den rydder opp i mellomrom, oversetter til engelsk, fjerner fyllord og legger til "Reply in Norwegian." slik at svaret blir på ditt språk. Den bruker oversetteren som er innebygd i Chrome 138+ / Edge 148+ på datamaskin; oversettelsen skjer på din egen enhet, og teksten lastes aldri opp. Trykk på **↩ Original** for å få tilbake originalen.

## I penger

Med en modell til 2 $ per million input-tokens koster det 68 $ på engelsk og 90 $ på norsk å sende prompten én million ganger. Svarer modellen også på norsk, gjelder den samme faktoren for output-tokens, som vanligvis er 300–400% dyrere.

## Slik sparer du

![Slik sparer du: Skriv systemprompten og faste instruksjoner på engelsk; la bare brukerens input være på norsk.; Be om mellomst](/tokens-norsk-gpt-slik-sparer-du-no.jpg)

- Skriv systemprompten og faste instruksjoner på engelsk; la bare brukerens input være på norsk.
- Be om mellomsteg (klassifisering, uttrekk, verktøykall) på engelsk eller som JSON, og bare det endelige svaret på norsk.
- Bruk prompt caching for den faste delen av prompten.

## Begrensninger

- Én prompt er målt; for andre tekster kan forholdet variere ±0,1–0,2.
- Claude og Gemini bruker andre tokenizere – tallene gjelder bare OpenAI-modeller.
- Oversettelsen bygger på en gjennomgått maskinoversettelse.

Alle resultater for 41 språk (på engelsk): [sammenligning av 41 språk](/blog/token-cost-by-language)

Alle 41 språk side om side finner du i [språktabellen](/languages).

## Kilder

- [tiktoken: OpenAIs tokenizer (o200k_base) på GitHub](https://github.com/openai/tiktoken)
- [Priser for OpenAI API](https://developers.openai.com/api/docs/pricing)

<!-- autoimg -->
