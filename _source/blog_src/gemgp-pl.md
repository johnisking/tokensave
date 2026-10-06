Google zmienia to, z których modeli można korzystać w aplikacji Gemini w poszczególnych planach. **Od 9 października darmowi użytkownicy dostaną tylko najmniejszy model, Flash-Lite**, a plan AI Plus za 23,99 zł wkrótce straci dostęp do modelu Pro. Do tej pory nawet za darmo dało się sporo korzystać z modelu Pro i Deep Research, więc różnica będzie odczuwalna. Dotyczy to wielu osób w Polsce: według Comscore udział Gemini w zapytaniach do chatbotów AI wzrósł w Polsce w tym roku z 17% do 30%. Poniżej: co się zmienia, ile kosztuje każdy plan w złotówkach i jak tanio korzystać z modeli klasy Pro, policzone na polskich tokenach.

## Jakie modele w którym planie

| Plan | Cena / mies. | Flash-Lite | Flash | Pro | Deep Think |
|---|---:|:---:|:---:|:---:|:---:|
| Darmowy | 0 zł | ✓ | ✗ | ✗ | ✗ |
| AI Plus | 23,99 zł | ✓ | ✓ | **✗ (usunięty)** | ✗ |
| AI Pro | 97,99 zł | ✓ | ✓ | ✓ | ✓ |
| AI Ultra | 469,99 zł | ✓ | ✓ | ✓ | ✓ |
| AI Ultra (wyższy limit) | 979,99 zł | ✓ | ✓ | ✓ | ✓ |

Ceny polskie z VAT, sprawdzone 6 października 2026. Zmiany dotyczą prywatnych kont Google; konta firmowe i szkolne mają osobne zasady.

## Od kiedy?

- **Plan darmowy:** od 9 października tylko Flash-Lite.
- **AI Plus:** nie ma jednej daty dla wszystkich. Każdy subskrybent dostanie e-mail z datą, od której zmiana obejmie jego konto.
- **AI Pro i Ultra:** bez zmian w dostępie, czyli Flash-Lite, Flash i Pro, a do tego Deep Think.

W dostępnych modelach można wybrać poziom wysiłku: niski, średni lub wysoki. Im wyższy, tym szybciej zużywa się limit. Limit nie jest liczony w wiadomościach, tylko w mocy obliczeniowej, i odnawia się co 5 godzin. Model Pro, Deep Research oraz generowanie obrazów i wideo zużywają go szybciej niż proste pytania.

## Dlaczego Google to robi

30 września Google pokazał swój najmocniejszy model, Gemini 4 Argon. Najdroższe w utrzymaniu modele trafiają teraz głównie do płatnych planów, a zmiana ma skłonić więcej osób do przejścia na wyższy plan.

## Co zrobić

- **Głównie szybkie wyszukiwanie, tłumaczenia i streszczenia:** darmowy Flash-Lite często wystarczy. Warto najpierw sprawdzić go w praktyce, a o płatnym planie decydować dopiero wtedy, gdy odpowiedzi okażą się za słabe.
- **Masz AI Plus dla modelu Pro:** od daty z e-maila za 23,99 zł nie skorzystasz już z Pro. Jeśli go potrzebujesz, zostaje AI Pro za 97,99 zł.
- **Studenci:** w Polsce studenci dostają za darmo na rok **Google AI Plus, a nie AI Pro**. A Plus właśnie traci model Pro, więc ta oferta daje teraz wyraźnie mniej niż jeszcze miesiąc temu.
- **97,99 zł to dla Ciebie dużo:** porównaj z planami w tej samej cenie: ChatGPT Plus (99,99 zł) i Claude Pro (20 USD + 23% VAT, ok. 92,59 zł). W ChatGPT nawet za darmo zwykły czat z modelem GPT-5.6 Luna nie ma limitu. Wszystkie plany w złotówkach zebrałem w [porównaniu cen subskrypcji AI](/pl/blog/ceny-subskrypcji-ai), a różnicę między tańszymi planami ChatGPT opisuję w tekście [ChatGPT Go czy Plus](/pl/blog/chatgpt-go-vs-plus).

## Model Pro taniej: przez API

Z modeli Gemini można też korzystać przez Google AI Studio lub API i płacić tylko za to, co się zużyje. Polski tekst dzieli się na około 88% więcej tokenów niż angielski ([pomiar tutaj](/pl/blog/polski-tokeny-gpt)), więc liczę na polskich tokenach: jedno pytanie to ok. 1580 tokenów wejścia i 730 tokenów odpowiedzi. Przy **20 pytaniach dziennie przez 30 dni** (600 zapytań):

| Model | Koszt API za miesiąc |
|---|---:|
| Gemini 3.5 Flash-Lite | ok. 1,38 USD (ok. 5,40 zł) |
| Gemini 3.8 Flash | ok. 2,35 USD (ok. 9,20 zł) |
| Gemini 3.1 Pro | ok. 7,15 USD (ok. 27,90 zł) |

Kurs: 1 USD = 3,90 zł. Ceny API za milion tokenów (wejście / wyjście): Flash-Lite 0,30 / 2,50 USD, Flash 0,75 / 3,75 USD, Pro 2 / 12 USD. W długich rozmowach koszt rośnie, bo przy każdym pytaniu wysyłana jest cała dotychczasowa rozmowa.

**Nawet model Pro przez API kosztuje przy takim użyciu ok. 71% mniej niż AI Pro (97,99 zł).** Tracisz jednak funkcje aplikacji: generowanie obrazów, Deep Research, integrację z Gmailem i Dokumentami. Potrzebna jest też osobna aplikacja czatu, która obsługuje klucz API. Czy przy Twoim sposobie korzystania taniej wychodzi subskrypcja czy API, sprawdzisz od razu w [kalkulatorze subskrypcja vs API](/pl/plans). Koszt pojedynczego polskiego promptu policzysz w [liczniku tokenów](/pl/), a więcej o tym, dlaczego polski jest droższy, przeczytasz w tekście [ile kosztuje prompt po polsku](/pl/blog/ile-kosztuje-prompt-po-polsku).

*Źródła: [Spider's Web](https://spidersweb.pl/2026/10/gemini-koniec-pro-za-darmo.html), [android.com.pl](https://android.com.pl/tech/1092166-darmowy-google-gemini-ograniczenia/), [Notebookcheck](https://www.notebookcheck.net/Google-Gemini-drops-Flash-and-Pro-for-free-users-on-October-9.1415964.0.html), polskie ceny wg [Promptowy](https://promptowy.com/gemini-za-darmo-zmiany-9-pazdziernika/) i [Bez Halucynacji](https://bezhalucynacji.pl/ile-kosztuje-gemini-ceny-ai-plus-pro-i-ultra-w-zl), oferta dla studentów wg [iMagazine](https://imagazine.pl/2026/08/21/gemini-za-darmo-dla-studentow-polska-poradnik/), udziały Gemini wg Comscore za [Wirtualnemedia](https://www.wirtualnemedia.pl/chatgpt-traci-udzialy-gemini-i-claude-ze-wzrostami,7332114180385024a). Stan na 6 października 2026. Daty i limity mogą się zmienić, więc przed zakupem sprawdź oficjalną stronę Google.*
