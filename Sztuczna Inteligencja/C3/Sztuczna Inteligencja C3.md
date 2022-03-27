# Sztuczna Inteligencja C3
## Wojciech Adamiec, 310064
### Ćwiczenia 3

### Deklarowane Zadania: 1, 2, 4, 5, 6, 7, 10
### Suma punktów: 7

#### Zad. 1

##### Treść:
Przeczytaj i opowiedz o tym, czym sa algorytmy mrówkowe (ant colony algorithms).
Powiedz, jak zastosować je do rozwiązania problemu komiwojażera.

#### Rozwiązanie:

Algorytmy mrókowowe opierają się na ciekawym, zaobserwowanym w przyrodzie u mrówek zachowaniu. Kiedy mrówki wyruszają z mrowiska, aby przynieść pokarm działają według pewnego schematu:

1. Na początku mrówki rozdzielają się i szukają w różnych miejscach pokarmu (oraz wybierają różne drogi prowadzące do tych miejsc).
2. Mrówka idąc zostawia za sobą ślad feromonowy, który wyparowuje wraz z upływem czasu.
3. Ślady pozostawione przez mrówki, które poszły najbardziej optymalną ścieżką są bardziej intensywne (mniej czasu na naturalne parowanie feromonów).
4. Następne mrówki statystycznie częściej wybierą te ścieżki, na których ślad feromonowy jest intensywniejszy.
5. Ostatecznie zdecydowana większość mrówek będzie przemieszczać się na *feromonowej autostradzie*, która z dużym prawdopodobieństwem jest najbardziej optymalną ścieżką.

Chcemy użyć tego spostrzeżenia do rozwiązania problemu komiwojażera, którego wikipedyczna definicja jest taka: "Given a list of cities and the distances between each pair of cities, what is the shortest possible route that visits each city and returns to the origin city?".

Do znalezienia najkrótszego cyklu będziemy używać cyber-mrówek, które w przeciwieństwie do tych prawdziwych potrafią dodatkowo:

1. Pamiętać już odwiedzone miasta.
2. Widzieć odległości między miastami.

Algorytm będzie wyglądał w ten sposób:

1. (Ten punkt można na wiele sposobów wykonać) Ustawiamy w każdym mieście po $m$ nowych cyber-mrówek.
2. Każda mrówka będzie przemieszczać się między miastami, aż wykona cały cykl. Poruszanie odbywa się według zasad:
    1. Mrówka odwiedza każde miasto tylko raz.
    2. Mrówka wybiera częściej miasta, które są od niej bliżej.
    3. Mrówka wybiera częściej miasta, gdy na ścieżkach do nich prowadzących jest więcej feromonu.
3. Dla każdego wykonanego cyklu na drogach (z tego cyklu) pojawia się ilość feromonu uzależniona od sumarycznej długości cyklu (im krótszy cykl, tym więcej feromonu).
4. Na każdej drodze część feromonu wyparowuje.

