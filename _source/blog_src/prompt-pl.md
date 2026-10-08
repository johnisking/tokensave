Płacąc za AI, płacisz za *tokeny*, a nie za słowa. Ten sam tekst po polsku dzieli się na znacznie więcej tokenów niż po angielsku, więc kosztuje więcej w API i szybciej wyczerpuje limity w ChatGPT Plus czy Claude Pro. Zmierzyłem, o ile.

![Polski prompt zużywa o 50–88% więcej tokenów niż angielski](/blog-prompt-polski.png)

## Test

Dwa teksty o identycznym znaczeniu, po angielsku i po polsku:

- **Krótki prompt**: prośba o streszczenie e-maila od klienta w trzech punktach (2 zdania).
- **Długi prompt**: instrukcje sprawdzenia faktury i napisania e-maila do klienta (ok. 100 słów).

Policzyłem tokeny dwoma tokenizerami: **o200k_base** (GPT-4o i nowsze modele OpenAI) oraz **Tekken** (tokenizer udostępniony przez Mistral).

## Wyniki

![Wyniki: Tekst, Angielski, Polski, Ile więcej](/ile-kosztuje-prompt-po-polsku-wyniki-pl.jpg)

| Tekst | Angielski | Polski | Ile więcej |
|---|---:|---:|---:|
| Krótki, OpenAI | 34 | 64 | **+88%** |
| Krótki, Mistral | 34 | 58 | **+71%** |
| Długi, OpenAI | 110 | 166 | **+51%** |
| Długi, Mistral | 110 | 165 | **+50%** |

Polski zużywa **od 50% do prawie 90% więcej tokenów** niż angielski. W rankingu 41 języków na tokenizerze GPT-4o polski (+88%, razem z ukraińskim) jest w ścisłej czołówce najdroższych: z Europy drożej wypadają tylko czeski, słowacki i grecki. Dla porównania niemiecki to +26%, francuski +29%, a hiszpański +18%.

## Dlaczego tak drogo

![Dlaczego tak drogo: „zaproponuj” → zap | ro | pon | uj (4 tokeny); „potwierdzenie” → pot | wier | d | zenie (4 tokeny); „rachunkow](/ile-kosztuje-prompt-po-polsku-dlaczego-tak-drogo-pl.jpg)

Tokenizery uczono głównie na angielskim tekście. Słowa takie jak „invoice” czy „polite” to jeden token, a polskie słowa z końcówkami fleksyjnymi są cięte na kawałki:

- „zaproponuj” → `zap | ro | pon | uj` (4 tokeny)
- „potwierdzenie” → `pot | wier | d | zenie` (4 tokeny)
- „rachunkowego” → `rach | unk | owego` (3 tokeny)
- „uprzejmy” → `upr | zej | my` (3 tokeny)

Odmiana przez przypadki i polskie znaki (ą, ę, ł, ż…) sprawiają, że tokenizer rzadko zna całe słowo.

## Co to oznacza w praktyce

![Co to oznacza w praktyce: W API płacisz za ten sam tekst o 50–90% więcej.; W abonamencie (ChatGPT Plus, Claude Pro, Gemini) limity liczo](/ile-kosztuje-prompt-po-polsku-co-to-oznacza-w-praktyce-pl.jpg)

- **W API** płacisz za ten sam tekst o 50–90% więcej.
- **W abonamencie** (ChatGPT Plus, Claude Pro, Gemini) limity liczone są w tokenach, więc kończą się szybciej, gdy piszesz po polsku.
- **Jeśli odpowiedź też jest po polsku**, ten sam mnożnik dotyczy tokenów wyjściowych, które zwykle są o 300–400% droższe od wejściowych.

## Jak płacić mniej: pisz po angielsku, odbieraj po polsku

Najprostszy sposób: napisz prompt po angielsku i dodaj na końcu **„Reply in Polish.”** Model rozumie tak samo dobrze, odpowiedź przychodzi po polsku, a wejście kosztuje mniej:

- krótki prompt: 64 → 38 tokenów (**−41%**)
- długi prompt: 166 → 114 tokenów (**−31%**)

Najbardziej opłaca się to przy:

- **promptach systemowych** i instrukcjach wysyłanych tysiące razy przez API,
- **długich dokumentach** wklejanych jako kontekst,
- abonamentach, w których **często trafiasz na limit**.

Przy jednorazowym krótkim pytaniu różnica jest pomijalna, więc pisz, jak ci wygodnie.

## Sprawdź na własnym tekście

Każdy tekst jest inny. [TokenSave](/pl/) liczy tokeny i koszt promptu dla GPT, Claude i Gemini, a jednym kliknięciem tłumaczy go na angielski bezpośrednio w przeglądarce i dodaje „Reply in Polish”. Kod zostaje nietknięty, tłumaczone są tylko komentarze. Za darmo, bez rejestracji, nic nie jest wysyłane na serwer.

Pełny ranking 41 języków: [Ile tokenów kosztuje polski?](/pl/blog/polski-tokeny-gpt)

*Pomiary z października 2026: o200k_base (OpenAI) i Tekken 2024-09 (Mistral). Wynik zależy od tekstu; najnowsze modele mogą używać zaktualizowanych tokenizerów.*

## Źródła

- [tiktoken (OpenAI): tokenizer o200k_base](https://github.com/openai/tiktoken)
- [Mistral NeMo i tokenizer Tekken (Mistral AI)](https://mistral.ai/news/mistral-nemo/)
- [Cennik API OpenAI (ceny za milion tokenów)](https://developers.openai.com/api/docs/pricing)
<!-- autoimg -->
