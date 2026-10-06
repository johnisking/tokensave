Nie miałem żadnego doświadczenia w programowaniu. Nie wiedziałem nawet, czym jest „silnik gry”. Mimo to, opisując AI zwykłymi słowami, czego chcę, zrobiłem grę w 3 dni, a doprowadzenie jej do premiery kosztowało mnie **45 USD**. Tak wygląda vibe coding gra w praktyce – i odpowiedź na pytanie, jak zrobić grę bez programowania.

![Grafika promocyjna Sperm Race w Google Play](/blog-spermrace-feature-en.jpg)

To część 1 dziennika dewelopera Sperm Race – głupiej gry o wyścigu plemników.

- **Google Play**: [Sperm Race](https://play.google.com/store/apps/details?id=com.spermrace.game&hl=pl)
- **Wersja webowa (itch.io)**: [Sperm Race](https://johnisking.itch.io/sperm-race) – gra najpierw ukazała się na itch.io, a potem w Google Play.

## Jak „zróbmy prostą grę” zaprowadziło mnie aż do plemników?

Szukałem gry z jedną zasadą, którą każdy zna bez tłumaczenia – i tak doszedłem do plemnika płynącego do komórki jajowej.

Na początku cel był prosty: **„Po prostu zrób prostą grę”.**

Ale im dłużej myślałem o tym, co znaczy „prosta”, tym bardziej pierwotne stawały się moje pomysły. Gra z jedną zasadą. Gra, której nie trzeba tłumaczyć. Gra, którą wszyscy już znają. Idąc tym tropem do samego końca, dotarłem do **plemnika**. Płyń do przodu, dotrzyj do komórki jajowej, koniec. Jak się nad tym zastanowić, to jedyny wyścig, który każdy z nas już raz wygrał.

W chwili, gdy ta myśl przyszła mi do głowy, roześmiałem się na głos. **„Chwila, to jest zabawne”.**

Ta jedna reakcja wyznaczyła kierunek. Nie poważna gra, tylko głupkowata – taka, przy której uśmiechasz się pod nosem, gdy tylko ją zobaczysz.

## Czy trzeba znać silnik gry, żeby zrobić grę z AI?

Nie – ja zacząłem bez żadnego silnika i grę dało się uruchomić w przeglądarce już pierwszego dnia.

Nigdy nie napisałem ani linijki kodu. Nie wiedziałem, że istnieją silniki takie jak Unity czy Godot, nie mówiąc już o tym, do czego służą.

Zacząłem więc bez silnika. Napisałem do Claude (Sonnet) po koreańsku: „Chcę zrobić taką grę”, a w odpowiedzi dostałem jeden plik HTML, który działał od razu w przeglądarce. Później zapakowałem ten sam plik w aplikację na Androida i wrzuciłem do Google Play. Tworzenie przez opisywanie AI tego, czego chcesz, zamiast samodzielnego pisania kodu, ma dziś swoją nazwę: **vibe coding**. Z perspektywy czasu start bez żadnej wiedzy okazał się nawet szybszy. Nie było silnika do instalowania ani niczego do nauki, a grać mogłem już pierwszego dnia.

## Pierwszy prompt: „Chcę zrobić grę, w której plemnik płynie na spotkanie z komórką jajową”

To jedno zdanie dało pierwszą wersję. Na ekranie pojawił się plemnik, którym mogłem sterować palcem.

Problemem był ogonek. Sztywny jak patyk – bardziej zapałka niż plemnik. Więc drugą rzeczą, którą powiedziałem, było:

**„Dodaj falowanie ogonka”.**

![Po lewej: pierwsza wersja ze sztywnym ogonkiem. Po prawej: kolejna wersja z falującym ogonkiem](/blog-spermrace-tail.gif)

Po lewej sztywny ogonek z pierwszej wersji, po prawej kolejna wersja z falowaniem. Samo to, że ogonek zaczął się wić, sprawiło, że plemnik w końcu wyglądał na żywego. Tak narodził się główny bohater.

## Trzy dni dodawania, wycinania i dodawania od nowa

Potem nie mogłem przestać. Za każdym razem, gdy grałem w nową wersję, pojawiał się kolejny pomysł. Jeśli coś przyszło mi do głowy – dodawałem. Jeśli nie działało – wycinałem. A potem znowu dodawałem.

1. **„Zrób mapę”.** Teraz było gdzie pływać.
2. **„Dodaj też przeszkody”.** Kiedy pojawiło się coś do omijania, zrobiła się z tego gra. To dzisiejszy tryb Adventure.
3. **„Dodaj wyścigi plemników, jak prawdziwe wyścigi samochodowe”.** Tryb Racing z 3 okrążeniami toru.
4. **„Zrób tryb, w którym biegną same jak na wyścigach konnych, a ja ustawiam przeszkody”.** Wybierasz plemnika, któremu kibicujesz, i pomagasz mu wygrać przeszkodami. To tryb Derby.
5. **„Zrób tryb przetrwania, w którym uciekasz, z motywem raka”.** Omijasz komórki nowotworowe w labiryncie i przetrwasz 1 minutę i 30 sekund.

Daty plików, które zostały w moim folderze Pobrane, pokazują, jak szybko to szło. Pierwszy plik HTML dostałem we wczesnych godzinach 19 sierpnia, a do popołudnia następnego dnia pobrałem nową wersję **16 razy**. To „popraw to → pobierz nowy plik → zagraj” cztery lub pięć razy co pół dnia. W tym czasie kod urósł z 47 KB do 149 KB. 21 sierpnia robiłem już zrzuty ekranu do sklepu.

![Menu główne Sperm Race (obecna wersja – przycisk gry ze znajomymi doszedł po premierze)](/blog-spermrace-menu-en.jpg)

## Skąd wziąć grafikę i dźwięki, jeśli nie umiesz rysować?

Nie musisz – w tej grze całą grafikę i efekty dźwiękowe napisała w kodzie AI.

W tej grze nie ma ani jednego pliku graficznego. Postać, tła, tory i labirynty – wszystko narysował w kodzie Sonnet.

![Cztery tryby narysowane w całości w kodzie: Adventure, Racing, Derby, Survival](/blog-spermrace-modes.jpg)

Od lewej: Adventure, Racing, Derby, Survival. Plemnik to jedna elipsa i wijąca się linia, tor to gruba krzywa, a labirynt to świecące proste linie. W głupiej grze ta prostota naprawdę się sprawdziła.

Tak samo z efektami dźwiękowymi. Nie ma żadnych plików dźwiękowych – Sonnet zsyntetyzował dźwięki w kodzie. Jedyny plik audio w folderze gry to darmowa muzyka w tle z Pixabay.

## Pierwsza reakcja testerów: „To jest bardzo oryginalne”

Przed premierą pokazałem grę testerom. Usłyszałem: **„To jest bardzo oryginalne”.**

Pomysł, który zaczął się od „chwila, to jest zabawne”, okazał się zabawny nie tylko dla mnie.

Oto co było w grze w dniu premiery:

- 4 tryby: Adventure (120 etapów), Racing (3 okrążenia), Derby, Survival (przetrwaj 1 minutę i 30 sekund)
- 13 języków
- Sterowanie: przeciąganie, strzałki/WASD, gamepad

Gra wieloosobowa ze znajomymi (do 10 graczy w Derby, do 4 w pozostałych trybach) pojawiła się później, w aktualizacji po premierze.

## Ile kosztowała gra z AI? 45 USD

Łącznie 45 USD: 20 USD za miesiąc Claude Pro i 25 USD za rejestrację w Google Play – reszta była darmowa.

| Pozycja | Czego użyłem | Koszt |
|---|---|---|
| Kod | Subskrypcja Claude Pro (Sonnet) | 20 USD (jeden miesiąc) |
| Grafika | Narysowana w kodzie | 0 USD |
| Muzyka w tle | Darmowe utwory z Pixabay | 0 USD |
| Efekty dźwiękowe | Zrobione w kodzie | 0 USD |
| Premiera | Rejestracja dewelopera Google Play | 25 USD (jednorazowo) |
| **Razem** | | **45 USD** |

Teraz używam Claude Max 20×, ale Sperm Race powstała **w całości na planie Pro.** Skończyłem w ciągu miesiąca, więc zapłaciłem tylko za jeden miesiąc. Co dokładnie dają te plany, opisałem w artykule o [limitach Claude Pro i Max](/pl/blog/limity-claude-pro-max).

Dla porównania: jeśli wpiszesz małą grę do [kalkulatora kosztów gry z AI](/pl/ai-game-cost-calculator), standardowy zestaw (AI do grafiki i muzyki plus Claude Max) wychodzi 128–181 USD. Sperm Race kosztowała ok. 25–35% tej kwoty. Pełne zestawienie znajdziesz w artykule [ile kosztuje stworzenie gry z AI](/pl/blog/ile-kosztuje-gra-z-ai).

## Następnym razem

Na razie wygląda to tak: „AI zrobiła grę w 3 dni, proste”. Ale prawdziwa walka zaczęła się później. Budowanie zajęło 3 dni, naprawianie błędów – 14.

**Dalej: [3 dni budowania, 14 dni naprawiania błędów](/pl/blog/testy-zamkniete-google-play-14-dni)** – dlaczego AI grzebie w niewłaściwym kodzie, gdy prosisz ją „znajdź błąd”, i jak w końcu sam zacząłem szukać błędów, a AI je naprawiała.
