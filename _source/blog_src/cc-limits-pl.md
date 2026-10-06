Komunikat „Claude usage limit reached” to jeden z najczęstszych i najbardziej mylących komunikatów w Claude Code, bo Claude Code limity działają na dwóch poziomach jednocześnie: jest limit 5 godzin i limit tygodniowy. Poniżej wyjaśniam, jak działają, co zmieniło się w 2026 roku i co zrobić, gdy na któryś trafisz.

**Krótko:** Claude Code ma dwa limity naraz – limit 5 godzin liczony od pierwszej wiadomości i limit tygodniowy – a oba dzieli z aplikacją Claude, więc po wyczerpaniu któregokolwiek trzeba poczekać na reset, włączyć dodatkowe użycie albo przejść na API.

## Jakie limity ma Claude Code?

Dwa: limit sesji (5 godzin) i limit tygodniowy. Działają równolegle, a zablokować cię może każdy z nich.

**1. Limit 5 godzin.** Twoje użycie jest liczone w kroczącym, pięciogodzinnym oknie, które zaczyna się od pierwszej wiadomości. Gdy wyczerpiesz pulę na to okno, musisz poczekać na reset.

**2. Limit tygodniowy.** Ponad limitem sesji obowiązuje też łączny limit użycia w skali tygodnia. Wprowadzono go w sierpniu 2025 roku, żeby niewielka część kont nie uruchamiała Claude Code bez przerwy, całą dobę. Gdy go osiągniesz, czekasz na reset tygodniowy, nawet jeśli Twoje okno 5-godzinne jest jeszcze świeże.

Oba limity są **wspólne dla Claude Code i aplikacji Claude** (web, desktop i mobile). Długa rozmowa w aplikacji zużywa tę samą pulę co sesja programowania.

## Ile użycia daje każdy plan?

Anthropic opisuje limity planów względem siebie, a nie w konkretnej liczbie tokenów:

| Plan | Cena | Użycie |
|---|---|---|
| Pro | 20 USD/mies. | Poziom bazowy |
| Max 5× | 100 USD/mies. | 5× Pro |
| Max 20× | 200 USD/mies. | 20× Pro |

To, na jak długo to wystarczy, mocno zależy od tego, co robisz. Duże pliki, długie sesje i Opus zużywają pulę dużo szybciej niż krótkie zadania na Sonnecie, bo każdy krok wysyła ponownie cały kontekst roboczy. Polskie ceny planów (z VAT) zebrałem w artykule [Ceny subskrypcji AI w Polsce](/pl/blog/ceny-subskrypcji-ai), a limity samych planów Claude opisuję w tekście [Limity Claude Pro i Max](/pl/blog/limity-claude-pro-max).

## Co zmieniło się w 2026 roku?

- **6 maja 2026:** Anthropic **podwoił pięciogodzinne limity Claude Code** w planach Pro, Max, Team i Enterprise opartym na stanowiskach (seat-based), a w Pro i Max zniósł dodatkowe obniżanie limitów w godzinach szczytu.
- **Lato 2026:** obowiązywało tymczasowe **zwiększenie limitów tygodniowych o 50%**.
- **14 września 2026:** Anthropic **na stałe podniósł standardowe limity tygodniowe o 25%** w planach Pro, Max, Team i seat-based Enterprise. Ponieważ zastąpiło to tymczasowe zwiększenie o 50%, limity tygodniowe są ok. 17% niższe niż latem, choć nadal o 25% wyższe niż na początku.

Jeśli więc masz wrażenie, że od połowy września szybciej trafiasz na limit tygodniowy, to nie złudzenie.

## Jak sprawdzić, ile limitu zostało?

W Claude Code polecenie **/status** pokazuje pozostałą pulę. Claude Code ostrzega też, gdy zbliżasz się do limitu. Sprawdzaj to przed rozpoczęciem długiego zadania, a nie w jego połowie.

## Co zrobić, gdy trafisz na limit?

1. **Poczekaj na reset.** Przy limicie 5 godzin to zwykle kwestia kilku godzin.
2. **Włącz dodatkowe użycie (extra usage).** W płatnych planach możesz pracować dalej na kredytach rozliczanych osobno, zamiast się zatrzymywać.
3. **Przejdź na kredyty API.** Claude Code może działać na rozliczeniu API pay-as-you-go; przed przełączeniem prosi o Twoją zgodę.
4. **Zmień plan na wyższy.** Z Pro na Max 5× albo z Max 5× na Max 20×.
5. **Zużywaj mniej tokenów na zadanie.** Często to najtańsze rozwiązanie. Szczegóły poniżej.

## Dlaczego limit kończy się szybciej, niż się spodziewasz?

Najczęściej przez długie sesje i duży kontekst, który wraca do modelu przy każdym kroku.

- **Długie sesje.** Każdy krok wysyła ponownie wszystko, co wydarzyło się wcześniej. Dwugodzinna sesja ciągnie ogromny kontekst do każdego nowego kroku.
- **Opus.** Zużywa pulę szybciej niż Sonnet.
- **Duże pliki i logi.** Odczytanie pliku na 3000 linii albo pełnego logu testów dodaje dziesiątki tysięcy tokenów.
- **Niejasne zadania.** „Uporządkuj projekt” może zająć dziesiątki kroków; „napraw padający test w auth.py” – kilka.
- **Równoczesne korzystanie z aplikacji Claude.** Oba narzędzia czerpią z tej samej puli.

## Jak wydłużyć limity Claude Code?

- Zaczynaj nową sesję (**/clear**) między niepowiązanymi zadaniami, a długą sesję streszczaj poleceniem **/compact**.
- Wskazuj Claude'owi właściwe pliki, zamiast pozwalać mu przeszukiwać projekt.
- Trzymaj instrukcje w CLAUDE.md krótko: są wysyłane przy każdym kroku.
- Używaj Sonneta do rutynowej pracy, a Opusa zostaw na trudne problemy.

Więcej szczegółów i liczb znajdziesz w artykule [How to save tokens in Claude Code](/blog/claude-code-save-tokens) (po angielsku). Ile tokenów zajmuje Twój tekst lub kod, sprawdzisz w [liczniku tokenów](/pl/).

## Plan czy API?

Jeśli regularnie trafiasz na limit tygodniowy, porównaj, ile to dodatkowe użycie kosztowałoby przez API, z ceną wyższego planu. Obliczenia zrobią za Ciebie poradnik [Claude Code cost per month](/blog/claude-code-cost-per-month) (po angielsku) oraz nasz [kalkulator kosztów agentów kodujących](/pl/agents). Plany różnych dostawców porównasz w [kalkulatorze planów](/pl/plans), a limity konkurencyjnego agenta OpenAI opisuję w tekście [Limity Codex](/pl/blog/limity-codex).

*Limity często się zmieniają. Aktualne zasady znajdziesz na stronie pomocy Anthropic [Claude Code w planie Pro lub Max](https://support.claude.com/en/articles/11145838-use-claude-code-with-your-pro-or-max-plan) oraz na [stronie z cennikiem](https://claude.com/pricing).*
