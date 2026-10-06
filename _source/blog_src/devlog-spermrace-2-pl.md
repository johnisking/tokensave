![3 dni budowania, 14 dni debugowania – dziennik dewelopera Sperm Race, część 2 (vibe coding gra)](/blog-spermrace-2-hero-en.jpg)

W [części 1](/blog/vibe-coding-a-game-beginner) (po angielsku) zrobiłem grę w 3 dni bez żadnego doświadczenia w programowaniu – po prostu opisując ją AI. Byłem gotów kliknąć „opublikuj”, kiedy zatrzymało mnie Google Play: nowe osobiste konto dewelopera musi przejść **testy zamknięte Google Play z co najmniej 12 testerami przez 14 dni**, zanim aplikacja trafi do sklepu.

Czternaście dni. Ponad cztery razy dłużej niż budowanie gry. Zamiast po prostu czekać, postanowiłem grać w nią codziennie. I okazało się, że bez tych 14 dni premiera byłaby katastrofą.

**3 dni budowania, 14 dni debugowania.** To historia 14 błędów, które naprawiłem – od budowania, przez testy zamknięte, po okres po premierze. Moja vibe coding gra nazywa się Sperm Race.

## Czym są 14-dniowe testy zamknięte Google Play?

Jeśli założyłeś **osobiste** konto dewelopera Google Play po 13 listopada 2023 roku, musisz przeprowadzić test zamknięty, zanim aplikacja trafi do wersji produkcyjnej.

- **Testerzy:** co najmniej 12 osób, które dołączyły do testu
- **Czas trwania:** ci testerzy pozostają w teście przez 14 dni
- **Potem:** składasz wniosek o dostęp do wersji produkcyjnej w panelu Play Console

Konta organizacji nie mają tego wymogu. Znalazłem ok. 20 testerów dzięki **wymianie testów** („test za test”) z innymi niezależnymi twórcami. Wielu samodzielnych twórców traktuje te 14 dni jak czas stracony. Dla mnie była to ostatnia szansa na wyłapanie błędów przed premierą.

![Droga do premiery: 3 dni budowania, 14 dni testów zamkniętych Google Play z 12 testerami, okres po premierze](/blog-spermrace-2-timeline-en.jpg)

## Kod Sperm Race w liczbach

Policzyłem kod w plikach wersji, które wciąż mam na komputerze (bez plików z tłumaczeniami).

![Linie kodu: pierwsza wersja 3112, gotowa wersja 6341, aplikacja na Androida 8513, najnowsza 13 822](/blog-spermrace-2-code-en.jpg)

- W pierwszych dwóch dniach dostałem od AI **16 poprawek**, a kod **się podwoił**.
- Podczas przerabiania gry na aplikację na Androida doszło ok. **2250 linii**, a liczba notatek w kodzie typu „to kiedyś był błąd” wzrosła **z 8 do 17**.
- Od pierwszej wersji do najnowszej doszło ok. **10 900 linii**. To nie tylko poprawki błędów, ale też nowe funkcje, jak tryb Survival i gra ze znajomymi.

Nie napisałem ani jednej z tych linii. Jedyne, co robiłem, to grałem i opisywałem, co widzę. Kod przekroczył 8000 linii, a plan Claude Pro wciąż wystarczał aż do premiery. Jeśli chcesz wiedzieć, ile tokenów ma Twój kod, wklej go do [licznika tokenów](/pl/).

## Dlaczego „znajdź błąd” nie działa?

Bo AI nie wie, gdzie szukać. Musisz powiedzieć, w jakim trybie, co zrobiłeś i co się stało.

Na początku pisałem po prostu „znajdź błąd i go napraw”. AI pewnym tonem odpowiadała „Naprawione!”, ale błąd wciąż był, a coś, co wcześniej działało, teraz się psuło. To tak, jakby wejść do gabinetu lekarza i powiedzieć „niech pan naprawi, co trzeba”, nie mówiąc, gdzie boli.

Zadziałało dopiero podawanie **trybu + tego, co zrobiłem + tego, co się stało**. Szczerze mówiąc, moje własne zgłoszenia też były na początku mgliste. Cytowane poniżej tytuły błędów to dokładnie to, co wpisywałem (przetłumaczone z koreańskiego), i wiele z nich, jak „sterowanie przeciąganiem jest trudniejsze niż wcześniej”, pomija, gdzie i jak.

