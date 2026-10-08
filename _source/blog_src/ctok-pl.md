![Limit Claude: ile tokenów daje Claude Pro i Max? (pomiary)](/limity-claude-pro-max-pl.jpg)

Anthropic nie podaje, ile tokenów zawierają Claude Pro i Max. Limit Claude opisuje jako wielokrotność planu Pro („5× Pro”, „20× Pro”) z limitem 5-godzinnym i tygodniowym, nigdy jako liczbę tokenów. Ludzie to jednak zmierzyli. Poniżej sprawdzisz, jak wyglądają Claude Pro limity i ile tokenów daje Claude Max, dlaczego te liczby są tak duże i jak przełożyć je na coś przydatnego: ile Twoje użycie kosztowałoby w API.

**Krótko:** według pomiarów z września 2026 w Claude Code na Opus 5 plan Max 5× daje ok. 39 mln tokenów na 5-godzinne okno, Max 20× ok. 1,9 mld tokenów tygodniowo, a Pro – według szacunku – ok. 8 mln tokenów na okno.

## Ile tokenów daje Claude Max i Claude Pro?

![Ile tokenów daje Claude Max i Claude Pro?: Plan, Cena, Na 5-godzinne okno, Na tydzień](/limity-claude-pro-max-ile-tokenow-daje-claude-max-i-claude-pro-pl.jpg)

Pomiary w Claude Code z września 2026, na modelu Claude Opus 5:

| Plan | Cena | Na 5-godzinne okno | Na tydzień |
|---|---|---|---|
| Pro | 20 USD | ok. 8 mln tokenów *(szacunek)* | ok. 95 mln *(szacunek)* |
| Max 5× | 100 USD | **ok. 39 mln tokenów** (mediana) | co najmniej 1,3 mld |
| Max 20× | 200 USD | ok. 155 mln *(szacunek)* | **ok. 1,9 mld tokenów** |

