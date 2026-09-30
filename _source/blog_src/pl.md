Przetłumaczyłem jeden zwykły prompt na 41 języków i policzyłem tokeny tokenizerem, którego używają obecne modele OpenAI (o200k_base, GPT-4o i nowsze). Spodziewałem się, że najdrożej wyjdą japoński albo tajski. Tymczasem na samym końcu znalazły się języki europejskie: **polski (razem z ukraińskim) ma 1,88×**, a z Europy drożej wypadają tylko czeski i słowacki (2,00×) oraz grecki (2,06×). Najdroższy w całym zestawieniu okazał się pendżabski (2,44×).

Prompt (po angielsku 34 tokeny):

> Podsumuj poniższy e-mail od klienta w trzech punktach i zaproponuj uprzejmą odpowiedź. Klient twierdzi, że zamówienie dotarło z dwudniowym opóźnieniem, a w paczce brakowało jednego produktu.

| Język | Tokeny | Względem angielskiego | Stary tokenizer GPT-4 |
|---|---:|---:|---:|
| Angielski | 34 | 1,00× | 1,00× |
| Chiński (uproszczony) | 35 | 1,03× | 1,53× |
| Niemiecki | 43 | 1,26× | 1,50× |
| Rosyjski | 45 | 1,32× | 2,15× |
| Koreański | 49 | 1,44× | 2,50× |
| Japoński | 61 | 1,79× | 2,21× |
| **Polski** | **64** | **1,88×** | **2,12×** |
| Ukraiński | 64 | 1,88× | 3,15× |
| Czeski | 68 | 2,00× | 2,59× |
| Słowacki | 68 | 2,00× | 2,53× |
| Grecki | 70 | 2,06× | 4,94× |
| Pendżabski | 83 | 2,44× | 7,41× |

![Wykres](/blog-language-tax-chart-v4.png)

**Dlaczego?** Tokenizer zna całe angielskie słowa (" polite", " customer" = 1 token), a polskie skleja z kawałków. Odmiana przez przypadki i znaki diakrytyczne robią swoje:

- " opóźnieniem" → ` op | ó | ź | n | ieniem` (5 tokenów)
- " uprzejmą" → ` upr | zej | m | ą` (4 tokeny)
- " dwudniowym" → ` dw | ud | ni | owym` (4 tokeny)

Ciekawostka: przy zmianie tokenizera ukraiński mocno potaniał (3,15× → 1,88×), a polski tylko trochę (2,12× → 1,88×).

**W pieniądzach:** model za 2 $ / 1M tokenów wejściowych, prompt wysłany milion razy: angielski 68 $, polski 128 $. I to tylko wejście. Jeśli model odpowiada po polsku, ten sam mnożnik dotyczy tokenów wyjściowych, które zwykle są 4–5× droższe.

**Co z tym zrobić:**

- Prompt systemowy i stałe instrukcje pisać po angielsku, po polsku tylko dane od użytkownika.
- Kroki pośrednie (klasyfikacja, ekstrakcja, wywołania narzędzi) zwracać po angielsku albo w JSON, po polsku tylko finalną odpowiedź.
- Korzystać z prompt caching dla stałej części promptu.

Ograniczenia: to jeden prompt, dla innych tekstów wynik może się różnić o ±0,1–0,2. Claude i Gemini mają inne tokenizery, liczby dotyczą tylko modeli OpenAI. Tłumaczenie jest maszynowe, jeśli coś brzmi nienaturalnie, dajcie znać, zmierzę ponownie.

Pełne wyniki dla 41 języków (po angielsku): [porównanie 41 języków](/blog/token-cost-by-language)
