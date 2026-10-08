Polski należy do najdroższych języków w promptach: ten sam tekst zajmuje w GPT prawie dwa razy więcej tokenów niż po angielsku. W dyskusji na forum 4programmers padła dobra uwaga: może to wina samego tekstu, a native speaker napisze go krócej? Sprawdziłem to, razem z kilkoma innymi sposobami na tańszy prompt po polsku.

![Ten sam prompt w różnych wersjach: od 64 do 28 tokenów](/blog-prompt-pl-skracanie.png)

## Test

![Test: Wersja, GPT (o200k), Mistral (Tekken)](/jak-skrocic-prompt-po-polsku-pl-1.jpg)

Prośba o streszczenie e-maila klienta, w siedmiu wersjach. Tokeny liczyłem dwoma tokenizerami: **o200k_base** (GPT-4o i nowsze modele OpenAI) oraz **Tekken** (Mistral).

| Wersja | GPT (o200k) | Mistral (Tekken) |
|---|---:|---:|
| Polski, formalnie | 64 | 58 |
| Polski, krótko | 42 | 41 |
| Polski, styl notatki | **39** | 38 |
| Polski bez polskich znaków | 41 | 42 |
| Angielski | 34 | 34 |
| Angielski, krótko | **28** | 28 |
| Angielski krótko + „Reply in Polish.” | 32 | 32 |

Teksty wyglądały tak:

- **Formalnie:** „Podsumuj poniższy e-mail od klienta w trzech punktach i zaproponuj uprzejmą odpowiedź. Klient twierdzi, że zamówienie dotarło z dwudniowym opóźnieniem, a w paczce brakowało jednego produktu.”
- **Krótko:** „Streść ten mail klienta w 3 punktach i zaproponuj grzeczną odpowiedź. Zamówienie przyszło 2 dni po terminie i brakowało jednego produktu.”
- **Styl notatki:** „Streść mail klienta w 3 punktach, zaproponuj grzeczną odpowiedź. Zamówienie: 2 dni spóźnienia, brak 1 produktu.”

## Co z tego wynika

**1. Krótsze pisanie po polsku działa, i to mocno.** Z 64 do 42 tokenów, czyli o 34% mniej, bez zmiany sensu. Styl notatki schodzi do 39. Najwięcej dają liczby zamiast słów („3” zamiast „trzech”), krótsze słowa („mail” zamiast „e-mail od klienta”) i wyrzucenie zbędnych zwrotów („Klient twierdzi, że…”).

**2. Usuwanie polskich znaków nic nie daje.** „Stresc”, „grzeczna”, „zamowienie” zamiast „Streść”, „grzeczną”, „zamówienie” to oszczędność jednego tokenu w GPT, a w Mistralu nawet o jeden więcej. Tekst jest za to mniej czytelny. Nie warto.

**3. Angielski nadal wygrywa, ale różnica się kurczy.** Krótki angielski to 28 tokenów, krótki polski 42. Po dopisaniu „Reply in Polish.”, żeby odpowiedź była po polsku, angielski ma 32. Przy krótkich poleceniach w czacie różnica to kilka tokenów, więc pisz, jak ci wygodnie.

**4. Mistral nie jest tańszy dla polskiego.** Przy formalnym tekście Tekken liczy trochę mniej (58 zamiast 64), ale przy krótkich wersjach wyniki są prawie takie same jak w GPT.

## Dlaczego polski kosztuje więcej

![Dlaczego polski kosztuje więcej: „zaproponuj” → z | apro | pon | uj (4 tokeny); „potwierdzenie” → pot | wier | d | zenie (4); „opóźnieniem” → o](/jak-skrocic-prompt-po-polsku-dlaczego-polski-kosztuje-wiecej-pl.jpg)

Tokenizery uczą się głównie na angielskim tekście, więc polskie słowa często są cięte na kawałki:

