# ASK Lista 2 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 3, 5, 7, 8, 9

### Zadanie 1.

:::info
![](https://i.imgur.com/uac4Glv.png)
:::

A. `(x > 0) || (x - 1 < 0)`

Kontrprzykład:
$x = 100...0_{(2)}$
$x > 0$ oblicza się do fałszu
$x - 1 = 0111...11_{(2)}$
$x - 1 < 0$ oblicza się do fałszu
Dostajemy fałsz

B. `(x & 7) != 7 || (x << 29 < 0)`

Zwracana wartość wyrażenia `(x & 7) != 7` będzie prawdą, jeżeli chociaż jeden z trzech najmniej znaczących bitów `x` będzie zgaszony. Weźmy więc $x=b_{31}b_{30}\dots b_{3}111_{(2)}$ (dający fałsz w lewym podwyrażeniu), a następnie przesuńmy o $29$ bitów w lewo - otrzymana liczba ma wartość $11100\dots 000_{(2)}$, a więc jest ujemna, czyli wyrażenie zawsze zwróci prawdę.

C. `(x * x) >= 0`

Kontrprzykład:
$x = 2147461$ # 00000000001000001100010010000101
$x*x = -1206129383$ # 01000111111001000001001011100111

Tutaj wyjdziemy poza zakres

D. `x < 0 || -x <= 0`

Dowolna ujemna daje prawdę z lewej. Dowolna dodatnia da prawdę z prawej (liczb ujemnych jest jedna więcej niż ujemnych, więc jesteśmy bezpieczni)

E. `x > 0 || -x >= 0`

Kontrprzykład:
Najmniejsza liczba ujemna nie ma dodatniego odpowiednika - przejdziemy poza zakres.
$x = 1000...000_{(2)}$
$-x = 0111...111_{(2)} + 1 = x$

F. `(x | -x) >> 31 == -1`

Kontrprzykład:
$x=00...000$

G. `x + y == (uint32_t)y + (uint32_t)x`
Zawsze prawdziwe, porównanie ze sobą inta z uintem automatycznie reinterpretuje inta do uinta.

H. `x * ~y + (uint32_t)y * (uint32_t)x == -x`

Obserwacja:
Dla każdego $a$: $\neg a + a = 111...11_{(2)}$

W naszym równaniu wszystkie liczby zmienią się na *uint*.

$L = x \cdot \neg y + y \cdot x = x \cdot (y + \neg y) = x \cdot 111...11_{(2)} = x \cdot unsigned(-1) = unsigned(-x) = P$

### Zadanie 2.
:::info
![](https://i.imgur.com/DXwwSAs.png)
:::
Rozwiązanie naiwne z *WDI*:

```c=
x = x + y
y = x - y
x = x - y
```

Tutaj jest problem: możemy wyjść poza zakres.
Alternatywne rozwiązanie:

```c=
y = y ^ x
x = x ^ y
y = y ^ x
```

![](https://i.imgur.com/OvIWlJN.png)

Dzięki temu nie mamy problemu z zakresem. Problemem tutaj z kolei jest przypadek, gdy $x = y$.
```c=
if (x != y) // dla x == y byłoby x^y = 0
{
    y = y ^ x;
    x = x ^ y;
    y = y ^ x;
}
```

### Zadanie 3.
:::info
![](https://i.imgur.com/jkltlyq.png)
:::

**Nadmiar** (ang. overflow) - przekroczenie zakresu wartości, które może przyjąć zmienna.

**Niedomiar** (ang. underflow) - wartość, na której działamy jest tak mała, że wzięta z niej wartość bezwzględna jest mniejsza niż najmniejsza liczba większa od zera możliwa do zapisania w tej zmiennej. Dla `int` nie ma możliwości wystąpenia niedomiaru.

Tutaj jest problem nazewnictwa, bo nie wiem jak tłumaczyć **overflow**, **underflow**, **positive overflow**, **negative overflow** dla intów i floatów.

```c=
s = x + y
bool is_overflow = ((s ^ y) & (s ^ x)) >> (N - 1);
```

Sprawdzanie nadmiaru ma sens tylko dla liczb tego samego znaku. Sprawdzamy czy po ich dodaniu nie zmieni się przypadkiem ich znak.

### Zadanie 5.
:::info
![](https://i.imgur.com/C7Giqff.png)
:::

```c=
int32_t threefourths(int32_t x)
{
    int32_t result = (x >> 1) + (x >> 2);
    int z = (x & 2) >> 1 & (x & 1); # Jeśli 2 odcinane bity są zapalone to dodaj 1
    result += z;
    return result;
}
```

Zauważmy pierw, że:
$3 \cdot x = (x \cdot 2) + x$

W naszym rozwiązaniu dodajemy $1/4 \cdot x$ do $1/2 \cdot x$ dostając $3/4 \cdot x$. Jedyny problem może się pojawić, gdy oba bity, które obcieliśmy przesunięciem bitowym były zapalone. Wówczas do wyniku musimy dodać 1.
### Zadanie 7.
:::info
![](https://i.imgur.com/rTSThG6.png)
:::

```c=
int32_t abs(int32_t x)
{
    int32_t mask = x >> 31; # Ad. 1
    return (mask & -x) + (~mask & x);
}
```
Ad. 1
Dla $x\geq0; mask=000...00_{(2)}$
Dla $x<0; mask=111...11_{(2)}$

Zawsze nam się jeden składnik wyzeruje. Zwracamy albo $-x$ albo $x$.
### Zadanie 8.

:::info
![](https://i.imgur.com/UAicju7.png)
:::

Rozwiązanie:

```c=
(x >> (N-1)) | -(-x >> (N-1))
```

Chcemy się upewnić, że rozwiązanie działa dla wszystkich przypadków. Rozważmy $N=4$.

A. Dla $0$:
![](https://i.imgur.com/H9fS6lu.png)

B. Dla generycznej dodatniej:
![](https://i.imgur.com/nz43Udf.png)

C. Dla generycznej ujemnej:
![](https://i.imgur.com/SRcDMIM.png)

D. Dla największej dodatniej:
![](https://i.imgur.com/PzUZmgo.png)

E. Dla najmniejszej ujemnej:
![](https://i.imgur.com/yvFK18E.png)

### Zadanie 9.
:::info
![](https://i.imgur.com/7X3aL8J.png)
:::

Algorytm prezentowany na poprzedniej liście.
```c=
int32_t aux(uint32_t x){
    uint32_t m1  = 0x55555555; // 01010101010101010101010101010101
    uint32_t m2  = 0x33333333; // 00110011001100110011001100110011
    uint32_t m4  = 0x0f0f0f0f; // 00001111000011110000111100001111
    uint32_t m8  = 0x00ff00ff; // 00000000111111110000000011111111
    uint32_t m16 = 0x0000ffff; // 00000000000000001111111111111111
    
    x = (x & m1 ) + ((x >>  1)  & m1 ); //put count of each 2 bits into those 2 bits  
    x = (x & m2 ) + ((x >>  2)  & m2 ); //put count of each 4 bits into those 4 bits 
    x = (x & m4 ) + ((x >>  4)  & m4 ); //put count of each 8 bits into those 8 bits 
    x = (x & m8 ) + ((x >>  8)  & m8 ); //put count of each 16 bits into those 16 bits 
    x = (x & m16) + ((x >> 16)  & m16); //put count of each 32 bits into those 32 bits
    
    return (x & 1);
}
```