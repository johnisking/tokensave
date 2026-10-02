Jag översatte samma kundtjänstprompt till 41 språk och räknade tokens med o200k_base, OpenAI:s nuvarande tokenizer (GPT-4o och senare). Engelska behöver 34 tokens, svenska **45 — 1,32× så många**, plats 12 av 41 (1 = billigast).

Den svenska versionen:

> Sammanfatta kundens e-post nedan i tre punkter och föreslå ett artigt svar. Kunden säger att beställningen kom två dagar för sent och att en vara saknades i lådan.

## Resultat

| Språk | Tokens | Jämfört med engelska | Besparing om det skickas på engelska |
|---|---:|---:|---:|
| English | 34 | 1,00× | – |
| 简体中文 | 35 | 1,03× | 3% |
| Español | 40 | 1,18× | 15% |
| Deutsch | 43 | 1,26× | 21% |
| **Svenska** | **45** | **1,32×** | **24%** |
| 한국어 | 49 | 1,44× | 31% |
| हिन्दी | 51 | 1,50× | 33% |
| 日本語 | 61 | 1,79× | 44% |
| Čeština | 68 | 2,00× | 50% |
| Ελληνικά | 70 | 2,06× | 51% |
| ਪੰਜਾਬੀ | 83 | 2,44× | 59% |

![Resultat](/blog-language-tax-chart-v4.png)

## Varför

Tokenizern lär sig mest från engelsk text: ord som " polite" eller " customer" är en enda token, medan många svenska ord – särskilt sammansättningar – delas upp:

- Sammanfatta → `Sam | man | f | atta` · 4
- beställningen → `best | äll | ningen` · 3
- saknades → `sak | n | ades` · 3

## Byt till engelska med en knapp

Den största besparingen får du genom att skicka prompten på engelska: cirka 24 % färre tokens för svenska. Dagens modeller förstår engelska instruktioner utmärkt och svarar på svenska om du ber om det. I TokenSaves tokenräknare klistrar du in prompten och trycker på **💸 Spara tokens**: den rensar mellanslag, översätter till engelska, stryker utfyllnad och lägger till "Reply in Swedish." så att svaret kommer på ditt språk. Den använder översättaren som är inbyggd i Chrome 138+ / Edge 148+ på dator; översättningen sker på din egen enhet och texten laddas aldrig upp. Tryck på **↩ Original** för att få tillbaka originalet.

## I pengar

Med en modell för 2 $ per miljon input-tokens kostar det 68 $ på engelska och 90 $ på svenska att skicka prompten en miljon gånger. Svarar modellen också på svenska gäller samma faktor för output-tokens, som oftast är 4–5× dyrare.

## Så sparar du

- Skriv systemprompten och fasta instruktioner på engelska; låt bara användarens input vara på svenska.
- Be om mellansteg (klassificering, extraktion, verktygsanrop) på engelska eller som JSON, och bara slutsvaret på svenska.
- Använd prompt caching för den fasta delen av prompten.

## Begränsningar

- En enda prompt mättes; för andra texter kan kvoten skilja ±0,1–0,2.
- Claude och Gemini har andra tokenizers – siffrorna gäller bara OpenAI-modeller.
- Översättningen bygger på en granskad maskinöversättning.

Alla resultat för 41 språk (på engelska): [jämförelse av 41 språk](/blog/token-cost-by-language)