| Ogólnikowo | Konkretnie |
|---|---|
| „Znajdź błąd i go napraw” | „W wyścigu licznik okrążeń skacze z 1/3 na 2/3 zaraz po przekroczeniu linii startu” |
| „Sterowanie przeciąganiem jest trudniejsze niż wcześniej” (to, co napisałem) | „W wyścigu, gdy na zakręcie przeciągnę palcem daleko w bok, nagle hamuje” |

Na szczęście za każdym razem, gdy AI coś naprawiała, zostawiała w kodzie notatkę w rodzaju „to kiedyś powodowało problem”, więc cała historia błędów wciąż tam była. Poniższe ekrany odtworzyłem **w prawdziwej grze** – uruchamiając stare pliki wersji albo cofając tylko jedną poprawkę. Błędy, które zepsułyby grę albo nie przeszłyby weryfikacji, to **błędy poważne**; reszta to **błędy drobne**.

## 7 poważnych błędów

**1. Jedno okrążenie zaliczone, zanim wyścig się zaczął** (podczas budowania)
W trybie wyścigu zapaliło się zielone światło, ruszyłem o krok i licznik okrążeń poszedł w górę. Dla gry plemniki ustawione tuż za linią startu wyglądały jak zawodnicy „kończący pełne okrążenie”. Wyścig na 3 okrążenia był w rzeczywistości wyścigiem na 2. Pomogło przesunięcie pola startowego przed linię.

![Odtworzenie: Okrążenie 1/3 na linii startu zmienia się w 2/3 krok później](/blog-spermrace-bug-lap-en.jpg)

**2. Wpychanie się na pierwsze miejsce** (podczas budowania)
W wyścigu ukończenie okrążeń otwiera bramę do środka, a wygrywa pierwszy plemnik, który dotknie komórki jajowej w środku. Tyle że brama otwierała się dla wszystkich, gdy tylko ktokolwiek ukończył okrążenia. Mogłem więc stać na linii startu, poczekać, aż NPC ukończy okrążenia, a potem prześlizgnąć się przez bramę i wygrać. Działało to też w drugą stronę: kończyłem okrążenia i kierowałem się do komórki jajowej, a NPC, który krążył bez celu po torze, wpychał się i zabierał pierwsze miejsce.

![Odtworzenie (GIF): NPC kończy okrążenia, brama się otwiera, a mój plemnik, wciąż na okrążeniu 1/3, przejeżdża przez nią i zajmuje 1. miejsce](/blog-spermrace-bug-cut-en.gif)

Poprosiłem więc o dwie zasady: „plemnik, który nie ukończył okrążeń, nie może wjechać do środka” i „wyścig kończy się dopiero po faktycznym dotknięciu komórki jajowej”. Obie wzięły się z tego, że irytowałem się podczas grania.

**3. „Naciśnięcie przycisku Wstecz w trakcie gry zamyka aplikację”** (testy zamknięte)
Przypadkiem nacisnąłem przycisk Wstecz w telefonie w trakcie wyścigu i aplikacja po prostu się zamknęła. Wyścig, który wygrywałem – przepadł. Gdyby to trafiło do sklepu, pierwsza recenzja brzmiałaby: „przycisk Wstecz zamyka grę, 1 gwiazdka”. Teraz w trakcie gry przycisk wraca do menu głównego.

**4. Bukmacher dla plemników** (testy zamknięte)
W okresie testów przeczytałem zasady Google Play i oblał mnie zimny pot. Tryb Derby pokazywał „kursy” i pytał „na kogo stawiasz?”. Gra, w której obstawia się ścigające się plemniki. Dla osoby weryfikującej wygląda to dokładnie jak aplikacja hazardowa. Zmieniłem to na oceny w gwiazdkach (★★★☆☆) i pytanie „komu kibicujesz?”.

![Stary ekran Derby z kursami obok nowego ekranu z ocenami w gwiazdkach](/blog-spermrace-bug-derby-en.jpg)

**5. Stuknij, a dostaniesz za darmo** (testy zamknięte)
W grze wciąż był fałszywy przycisk zakupu z czasu tworzenia. Stuknięcie go niczego nie pobierało i od razu pokazywało „zakup zakończony”. Fałszywa reklama dawała nagrodę po 5 sekundach czekania. Raj dla graczy, a dla Google – wprowadzające w błąd działanie. Usunąłem to wszystko.

**6. Cała gra się zawiesiła** (po premierze)
Przetrwałem 14 dni i wydałem grę. Myślałem, że to koniec, ale najstraszniejsze dopiero miało nadejść. Zgłosiłem grę na inną platformę i dostałem odrzucenie. Licznik czasu stał na 00.0s, a ekran wyścigu był czarny. We wszystkich czterech trybach.

