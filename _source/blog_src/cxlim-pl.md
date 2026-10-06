Codex, agent kodujący OpenAI, jest wliczony w plany ChatGPT Plus, Pro i Business i to właśnie na nim większość osób najczęściej trafia na limity. Codex limity dzieli z ChatGPT Work, korzysta z okna 5-godzinnego i limitu tygodniowego, a tempo ich zużycia bardzo zależy od wybranego modelu. Poniżej wyjaśniam, jak to działa, ile daje Codex limit Plus i jak wycisnąć z niego więcej.

**Krótko:** Codex ma dwa limity naraz – kroczące okno 5-godzinne i limit tygodniowy, wspólne z ChatGPT Work – a w planie Plus daje szacunkowo od ok. 5–45 wiadomości na 5 godzin (GPT-6 Astra) do ok. 250–2000 (GPT-5.6 Luna), zależnie od modelu.

## Które plany obejmują Codex?

Użycie Codex (i ChatGPT Work) jest wliczone w plany **Plus** (20 USD), **Pro** (100, 200 lub 500 USD) oraz stanowiska **Business** Standard i Premium. Użycie nie jest nielimitowane: każdy plan dostaje pulę, mierzoną w dwóch oknach czasowych. Polskie ceny tych planów znajdziesz w artykułach [Ceny subskrypcji AI w Polsce](/pl/blog/ceny-subskrypcji-ai) i [ChatGPT Pro za 100, 200 i 500 USD](/pl/blog/chatgpt-pro-100-200-500).

## Jakie limity ma Codex?

Dwa jednocześnie: okno 5-godzinne i limit tygodniowy.

**Okno 5-godzinne.** Krocząca pula, która zaczyna się od Twojego pierwszego zapytania. Gdy ją wyczerpiesz, czekasz na reset okna. OpenAI przywróciło okno 5-godzinne w planie Plus pod koniec sierpnia 2026 roku; zapowiedziało wtedy, że Pro 100 i Pro 200 nie będą go miały przez najbliższe miesiące.

**Limit tygodniowy.** Do tego dochodzi kroczący, siedmiodniowy limit. Gdy go osiągniesz, czekasz na reset tygodniowy, nawet jeśli okno 5-godzinne jest jeszcze świeże.

Codex i ChatGPT Work korzystają z **tej samej puli**.

## Ile daje Codex limit Plus i Pro?

Centrum pomocy OpenAI podaje szacunkową liczbę wiadomości na jedno okno 5-godzinne. Wybrany model zmienia ją ogromnie:

| Model | Plus | Pro (poziom 5×) |
|---|---|---|
| GPT-6 Astra | ok. 5–45 | ok. 25–225 |
| GPT-5.6 Sol | ok. 10–100 | ok. 50–500 |
| GPT-5.6 Terra | ok. 25–200 | ok. 125–1000 |
| GPT-5.6 Luna | ok. 250–2000 | ok. 1250–10 000 |

Dolna granica każdego przedziału to długie, wieloetapowe zadania na dużej bazie kodu; górna – krótkie, proste prośby. Wyższe poziomy Pro skalują się w górę: Pro 200 daje 10× Plus dla nowych subskrybentów od 29 września 2026 roku, a Pro 500 – 25×.

**Ultrafast**, dostępny tylko w Pro 500, to szybszy tryb, który szybciej zużywa wliczone użycie i kredyty.

## Dlaczego Codex tak szybko zużywa limit?

Jak każdy agent kodujący, Codex pracuje krokami i przy każdym kroku wysyła do modelu cały kontekst roboczy: instrukcje, definicje narzędzi, przeczytane pliki i wcześniejsze kroki. Typowe zadanie polegające na dodaniu funkcji, liczące 25 kroków, wysyła ok. 1,6 mln tokenów wejściowych. Przez API takie zadanie kosztowałoby ok. 0,72 USD na modelu klasy Sol i ok. 3,60 USD na GPT-6 Astra – dlatego pula dla Astry jest o tyle mniejsza. Zobacz [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost) (po angielsku) albo policz to sam w [kalkulatorze kosztów agentów kodujących](/pl/agents).

## Jak sprawdzić zużycie?

Centrum pomocy OpenAI wskazuje **Ustawienia → Użycie** (Settings → Usage) w ChatGPT, gdzie widać pozostałą pulę i godziny resetu. Codex ostrzega też, gdy zbliżasz się do limitu.

## Co zrobić, gdy trafisz na limit?

1. **Poczekaj na reset.** Okno 5-godzinne odnawia się w ciągu kilku godzin.
2. **Użyj zachowanego resetu albo kup natychmiastowy reset** – dostępne na uprawnionych kontach Plus i Pro.
3. **Skorzystaj z kredytów**, żeby pracować dalej w planach, które je obsługują.
4. **Przejdź na wyższy poziom** Pro.
5. **Użyj klucza API** z rozliczeniem pay-as-you-go do pracy ponad limit. Ceny API różnych modeli porównuję w artykule [Najtańsze API AI](/pl/blog/najtansze-api-ai).

## Jak wydłużyć limit Codex?

- **Domyślnie używaj GPT-5.6 Sol lub Terra.** GPT-6 Astra zostaw na trudne problemy, w których widać różnicę: zużywa kilkukrotnie więcej puli.
- **Do prostych zmian używaj Luny** – zmian nazw i powtarzalnego kodu.
- **Dawaj małe, konkretne zadania.** Mniej kroków to mniej ponownie wysyłanego kontekstu.
- **Zaczynaj od nowa między niepowiązanymi zadaniami**, żeby nie ciągnąć starej historii.
- **Wskazuj Codexowi właściwe pliki**, zamiast pozwalać mu przeszukiwać całe repozytorium.
- **Trzymaj plik instrukcji krótko** i pisz go po angielsku, jeśli na co dzień używasz innego języka: w tokenizerze GPT koreański zajmuje ok. 44% więcej tokenów niż angielski, a japoński ok. 79% więcej. Jak wypada polski, opisuję w artykule [Ile tokenów zajmuje polski w GPT](/pl/blog/polski-tokeny-gpt), a swój tekst sprawdzisz w [liczniku tokenów](/pl/).

Wiele z tych nawyków sprawdza się też w Claude Code: zobacz [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (po angielsku) oraz [Limity Claude Code](/pl/blog/limity-claude-code).

## Codex czy Claude Code?

Oba są wliczone w plany za 20, 100 i 200 USD i mają podobne systemy limitów. Różnice omawia porównanie [ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max) (po angielsku), a [kalkulator kosztów agentów kodujących](/pl/agents) zestawia miesięczne koszty API z każdym planem. Same plany porównasz w [kalkulatorze planów](/pl/plans).

*Limity często się zmieniają. Aktualne liczby znajdziesz na stronie pomocy OpenAI [o użyciu Codex i Work](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex).*