Wartości **pogrubione** zmierzył [FinOps LLM](https://finopsllm.com/research/claude-pro-max-tokens-limit), który rejestrował sesje Claude Code jednego intensywnego użytkownika, aż zatrzymywały go limity: limit 5-godzinny w Max 5× dwanaście razy, a limit tygodniowy w Max 20× dwa razy. Pozostałe wartości to nasze szacunki, przeskalowane z tych pomiarów według mnożników samego Anthropic (Max 5× = 5× Pro, Max 20× = 20× Pro). Traktuj je jako rząd wielkości, a nie gwarancję.

W Polsce za Claude płaci się w dolarach z 23% VAT: Pro to ok. 92,59 zł, Max 5× ok. 462,96 zł, a Max 20× ok. 925,92 zł miesięcznie (po kursie NBP z 16 września 2026), do czego bank lub karta zwykle doliczają 3–6% za przewalutowanie. Szczegóły w tekście [ceny subskrypcji AI w Polsce](/pl/blog/ceny-subskrypcji-ai).

## Dlaczego te liczby są tak duże?

Bo prawie wszystko to tanie odczyty z cache, a nie nowy tekst. Trzydzieści dziewięć milionów tokenów w pięć godzin brzmi jak ogrom tekstu, ale nim nie jest. W zmierzonych sesjach **96% tokenów stanowiły odczyty z cache**: Claude Code na każdym kroku zadania ponownie czyta swój kontekst (Twoje pliki, dotychczasową rozmowę, wyniki narzędzi). Tylko około 0,6% tokenów to wyjście, czyli to, co Claude faktycznie napisał.

Odczyty z cache są w API tanie – około jednej dziesiątej zwykłej ceny wejścia – więc limity Anthropic najwyraźniej nie liczą każdego tokena tak samo. Działają raczej jak **budżet kosztowy**. Mediana okna Max 5× odpowiadała mniej więcej **37 USD użycia API**, co w tej samej skali daje ok. 7 USD na okno Pro i ok. 150 USD na okno Max 20×.

Dlatego sama liczba tokenów mówi mniej, niż mogłoby się wydawać. Dwie sesje z tą samą liczbą tokenów mogą zużyć zupełnie inną część limitu, zależnie od tego, ile jest w nich świeżego wejścia i wyjścia oraz jakiego modelu używasz.

## Co najszybciej zużywa limit Claude?

![Co najszybciej zużywa limit Claude?: Opus zamiast Sonnet. Opus 5.5 kosztuje w API dwa razy więcej za token niż Sonnet 5.5 i szybciej zużywa też lim](/limity-claude-pro-max-co-najszybciej-zuzywa-limit-claude-pl.jpg)

- **Opus zamiast Sonnet.** Opus 5.5 kosztuje w API dwa razy więcej za token niż Sonnet 5.5 i szybciej zużywa też limit planu.
- **Długie sesje.** Każdy krok wysyła ponownie cały kontekst. Sesja, która urosła do 150 000 tokenów, kosztuje na krok dużo więcej niż świeża. Używaj **/clear** między niepowiązanymi zadaniami i **/compact** przy długich.
- **Duży CLAUDE.md albo wiele narzędzi.** Są wysyłane z każdym krokiem.
- **Pisanie w innym języku.** Koreański zużywa około 44% więcej tokenów niż angielski na tę samą treść, japoński około 79% więcej. Polski tekst zużywa około 88% więcej tokenów niż angielski ([pomiar](/pl/blog/polski-tokeny-gpt)), a Claude liczy polskie teksty na jeszcze więcej tokenów niż modele OpenAI. Jak to ograniczyć: [jak skrócić prompt po polsku](/pl/blog/jak-skrocic-prompt-po-polsku).

## Ile to wiadomości?

Anthropic nie publikuje liczby wiadomości także dla Claude Code. Szacunki społeczności mówią o mniej więcej **90 promptach na 5-godzinne okno w Sonnet** w planie Pro, po tym jak w maju 2026 Anthropic podwoił limity 5-godzinne, oraz o **200 do 900 promptach** na okno w Max 20×, mocno zależnie od wielkości zadania ([źródło](https://fast.io/resources/claude-code-usage-limits-guide/)). Aplikacja Claude i Claude Code dzielą ten sam limit. Więcej o tym w tekście [limity Claude Code](/pl/blog/limity-claude-code).

## Czy Claude ma limit dzienny?

Nie, limitu dziennego nie ma. Masz ruchome 5-godzinne okno, które zaczyna się od Twojej pierwszej wiadomości, a do tego limit tygodniowy. Jeśli dobijasz do limitu tygodniowego, jedynym rozwiązaniem poza wyższym planem jest równiejsze rozłożenie ciężkiej pracy na cały tydzień.

## Czy subskrypcja Claude jest tańsza niż API?

Prawie na pewno tak, jeśli intensywnie korzystasz z Claude Code: tydzień w Max 20× zmierzony na ok. 1,9 mld tokenów to przy cenach API mniej więcej 1800 USD za ten sam miks modeli i odczytów z cache, wobec 200 USD miesięcznie za plan. Przy lżejszym użyciu odpowiedź może być odwrotna. Wpisz wielkość swoich zadań i ich liczbę dziennie w [kalkulator kosztów agentów kodujących](/pl/agents), a dla czatu użyj [kalkulatora subskrypcja vs API](/pl/plans).

Powiązane: [Claude Max vs Pro](/blog/claude-max-vs-pro) (po angielsku) · [limity Claude Code](/pl/blog/limity-claude-code) · [limity Codex](/pl/blog/limity-codex) · [jak oszczędzać tokeny w Claude Code](/blog/claude-code-save-tokens) (po angielsku) · [licznik tokenów Claude](/claude-token-counter) · [licznik tokenów po polsku](/pl/)

*Anthropic często zmienia limity i nie publikuje limitów tokenów. Wpisz **/status** w Claude Code, żeby sprawdzić, ile Ci zostało. Polskie ceny wg [SSD Nodes](https://www.ssdnodes.com/learn/lang/pl/claude-plans-in-poland-what-you-pay) (kurs NBP z 16 września 2026), podatek tokenowy wg [Promptowy](https://promptowy.com/podatek-tokenowy-2026-polski-tekst-osiem-modeli/).*
<!-- autoimg -->
