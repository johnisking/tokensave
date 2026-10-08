![Najtańsze API AI 2026: cennik API i koszt 1 mln tokenów](/najtansze-api-ai-pl.jpg)

Jeśli liczy się tylko najniższy rachunek, najtańsze API AI w październiku 2026 to **GPT-5 nano**, a za nim **GPT-6 Luna** i **Qwen 3.8 Flash**. Najtańszy model rzadko jednak nadaje się do każdego zadania. Poniżej cennik API wszystkich głównych modeli ułożony według kosztu prawdziwego zapytania, koszt 1 mln tokenów na wejściu i wyjściu, tanie modele, których warto używać, oraz sytuacje, w których droższy model wychodzi taniej.

**Krótko:** najtańszym API AI jest GPT-5 nano (0,05 / 0,40 USD za 1 mln tokenów wejściowych / wyjściowych, ok. 3 USD za 10 000 typowych zapytań), ale na start lepiej wypróbować GPT-6 Luna, która kosztuje niewiele więcej.

## Jak porównaliśmy ceny?

Porównaliśmy koszt jednego typowego zapytania, a nie samą cenę za milion tokenów, bo ta bywa myląca z dwóch powodów:

- **Wyjście kosztuje od 200 do 700% więcej niż wejście** w większości modeli, więc model z tanim wejściem i drogim wyjściem może przegrać z modelem odwrotnym.
- **Tokenizery się różnią.** Ten sam angielski tekst to w Claude Opus i Sonnet około 30% więcej tokenów niż w GPT, a w Gemini około 5% mniej. Model Claude za „2 USD za milion” kosztuje więc więcej na zapytanie niż model GPT za „2 USD za milion”.

Dlatego wyceniliśmy jedno typowe zapytanie: **2000 tokenów wejściowych i 500 wyjściowych po angielsku**, policzonych tak, jak policzyłby je tokenizer danego modelu, według oficjalnych cenników sprawdzonych 1 października 2026. Bez cache'owania i rabatów za batch.

## Najtańsze API AI – cennik i koszt 1 mln tokenów

![Najtańsze API AI – cennik i koszt 1 mln tokenów: Model, Firma, Wejście / wyjście za 1 mln (USD), 1 zapytanie (USD), 10 000 zapytań (USD)](/najtansze-api-ai-najtansze-api-ai-cennik-i-koszt-1-mln-to-pl.jpg)

| Model | Firma | Wejście / wyjście za 1 mln (USD) | 1 zapytanie (USD) | 10 000 zapytań (USD) |
|---|---|---|---:|---:|
| GPT-5 nano | OpenAI | 0,05 / 0,40 | 0,00030 | 3,00 |
| GPT-6 Luna | OpenAI | 0,10 / 0,50 | 0,00045 | 4,50 |
| Qwen 3.8 Flash | Qwen | 0,15 / 0,47 | 0,00053 | 5,35 |
| GPT-4o mini | OpenAI | 0,15 / 0,60 | 0,00060 | 6,00 |
| Mistral Small | Mistral | 0,15 / 0,60 | 0,00063 | 6,30 |
| Gemini 3.1 Flash-Lite | Google | 0,25 / 1,50 | 0,00119 | 11,88 |
| DeepSeek V4.1 Flash (szczyt) | DeepSeek | 0,30 / 1,20 | 0,00120 | 12,00 |
| GPT-5 mini | OpenAI | 0,25 / 2,00 | 0,00150 | 15,00 |
| GPT-4.1 mini | OpenAI | 0,40 / 1,60 | 0,00160 | 16,00 |
| Gemini 3.5 Flash-Lite | Google | 0,30 / 2,50 | 0,00176 | 17,57 |
| Mistral Large 3 | Mistral | 0,50 / 1,50 | 0,00184 | 18,38 |

Dla porównania te same 10 000 zapytań kosztuje **90 USD** w GPT-6 Sol, **117 USD** w Claude Sonnet 5.5, **234 USD** w Claude Opus 5.5 i **450 USD** w GPT-6 Astra. Najtańszy model z tabeli kosztuje mniej niż 1% tego, co GPT-6 Astra.

Ceny są w dolarach. Przy płatnościach w dolarach z polskiej karty bank lub karta zwykle doliczają 3–6% za przewalutowanie, a przy subskrypcjach Claude osoby prywatne płacą do tego 23% VAT – szczegóły w tekście [ceny subskrypcji AI w Polsce](/pl/blog/ceny-subskrypcji-ai).

## Który tani model wybrać?

![Który tani model wybrać?: GPT-6 Luna warto wypróbować jako pierwszy. To najnowszy mały model OpenAI (wrzesień 2026), droższy od GPT-5 na](/najtansze-api-ai-ktory-tani-model-wybrac-pl.jpg)

Na start wybierz GPT-6 Luna, a do najprostszych zadań na masową skalę – GPT-5 nano.

