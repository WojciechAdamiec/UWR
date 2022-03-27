# Sztuczna Inteligencja C4
### Wojciech Adamiec
#### Zadania: 2, 3, 4, 8, 9
#### Pkt: 5


#### Zad. 1

##### Treść:

##### Rozwiązanie:

#### Zad. 2

##### Treść:
Tworzymy agenta grającego w karty. W tym celu często używanym pomysłem jest wielokrotne losowanie możliwego stanu gry (czyli bieżącego układu kart), znajdywanie najlepszego ruchu w tym stanie (używając metod rozwiązywania gier z jawnym stanem) i ostateczny wybór ruchu, który był najlepszy w największej liczbie losowań. Wyjaśnij:

1. Co oznacza losowanie możliwego stanu?
2. W jakich sytuacjach losowanie z poprzedniego punktu chcielibyśmy wykonywać przypisując stanom niejednakowe prawdopodobieństwa? Co można uzyskać i jakie problemy to rodzi? Co z grami z elementem licytacji?
3. Jakie aspekty gier karcianych pomijamy w tym podejściu?

##### Rozwiązanie:

1. O ile wiemy jakie karty mamy na ręce, nie wiemy (lub możemy nie wiedzieć) jakie karty dobrał na rękę inny gracz. Znając skład talii kart możemy rozważać potencjalne ręce innych graczy.
2. Być może zamiast symulować dokładny skład ręki przeciwnika lepiej z wyższego poziomu abstracji patrzeć na np. potencjalne kombinacje kart na rękach innych (np. ustawienia w pokerze). Wtedy chcemy optymalizować nasz algorytm, tak że bardzo dobrze bedzie radził sobie z statystycznie najczęstymi rękami innych graczy. Podobnie, jeśli w talii kart danego typu jest więcej niż jedna to z większym prawdopdoobnieństwem znajdzie się na ręce przeciwnika. W grach z elementami licytacji możemy dodatkowo brać pod uwagę *pewność siebie* przeciwników. Jeśli jakiś gracz np. w tysiącu bardzo agresywnie przeprowadza licytację to warto przede wszystkim rozważyć ręce, w których są wysokiej wartości ustawienia kart (inaczej racjonalny gracz nie grałby agresywnie).
3. Pomijamy aspekt znajomości składu talii - w wielu grach skład talii przeciwnika nie jest znany przed grą (np. Magic: The Gathering, Hearthstone), co znacząco utrudnia przewidywanie rąk przeciwników. Innym pomijanym aspektem jest możliwość współpracowania np. w Tysiącu, jeśli jakiś gracz jest bliski uzyskania tytułowego tysiąca warto porozumieć się z innymi graczami, aby uniemożliwić mu zwycięstwo.

#### Zad. 3

##### Treść:

Rozważmy grę oszust (zob. Cheat_(game) w Wikipedii). Gramy standardową talią 52
kart (asy są najniższymi kartami). Mamy k graczy, którym rozdane są wszystkie karty. Zaczyna rozdający, po czym gracze na zmianę „zagrywają” od 1 do 4 kart (przy czym zagrywają je koszulkami do góry, tak że nie są widoczne dla innych graczy). Celem jest pozbycie się wszystkich kart. Gracz zagrywając kartę (karty) mówi o ich wartości (na przykład mówi: zagrywam dwie siódemki). Można deklarować jedynie karty o równej wielkości, dodatkowo deklaracja powinna być starsza (bądź równa) deklaracji poprzedniego gracza.

Gracze mogą kłamać odnośnie tego, co rzucili. Po każdej zagrywce jest faza sprawdzania, w której kolejni gracze mogą spasować lub sprawdzić zagrywającego (ta faza albo zawiera k − 1 pasów, albo pewną liczbę pasów i pierwsze sprawdzenie). 

Jeżeli zagrywający kłamał, to zabiera wszystkie karty. Jeżeli zagrywający powiedział prawdę, to karty bierze sprawdzający. W obu przypadkach kolejny gracz kontynuuje rozgrywkę (ponieważ stos jest pusty, może wyrzucić karty o dowolnej wysokości, oczywiście wyrzucając karty może skłamać o ich wartości).

Zaproponuj dwóch przykładowych prostych agentów, grających w tą grę (dozwolone są tylko takie idee, co do których masz przekonanie, że dadzą lepszą grę od agenta w pełni losowego).

##### Rozwiązanie:

Będziemy rozważać dwóch agentów nazywanych: *Paranoik* i *Łgarz*. Dla obu agentów jednak warto zaimplementować kilka oczywistych mechanik:

1. Chemy zapisywać jakie karty wyrzuciliśmy (oraz co deklarowaliśmy w momencie ich rzucania). Chcemy spamiętywać wszystkie poprzednie deklaracje innych graczy. 
2. W momencie, gdy ktokolwiek sprawdza chcemy osobie, która kłamie (lub mówi prawdę) przypisać jakąś dodatkową wartość. W ten sposób będziemy śledzili wiarygodność poszczególnych graczy. (Być może informacja o tym, że ktoś nie kłamał pozwala wydedukować, że kłamał ktoś wcześniej. Jeśli to my sprawdzaliśmy i musieliśmy wziąć wszystkie karty ze stosu, to możemy znając kolejność kart odpowiednio zaktualizować wskaźniki wiarygodności)
3. Jeśli jesteśmy absolutnie pewni (skład naszej ręki, nasza osobista historia), że ktoś kłamie należy go po prostu sprawdzić.
4. Jeśli ktoś na pusty stos zadeklaruje kartę najwyższej wartości zawsze sprawdza.

Paranoik będzie unikał kłamania i jeśli prawdopodobieństwo tego, że ktoś inny kłamie jest wysokie oraz sytuacja Paranoika nie pozwala mu na wygraną bez kłamania będzie sprawdzał stos.

Paranoik:

1. Ocenia dostępne ruchy tak, że:
    1. Wyrzucenie karty mocniejszej od najsłabszej dopuszczalnej wiąże się z karą (liniowa zależność, rzucenie najsłabszej dopuszczalnej to 0, rzucienie kart o 1 starszej to -1 itd.) Modyfikator działa jednorazowo tylko dla najstarszej karty.
    2. Ilość wyrzucanych kart dodawana jest do oceny ruchu.
    Przykład.

    Na stosie jest 6. Mamy na ręce: 6, 7, 8 to wyrzucamy 6.
    Na stosie jest 6. Mamy na ręce: 6, 8, 8, 8 to wyrzucamy trzy 8.
2. Jeśli trzeba kłamać to wykonuje najmniej agresywne kłamstwo (wyrzuca tylko jedną kartę, deklaruje najniższą racjonalną wartość)
3. Kiedy ktoś wykonuje zagranie, które jest dowodem na to, że ktoś musiał skłamać analizuje historię rzucania karty danej wartości pod kątem potencjalnych kłamców. Na podstawie wskaźników wiarygodność ocenia kto prawdopodobnie dopuścił się kłamstwa i na tej podstawie potencjalnie podejmuje decyzję czy chce sprawdzić stos. Jeśli ręka Paranoika jest *wygrywająca* to nie będzie podejmował zbędnego ryzyka.

Łgarz będzie kłamał, jeśli to sensowne. Będzie unikał sprawdzania stosu (chyba, że ma pewność)

Łgarz:

1. Ocenia dostępne ruchy tak, że:
    1. Wyrzucenie karty mocniejszej od najsłabszej dopuszczalnej wiąże się z karą (liniowa zależność, rzucenie najsłabszej dopuszczalnej to 0, rzucienie kart o 1 starszej to -1/2 - słabsza kara niż poprzednio) Modyfikator działa jednorazowo tylko dla najstarszej karty.
    2. Ilość wyrzucanych kart dodawana jest do oceny ruchu.
    3. Po wybraniu ruchu deklarujemy to co wybraliśmy, ale na stos wyrzucamy z dużym prawdopodobieństem najgorsze karty z ręki.
2. Jeśli trzeba kłamać z innego powodu niż w podpunkcie 1. to wykonuje najmniej agresywne kłamstwo (wyrzuca tylko jedną kartę, deklaruje najniższą racjonalną wartość)

Agent łączący sensownie obie strategie prawdopodobnie byłby lepszy niż każdy z osobna.

#### Zad. 4

##### Treść:

Potestuj playground.tensorflow.org. Odpowiedz na pytania:
1. Dla jakich zbiorów danych i jakich cech wystarcza 1 neuron do poprawnej klasyfikacji?
2. Co dzieje się, gdy dla bardziej złożonych sieci damy zbyt duży Learning rate?
3. W którym zadaniu przydają się cechy sin i cos?
4. Dla każdego zbioru danych (oprócz spirali) powiedz, jaka najprostsza sieć neuronowa korzystająca tylko z cech $x_1$ i $x_2$ poprawnie klasyfikuje ten zbiór danych.

