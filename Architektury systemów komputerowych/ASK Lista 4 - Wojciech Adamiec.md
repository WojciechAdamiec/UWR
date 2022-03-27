# ASK Lista 4 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 4, 5, 6, 7

### Zadanie 1.
:::info
![](https://i.imgur.com/QIjPLVd.png)
:::

**Operand źródłowy**
Pierwszy operand instrukcji: mov Source, Dest

Zacznijmy od *ściągi*:

*    $\text{D(Rb, Ri, S) = Mem[Reg[Rb]+S*Reg[Ri]+D]}$
*    $\text{(Rb, Ri) = Mem[Reg[Rb]+Reg[Ri]]}$
*    $\text{D(Rb, Ri) = Mem[Reg[Rb]+Reg[Ri]+D]}$
*    $\text{(Rb, Ri, S) = Mem[Reg[Rb]+S*Reg[Ri]]}$

Gdzie $D$ to przesunięcie o stałą liczbę bajtów; $Rb$, $Ri$ to rejestry; $S$ to skala.

Odpowiedzi:

1. `%rax` zwraca `0x100`
2. `0x110` zwraca `0x13`
3. `$0x108` zwraca `0x108` (`$` oznacza stałą)
4. `(%rax)` zwraca `0xFF` - dereferencja; wartość `%rax` jako adres
5. `8(%rax)` zwraca `(%rax + 8) = (0x108) = 0xAB`
6. `21(%rax, %rdx)` zwraca `(%rax + %rdx + 21) = (0x100 + 3 + 21) = (0x100 + 0x18) = (0x118) = 0x11`
7. `0xFC(, %rcx, 4)` zwraca `(4 * %rcx + 0xFC) = (0x4 + 0xFC) = (0x100) = 0xFF`
8. `(%rax, %rdx, 8)` zwraca `(0x100 + 8 * %rdx) = (0x100 + 24) = (0x100 + 0x18) = (0x118) = 0x11`
9. `265(%rcx, %rdx, 2)` zwraca `(%rcx + 2 * %rdx + 265) = (0x1 + 0x6 + 0x109) = (0x110) = 0x13`

### Zadanie 2.
:::info
![](https://i.imgur.com/zaan8dd.png)
:::

![](https://i.imgur.com/yZE4k6p.png)
![](https://i.imgur.com/98ft2qR.png)
![](https://i.imgur.com/RmLf1YO.png)

| Instrukcja                    | Miejsce | Wartość                                               |
| ----------------------------- | --------------- | ----------------------------------------------------- |
| `addq %rcx, (%rax)`           | `0x100`         | `0xFF + 0x1 = 0x100`                                  |
| `subq 16(%rax), %rdx`         | `%rdx`          | `3 - (16 + 0x100) = 3 - (0x110) = 0x3 - 0x13 = -0xF0` |
| `shrq $4,%rax`                | `%rax`          | `0x100 >> 4 = 0x10`                                   |
| `incq 16(%rax)`               | `(%rax + 0x10) = (0x100 + 0x10) = (0x110)` |     `0x13 + 0x1 = 0x14`    |
| `decq %rcx`                   | `%rcx`          | `0x1 - 0x1 = 0x0`                                     |
| `imulq 8(%rax)`               |`%rax`| `(%rax + 0x8) = (0x100 + 0x8) = (0x108)`; Zatem `0xAB * 0x100 = 0xAB00` |
| `leaq 7(%rcx, %rcx, 8), %rdx` | `%rdx`          | `(%rcx + 8 * %rcx + 7) = (0x10) = 0x10`              |
| `leaq 0xA(, %rdx, 4), %rdx`   | `%rdx`          | `(%rdx * 4 + 0xA) = (0xC + 0xA) = (0x16) = 0x16`     |

![](https://i.imgur.com/fNIxfgi.png)
![](https://i.imgur.com/QrHRcme.png)

Screenshot z .pdf (https://www.cs.cmu.edu/~fp/courses/15213-s07/misc/asm64-handout.pdf)

### Zadanie 4.
:::info
![](https://i.imgur.com/WDXtg9l.png)
:::

Funkcja sprawdza czy doszło do przepełnienia przy dodawaniu.

Asembler robi dokładnie to:

![](https://i.imgur.com/Fpt6NKL.png)

```c=
long decode(long x, long y) {
    long res = x + y;
    x ^= res;
    y ^= res; 

    res = x & y; 
    res >> 63;
    
    return res;
}
```
Wersja zwięzła:
```c=
long decode(long x, long y) {
    return (((x + y)^x) & (x + y)^y) >> 63;
}
```


### Zadanie 5.
:::info
![](https://i.imgur.com/Vw3AVra.png)
:::

![](https://i.imgur.com/zMhnsEv.png)
![](https://i.imgur.com/iIemsz9.png)
![](https://i.imgur.com/Yo163o1.png)

```=
convert:    movl %edi, %r8
            movl %edi, %r9
            andl $0xFF00FF00, %r8
            andl $0x00FF00FF, %r9
            roll $0x8, %r8
            rorl $0x8, %r9
            orl %r8, %r9
            movl %r9, %eax
            ret
```
![](https://i.imgur.com/vuqWbv2.png)


Wyrażenie w C, które zostanie przetłumaczone do rol/ror:

![](https://i.imgur.com/IKlWTkH.png)
![](https://i.imgur.com/eFTCTVN.png)

### Zadanie 6.

:::info
![](https://i.imgur.com/udVKWUI.png)
:::

Sumujemy ze sobą młodsze bity za pomocą `add`. Może dojść do przeniesienia, jeśli tak się stanie to przeniesienie zostanie we fladze `CF`.

Sumujemy ze sobą starsze bity ORAZ flagę `CF` za pomocą `adc`.

```=
sum_big:    addq %rsi, %rcx
            adc  %rdi, %rdx
            movq %rcx, %rax
            ret
```

adc: https://pl.wikibooks.org/wiki/Asembler_x86/Instrukcje/Arytmetyczne#adc
flags: https://pl.wikipedia.org/wiki/FLAGS

### Zadanie 7.

:::info
![](https://i.imgur.com/XHF7bb5.png)
:::

![](https://i.imgur.com/c8aU0l6.png)

$x = x_1 \cdot 2^{64} + x_0$ : $x_0$, $x_1$ to ciągi odpowiednich bitów. 

Mnożenie liczb 128-bitowych. 

Niech: $x = x_1 \cdot 2^{64} + x_0$ oraz $y = y_1 \cdot 2^{64} + y_0$. 

Wówczas: 
$x \cdot y = (x_1 \cdot 2^{64} + x_0)\cdot (y_1 \cdot 2^{64} + y_0) = x_1\cdot y_1\cdot 2^{128} + (x_1\cdot y_0 + x_0\cdot y_1)\cdot 2^{64} + x_0\cdot y_0$. 

Wartość $x_1\cdot y_1\cdot 2^{128}$ jest za duża i wyjdzie poza zakres - nie musimy jej pamiętać.

$x_1=\%rdi$
$x_0=\%rsi$
$y_1=\%rdx$
$y_0=\%rcx$

```=
mult_big:
    movq %rdx, %rax
    mulq %rsi         // x0 * y1
    movq %rax, %r8
    movq %rdi, %rax
    mulq %rcx         // x1 * y0
    addq %rax, %r8    // r8 przechowuje: x0 * y1 + x1 * y0
    movq %rsi, %rax
    mulq %rcx         // x0 * y0
    addq %r8, %rdx    // dodajemy do starszych bitów wyniku x0 * y0 nasze r8
    ret
```