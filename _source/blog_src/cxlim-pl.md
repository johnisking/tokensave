![Codex limity: okno 5 godzin, limit tygodniowy i Codex limit Plus](/limity-codex-pl.jpg)

Codex, agent kodujący OpenAI, jest wliczony w plany ChatGPT Plus, Pro i Business i to właśnie na nim większość osób najczęściej trafia na limity. Codex limity dzieli z ChatGPT Work, w planach Plus i Business korzysta z okna 5-godzinnego (mogą też obowiązywać limity tygodniowe), a tempo zużycia bardzo zależy od wybranego modelu. Poniżej wyjaśniam, jak to działa, ile daje Codex limit Plus i jak wycisnąć z niego więcej.

**Krótko:** Codex w planach Plus i Business ma kroczące okno 5-godzinne, wspólne z ChatGPT Work, i mogą też obowiązywać limity tygodniowe; Pro nie ma obecnie limitu 5-godzinnego. W planie Plus Codex daje szacunkowo od ok. 5–45 wiadomości na 5 godzin (GPT-6 Astra) do ok. 350–3000 (GPT-6 Luna), zależnie od modelu.

## Które plany obejmują Codex?

Użycie Codex (i ChatGPT Work) jest wliczone w plany **Plus** (20 USD), **Pro** (100, 200 lub 500 USD) oraz stanowiska **Business** Standard i Premium. Użycie nie jest nielimitowane: każdy plan dostaje wliczoną pulę. Polskie ceny tych planów znajdziesz w artykułach [Ceny subskrypcji AI w Polsce](/pl/blog/ceny-subskrypcji-ai) i [ChatGPT Pro za 100, 200 i 500 USD](/pl/blog/chatgpt-pro-100-200-500).

## Jakie limity ma Codex?

W planach Plus i Business okno 5-godzinne, a do tego mogą obowiązywać limity tygodniowe.

**Okno 5-godzinne.** Krocząca pula, która zaczyna się od Twojego pierwszego zapytania. Gdy ją wyczerpiesz, czekasz na reset okna. Pro 100, Pro 200 i Pro 500 nie mają obecnie limitu 5-godzinnego w Work i Codex; nadal mają wliczoną pulę.

**Limit tygodniowy.** Według OpenAI do tego mogą dochodzić limity tygodniowe. Gdy osiągniesz taki limit, czekasz na jego reset, nawet jeśli okno 5-godzinne jest jeszcze świeże.

Codex i ChatGPT Work korzystają z **tej samej puli**.

## Ile daje Codex limit Plus i Pro?

![Ile daje Codex limit Plus i Pro?: Model, Plus, Business (Standard)](/limity-codex-ile-daje-codex-limit-plus-i-pro-pl.jpg)

Centrum pomocy OpenAI podaje szacunkową liczbę lokalnych wiadomości na jedno okno 5-godzinne dla planów Plus i Business Standard. Wybrany model zmienia ją ogromnie:

| Model | Plus | Business (Standard) |
|---|---|---|
| GPT-6 Astra | ok. 5–45 | ok. 5–45 |
| GPT-6.1 Sol | ok. 15–160 | ok. 15–160 |
| GPT-6 Sol | ok. 15–150 | ok. 15–150 |
| GPT-6 Luna | ok. 350–3000 | ok. 350–3000 |

Dolna granica każdego przedziału to długie, wieloetapowe zadania na dużej bazie kodu; górna – krótkie, proste prośby. Plany Pro nie mają obecnie okna 5-godzinnego, ale mają większą wliczoną pulę: Pro 100 daje 5× Plus, Pro 200 – 10× Plus dla nowych subskrybentów (kto miał aktywną subskrypcję Pro 200 między 22 a 29 września 2026 roku, zachowuje poprzedni limit do 29 października), a Pro 500 – 25× Plus. Te mnożniki nie pochodzą ze strony cennika OpenAI, tylko z wpisu Thibaulta Sottiaux (OpenAI) na X i doniesień prasowych (WinBuzzer, Windows Report).

**Ultrafast**, dostępny tylko w Pro 500, to szybszy tryb, który szybciej zużywa wliczone użycie i kredyty.

## Dlaczego Codex tak szybko zużywa limit?

Jak każdy agent kodujący, Codex pracuje krokami i przy każdym kroku wysyła do modelu cały kontekst roboczy: instrukcje, definicje narzędzi, przeczytane pliki i wcześniejsze kroki. Typowe zadanie polegające na dodaniu funkcji, liczące 25 kroków, wysyła ok. 1,6 mln tokenów wejściowych. Przez API takie zadanie kosztowałoby ok. 0,72 USD na modelu klasy Sol i ok. 3,60 USD na GPT-6 Astra – dlatego pula dla Astry jest o tyle mniejsza. Zobacz [What does an AI coding agent cost per task?](/blog/ai-coding-agent-cost) (po angielsku) albo policz to sam w [kalkulatorze kosztów agentów kodujących](/pl/agents).

