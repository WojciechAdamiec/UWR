# ASK Lista 3 - Wojciech Adamiec
## Zadania Deklarowane: 2, 3, 4, 5

### Zadanie 2.
:::info
Autor: Wojciech Adamiec	
:::

:::info
![](https://i.imgur.com/vD5FPLC.png)
:::

Single precision:
![](https://i.imgur.com/MLsCgRj.png)

Half precision:
![](https://i.imgur.com/1YCp9Z5.png)

Chcemy zapisać w half precision liczbę $0.15625_{10}$. Zacznijmy od konwersji na postać binarną:

$0.15625_{10} = 0.00101_{2} = 1.01 \cdot 2^{-3}$

Sposób na liczenie:
$0.15625 \cdot 2 = 0.3125 \space | \space 0$
$0.3125  \cdot 2 = 0.625 \space | \space 0$
$0.625 \cdot 2 = 1.25 \space | \space 1$
$0.25 \cdot 2 = 0.5 \space | \space 0$
$0.5 \cdot 2 = 1 \space | \space 1$

Znak bitu jest oczywisty: $s=0$.
Liczymy teraz $bias$: $2^{5-1}-1 = 15$
Cecha: $-3 = 12 - 15$

Zatem cała liczba:

$0|01100|0100000000$

Porównanie zakresu i dokładności:

Half precision:

$0|11110|1111111111 = 2^{30-15} \cdot (2 - \frac{1}{1024}) = 65504$
$0|00001|0000000000 = 2^{-14} = 6.1 \cdot 10^{-6}$
$0|00000|1111111111 = 2^{-14} \cdot \frac{1023}{1024} = 6.09 \cdot 10^{-6}$
$0|00000|0000000001 = 2^{-14} \cdot \frac{1}{1024} = 5.96 \cdot 10^{-8}$

Single precision:

$0|11111110|11...11 = 2^{254-127} \cdot (2 - \frac{1}{2^{23}}) = 3.4 \cdot 10^{38}$
$0|00000001|00...00 = 2^{-126} = 1.1754943 \cdot 10^{-38}$
$0|00000000|11...11 = 2^{-126} \cdot \frac{2^{23}-1}{2^{23}} = 1.1754942 \cdot 10^{-38}$
$0|00000000|00...01 = 2^{-126} \cdot \frac{1}{2^{23}}= 1.4012 \cdot 10^{-45}$


### Zadanie 3.
:::info
![](https://i.imgur.com/CqsTHhW.png)
:::
![](https://i.imgur.com/kbjyhPY.png)

Zacznijmy od konwersji na zapis binarny:

$b = 0.34375_{10} = 0.01011_{2} = 1.011 \cdot 2^{-2}$
Binarnie: $0|01101|0110000000$

Sposób na liczenie:
$0.34375 \cdot 2 = 0.6875 \space | \space 0$
$0.6875  \cdot 2 = 1.375 \space | \space 1$
$0.375 \cdot 2 = 0.75 \space | \space 0$
$0.75 \cdot 2 = 1.5 \space | \space 1$
$0.5 \cdot 2 = 1 \space | \space 1$

Analogicznie robimy pozostałe 2 liczby:

$a = 0.3984375_{10} = 0.0110011_{2} = 1.10011 \cdot 2^{-2}$
Binarnie: $0|01101|1001100000$

$c = 1771_{10} = 11011101011_{2} = 1.1011101011 \cdot 2^{10}$
Binarnie: $0|11001|1011101011$

$(0.3984375 + 0.34375) + 1771 = 2^{-2}(1.10011 + 1.011) + 2^{10}(1.1011101011) = \\2^{-2}(10.11111) + 2^{10}(1.1011101011) = \\2^{10}(0.0000000000|1011111) + 2^{10}(1.1011101011) = \\2^{10}(1.1011101011|1011111) \approx 2^{10}(1.1011101100) = 1772$

Wynik w formacie half precision:
$0|11001|1011101100$

$0.3984375 + (0.34375 + 1771) = 2^{-2}(1.10011) + (2^{-2}(1.011) + 2^{10}(1.1011101011)) =\\ 2^{-2}(1.10011) + 2^{10}(0.0000000000|01011 + 1.1011101011) = \\ 2^{-2}(1.10011) + 2^{10}(1.1011101011|01011) \approx 2^{10}(0.00000000000110011 + 1.1011101011) = \\2^{10}(1.1011101011|0110011) \approx 2^{10}(1.1011101011) = 1771$
### Zadanie 4.
:::info
![](https://i.imgur.com/zguXNOd.png)
:::

1. Obliczy się do prawdy: można bez utraty precyzji zrzutować inta na doubla. Następnie po obu stronach robimy to samo rzutowanie na floata.
2. Kontrprzykład: x = intMIN; y=intMAX. Po lewej stronie policzymy wynik. Po prawej wyjdziemy poza zakres.
3. Mantysa dobule precision ma 52 bity, int ma długość 32 bitów. Przy dodawaniu dwóch intów może się nam zwiększyć rozmiar o co najwyżej 1 bit. Oznacza to, że mamy jeszcze spory zapas i nie będziemy tracić precyzji.
4. Kontrprzykład:
![](https://i.imgur.com/hxN1lrj.png)
![](https://i.imgur.com/F7iPqwf.png)
5. Kontrprzykład: Dla $0/0$ dostajemy $NaN$ co jest innym wynikiem niż np. $1/1$

### Zadanie 5.
:::info
![](https://i.imgur.com/BLc52Sc.png)
:::

1. Zmiana znaku liczby: 
```
x ^ 0x80000000
```
2. Wyciągamy bity wykładnika, robimy logarytm poprzez przesunięcie bitowe i na końcu odejmujemy $bias$: 
```
((x & 0x7f800000) >> 23) - 127
```
3. Sprawdzamy czy liczby są takie same i rozważamy dodatkowo przypadek obu zer:
```
(a == b) | ((a | b) == 0x80000000)
```
4. Rozpatrujemy przypadek kiedy: Obie liczby są dodatnie; Obie są ujemne; Tylk jedna jest dodatnia; Przypadek dla dwóch różnych zer
```
((((~(x | y) & (x - y)) |
(x & y & (y - x)) |
(x & ~y)) &
0x80000000) != 0) & 
((x | y) != 0x80000000)
```