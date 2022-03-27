# ASK Lista 11 - Wojciech Adamiec
## Zadania Deklarowane:  1, 2, 3, 4, 5, 7

### Zadanie 1.
:::info
![](https://i.imgur.com/LSryS3s.png)
:::

![](https://i.imgur.com/wJlXEe9.png)

Offset zapisywany jest na $5$ bitach, a więc jego maksymalna wartość (pamiętając, że offset jest zawsze `unsigned int`) to $11111_{2} = 31$. Stąd mamy, że blok ma $32$ bajty, a więc zmieści się 8 $32$-bitowych słów.

W pamięci podręcznej z mapowaniem bezpośrednim mamy tyle samo zbiorów co wierszy/linii, a więc musimy spojrzeć na bity $\text{index}$. Jest ich $5$, podobnie jak przy bitach przesunięcia, a więc są $32$ różne możliwości, stąd mamy $32$ wiersze w pamięci podręcznej.

Przechowujemy dane w $8 \cdot 32 = 256$ bitach, a metadane zajmują kolejno $22$ bity na tag oraz $1$ valid bit. Mamy więc stosunek $\frac{23}{279} \sim 0,0825$.

### Zadanie 2.
:::info
![](https://i.imgur.com/XA7fiwv.png)
:::

Pracujemy na systemie z sekcyjno-skojarzeniową pamięcią podręczną, w której każdy zbiór ma $2$ wiersze, a blok $4$ bajty. Szerokość szyny adresowej wynosi $12$ bitów. 

Na podstawie tabelki z określonym stanem pamięci podręcznej mamy określić które bity adresu wyznaczają offset, indeks oraz tag. Skoro blok zajmuje $4$ bajty, to $B = 4 = 2^b \Rightarrow b = 2$, to offset będzie na bitach $a_1, a_0$. Indeksy w naszej pamięci są z zakresu od $0$ do $3$, a więc można je przedstawić na dwóch bitach, stąd będą to bity $a_3, a_2$. Pozostałe bity będą zarezerwowane na tag. Przedstawia to tabelka poniżej:


| $a_{11}$ | $a_{10}$ | $a_9$ | $a_8$ | $a_7$ | $a_6$ | $a_5$ | $a_4$ | $a_3$ | $a_2$ | $a_1$ | $a_0$ |
|  :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| t        | t        | t     | t     | t     | t     | t     | t     | i     | i     | o     | o     |

Kolejnym zadaniem jest określenie czy operacja na danym adresie wygeneruje trafienie lub chybienie. Najłatwiej jest to sprawdzić zmieniając adresy (a dokładniej ostatnią cyfrę) na system binarny, a następnie dopasować dane do tych, które znajdują się w tabelce.

Znacznik `83` pokrywa się w pierwszych dwóch adresach, musimy więc sprawdzić wartość ostatniej cyfry w systemie szesnastkowym. W pierwszym przypadku $2_{16} = 0010_{2}$, a więc sprawdzamy pierwszy zbiór (o indeksie $0$), a następnie wybieramy blok z przesunięciem $10_{2}$, czyli B2. Otrzymujemy wartość `0xCC`. Drugi adres jest w zbiorze o indeksie $1$, jednak nie ma tam żadnej wartości, więc chybimy. Ostatnim adresem jest `0xFFD`, jest to zbiór o indeksie $3$, znaczniku `0xFF` i przesunięciu $01_{2}$ (blok B1), a więc trafiamy w wartość `0xC0`.

| Adres HEX |    Adres BIN     | Trafienie? | Wartość |
|:---------:|:----------------:|:----------:|:-------:|
|  `0x832`  | `1000 0011 0010` |     Tak    | `0xCC`  |
|  `0x835`  | `1000 0011 0101` |     Nie    |   $-$   |
|  `0xFFD`  | `1111 1111 1101` |     Tak    | `0xC0`  |

### Zadanie 3.
:::info
![](https://i.imgur.com/zwXKkvO.png)
:::

**Compulsory miss** - zachodzi, gdy pytamy o blok po raz pierwszy(pierwszy raz go ściągamy z pamięci).

**Conflict miss** - zachodzi wtedy, gdy bloki danych należą do tego samego seta i się nadpisują nawzajem ze względu na zbyt małą pojemność setu.

Blok zostaje **zastąpiony** gdy dochodzi do chybienia, wtedy kontroler pamięci podręcznej musi wybrać blok, który zostanie zastąpiony nowymi danymi. W rozwiązaniu zastąpienie bloku występuje na dwa możliwe sposoby: przy pierwszym zapisie zastępywany jest pusty blok, a przy kolejnych zapisach ten, który był używany najdawniej (LRU), stąd w naszej pamięci wszystkie bloki zostały zastąpione i wskaźnik trafień wynosi $0\%$.


|  #  |  Adres  | Tag  | Set | Offset |    Krotki    |   Trafienie?    | Zastąpiony? |
|:---:|:-------:|:----:|:---:|:------:|:------------:|:---------------:|:-----------:|
|  1  | `0x000` | `00` | `0` |  `0`   | `(00, 0, 0)` |       compulsory miss       |     tak     |
|  2  | `0x004` | `00` | `1` |  `0`   | `(00, 1, 0)` |       compulsory miss       |     tak     |
|  3  | `0x010` | `01` | `0` |  `0`   | `(01, 0, 0)` | compulsory miss |     tak     |
|  4  | `0x084` | `08` | `1` |  `0`   | `(08, 1, 0)` | compulsory miss |     tak     |
|  5  | `0x03C` | `03` | `3` |  `0`   | `(03, 3, 0)` | compulsory miss |     tak     |
|  6  | `0x0E8` | `0E` | `2` |  `0`   | `(0E, 1, 0)` | compulsory miss |     tak     |
|  7  | `0xC8C` | `C8` | `3` |  `0`   | `(C8, 3, 0)` | compulsory miss |     tak     |
|  8  | `0x0A0` | `0A` | `0` |  `0`   | `(0A, 0, 0)` | compulsory miss |     tak     |
|  9  | `0x004` | `00` | `1` |  `0`   | `(00, 1, 0)` |  hit  |     nie     |
| 10  | `0x400` | `40` | `0` |  `0`   | `(40, 0, 0)` | compulsory miss |     tak     |
| 11  | `0x084` | `08` | `1` |  `0`   | `(08, 1, 0)` |  hit  |     nie     |
| 12  | `0x010` | `01` | `0` |  `0`   | `(01, 0, 0)` |  conflict miss  |     tak     |
| 13  | `0x0E8` | `0E` | `2` |  `0`   | `(0E, 2, 0)` | hit |     nie     |
| 14  | `0x884` | `88` | `1` |  `0`   | `(88, 1, 0)` | compulsory miss |     tak     |
| 15  | `0xC8C` | `C8` | `3` |  `0`   | `(C8, 3, 0)` |       hit       |     nie     |
| 16  | `0x000` | `00` | `0` |  `0`   | `(00, 0, 0)` |  conflict miss  |     tak     |



| Index    | tag      |    valid | victim |
| -------- | -------- | -------- |------- |
| 0        | 01       | 1        |0       |
| 0        | 00       | 1        |1       |
| 1        | 08       | 1        |1       |
| 1        | 88       | 1        |0       |
| 2        | 0E       | 1        |0       |
| 2        | 00       | 0        |1       |
| 3        | C8       | 1        |0       |
| 3        | 03       | 1        |1       |



Ile było chybień przymusowych? odp: 12
Hit ratio: 25%

Na wyznaczenie potencjalnej ofiary potrzebujemy 1 bitu na zbiór, ponieważ musimy pamiętać tylko która była ostatnio użyta, a zbiór ma 2 linie. Czyli kiedy wrzucamy do zbioru blok do linii 0, ten bit ustawiamy na 1, a kiedy do pierwszej to na 0. 

### Zadanie 4.
:::info
![](https://i.imgur.com/JIxuHPS.png)
:::

![](https://i.imgur.com/mGdTunq.png)
![](https://i.imgur.com/d5swamp.png)

In a fully associative cache, the cache is organized into a single cache set with multiple cache lines. A memory block can occupy any of the cache lines. The cache organization can be framed as (1*m) row matrix.

|  #  |  Adres  | Tag  | Offset |    Krotki    |   Trafienie?    | Zastąpiony? |
|:---:|:-------:|:----:|:------:|:------------:|:---------------:|:-----------:|
|  1  | `0x000` | `0000 0000 00` |  `0`   | `(00, 0)` |       compulsory miss       |     tak     |
|  2  | `0x004` | `0000 0000 01` |  `0`   | `(01, 0)` |       compulsory miss       |     tak     |
|  3  | `0x010` | `0000 0001 00` |  `0`   | `(04, 0)` | compulsory miss |     tak     |
|  4  | `0x084` | `0000 1000 01` |  `0`   | `(21, 0)` | compulsory miss |     tak     |
|  5  | `0x03C` | `0000 0011 11` |  `0`   | `(0F, 0)` | compulsory miss |     tak     |
|  6  | `0x0E8` | `0000 1110 10` |  `0`   | `(3A, 0)` | compulsory miss |     tak     |
|  7  | `0xC8C` | `1100 1000 11` |  `0`   | `(323, 0)` | compulsory miss |     tak     |
|  8  | `0x0A0` | `0000 1010 00` |  `0`   | `(28, 0)` | compulsory miss |     tak     |
|  9  | `0x004` | `0000 0000 01` |  `0`   | `(01, 0)` |  hit  |     nie    |
| 10  | `0x400` | `0100 0000 00` |  `0`   | `(100, 0)` | compulsory miss |     tak     |
| 11  | `0x084` | `0000 0100 01` |  `0`   | `(11, 0)` |  hit  |     nie     |
| 12  | `0x010` | `0000 0001 00` |  `0`   | `(04, 0)` |  hit  |     nie     |
| 13  | `0x0E8` | `0000 1110 10` |  `0`   | `(3A, 0)` | hit |     nie     |
| 14  | `0x884` | `1000 1000 01` |  `0`   | `(221, 0)` | compulsory miss |     tak     |
| 15  | `0xC8C` | `1100 1000 11` |  `0`   | `(323, 0)` |       hit       |     nie     |
| 16  | `0x000` | `0000 0000 00` |  `0`   | `(00, 0)` |  conflict miss  |     tak     |

|Age bits| Adres     |    valid |
|-| --------- | -------- |
|7| 0x000     | 1        |
|6| 0xC8C     | 1        |
|5| 0x884     | 1        |
|4| 0x0E8     | 1        |
|3| 0x010     | 1        |
|2| 0x084     | 1        |
|1| 0x400     | 1        |
|0| 0x004       | 1        |


Ile było chybień przymusowych? odp: 10
Hit ratio: 31,25%

Dla każdej linii musimy pamiętać "age bits" log(liczba linii).
3*8 = 24

### Zadanie 5.
:::info
![](https://i.imgur.com/clgeeyf.png)
:::

Źródła: [pytanie pierwsze](https://courses.cs.washington.edu/courses/cse351/10sp/sections/section7-ppham-boards.html), [pytanie drugie](https://softwareengineering.stackexchange.com/questions/44731/why-are-there-separate-l1-caches-for-data-and-instructions).

Używane bity do wyboru zbioru (set index bits) są podstawową "restrykcją" mówiącą o tym, gdzie znajdują się dane w pamięci podręcznej. Gdyby te bity były ułożone na najbardziej znaczących bitach adresu, wtedy bardzo rozległe adresy odwoływałyby się do tego samego zbioru, powodując problemy - między innymi przez wiele chybień spadłaby wydajność cache.
![](https://i.imgur.com/OPGIIqe.png)


Aby odpowiedzieć na drugie pytanie, spójrzmy na hierarchię pamięci procesora Intel Core i7:
![](https://i.imgur.com/nKh4s6f.png)
Możemy zauważyć, że pamięć podręczna L1 jest podzielona na pamięć przeznaczoną dla danych (d-cache) oraz instrukcji (i-cache). Taki podział powstał ze względu na to, że w ogólności te dwie rzeczy są od siebie różne: cache instrukcji oprócz swoich danych przechowuje również przypisy o np. miejscu rozpoczęcia kolejnej instrukcji. 

Kolejnym powodem jest możliwość uproszczenia budowy obwodu, gdyż cache instrukcji tylko odczytuje dane, gdy cache danych może je zapisywać i odczytywać.

Trzecim powodem jest zwiększenie przepustowości. Nowoczesne procesory mogą jednocześnie odczytywać dane z cache'u instrukcji oraz danych. 

### Zadanie 6.
:::info
![](https://i.imgur.com/nAXy0gU.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/WIFUn0f.png)
:::

Średni czas dostępu do procesora tylko z pamięcią podręczną L1:
$$t_{\text{avg}} = \text{wsp. trafien} \times \text{czas L1} + \text{wsp. chybien} \times (\text{czas L1 + czas pamieci glownej}) =\\
= 0.92 \cdot 0.66 ns + 0.08 \cdot (0.66 ns + 70ns) = 6.26 ns = 9.48 \text{ cykli}$$

Średni czas dostępu do procesora z pamięcią podręczną L1 i L2 (wzór analogiczny do powyższego, uwzględniamy jezscze dostęp do L2):
$$t_{\text{avg}} = 0.92 \cdot 0.66ns + 0.08 \cdot 0.995 \cdot (0.66 ns + 5.62 ns) + \\ + 0.08 \cdot 0.005 \cdot (0.66 ns + 5.62 ns + 70 ns) = 1.1376 ns = 2.14 \text{ cykli}$$

**CPI** *(ang. clocks per instruction)* to jeden z aspektów określających wydajność procesora, określa on liczbę potrzebnych cykli zegarowych na wykonanie instrukcji.

CPI dla pamięci podręcznej L1:
$$CPI_{L1} = \text{wsp. instrukcji} \times \frac{\text{ilosc cykli}}{\text{instrukcja}} + \text{wsp. dostepow do pamieci} \times t_{\text{avg} (L1)} = \\
= 0.64 \cdot 1 + 0.36 \cdot 9.48 \approx 4.0528 \text{ cykli}$$

Jest 0.36 bo 36% wszystkich instrukcji stanowią dostępy do pamięci, a 0.64 * 1 bo 64% to operacje bez dostępu do pamięci, czyli dla nich CPI to 1.

CPI dla pamięci podręcznej L1 z L2 (wzór identyczny jak wyżej):
$$CPI_{L1 + L2} = 0.64 \cdot 1 + 0.36 \cdot 2.14 \approx 1.41 \text{ cykli}$$

### Zadanie 8.
:::info
![](https://i.imgur.com/1EjieNy.png)
:::