Winowajcą okazał się gamepad. Sperm Race obsługuje gamepady, więc w każdej klatce sprawdza, „czy gamepad jest podłączony?”. Na tamtej platformie sprawdzanie gamepada w ogóle nie było dozwolone. Każde sprawdzenie zgłaszało błąd, a każdy błąd zamrażał grę. Na moim telefonie nigdy się to nie zdarzyło, cokolwiek bym robił. Funkcja „miło, że jest” zamroziła całą grę gdzie indziej.

![W środowisku blokującym sprawdzanie gamepada gra zamarza na czarnym ekranie z czasem 00.0s; po poprawce wyścig działa normalnie](/blog-spermrace-bug-freeze-en.jpg)

**7. Koreański dla wszystkich pozostałych** (po premierze)
Sperm Race obsługuje 13 języków. Ale każdy, kto miał w telefonie ustawiony język spoza tych 13, dostawał całą grę po koreańsku. Winowajca był zapisany czarno na białym w notatce z 20 sierpnia: „Jeśli wykrywanie się nie powiedzie, domyślnie ustaw koreański”. Ustawienie domyślne, które wybrałem, budując grę w 3 dni, wróciło jako błąd miesiąc później. Teraz nieznane języki dostają angielski.

![Telefon ustawiony na węgierski: przed poprawką gra po koreańsku, po poprawce po angielsku](/blog-spermrace-bug-lang-en.jpg)

## 7 drobnych błędów

Nie psują gry, ale od razu rzucają się w oczy.

- **Niekończące się kręcenie przy komórce jajowej:** Na ostatnim okrążeniu plemniki NPC kręciły się przed komórką jajową, zamiast do niej wjechać. Skręcały za szybko i ciągle się odbijały. Teraz zwalniają przed ostrymi zakrętami.
- **Głowa tu, ogon tam:** Po uderzeniu w przeszkodę głowa odbijała się do tyłu, ale ogon zostawał na miejscu, więc wystawał przed głowę.
- **„Dźwięk gry gra dalej w tle”:** Nawet po zminimalizowaniu aplikacji albo wyłączeniu ekranu dźwięki gry leciały dalej. Plemniki wciąż się ścigały w mojej kieszeni.
- **Cicha ścieżka dźwiękowa:** Gdy telefon zablokował pierwszą próbę odtworzenia muzyki, gra uznawała, że „muzyka już gra”, i nigdy nie próbowała ponownie.
- **„Sterowanie przeciąganiem jest trudniejsze niż wcześniej”:** Na zakrętach, jeśli palec choć trochę zjechał w dół, gra odczytywała to jako hamowanie, więc każdy zakręt oznaczał nagłe zatrzymanie.
- **„Tajfun nie działa albo go nie widzę”:** Nowa przeszkoda pojawiała się dopiero od etapu 29. Nigdy tak daleko nie doszedłem. Przeniosłem ją na etap 12.
- **Dla AI zero to nie liczba:** Labirynt, który miał mieć „0 rywali”, miał ich 3. Kod odczytywał 0 jako „brak wartości” i wstawiał domyślne 3. Przyczyną był jeden znak.

![Ogon wystający przed głowę zaraz po uderzeniu i wersja po poprawce](/blog-spermrace-bug-tail-en.jpg)

## Jak wykorzystać 14 dni testów zamkniętych z 12 testerami?

Jeśli właśnie czekasz, aż minie Twój test zamknięty, oto trzy rzeczy, które możesz wziąć prosto z mojego doświadczenia.

### 1. Zgłaszaj błędy AI według tego szablonu

```
[Tryb/ekran] Tryb wyścigu, tor Stadium
[Co zrobiłem] Nacisnąłem gaz po sygnale startu i przekroczyłem linię startu
[Oczekiwane] Okrążenie zostaje na 1/3
[Co się stało] Okrążenie od razu skoczyło na 2/3
[Za każdym razem?] Za każdym razem
[Urządzenie] Aplikacja na Androida (model telefonu)
Po naprawie zostaw w kodzie komentarz wyjaśniający, dlaczego to się działo.
```

Zostaw ostatnią linijkę. Moja AI za każdym razem, gdy coś naprawiała, zostawiała notatkę „to kiedyś powodowało problem”, więc zawsze mogłem sprawdzić, co i dlaczego zostało zmienione. Dzięki tym notatkom mogłem napisać ten wpis.

