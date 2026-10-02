Jeg oversatte den samme kundeserviceprompten til 41 språk og talte tokens med o200k_base, OpenAIs nåværende tokenizer (GPT-4o og nyere). Engelsk trenger 34 tokens, norsk **45 – altså 1,32× så mange**, plass 13 av 41 (1 = billigst).

Den norske versjonen:

> Oppsummer kundens e-post nedenfor i tre punkter, og foreslå et høflig svar. Kunden sier at bestillingen kom to dager for sent, og at det manglet en vare i esken.

## Resultater

| Språk | Tokens | Sammenlignet med engelsk | Spart hvis sendt på engelsk |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| **Norsk** | **45** | **1,32×** | **24%** |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Resultater](/blog-language-tax-chart-v4.png)

## Hvorfor

Tokenizeren lærer mest av engelsk tekst: ord som " polite" eller " customer" er ett token, mens mange norske ord – særlig sammensatte ord – deles opp:

- bestillingen → `best | ill | ingen` · 3
- høflig → `hø | fl | ig` · 3
- Oppsummer → `Opp | summer` · 2

## Bytt til engelsk med én knapp

Den største besparelsen får du ved å sende prompten på engelsk: omtrent 24 % færre tokens for norsk. Dagens modeller forstår engelske instruksjoner svært godt og svarer på norsk hvis du ber om det. I TokenSaves token-teller limer du inn prompten og trykker på **💸 Spar tokens**: den rydder opp i mellomrom, oversetter til engelsk, fjerner fyllord og legger til "Reply in Norwegian." slik at svaret blir på ditt språk. Den bruker oversetteren som er innebygd i Chrome 138+ / Edge 148+ på datamaskin; oversettelsen skjer på din egen enhet, og teksten lastes aldri opp. Trykk på **↩ Original** for å få tilbake originalen.

## I penger

Med en modell til 2 $ per million input-tokens koster det 68 $ på engelsk og 90 $ på norsk å sende prompten én million ganger. Svarer modellen også på norsk, gjelder den samme faktoren for output-tokens, som vanligvis er 4–5× dyrere.

## Slik sparer du

- Skriv systemprompten og faste instruksjoner på engelsk; la bare brukerens input være på norsk.
- Be om mellomsteg (klassifisering, uttrekk, verktøykall) på engelsk eller som JSON, og bare det endelige svaret på norsk.
- Bruk prompt caching for den faste delen av prompten.

## Begrensninger

- Én prompt er målt; for andre tekster kan forholdet variere ±0,1–0,2.
- Claude og Gemini bruker andre tokenizere – tallene gjelder bare OpenAI-modeller.
- Oversettelsen bygger på en gjennomgått maskinoversettelse.

Alle resultater for 41 språk (på engelsk): [sammenligning av 41 språk](/blog/token-cost-by-language)
