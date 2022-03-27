# Systemy Operacyjne - Lista 8

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 2, 3, 4

### Zadanie 1.
:::info
![](https://i.imgur.com/p1edBMS.png)
:::

brk, sbrk - change data segment size

![](https://i.imgur.com/3trWEtj.png)

![](https://i.imgur.com/KM94pdZ.png)

### Zadanie 2.
:::info
![](https://i.imgur.com/tTBkXBe.png)
:::

**Fragmentacja** - kiepskie wykorzystanie pamięci.

![](https://i.imgur.com/mKvKFlO.png)

![](https://i.imgur.com/UbHp3OP.png)

**Kompaktowanie** to proces konsolidacji pofragmentowanych danych (zaalokowanej pamięci) w taki sposób, aby były obok siebie. Nie możemy kompaktować pamięci przydzielonej przez `malloc`, bo wszystkie istniejące wskaźniki by się unieważniły. Być może mamy wskaźnik do tego bloku, który chcemy przenieść, ale algorytm nie zapamiętuje w żaden sposób tego, gdzie są w pamięci wskaźniki wskazujące na ten blok.

Głównymi przyczynami występowania fragmentacji zewnętrznej są:

**Fragmentation is caused by isolated deaths**: krytycznym problemem jest tworzenie wolnych obszarów, których sąsiadujące obszary nie są wolne. Składają się na to dwie rzeczy: które obiekty są umieszczone w sąsiednich obszarach i kiedy te obiekty umierają. Jeśli alokator umieszcza obiekty razem w pamięci i umierają w tym samym czasie, to nie dochodzi do fragmentacji - obiekty żyją w tym samym czasie, używają ciągłej pamięci i gdy umierają, zwalniają ciągłą pamięć. Jeśli jednak obiekty zostaną uwolnione w różnym czasie, to mogą powstać między nimi przerwy.

**Fragmentation is caused by time-varying behavior**: fragmentacja powstaje w wyniku zmiany sposobu użycia pamięci przez program, np. zwalnianie małych bloków i alokowanie bardzo dużych. Zadaniem alokatora jest wykorzystywanie takich wzorców, aby zminimalizować fragmentacje.

### Zadanie 3.
:::info
![](https://i.imgur.com/J3iSyJZ.png)
:::

Peaks
![](https://i.imgur.com/hld2vGV.png)
Ramps
![](https://i.imgur.com/1Mtvoj6.png)
Plateaus
![](https://i.imgur.com/nIAfVsT.png)

-> Obiekty zaalokowane w tym czasie prawdopodobnie umrą w tym samym czasie. Dlatego warto alokować je koło siebie, tak aby po ich śmierci został zwolniony ciągły przedział pamięci.

-> Rozmiar bloku bardzo często związany jest bezpośrednio z jego przeznaczeniem oraz typem obiektu. Co za tym idzie, nie warto przeplatać dużych bloków pamięci z tymi małymi, bo istnieje duże ryzyko, że będziemy je dealokować w różnym czasie.

-> Generalna strategia jest więc taka, aby alokować koło siebie obiekty powstałe w tym samym czasie, ale biorąc poprawkę na to, aby bloki były segregowane ze względu na ich rozmiar.

**First fit:**

- Wybierany jest pierwszy wolny blok o wystarczającym rozmiarze.
- Jeśli rozmiar jest za duży, blok zostaje podzielony.
- Wyszukiwanie zaczyna się od początku listy wolnych bloków.
- **Zalety:** prostota działania.
- **Wady:** prowadzi do dużej fragmentacji pamięci, powstaje zjawisko *drzazg* na początku listy (dużego rozdrobnienia bloków), które doprowadza do znacznego wydłużenia czasu szukania wolnej pamięci.

**Next fit:**

- First fit, tylko wyszukiwanie następuje od miejsca, w którym osatnio wystąpiła alokacja.
- **Zalety:** Działa szybciej niż first fit. Eliminuje zjawisko *drzazg*.
- **Wady:** Polityka niekorzystna dla lokalności przestrzennej. Obiekty z tych samych faz programu są rozrzucone w różnych miejsach pamięci, powoduje to większą fragmentację, gdy obiekty w różnych fazach programu mają różne czasy życia.

**Best fit:**

- Wybierany jest najmniejszy blok wystarczająco duży, aby przechować dane.
- **Zalety:** Najefektywniejsza alokacja pamięci pod względem oszczędności miejsca.
- **Wady:** Działa wolniej od pozostałych strategii. Nie skaluje się dobrze z dużymi stertami o wielu blokach.

### Zadanie 4.
:::info
![](https://i.imgur.com/Kx7OnrB.png)
:::

**Gorliwe złączanie** (ang. immediate coalescing) polega na złączaniu wolnych bloków tak szybko, jak jest to możliwe, a więc po zwolnieniu pamięci przez `free()`.

![](https://i.imgur.com/NmZLBFV.png)

![](https://i.imgur.com/72SZIR9.png)

Dla best-fit

![](https://i.imgur.com/IMVeCmr.png)

Dla first-fit

![](https://i.imgur.com/FyRpUCk.png)
### Zadanie 5.
:::info
![](https://i.imgur.com/0UJt36j.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/qvcNNTr.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/5VwQn6m.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/p1wpUsi.png)
:::