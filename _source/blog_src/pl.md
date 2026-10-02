Przetłumaczyłem jeden zwykły prompt na 41 języków i policzyłem tokeny tokenizerem, którego używają obecne modele OpenAI (o200k_base, GPT-4o i nowsze). Spodziewałem się, że najdrożej wyjdą japoński albo tajski. Tymczasem na samym końcu znalazły się języki europejskie: **polski (razem z ukraińskim) ma 1,88×**, a z Europy drożej wypadają tylko czeski i słowacki (2,00×) oraz grecki (2,06×). Najdroższy w całym zestawieniu okazał się pendżabski (2,44×).

Prompt (po angielsku 34 tokeny):

> Podsumuj poniższy e-mail od klienta w trzech punktach i zaproponuj uprzejmą odpowiedź. Klient twierdzi, że zamówienie dotarło z dwudniowym opóźnieniem, a w paczce brakowało jednego produktu.

| Język | Tokeny | Względem angielskiego | Oszczędność przy wysłaniu po angielsku |
|---|---:|---:|---:|
| Angielski | 34 | 1,00× | – |
| Chiński (uproszczony) | 35 | 1,03× | 3% |
| Niemiecki | 43 | 1,26× | 21% |
| Rosyjski | 45 | 1,32× | 24% |
| Koreański | 49 | 1,44× | 31% |
| Japoński | 61 | 1,79× | 44% |
| **Polski** | **64** | **1,88×** | **47%** |
| Ukraiński | 64 | 1,88× | 47% |
| Czeski | 68 | 2,00× | 50% |
| Słowacki | 68 | 2,00× | 50% |
| Grecki | 70 | 2,06× | 51% |
| Pendżabski | 83 | 2,44× | 59% |

![Wykres](/blog-language-tax-chart-v4.png)

**Dlaczego?** Tokenizer zna całe angielskie słowa (" polite", " customer" = 1 token), a polskie skleja z kawałków. Odmiana przez przypadki i znaki diakrytyczne robią swoje:

- " opóźnieniem" → ` op | ó | ź | n | ieniem` (5 tokenów)
- " uprzejmą" → ` upr | zej | m | ą` (4 tokeny)
- " dwudniowym" → ` dw | ud | ni | owym` (4 tokeny)

**Przejdź na angielski jednym przyciskiem:** Największą oszczędność daje wysyłanie promptu po angielsku: dla języka polskiego to około 47% mniej tokenów. Obecne modele świetnie rozumieją instrukcje po angielsku i odpowiadają po polsku, jeśli o to poprosisz. W liczniku tokenów TokenSave wklej prompt i naciśnij **💸 Oszczędź tokeny**: usuwa zbędne spacje, tłumaczy na angielski, wycina „lanie wody” i dodaje „Reply in Polish.”, żeby odpowiedź pozostała w Twoim języku. Korzysta z tłumacza wbudowanego w Chrome 138+ / Edge 148+ na komputerze; tłumaczenie odbywa się na Twoim urządzeniu, a tekst nigdy nie jest przesyłany. Naciśnij **↩ Oryginał**, aby przywrócić oryginał.

**W pieniądzach:** model za 2 $ / 1M tokenów wejściowych, prompt wysłany milion razy: angielski 68 $, polski 128 $. I to tylko wejście. Jeśli model odpowiada po polsku, ten sam mnożnik dotyczy tokenów wyjściowych, które zwykle są 4–5× droższe.

**Co z tym zrobić:**

- Prompt systemowy i stałe instrukcje pisać po angielsku, po polsku tylko dane od użytkownika.
- Kroki pośrednie (klasyfikacja, ekstrakcja, wywołania narzędzi) zwracać po angielsku albo w JSON, po polsku tylko finalną odpowiedź.
- Korzystać z prompt caching dla stałej części promptu.

Ograniczenia: to jeden prompt, dla innych tekstów wynik może się różnić o ±0,1–0,2. Claude i Gemini mają inne tokenizery, liczby dotyczą tylko modeli OpenAI. Tłumaczenie jest maszynowe, jeśli coś brzmi nienaturalnie, dajcie znać, zmierzę ponownie.

Pełne wyniki dla 41 języków (po angielsku): [porównanie 41 języków](/blog/token-cost-by-language)

Ile to kosztuje w praktyce i jak płacić mniej: [Ile naprawdę kosztuje prompt po polsku?](/pl/blog/ile-kosztuje-prompt-po-polsku)