- **GPT-6 Luna** warto wypróbować jako pierwszy. To najnowszy mały model OpenAI (wrzesień 2026), droższy od GPT-5 nano tylko o 1,50 USD na 10 000 zapytań. Dobry do klasyfikacji, wyciągania danych, routingu, krótkich odpowiedzi i streszczeń.
- **GPT-5 nano** do najprostszej pracy na największą skalę, gdzie liczy się każdy ułamek centa: tagowanie, sprawdzanie tak/nie, filtrowanie spamu.
- **Qwen 3.8 Flash** i **Mistral Small** to najtańsze opcje spoza OpenAI – przydatne, jeśli chcesz mieć drugiego dostawcę albo modele open-weight, które później możesz hostować sam.
- **Gemini 3.1 Flash-Lite** i **DeepSeek V4.1 Flash** kosztują mniej więcej o 100% więcej niż Luna, ale są o krok lepsze w pisaniu i rozumowaniu, a i tak wychodzą o około 87% taniej na zapytanie niż GPT-6 Sol. DeepSeek V4.1 Flash poza godzinami szczytu kosztuje połowę (0,15 / 0,60 USD), co stawia go tuż za GPT-6 Luna; zobacz [cennik DeepSeek V4.1 Flash](/blog/deepseek-v4-1-flash-api-pricing) (po angielsku). O darmowym dostępie do Gemini piszę w tekście [Gemini za darmo: Flash-Lite](/pl/blog/gemini-za-darmo-flash-lite).
- **Claude Haiku 5.5** to najtańszy model Claude: 0,10 / 0,50 USD za milion tokenów przy promptach do 100 000 tokenów (powyżej drożej), czyli około 0,00059 USD za zapytanie – mniej więcej o 30% więcej niż Luna. Starszy Claude Haiku 4.5 (1 / 5 USD) kosztuje 0,0047 USD za zapytanie. Wybierz Haiku, gdy potrzebujesz konkretnie zachowania Claude.

## Kiedy najtańszy model kosztuje więcej?

Wtedy, gdy się myli: tani model, który zawodzi, kosztuje Cię dwa razy – raz za złą odpowiedź i drugi raz za ponowienie w lepszym modelu, plus Twój czas. Dwa sposoby oszczędzają więcej niż wybieranie wszędzie najtańszego modelu:

1. **Kieruj zapytania według trudności.** Wysyłaj wszystko najpierw do małego modelu, a do GPT-6 Sol, Claude Sonnet lub Gemini 3.1 Pro przekazuj tylko zapytania, z którymi sobie nie poradził (albo które oznaczysz jako trudne). Jeśli 80% zapytań zostaje w GPT-6 Luna, a 20% idzie do GPT-6 Sol, średni koszt spada o około 75% w porównaniu z wysyłaniem wszystkiego do Sol.
2. **Tnij tokeny, nie tylko cenę.** Prompt caching u większości dostawców nalicza powtarzane instrukcje i dokumenty po około jednej dziesiątej ceny wejścia, a API batch bierze mniej więcej połowę ceny za zadania, które mogą poczekać. Zobacz [prompt caching](/blog/prompt-caching-explained) i [API batch za pół ceny](/blog/batch-api-half-price) (po angielsku) oraz [jak skrócić prompt po polsku](/pl/blog/jak-skrocic-prompt-po-polsku).

## Czy język zmienia ranking najtańszych API?

Ranking zostaje ten sam, ale rachunek rośnie. Wszystkie koszty powyżej dotyczą angielskiego, a inne języki zużywają więcej tokenów na tę samą treść: w GPT koreański około 44% więcej, a japoński około 79% więcej, więc każda cena w tabeli rośnie o tyle samo. **Polski tekst zużywa około 88% więcej tokenów niż angielski** ([pomiar](/pl/blog/polski-tokeny-gpt)), a Claude liczy polskie teksty na jeszcze więcej tokenów niż modele OpenAI. Zobacz też [ten sam prompt w 41 językach](/blog/token-cost-by-language) (po angielsku) i [ile kosztuje prompt po polsku](/pl/blog/ile-kosztuje-prompt-po-polsku).

## Jak sprawdzić koszt własnego promptu?

Wklej prawdziwy prompt do [licznika tokenów](/pl/), a zobaczysz jego dokładną liczbę tokenów i koszt w każdym modelu. Możesz też otworzyć licznik dla [OpenAI](/openai-token-counter), [Claude](/claude-token-counter) lub [Gemini](/gemini-token-counter). Pełne zestawienie możliwości i ceny znajdziesz w porównaniu [możliwości modeli AI a cena](/compare/performance).

*Ceny według oficjalnych cenników, sprawdzone 1 października 2026. Polska prowizja za przewalutowanie i VAT wg [SSD Nodes](https://www.ssdnodes.com/learn/lang/pl/claude-plans-in-poland-what-you-pay), podatek tokenowy wg [Promptowy](https://promptowy.com/podatek-tokenowy-2026-polski-tekst-osiem-modeli/). Ceny często się zmieniają – przed wyborem modelu sprawdź cennik dostawcy.*

## Źródła

- [Cennik API OpenAI](https://developers.openai.com/api/docs/pricing)
- [OpenAI: model GPT-5 nano](https://developers.openai.com/api/docs/models/gpt-5-nano)
- [Alibaba Cloud: cena qwen3.8-flash](https://www.alibabacloud.com/help/en/model-studio/qwen3-8-flash)
- [Mistral AI: Mistral Large 3](https://docs.mistral.ai/models/mistral-large-3-25-12)
- [Cennik API Gemini](https://ai.google.dev/gemini-api/docs/pricing)
- [Modele i cennik API DeepSeek](https://api-docs.deepseek.com/quick_start/pricing/)
- [Cennik API Claude](https://platform.claude.com/docs/en/about-claude/pricing)
<!-- autoimg -->