### 2. Lista kontrolna na 14 dni

Napisałem ją tak, żeby sprawdzała się w każdej grze mobilnej, niezależnie od gatunku. W nawiasach – błędy, na które faktycznie trafiłem.

**Rzeczy, które robi Twój telefon**
- Naciśnij **Wstecz** w trakcie gry (aplikacja po prostu się zamknęła)
- **Zminimalizuj aplikację, wyłącz ekran i wróć** w trakcie gry. Czy dźwięk się zatrzymuje? Czy gra wznawia się? (dźwięk grał dalej)
- Sprawdź, czy dźwięk działa **zaraz po pierwszym uruchomieniu, zanim cokolwiek stukniesz**, i po pierwszym stuknięciu (muzyka nigdy nie ruszyła)
- Wypróbuj **inne telefony i proporcje ekranu**. Poproś o to testerów

**Zapisywanie**
- Zmień ustawienia i postęp, a potem **całkowicie zamknij i otwórz aplikację ponownie**. Czy wszystko jest na miejscu?

**Język**
- Ustaw w telefonie **język, którego Twoja gra nie obsługuje**, i ją uruchom (koreański dla wszystkich pozostałych)
- W każdym obsługiwanym języku sprawdź, czy **tekst nie wychodzi poza przyciski**

**Graj do końca i oszukuj**
- Zagraj **do ostatniego etapu**. Jeśli to trwa za długo, poproś AI o przeskok tylko do testów (tajfun na etapie 29)
- **Spróbuj oszukać warunek zwycięstwa:** stój w miejscu, jedź do tyłu, przejmij to, co przygotował ktoś inny (wpychanie się na pierwsze miejsce)
- Wpisz **0 albo wartość maksymalną** w ustawieniach liczbowych: 0 przeciwników, 0 sekund, maksymalny poziom (0 rywali, pojawiło się 3)

**Zasady sklepu**
- Szukaj słów takich jak **„kursy”, „zakład” czy „stawiać”**, przez które gra może wyglądać na hazardową (bukmacher)
- Usuń wszystkie **fałszywe zakupy, fałszywe reklamy i przyciski testowe** z czasu tworzenia (stuknij, a dostaniesz za darmo)

**Funkcje, które mogą być niedostępne**
- Poproś AI, żeby sprawdziła, czy **gra działa dalej, gdy opcjonalne funkcje, jak gamepady, wibracje czy powiadomienia, są zablokowane** (cała gra się zawiesiła)

### 3. Dwa zabezpieczenia na błędy, których nie widzisz

Po premierze błędy wychodzą na urządzeniach, w językach i na platformach, których nigdy nie widziałeś. Sperm Race ma teraz te dwa zabezpieczenia. Możesz poprosić o nie AI w ten sposób:

- **Przycisk zgłaszania błędów:** „Dodaj przycisk zgłaszania błędów na ekranie ustawień. Gdy ktoś zgłasza błąd, wyślij razem ze zgłoszeniem wersję gry, informacje o urządzeniu i ostatni błąd”. Cytując notatkę, którą zostawiła AI: „Mając razem wersję, urządzenie i ostatni błąd, zwykle da się od razu zawęzić przyczynę”.
- **Siatka bezpieczeństwa przed zawieszeniem:** „Jeśli podczas rysowania klatki wystąpi błąd, nie pozwól, żeby cała gra się zatrzymała, i zapisz ten błąd w logu. Opcjonalne funkcje, jak gamepady, po prostu po cichu pomijaj, jeśli nie działają”.

14 dni testów zamkniętych na początku wydawało mi się przykrym obowiązkiem. Teraz jestem za nie wdzięczny.

## Zagraj w Sperm Race

Sperm Race jest darmowa w Google Play. Jeśli trafisz na błąd, stuknij przycisk zgłaszania błędów na ekranie ustawień. Takie zgłoszenia to moja ulubiona rzecz.

- **Google Play**: [Sperm Race](https://play.google.com/store/apps/details?id=com.spermrace.game&hl=pl)
- **Wersja webowa (itch.io)**: [Sperm Race](https://johnisking.itch.io/sperm-race)

Ciekawi Cię, ile pieniędzy i czasu kosztuje gra zrobiona z AI? Wpisz gatunek i rozmiar swojej gry w [kalkulatorze kosztów gry z AI](/pl/ai-game-cost-calculator). I zaplanuj w harmonogramie czas na naprawianie błędów. Mnie zajęło to ponad cztery razy dłużej niż budowanie.