W ten sposób po $n$ iteracjach w naszym grafie zacznie się *wyłaniać* optymalny cykl.
![alt text](https://i.imgur.com/EEi2Epu.png "Ant_colony_optimization_algorithms")


#### Zad. 2

##### Treść:
Podobnie jak burze, obrazki logiczne można również rozwiązać za pomocą więzów w Prologu. Opisz, jak modelować obrazki logiczne używając więzów dostępnych w SWI-Prologu (końcówka w4 oraz w5, możesz też skonsultować się z dokumentacją modułu clpfd w SWI-Prologu).

#### Rozwiązanie:

Dla każdego pixela tworzymy zmienną $Pij$ o dziedzinie $\{0, 1\}$. (Pixel zapalony lub nie).

Dla każdego rzędu oraz kolumny, których opis ma postać $(w_1, w_2, ..., w_n)$. Tworzymy $n$ zmiennych. Każdej z nich przyporządkowujemy odpowiednią dziedzinę - dla bloku długości $m$ dziedziną jest $\{ 0, 1, ..., (szerokość - 1) \}$.

Teraz będziemy chcieli zapewnić sobie właściwą kolejność: 
$\forall{i\in\{2, ..., n\}} \space \space w_i > w_{i-1} + len(w_n)$

Nie możemy wyjść poza obrazek:
$w_n + len(w_n) < szerokość$

Ostatni więz będziecie dotyczył korelacji między pixelami, a rzędami. Dla każdej zmiennej $w_i$, która reprezentuje blok pixeli odpowiednie pixele muszą być zapalone:

$P_{w_i,j} = 1, P_{w_i+1,j} = 1, ..., P_{w_i+len(w_i) - 1,j} = 1$

Analogicznie dla kolumn.

Możemy też skorzystać z *tuple_in*, które służy do podania wartości jakie może przyjmować krotka zmiennych. To znacząco może uprościć nasze zadanie:

Zmiennymi są teraz tylko wszystkie pixele.

Każdy wiersz (kolumna) jest krotką zmiennych, dziedziną są wtedy wszystkie możliwe ułożenia wiersza (kolumny), które spełniają informacje wejściowe $(w_1, w_2, ..., w_n)$. Wtedy musimy wygenerować wszystkie legalne kombinacje, ale za to mamy mniej zmiennych, i mniej więzów (nie musimy się już martwić o kolejność bloków, ani o wychodzenie poza granice). 

#### Zad. 3

##### Treść:
Rozważamy uproszczone zadanie układania planu lekcji, w którym (między innymi)
nie przejmujemy się dostępnością sal.
• Mamy pewną liczbę zajęć do rozmieszczenia.
• Każde zajęcia mają następujące parametry: klasa (w znaczeniu „grupa uczniów”) oraz nauczyciel.
• Każdemu zajęciu należy przypisać termin: liczbę od 1 do 50. Liczby od 1 do 10 oznaczają
poniedziałek, od 11 do 20 – wtorek, itd.
• Żadna klasa nie może mieć „okienka”, czyli przerwy w zajęciach. Czyli każdego dnia przychodzi na
jakąś godzinę, ma zajęte wszystkie kolejne godziny, a potem idzie do domu i do szkoły przychodzi
następnego dnia.
Przedstaw to zadanie jako problem więzowy, który da się wyrazić za pomocą konstrukcji dostępnych w
SWI-Prologu. Przy definiowaniu warunków na bezokienkowość planu możesz potrzebować dodatkowych
zmiennych.

#### Rozwiązanie:

#### Zad. 4

##### Treść:
Przedstaw zadanie układania planu zajęć w Instytucie Informatyki jako problem
spełnialności więzów, w którym oprócz twardych wymagań, określających jakie plany są dopuszczalne, istnieje funkcja określająca jakość dopuszczalnego planu i tym samym jesteśmy zainteresowani znalezieniem dopuszczalnego planu maksymalizującego tę jakość. Najważniejszą częścią tego zadania jest przedstawienie propozycji takiej funkcji, czyli próba precyzyjnego opisania, co sprawia, że jakiś plan jest lepszy od innego. Powinieneś uwględnić wyniki głosowania.

#### Rozwiązanie:

Więzy gwarantujące dopuszczalność planu zajęć:

1. Każdy przedmiot umiejscowiony jest między 8.00 a 20.00.
2. Profesor nie może jednocześnie prowadzić więcej niż jednego przedmiotu.
3. Obowiązkowe przedmioty dla danego semestru nie pokrywają się ze sobą.
4. Dane pomieszczenie (sala) nie może być jednocześnie używane do różnych zajęć.

Jakość planu zajęć będziemy oceniać biorąc pod uwagę następujące czynniki (kolejność jest istotna):

1. Obowiązkowe przedmioty nie pokrywają się ze sobą (W pierwszej kolejności wykłady, potem ćwiczenia).
2. Rozpatrujemy dla każdej pary przedmiotów ilość osób, które głosowały jednocześnie na oba przedmioty. Przedmioty o największej wspólnej grupie głosujących nie powinny ze sobą kolidować.
3. Dla tych samych przedmiotów staramy się możliwie unikać okienek (jeśli są tego samego dnia).
4. Piątek jest wolny od zajęć (jak najmniej przedmiotów).
5. Prowadzący nie powinni prowadzić zbyt wielu zajęć pod rząd (zmęczenie zmniejsza skuteczność).
6. Nie ma zajęć w godzinach *trudnych* to jest wcześnie rano lub późno wieczorem (jak najmniej przedmiotów).
7. Minimalna ilość studentów z długimi blokami zajęć jednego dnia.

#### Zad. 5

##### Treść:
Wybierz jedną z następujących gier: lis i gęsi, breakthrough (board game), pentago, skoczki (gra planszowa). Zaproponuj dla wybranej gry heurystyczną funkcję oceniającą sytuację na planszy. 

#### Rozwiązanie:
Zasady Gry:

The fox is placed in the middle of the board, and 13 geese are placed on one side of the board. The fox and geese can move to any empty space around them (also diagonally). The fox can jump over geese like in checkers, capturing them. Repeated jumps are possible. Geese can not jump. Capturing is not mandatory. The geese win if they surround the fox so that it cannot move. The fox wins if it captures enough geese so that the remaining geese cannot surround it.
![alt text](https://i.imgur.com/CRILIZI.png "Fox and Geese")

Nasza funkcja heurystyczna będzie brała pod uwagę 2 parametry:

1. Ilość żywych gęsi.
2. Ilość dostępnych ruchów lisa. Zauważmy, że lis potrafi wykonywać skoki (także skoki wielokrotne), w związku z tym sytuacja, w której lis jest okrążony z 7 "stron", ale ma do wyboru ruchy poprzez skoki, tak że można osiągnąć np. 4 różne stany końcowe jest lepszy niż gdyby miał obok siebie 3 "wolne" pola. 

#### Zad. 6

##### Treść:
Wybierz jedną z następujących gier: lis i gęsi, breakthrough (board game), pentago, skoczki (gra planszowa). Zaproponuj dla wybranej gry heurystyczną funkcję oceniającą sytuację na planszy. 

#### Rozwiązanie:

Celem gry jest przestawienie wszystkich swoich pionków na pozycje zajmowane na początku przez przeciwnika, czyli przeciwległe, skrajne dwie linie pól. Gracz, który pierwszy tego dokona − wygrywa. Nie ma możliwości gry remisowej.

![alt text](https://i.imgur.com/9w2GVWS.png "Skoczki")

Ruch polega na:

1. przesunięciu swojego pionka na dowolne sąsiednie pole wolne poziomo lub pionowo (do przodu, do tyłu lub na boki),
2. przeskoczeniu przez pionek własny lub przeciwnika z pola bezpośrednio sąsiadującego z przeskakiwanym pionem na pole bezpośrednio za nim,
3. przeskoczeniu kilku pionów swoich lub przeciwnika z pola bezpośrednio sąsiadującego z przeskakiwanym pionem na pole bezpośrednio za nim,
4. wykonaniu całej serii skoków jednym pionkiem zgodnie z dwiema poprzednimi zasadami – zmiana kierunku kolejnych skoków jest możliwa.

Pionki nie biją się wzajemnie.

Nasza funkcja heurystyczna będzie brała pod uwagę 3 parametry:

1. Sumaryczną odległość naszych pionów od docelowego rzędu (odległość w pionie) oraz jednocześnie analogiczną sumaryczną odległość, ale dla przeciwnika.
2. Nadmiar skoczków w kolumnie, każdy nadmiarowy (więcej niż 2) skoczek w dowolnej z kolumn wymaga co najmniej jednego ruchu, żeby to poprawić. Analogicznie liczymy ten nadmiar dla przeciwnika.
3. Najlepszy (dowolny z najlepszych) ruchów jakie możemy wykonać. Bierzemy pod uwagę czy taki ruch nie ułatwi przeciwnikowi wykonania względnie lepszego ruchu (niż jego najlepszy).


#### Zad. 7

##### Treść:
Rozważamy grę „kółko i krzyżyk z buczeniem”. Mamy zwykłą planszę do kółka i krzyżyka, dwóch graczy i serwer gry. Gracze zgłaszają propozycje ruchu do serwera gry (gracz A nie widzi propozycji gracza B i odwrotnie) i serwer albo przyjmuje ten ruch (jeżeli zaproponowane pole jest puste), albo buczy i gracz ma prawo do kolejnej próby (dowolnie wiele razy). Buczenie jest słyszalne dla obu graczy, niedozwolone jest powtarzanie jakiegoś ruchu (tzn. jak przy ruchu przeciwnika usłyszałem buczenie, to mogę założyć, że zdobył on dodatkową wiedzę, a nie że próbuje mnie zmylić). Oprócz tego to normalne kółko i krzyżyk (tzn. celem jest ustawienie 3 swoich znaków w wierszu, kolumnie lub na przekątnej). Zaproponuj agenta, który grałby w tę grę (możliwie dobrze). Oczywiście pierwszy gracz ma dużą przewagę (dlaczego?), więc zakładamy, że rozgrywka składa się z 2K partii, w których gracze rozpoczynają na zmianę. 

#### Rozwiązanie:

Zacznijmy od kilku obserwacji:
1. Grę można wygrać za pomocą 8 różnych ustawień.
2. Wszystkie pola można powartościować ze względu na ilość wygrywających ustawień, w których biorą udział.

![alt text](https://i.imgur.com/a2UqGE5.png "Kółko i Krzyżyk")

Od razu widać, że środek jest wyjątkowo cennym polem i gracz, który go kontroluje ma dużą przewagę nad przeciwnikiem. Jest to jeden z dwóch powodów, dla których gracz zaczynający ma dużą przewagę, wybierając jako pierwszy pole, może wybrać środek.

3. Potrzeba 3 pól, aby wygrać grę.

3 pola oznaczają co najmniej 3 ruchy, gracz zaczynący jako pierwszy wykona swój 3rd ruch, a tym samym może od razu zakończyć grę.

Po krótkiej analizie orientujemy się, że gracz zaczynający może przyjąć 2 strategie - ofensywną i defensywną. W ofensywnej naszym drugim polem będzie róg, a w defensywnej naszym drugim polem będzie bok. Strategia defensywna zapewnia, że niezależnie od przeciwnika nie możemy przegrać. Strategia ofensywna dopuszcza wariant, w którym przegrywamy (1/16 szansy w przypadku losowego przeciwnika). W przypadku strategii defensywnej nasza szansa na wygranie wynosi trochę ponad 5/8 na losowego przeciwnika oraz nie więcej niż 5/8 na racjonalnego przeciwnika. Dla wersji ofensywnej szansa na wygranie jest trochę większa.

W przypadku, gdy jesteśmy drudzy nie możemy liczyć na wygraną (zakładając, że przeciwnik przejął środek - prawdopodobieństwo nie większe niż 1/8). Będziemy zatem chcieli doprowadzić do remisu. Na początku oczywiście upewniamy się, że przeciwnik zabrał środek (jeśli nie to nasze szanse właśnie bardzo wzrosły, żaden normalny przecwnik nie odda środka). A następnie wybieramy losowo pola licząc na to, że zablokujemy przeciwnika. 

Głównym problemem w jednoznacznym wyborze strategii jest fakt, że dowolna strategia jest kontrowana przez inną. Wiedząc, że zaczynający jest ofensywny/defensywne można znacząco podnieść szansę na wygraną/remis grając jako drugi gracz. Podobnie grając jako pierwszy można zwiększyć szansę na wygraną, wybierając strategię, która kontruje drugiego gracza. (wybieranie boku lub rogu, zdanie fałszywe gdy przeciwnik losuje pole)

W przypadku rozgrywania większej ilości potyczek warto by zapamiętywać ruchy wykonywane przez przeciwnika i w przyszłych grach starać się skontrować jego strategię. Podobnie, aby przecwnik nie był w stanie łatwo odgadnąć naszej strategii warto wprowadzić do naszego algorytmu pewną losowość.

Zakładając, że jedyne sensowne strategie zaczynającego to ofensywna/defensywna to drugi gracz wiedząc, której strategii używa gracz pierwszy może albo doprowadzić do 100% remisu (defensywna) albo znacząco podnieść szasnę a wygraną/remis (ofensywna). Analogicznie gracz pierwszy wiedząc, którą strategie kontruje gracz drugi może zwiększyć szansę na wygraną do 100% (z ofensywnej na defensywną) oraz prawie 100% (z defensywnej na ofensywną).

#### Zad. 8

##### Treść:
Pokaż, że jeżeli graf MDP jest acykliczny, to (również dla γ = 1) alborytm Value Iteration
(Bellmana) znajduje optymalną politykę. Pokaż, jak znaleźć tę politykę w krótszym czasie.
1W znacznym stopniu analogicznych do przedstawionych w poprzednim zadaniu.

#### Rozwiązanie:

#### Zad. 10

##### Treść:
Dla algorytmów Alpha-Beta-Search oraz MCTS odpowiedz na pytania:
a) W jaki sposób można wykorzystać czas poświęcony na obliczenia najlepszego poprzedniego ruchu do obliczenia najlepszego bieżącego ruchu (zakładamy, że rozgrywamy tylko jedną partię).
b) W jaki sposób wykorzystać możliwość równoległego wykonywania kodu w celu poprawy jakości gry?

##### Rozwiązanie:
a) Gramy w ramach jednej partii, w pewnym ruchu $n$ używamy algorytmu AB-search (MCTS), żeby rozważyć, który ruch jest dla nas najkorzystniejszy. Rozwiniemy w ten sposób drzewo gry do pewnego momentu (to zależy od tego jaki mamy czas na podjęcie decyzji). Podejmujemy wtedy pewną (lokalnie korzystną decyzję), przecniwnik podejmuje następnie swoją. Jesteśmy teraz w drzewie gry 2 poziomy niżej w pewnym podrzewie, ale podczas wyliczania optymalnego ruchu już tutaj byliśmy, i mamy to podrzewo częściowo rozwinięte. Korzystamy z już wyliczonych wartości i zapominamy o reszcie drzewa. 

b) Zauważamy, że możemy wykonywać algorytmy równlegle dla różnych poddrzew, które nie wpływają na siebie bezpośrednio. Wszystkie informacje jakie przesyłamy *do góry* to zmiany zakresów przedziałów (AB-search) lub propagacja (MCTS), ale one nie wpływają na wyniki obliczeń z innych poddrzew (mogą jedynie wydłużyć ewentualnie obliczenia, jeśli np. informacja o ucięciu jakiejś gałęzi dotrze później niż zaczniemy gałęź rozwijać). 