- „zaproponuj” → `z | apro | pon | uj` (4 tokeny)
- „potwierdzenie” → `pot | wier | d | zenie` (4)
- „opóźnieniem” → `op | ó | ź | n | ieniem` (5)
- „uprzejmą” → `upr | zej | m | ą` (4)

Po angielsku „suggest”, „confirmation”, „late” czy „polite” to jeden token. Krótszy polski tekst pomaga głównie dlatego, że zawiera mniej takich długich, odmienionych słów.

## Prompt systemowy: tu skracanie daje najwięcej

![Prompt systemowy: tu skracanie daje najwięcej: Wersja, GPT (o200k), Mistral (Tekken)](/jak-skrocic-prompt-po-polsku-prompt-systemowy-tu-skracanie-daje-najwi-pl.jpg)

Prompt systemowy wysyłasz z każdym zapytaniem, więc tam liczy się każdy token. Przetestowałem instrukcję dla asystenta obsługi klienta sklepu internetowego:

| Wersja | GPT (o200k) | Mistral (Tekken) |
|---|---:|---:|
| Polski, pełne zdania | 122 | 129 |
| Polski, skrócony | **85** | 89 |
| Angielski + „Reply in Polish.” | **83** | 86 |

Skrócona polska wersja:

> Jesteś asystentem obsługi klienta sklepu online. Odpowiadaj uprzejmie i konkretnie, max 5 zdań. Zwrot: 14 dni od otrzymania paczki, podaj link do formularza. Nie obiecuj rabatów ani terminów dostawy bez potwierdzenia logistyki. Nie wiesz – przekaż do konsultanta.

Dobrze skrócony polski prompt systemowy jest prawie tak tani jak angielski (85 vs 83 tokeny), a cały zespół nadal może go czytać i poprawiać po polsku. Jeśli nie chcesz tłumaczyć instrukcji, to jest najlepsza opcja.

## Ile to daje w pieniądzach

Prompt systemowy wysyłany 1 000 razy dziennie, czyli 30 000 razy w miesiącu, przy cenie 2 $ za milion tokenów wejściowych:

| Wersja | Tokeny miesięcznie | Koszt miesięcznie |
|---|---:|---:|
| Polski, pełne zdania | 3,66 mln | 7,32 $ |
| Polski, skrócony | 2,55 mln | 5,10 $ |
| Angielski + „Reply in Polish.” | 2,49 mln | 4,98 $ |

Przy jednym prompcie to niewiele, ale w produkcie prompty systemowe mają często tysiące tokenów, a zapytań jest więcej. Skrócenie o 30% przekłada się wtedy bezpośrednio na rachunek.

## Podsumowanie

1. **W czacie** pisz krótko i konkretnie. Liczby zamiast słów, bez zbędnych zwrotów. Polskich znaków nie usuwaj.
2. **W promptach systemowych i automatyzacjach** skróć instrukcje do stylu notatki albo napisz je po angielsku i dodaj „Reply in Polish.”.
3. **Zanim zaczniesz optymalizować,** policz tokeny swojego promptu. Czasem największy zysk jest gdzie indziej, np. w długości odpowiedzi.

## Sprawdź swój prompt

[TokenSave](/pl/) liczy tokeny i koszt promptu dla GPT, Claude i Gemini bezpośrednio w przeglądarce, bez wysyłania tekstu na serwer. Przycisk **💸 Oszczędź tokeny** tłumaczy prompt na angielski wbudowanym tłumaczem Chrome lub Edge na twoim urządzeniu i dodaje „Reply in Polish.”. Za darmo, bez rejestracji.

Więcej pomiarów: [Ile naprawdę kosztuje prompt po polsku? GPT i Mistral zmierzone](/pl/blog/ile-kosztuje-prompt-po-polsku)

*Pomiary: październik 2026, o200k_base (OpenAI) i Tekken 2024-09 (Mistral). Cena w przykładzie jest hipotetyczna.*
<!-- autoimg -->
