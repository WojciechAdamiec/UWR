# Sztuczna Inteligencja C2
### Wojciech Adamiec, 310064
### Lista Ćwiczeniowa 2

#### Zad. 1
##### Treść:
Na wykładzie 3 (ostatnie slajdy) była podana informacja o najlepszych heurystykach dla 15-ki. Przypomnij te heurystyki i zaproponuj przeniesienie ich idei do zadania o Sokobanie.

##### Rozwiązanie:
Najlepsze heurystyki dla 15-tki opierają się na *Bazie Wzorców*. Polega to na spamiętywaniu kosztów rozwiązań dla podproblemów zadania, a następnie zwracania maksimum kosztów.

W przypadku np. 8-ki podproblemami mogły być: znalezienie kosztów rozwiązań dla kafelków 1, 2, 3, 4 oraz 5, 6, 7, 8 przy założeniu że uporządkowanie pozostałych kafelków nie ma znaczenia.

![alt text](https://i.imgur.com/EnMKVAz.png "Obrazek z Wykładu 3")

W zadaniu o Sokobanie podproblemem będzie przeniesienie danej skrzynki na najbliższe pole docelowe. W tym celu będziemy wykonywać BFS dla ruchów skrzynki, w którym będziemy: Ignorować położenie pozostałych skrzynek, Ignorować położenie magazyniera. Jako dopuszczalny ruch będziemy uznawać każdy ruch na wolne pole, który dałoby się wykonać przy pomocy magazyniera (a zatem skrzynka przy ścianie z lewej strony - nie może poruszyć się w prawo). Dodatkowo, jeśli skrzynka znajduje się w rogu i ów róg nie jest miejscem docelowym to heurystyka będzie zwracać $\infty$. Podobnie skrzynka będąca przy ścianie (z której nie da się już "odkleić"), przy której nie ma miejsca docelowego będzie również mieć heurystykę równą $\infty$.

#### Zad. 2
##### Treść:
Zaproponuj jakąś końcówkę szachową (zawierającą skoczki i/lub gońce), w której możliwy jest mat kooperacyjny. Bądź przygotowany, by wszystko wyjaśnić osobom nie znającym szachów. Podaj dla tej końcówki optymistyczną (i użyteczną) funkcję heurystyki.

##### Rozwiązanie:
Będziemy rozważać końcówkę szachową, w której czarny gracz ma tylko króla, a biały gracz -  króla oraz 2 gońce (na polach różnego koloru).

Warto odnotować, że w przypadku *świadomego* gracza taka końcówka jest nierozstrzygalna. Kiedy jednak interesuje nas *mat kooperacyjny* rozwiązanie istnieje. W każdym macie czarny król musi znajdować się w rogu i musi być *bity* przez gońca:

![alt text](https://i.imgur.com/dzK1APm.png "Przykładowy Mat")

Nasza heurystyka będzie sumą kilku składników:
* Odległość czarnego króla od najbliższego rogu
* Odległość białego króla od czarnego króla - 2
* 1, jeśli czarny król *bije* gońca znajdującego się na polu drugiego koloru
* 1, jeśli goniec tego samego koloru co czarny król nie *bije* czarnego króla

Heurystyka ta jest istotnie optymistyczna, dla każdego ustawienia szachowego czarny król musi co najmniej przejść do najbliższego rogu, biały król musi co najmniej zrobić tyle kroków aby znaleźć się w odległości 2 od czarnego króla. Jeśli żaden z gońców nie bije króla, to potrzeba co najmniej ruchu, aby to poprawić. Jeśli żaden goniec przeciwnego koloru co czarny król jest przez tego króla bity, to musi co najmniej w 1 ruchu się cofnąć.

Twierdzę, że ta heurystyka jest użyteczna, na pewno $A*$ przy jej użyciu będzie działał zdecydowanie szybciej niż zwykły BFS. Jednocześnie obliczanie heurystyki sprowadza się do wykonania kilku działań i przejścia kilku *if'ów*, jest zatem stosunkowo tanie.

#### Zad. 3

#### Zad. 4
##### Treść:
W zadaniu rozważymy ogólną metodę binaryzacji, dla więzów, które są zdefiniowane za pomocą wyrażeń arytmetycznych i symboli relacyjnych (przykładowo $2A+ 4B > 7C + D^2 +EF +G^3$). Pokaż, jak zamieniać takie więzy na więzy o arności 2 lub 3 (być może dodając nowe zmienne, pamiętaj o tym, że nowe zmienne muszą mieć dziedziny). A następnie pokaż, jak eliminować więzy o arności 3 (zamieniając je na binarne).

##### Rozwiązanie:
Będziemy od razu zamieniać więzy arności 3 i więcej na binarne. Skupmy się na pojedynczym więzie $n$-arnym ($n \geq 3$). Nazwijmy go $W$. Idea polega na wprowadzaniu w jego miejsce nowej zmiennej $U$, której dziedziną $D(U)$ będzie produkt kartezjański $D(X_1)\times D(X_2) \times ...\times D(X_n)$ dziedziń wszystkich zmiennych związanych w $W$. Wówczas wartości nowej zmiennej będą krotkami skontruowanymi w taki sposób, że na $i$-tej pozycji znajduje się wartość z $D(X_i)$.

Zauważmy, że w ten sposób możemy dowolny $n$-arny więz zamienić na odpowiadający mu unarny więz wiążący nową zmienną zawierającą krotki  wszystkich indywidualnych zmiennych. Możemy od razu przeprowadzić wnioskowanie na unarnym więzie i ograniczyć dziedzinę nowej zmiennej.

Teraz pozostaje jeszcze zdefiniować nowe więzy, to jest - $c(U, X_1), c(U, X_2), ..., c(U, X_n)$. Robimy to w taki sposób, że dla $i = 1, 2, ..., n$:
$c(U, X_i)$ to po prostu $X_i=ity:element(U).$

Przykład:
Zmienne: $X[1, 2]$, $Y[3,4]$, $Z[5,6]$, więzy: $X+Y=Z$, $X<Y$.
Chcemy zbinaryzować więz $X+Y=Z$:

W tym celu tworzymy nową zmienną $U$ o dziedzinie $D(X)\times D(Y)\times  D(Z)$:
$[(1,3,5),(1,3,6),
 (1,4,5),(1,4,6),
 (2,3,5),(2,3,6)
 (2,4,5),(2,4,6)]$
 
Zauważmy, że teraz first($u \in U$) jest teraz równoważny z dawnym $x\in X$. Analogicznie second($u \in U$) jest równoważne z $y \in Y$ i third($z \in Z$) jest równoważne z $z \in Z$.

Następnie przeprowadzamy wnioskowanie na podstawie więzu $X+Y=Z$, przy czym używamy równoważnym im odpowiadającym pozycjom w krotkach. Dzięki temu zmniejszamy dziedzinę $U$ do:
$[(1,4,5),(2,3,5),(2,4,6)]$

![alt text](https://i.imgur.com/AbBXAkM.png "Wizualizacja grafu")



#### Zad. 5

#### Zad. 6

#### Zad. 7

#### Zad. 8
##### Treść:
Opisz poniższe algorytmy (możesz użyć nazw, jeżeli znasz):
a) local beam search dla $k = 1$,
b) local beam search z jednym początkowym stanem i bez limitu na  liczbę zachowanych stanów po generacji następnika,
c) symulowane wyżarzanie z $T = 0$ przez cały czas działania algorytmu,
d) symulowane wyżarzanie z $T = \infty$ przez cały czas działania algorytmu,
e) algorytm genetyczny z populacją wielkości $1$.
Odpowiedzi uzasadnij.

##### Rozwiązanie:

a) Hill Climbing. Pamiętamy tylko jeden stan (aktualny). Generujemy wszystkie stany do których którzych możemy przejść i wybieramy z nich 1 lidera - czyli przechodzimy do najlepszego następnika.

b) BFS. W każdym ruchu zapamiętujemy kolejne stany oddalone coraz dalej od stanu początkowego. Pamiętamy wszystkie odwiedzone stany i wybieramy wszystkie jako liderów (k jest nieogranczone).

c) First Choice Hill Climbing. Dla zerowej temperatury mamy zerową szansę na podjęcie ruchu pogarszającego sprawę. (takiego, że $\Delta F \leq 0$)

d) Losowe błądzenie po przestrzeni stanów. DFS bez spamiętywania już odwiedzonych stanów.

e) Hill Climbing. Ewolucja dla populacji wielkości 1 nie może się skrzyżować (lub krzyżowania martwe), więc dostajemy local beam search dla $k=1$, czyli jak w pierwszym podpunkcie: Hill Climbing.

#### Zad. 9