## Jak sprawdzić zużycie?

Centrum pomocy OpenAI wskazuje **Ustawienia → Użycie** (Settings → Usage) w ChatGPT, gdzie widać pozostałą pulę i godziny resetu. Codex ostrzega też, gdy zbliżasz się do limitu.

## Co zrobić, gdy trafisz na limit?

![Co zrobić, gdy trafisz na limit?: Poczekaj na reset. Okno 5-godzinne odnawia się w ciągu kilku godzin.; Użyj zachowanego resetu albo kup natychm](/limity-codex-co-zrobic-gdy-trafisz-na-limit-pl.jpg)

1. **Poczekaj na reset.** Okno 5-godzinne odnawia się w ciągu kilku godzin.
2. **Użyj zachowanego resetu albo kup natychmiastowy reset** – dostępne na uprawnionych kontach Plus i Pro.
3. **Skorzystaj z kredytów**, żeby pracować dalej w planach, które je obsługują.
4. **Przejdź na wyższy poziom** Pro.
5. **Użyj klucza API** z rozliczeniem pay-as-you-go do pracy ponad limit. Ceny API różnych modeli porównuję w artykule [Najtańsze API AI](/pl/blog/najtansze-api-ai).

## Jak wydłużyć limit Codex?

![Jak wydłużyć limit Codex?: Domyślnie używaj GPT-6.1 Sol lub GPT-6 Sol. GPT-6 Astra zostaw na trudne problemy, w których widać różnicę; Do pro](/limity-codex-jak-wyduzyc-limit-codex-pl.jpg)

- **Domyślnie używaj GPT-6.1 Sol lub GPT-6 Sol.** GPT-6 Astra zostaw na trudne problemy, w których widać różnicę: zużywa kilkukrotnie więcej puli.
- **Do prostych zmian używaj Luny** – zmian nazw i powtarzalnego kodu.
- **Dawaj małe, konkretne zadania.** Mniej kroków to mniej ponownie wysyłanego kontekstu.
- **Zaczynaj od nowa między niepowiązanymi zadaniami**, żeby nie ciągnąć starej historii.
- **Wskazuj Codexowi właściwe pliki**, zamiast pozwalać mu przeszukiwać całe repozytorium.
- **Trzymaj plik instrukcji krótko** i pisz go po angielsku, jeśli na co dzień używasz innego języka: w tokenizerze GPT koreański zajmuje ok. 44% więcej tokenów niż angielski, a japoński ok. 79% więcej. Jak wypada polski, opisuję w artykule [Ile tokenów zajmuje polski w GPT](/pl/blog/polski-tokeny-gpt), a swój tekst sprawdzisz w [liczniku tokenów](/pl/).

Wiele z tych nawyków sprawdza się też w Claude Code: zobacz [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (po angielsku) oraz [Limity Claude Code](/pl/blog/limity-claude-code).

## Codex czy Claude Code?

Oba są wliczone w plany za 20, 100 i 200 USD i mają podobne systemy limitów. Różnice omawia porównanie [ChatGPT Pro vs Claude Max](/blog/chatgpt-pro-vs-claude-max) (po angielsku), a [kalkulator kosztów agentów kodujących](/pl/agents) zestawia miesięczne koszty API z każdym planem. Same plany porównasz w [kalkulatorze planów](/pl/plans).

*Limity często się zmieniają. Aktualne liczby znajdziesz na stronie pomocy OpenAI [o użyciu Codex i Work](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex).*

## Źródła

- [Pomoc OpenAI: użycie w Work i Codex](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex)
- [Pomoc OpenAI: zapisane resety Codex](https://help.openai.com/en/articles/20001498-how-banked-codex-resets-work)
- [Plany ChatGPT i ceny Codex](https://learn.chatgpt.com/docs/pricing)
- [Pomoc OpenAI: poziomy ChatGPT Pro](https://help.openai.com/en/articles/9793128-about-chatgpt-pro-tiers)
- [WinBuzzer: OpenAI Adds $500 ChatGPT Pro Plan, Cuts Allowance for New $200 Plan Subscribers](https://winbuzzer.com/2026/09/30/openai-adds-500-chatgpt-pro-cuts-allowance-new-200-subscribers-a005-xcxwbn/)
- [Windows Report: OpenAI Launches $500 ChatGPT Pro 500 Plan With 25x Plus Usage and Ultrafast Access](https://windowsreport.com/?p=1510692)
<!-- autoimg -->
