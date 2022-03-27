# ASK Lista 10 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 4, 6, 7?, 8?

### Zadanie 1.
:::info
![](https://i.imgur.com/p6xLKWs.png)
:::

![](https://i.imgur.com/GUN91CL.png)

**Czas wyszukiwania** - Aby odczytać zawartość jakiegoś sektora docelowego, ramię najpierw ustawia głowę nad ścieżką, która zawiera sektor docelowy. Czas potrzebny do przesunięcia ramienia nazywany jest czasem wyszukiwania. 
**Czas opóźnienia obrotowego** - Czas oczekiwania, aż pierwszy bit sektora docelowego przejdzie pod głowicą, gdy głowica znajdzie się nad ścieżką.
**Czas transferu sektora** - Czas, za który zawartość sektora będzie przeczytana lub zapisana.

1. $T_{seek-max}=\frac{400}{50}=8ms$
    $T_{seek-min}=0 ms$
    $T_{seek-avg}=2.66 ms$

**Pytanie:** Czy to jest liniowa zależność? Chyba nie. (Jeśli tak to $T_{seek-avg}=4 ms$). https://math.stackexchange.com/questions/195245/average-distance-between-random-points-on-a-line-segment

2. res = $T_{max} / 2$
![](https://i.imgur.com/x7zyRBG.png)
$T_{max} = 60s/7200$
czyli 
$res = 4.17ms$

3. ![](https://i.imgur.com/izT3vzx.png)
 
$T_{avg transfer} = \frac{1}{7200 \cdot \frac{1}{m}} \cdot \frac{1}{2500} = \frac{1}{18000000}m = \frac{60}{18000000}s = 0.003ms$

4. ![](https://i.imgur.com/34LcZks.png)

$T=T_{\text{seek time}}+T_{\text{rotational latency}}+T_{\text{transfer time}}=2.66+4.17+0.003=13.173$ ms

### Zadanie 2.
:::info
![](https://i.imgur.com/mCQrOsQ.png)
:::

**Przerwanie** - (ang. interrupt) sygnał powodujący zmianę przepływu sterowania, niezależnie od aktualnie wykonywanego programu. Pojawienie się przerwania powoduje wstrzymanie aktualnie wykonywanego programu i wykonanie przez procesor kodu **procedury obsługi przerwania** (ang. interrupt handler). Procedura ta wykonuje czynności związane z obsługą przerwania i na końcu wydaje instrukcję powrotu z przerwania, która powoduje powrót do programu realizowanego przed przerwaniem

**Kontroler DMA** - (ang. direct memory access) The hardware device used for direct memory access is called the DMA controller. DMA controller is a control unit, part of I/O device’s interface circuit, which can transfer blocks of data between I/O devices and main memory with minimal intervention from the processor.

Czas potrzebny na sciągnięcie 1 sektora
$T_{\text{avg transfer}} = \frac{1}{\text{RPM}\cdot \text{avg # sectors/track}} = \frac{m}{360} \cdot \frac{1}{96} = \frac{1}{34560} m = \frac{60}{34560} s = 1.736ms$

A) 
Łączny czas przerwań na sektor wyniesie:
$512 \cdot 2.5\mu s = 0.00128 s = 1.28 ms$

$n \cdot (1.736ms - 1.28ms) = 0.456ms \cdot n$


Z kontrolerem DMA mamy tylko jedno przerwanie na sektor.
B)
$n \cdot (1.736ms - 0.0025ms) = 1.7335ms \cdot n$

### Zadanie 3.
:::info
![](https://i.imgur.com/ug1dqe2.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/VZ2FNhe.png)
:::

**Pamięć podręczna** (ang. cache) – mechanizm, w którym część spośród danych zgromadzonych w źródłach o długim czasie dostępu i niższej przepustowości jest dodatkowo przechowywana w pamięci o lepszych parametrach. Ma to na celu poprawę szybkości dostępu do tych informacji, które przypuszczalnie będą potrzebne w najbliższej przyszłości.

**Hierarchia pamięci**
![](https://i.imgur.com/tt0PJEe.png)

W tym rozwiązaniu zakładamy, że czasy dostępu nie są kumulatywne:
Oznacza to, że czas dostępu np. do L3 zajmie $4+12+40 = 56$ cykli.

**[Średni czas dostępu do pamięci (AMAT)](https://en.wikipedia.org/wiki/Average_memory_access_time)** możemy policzyć w sposób przedstawiony w powyższym linku:
$AMAT = A_1 + MR \cdot AMP_1, \text{ gdzie } AMP_i = A_{i+1} + MR_{i+1} \cdot AMP_{i+1}$, ($MR=1 - H$)

$AMP_3 = 200 + (1 - 1) \cdot AMP_4 = 200$
$AMP_2 = 40 + (1 - 0.98) \cdot AMP_3 = 44$
$AMP_1 = 12 + (1 - 0.95) \cdot AMP_2 = 14.2$
$AMAT = 4 + (1-0.9) \cdot AMP_1 = 5.42  \text{ cykli}$

Pesymistyczny czas możemy łatwo policzyć sumując ilość wszystkich cykli na poszczególnych poziomach pamięci, a więc jest to $4+12+40+200=256$ cykli.

### Zadanie 5.
:::info
![](https://i.imgur.com/APm7zTK.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/OD7yi3z.png)
:::

**DRAM** (od ang. dynamic random-access memory) – rodzaj ulotnej pamięci półprzewodnikowej RAM, która przechowuje każdy bit danych w oddzielnym kondensatorze wewnątrz układu scalonego. W przeciwieństwie do pamięci statycznych wymagają okresowego odświeżania zawartości (ze względu na rozładowywanie się kondensatorów).

Program wybiera lokalizację pamięci używając wirtualnego adresu, a procesor tłumaczy go na adres fizyczny, a na samym końcu kontroler pamięci wybiera odpowiedni chip pamięci RAM odpowiadający temu adresowi. W celu wybrania pojedynczej komórki pamięci RAM na chipie, części adresu fizycznego są przekazywane w formie numerów linii adresu.

Odczyt danych z pamięci DRAM ([jakis polski opis (lekko sie rozni od pdfa)](http://cygnus.tele.pw.edu.pl/olek/doc/syko/www/rozdzial4_3_2.html)):
1. Cykl odczytu rozpoczyna się poprzez udostępnienie przez kontroler adresu wiersza na szynie adresowej. Zostaje zmniejszony sygnał $RAS$. Wszystkie sygnały są czytane przy wzroście sygnału na zegarze $CLK$, a więc nie ma to znaczenia, czy sygnał jest całkowicie kwadratowy, dopóki jest on stabilny w czasie odczytu. Ustawienie adresu wiersza powoduje, że chip RAMu zaczyna zamykać ten wiersz.

![](https://i.imgur.com/pXUrS5E.png)

2. Sygnał CAS wysyłany jest po czasie cyklu $t_{RCD}$ ($RAS$-$CAS$ delay). Adres kolumny jest przekazywany poprzez udostępnienie go na szynie adaresowej i zmniejszeniu sygnału CAS.

![](https://i.imgur.com/Eud9FuE.png)

3. Adresowanie kończy się i dane mogą być przesyłane. Chip RAMu musi jednak się do tego "przygotować" - opóźnienie to nazywa się zwykle $t_{CAS}$ lub CL (na diagramie na dole opóźnienie $t_{CAS} = 2$), różni się ono w zależności od jakości kontrolera pamięci, płyty głównej i samego modułu DRAM, może przyjmować również wartości połówkowe.


4. Moduł DRAM umożliwia wysyłanie większej ilości informacji, zwykle jest to 2, 4 albo 8 słów. Umożliwia to uzupełnienie całej pamięci podręcznej bez konieczności powtarzania kroków 1-3, jest również możliwe wysłanie sygnału CAS bez przestawiania aktualnego wiersza. Wtedy odczyty pamięci są znacznie szybsze, ponieważ  sygnał RAS nie musi być co chwile wysyłany, a wiersz dezaktywowany.
![](https://i.imgur.com/k6a3zfj.png)
![](https://i.imgur.com/L6O1tQZ.png)


Źródło opóźnień:
- $t_{CAS}$ (CL, Column Access Strobe Latency - wczytanie komórki): oczekiwanie między wysłaniem przez kontroler pamięci RAM żądania dostępu do określonej kolumny pamięci a otrzymaniem danych z tej kolumny przez kontroler,

- $t_{RCD}$
![](https://i.imgur.com/thUsgSB.png)


- $t_{RP}$ (Row Precharge - przygotowanie wiersza): czas między wykonaniem polecenia zamknięcia dostępu do wcześniej aktywowanego wiersza a rozpoczęciem wykonywania polecenia aktywacji kolejnego
- $t_{RAS}$ (Row Access Strobe): czas między żądaniem wykonania polecenia aktywacji wiersza aż do jego dezaktywacji
![](https://i.imgur.com/3jYmWLA.png)

### Zadanie 7.
:::info
![](https://i.imgur.com/e72tZHp.png)
:::

Wiemy, że jeden blok ma $64$ bajty, a w trakcie jednego cyklu można przesłać $64$ bity, czyli jedno słowo. My jednak przesyłać będziemy $8$ słów, jako że pracujemy na pamięciach `DDR4`.

Przygotowanie wiersza zajmie czas $t_{RP}$, a więc musimy wybrać kolumnę, a następnie wczytać ją do specjalnego wiersza. Wczytanie wiersza zajmie czas $t_{RP} + t_{RCD}$, jako że najpierw musimy wyszukać wiersz, a następnie znaleźć szukaną komórkę w tym wierszu. Kolejnym krokiem jest wczytanie tej komórki, a więc ustawiany jest na niej wskaźnik i w razie odczytywania danych z kolejnych komórek, dodajemy czas $t_{CAS}$.

W pesymistycznym przypadku liczba cykli (odpowiednio dla `DDR4-1600` i `DDR4-2133`) wyniesie:

$c_1 = t_{RP} + t_{RCD} + 8(t_{CAS} + 1) = 108$

$c_2 = t_{RP} + t_{RCD} + 8(t_{CAS} + 1) = 150$

Obliczmy więc czas wykorzystując obliczoną liczbę cykli i znane nam taktowanie:

$t_1 = \frac{c_1}{t_{CLK}} = \frac{108}{800\text{MHz}} = 135 ns$

$t_2 = \frac{c_2}{t_{CLK}} = \frac{150}{1066.67\text{MHz}} = 141 n s$

![](https://i.imgur.com/X1oaLef.png)

Powtórzone obliczenia dla pamięci działającej w trybie sekwencyjnym, a więc wiersz jest wyszukiwany tylko raz, a następne komórki czytamy sekwencyjnie:

$c_1 = t_{RP} + t_{RCD} + t_{CAS} + 4 = 34$

$c_2 = t_{RP} + t_{RCD} + t_{CAS} + 4 = 49$

Taktowanie nie ulega zmianie, korzystamy więc z tych samych wzorów:

$t_1 = \frac{c_1}{t_{CLK}} = \frac{34}{800\text{MHz}} = 42.5ns$

$t_2 = \frac{c_2}{t_{CLK}} = \frac{49}{1066.67\text{MHz}} = 45.9 ns$

### Zadanie 8.
:::info
![](https://i.imgur.com/rzbf41v.png)
:::

Wiemy, że cała tablica zajmuje $4\text{GiB} = 2^{32} \text{ bajtów}$. Tablica będzie miała wymiary $2^{19} \text{ wierszy} \times 2^{13} \text{ kolumn}$. W jednym momencie możemy przeczytać $16$ słów, co odpowiada $2^7$ bajtom, a na cały wiersz składa się $8\text{KiB} = 2^{13}\text{bajtów}$. To znaczy, że w ciągu $\frac{2^{13}}{2^7} = 64$ cykli można sprowadzić cały wiersz.

![](https://i.imgur.com/X1oaLef.png)

Dla DDR4-2133 mamy: $CLK = 1066.67 MHz$

$c_w = max(t_{RAS}, t_{RCD} + 64 \cdot t_{CAS}+ 64) + t_{RP}$

$c_w = max(36, 15 + 64 \cdot 15 + 64) + 15 = 1054$

$c_t = 2^{19} \cdot c_w = 552.599.552$

$t=\frac{552599552}{1066.67\text{MHz}} = \frac{552599552}{1066.67 \cdot 1000000}s = 0.519s$


Dla konfiguracji dwukanałowej jesteśmy w stanie 2-razy szybciej sprowadzić cały wiersz, bo czytamy na cykl 32 słowa.

$c_w = max(t_{RAS}, t_{RCD} + 32 \cdot t_{CAS}+ 32) + t_{RP}$

$c_w = max(36, 15 + 32 \cdot 15 + 32) + 15 = 542$

$c_t = 2^{19} \cdot c_w = 276.299.776$

$t=\frac{276299776}{1066.67\text{MHz}} = \frac{276299776}{1066.67 \cdot 1000000}s = 0.267s$
