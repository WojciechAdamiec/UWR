# ASK Lista 9 - Wojciech Adamiec
## Zadania Deklarowane: 2, 5

### Zadanie 2.
:::info
![](https://i.imgur.com/2WStHnK.png)
:::

**Dekorowanie nazw** służy do tego, aby odróżnić implementację różnych funkcji (o różnych sygnaturach) mających taką samą nazwę. Jest to oczywiście potrzebne w C++, ponieważ możemy przeciążać funkcje. Funkcja dekorująca jest różnowartościowa.

W `Intel C++ 8.0 for Linux` udekorowane symbole zaczynają się od `_Z`.
Następnie mamy literę `N` mówiącą o tym, czy mamy jakieś `namespace`'y, czy nie. 
1. Jeśli nie ma `N` to od razu po `Z` kodujemy nazwę podając najpierw liczbę liter wchodzących w skład nazwy, a następnie pełną nazwę. 
2. Jeśli jest `N` to podajemy kolejne `namespace`'y na tej samej zasadzie co powyżej a po podaniu nazwy funkcji mamy literę `E`.

Następnie przechodzimy do argumentów funkcji. Tutaj mamy:
1. `P` oznacza `*`
2. `K` oznacza `const`
3. `R` oznacza `&`
4. `i` oznacza `int`, podobnie `d` oznacza `double` itd.

Można to sprawdzić na stronie: https://demangler.com/

Przykłady z zadania:
- `_Z4funcPKcRi` $\rightarrow$ `func(char const*, int&)`
- `_ZN3Bar3bazEPc` $\rightarrow$ `Bar::baz(char*)`
- `_ZN3BarC1ERKS_` $\rightarrow$ `Bar::Bar(Bar const&)`
`C1` mówi nam o tym, że jest to konstruktor (analogicznie `D1` dałoby destruktor `~Bar`),
`S_` to typ pierwszego argumentu. Typy kolejnych argumentów są kodowane `S0_`, `S1_` itd.
- `_ZN3foo6strlenER6string` $\rightarrow$ `foo::strlen(string&)`
Ten przykład ma nietypowy typ argumentu, ponieważ nie jest to typ prosty, lecz złożony `string`. Stąd trzeba było użyć notacji takiej, w której najpierw podajemy długość nazwy typu, a potem nazwę.

### Zadanie 5.
:::info
![](https://i.imgur.com/xooVenK.png)
:::

**Dyrektywa asemblera** (assembler directive, pseudo-op) to fraza w języku asemblera, która określa działanie asemblera i nie tłumaczy się bezpośrednio na kod maszynowy. Pozwalają m. in. definiować stałe, oddzielać sekcje, używać makr.

Kod napisany w C. Potem przetłumaczony do `.s`:
`gcc -S -Og 1.c`
`gcc -S 2.c`
`gcc -S -O0 3.c`

Teraz, żeby sprawdzić `.symtab` to trzeba przetłumaczyć do `.o`. Po czym robimy `readelf -s nazwa.o`

Foo:
![](https://i.imgur.com/Lrph5St.png)

Struct:
![](https://i.imgur.com/bA35cIB.png)

Array:
![](https://i.imgur.com/Uh8yDRM.png)

Sprawdzamy `.symtab`:
1.
![](https://i.imgur.com/AL0Bpue.png)
2.
![](https://i.imgur.com/k4EIV1Q.png)
3.
![](https://i.imgur.com/rKiv6Rv.png)