##### Rozwiązanie:

Układy będziemy nazywać: Koło, Kratka, 2 kupki, Spirala.
Za poprawną klasyfikację uznajemy *test loss* na poziomie mniejszym niż 0.01. 
Sieci uczone na 70% danych.
1. Dla dwóch kupek wystarcza tylko $x_1$ lub $x_2$. Dla kratki wystarczy $x_1x_2$. 
2. Sieć będzie bardzo niestabilna, gwałtowne zmiany uniemożliwią zbliżenie się niskiej wartości *test loss*.
3. W układzie ze spiralą.
4. Dla koła: 1 ukryta warstwa z 3 neuronami; Dla kratki: 1 ukryta warstwa z 5 neuronami; Dla dwóch kupek: tylko 2 wejściowe neurony.

#### Zad. 5

##### Treść:

##### Rozwiązanie:

#### Zad. 6

##### Treść:

##### Rozwiązanie:

#### Zad. 7

##### Treść:

##### Rozwiązanie:

#### Zad. 8

##### Treść:
Co to jest nadracjonalność (superrationality)?

##### Rozwiązanie:

Nadracjonalność to założenie, że przeciwnik przeprowadza identyczne rozumowanie jak my i szukanie strategii, która daje najlepsze wyniki przy tym założeniu. (Chcemy maksymalizować nasze *utility*)

W przypadku *Dylematu więźnia* gracze nadracjonalni będą ze sobą współpracować, bo to daje sumarycznie najlepszy wynik, mimo iż indywidualnie współpraca nikomu się nie opłaca.

Założenie nadracjonalności w przypadku, gdy przeciwnik będzie zachowywał się racjonalnie zwykle kończy się przegraną (np. iteracyjny dylemat więźnia dla 2 graczy).

#### Zad. 9

##### Treść:
Wyjaśnij, co to jest punkt równowagi Nasha. Opowiedz, na czym polega gra w Dylemat więźnia i jaki jest dla niej punkt równowagi Nasha. Jak twórca agenta grającego w tę grę mógłby wykorzystać to, że prawdziwe są następujące fakty:
1. Jest wielu graczy, każdy gra w tę grę wiele razy, w różnych parach.
2. Każdy gracz przedstawia się przed rozgrywką swoim unikalnym identyfikatorem
3. Liczy się sumaryczny wynik wielu rozgrywek.

##### Rozwiązanie:

Dylemat Więźnia:

Dwóch podejrzanych zostało zatrzymanych przez policję. Policja, nie mając wystarczających dowodów do postawienia zarzutów, rozdziela więźniów i przedstawia każdemu z nich tę samą ofertę: jeśli będzie zeznawać przeciwko drugiemu, a drugi będzie milczeć, to zeznający wyjdzie na wolność, a milczący dostanie dziesięcioletni wyrok. Jeśli obaj będą milczeć, obaj odsiedzą 6 miesięcy za inne przewinienia. Jeśli obaj będą zeznawać, obaj dostaną pięcioletnie wyroki. Każdy z nich musi podjąć decyzję niezależnie i żaden nie dowie się, czy drugi milczy czy zeznaje, aż do momentu wydania wyroku. Jak powinni postąpić?

Punkt równowagi Nasha:

Sytuacja, w której strategia każdego z graczy jest optymalna, przyjmując wybór jego oponentów za ustalony. Żaden z graczy nie ma powodów jednostronnie odstępować od strategii równowagi. Ta równowaga jest stabilna.

Dla gry dwuosobowej: Wybieram to, co jest dla mnie najlepsze, gdy ty robisz to, co robisz; ty robisz to, co jest dla ciebie najlepsze, gdy ja robię to, co robię.

Iteracyjny dylemat więźnia:

Grając skończoną i określoną ilość gier, gdy w turnieju biorą udział tylko 2 osoby jedyną sensowną strategią jest *Zawsze zdradzaj*.

Dla więcej niż dwóch osób sytuacja jest inna, możemy śledzić wyniki gier i każdemu graczowi przyporządkować wskaźnik jest wiarygodności. Na tej podstawie można wnioskować jak bardzo ktoś jest skłonny do współpracy.

Przykładowy agent (wet za wet z wybaczaniem):
W pierwszej rundzie idzie na współpracę, w każdej kolejnej wykonują tą samą akcje co aktualny przeciwnik w poprzedniej rundzie. Z niewielkim prawdopodobieństwme wybacza przeciwnikowi i idzie tak czy siak na współpracę.