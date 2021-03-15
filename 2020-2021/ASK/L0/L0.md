# ASK Lista 0 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 3, 5, 7, 8
### Zadanie 1.

Przekształć każdą z podanych liczb z systemu ósemkowego na system binarny, szesnastkowy i dziesiętny:

42, 255, 3047 i 140336.

$42_8 = 34_{10} = 100010_2 = 22_{16}$
$255_8 = 173_{10} = 10101101_2 = AD_{16}$
$3047_8 = 1575_{10} = 11000100111_2 = 627_{16}$
$140336_8 = 49374_{10} = 1100000011011110_2 = C0DE_{16}$

### Zadanie 2.

Oblicz bez konwersji na inny system:

$22_{16} + 8_{16} = 2A_{16}$
$73_{16} + 2C_{16} = 9F_{16}$
$7F_{16} + 7F_{16} = FE_{16}$
$C2_{16} + A4_{16} = 166_{16}$

### Zadanie 3.

Napisz fragment kodu, który dla zmiennych $x$ i $k$ wykona poniższe operacje:
• wyzeruje k-ty bit zmiennej $x$,
• ustawi k-ty bit zmiennej $x$,
• zaneguje k-ty bit zmiennej $x$.


```c=
#include <stdint.h>
#include <stdio.h>

void zeruj(uint32_t &x, uint8_t k){
    x &= ~(1 << k);
}

void ustaw(uint32_t &x, uint8_t k){
    x |= (1 << k);
}

void neguj(uint32_t &x, uint8_t k){
    x ^= (1 << k);
}

int main(){

    uint32_t a = 7;
    uint32_t b = 2;
    uint32_t c = 2;

    printf("Dla %d (111): \n", a);
    zeruj(a, 2);
    printf("Zeruj 2: %d\n", a);

    printf("Dla 2 (010): \n");
    ustaw(b, 0);
    printf("Ustaw 0: %d\n", b);
    
    printf("Dla 2 (010): \n");
    neguj(c, 2);
    neguj(c, 1);
    printf("Neguj 2, Neguj 1: %d\n", c);

    return 0;
}
```

```
Dla 7 (111): 
Zeruj 2: 3
Dla 2 (010): 
Ustaw 0: 3
Dla 2 (010): 
Neguj 2, Neguj 1: 4
```

### Zadanie 4.

Napisz fragment kodu, który dla zmiennych x i y obliczy poniższe wyrażenia:
• $x \cdot 2^y$
• $\lfloor x/2^y \rfloor$
• $x \mod 2^y$
• $\lceil x/2^y \rceil$

```c=
#include <stdint.h>
#include <stdio.h>

uint32_t foo1(uint32_t &x, uint8_t y){
    return x << y;
}

uint32_t foo2(uint32_t &x, uint8_t y){
    return x >> y;
}

int main(){

    uint32_t a = 32;
    uint32_t b = 33;

    printf("%d\n", foo1(a, 5));
    printf("%d\n", foo2(b, 4));
    return 0;
}
```

```
1024
2
```
### Zadanie 5.

Napisz fragment kodu, który stwierdza czy dana liczba $x$ nie jest potęgą dwójki.

```c=
#include <stdint.h>
#include <stdio.h>

bool is_power(uint32_t x){
    return !(x & (x - 1));
}

int main(){

    printf("27  : %d\n", is_power(27));
    printf("32  : %d\n", is_power(32));
    printf("15  : %d\n", is_power(15));
    printf("1024: %d\n", is_power(1024));
    printf("7   : %d\n", is_power(7));
    return 0;
}
```

```
27  : 0
32  : 1
15  : 0
1024: 1
7   : 0
```
### Zadanie 6.

Napisz fragment kodu, który skonwertuje zmienną x z formatu **little-endian** do formatu **bigendian**. Należy użyć jak najmniejszej liczby operacji bitowych.


W sytuacjach, kiedy liczby całkowite lub jakiekolwiek inne dane zapisywane są przy użyciu wielu (przynajmniej dwóch) bajtów, nie istnieje jeden unikatowy sposób uporządkowania tych bajtów w pamięci lub w czasie transmisji przez dowolne medium i musi być użyta jedna z wielu konwencji ustalająca kolejność bajtów (ang. byte order lub endianness).

**Big endian** to forma zapisu danych, w której najbardziej znaczący bajt umieszczony jest jako pierwszy.

**Little endian** to forma zapisu danych, w której najmniej znaczący bajt umieszczony jest jako pierwszy.


### Zadanie 7.

Jaką rolę pełnią **kody sterujące** standardu **ASCII** o numerach 0, 4, 7, 10 i 12?

**ASCII** (American Standard Code for Information Interchange) -- siedmiobitowy system kodowania znaków. 

**Kod sterujący** -- kod, który w danym kodowaniu znaków nie przenosi informacji o samym znaku, ale służy do sterowania urządzeniem przetwarzającym.

Kody:

* 0 - **Null**: Do nothing
* 4 - **End-of-Transmission**: Its intended use is to indicate the conclusion of a transmission that may have included one or more texts and any associated message headings.
* 7 - **Bell character**: Originally sent to ring a small electromechanical bell on tickers and other teleprinters and teletypewriters to alert operators at the other end of the line, often of an incoming message.
* 10 - **Newline**: Used to signify the end of a line of text and the start of a new one.
* 12 - **Page break**: A marker in an electronic document that tells the document interpreter that the content which follows is part of a new page. A page break causes a form feed to be sent to the printer during spooling of the document to the printer.

### Zadanie 8.

Jakie ograniczenia standardu ASCII przyczyniły się do powstania **UTF-8**? Wyjaśnij zasadę
kodowania znaków do postaci binarnej UTF-8 i zapisz poniższy ciąg znaków w systemie szesnastkowym:

**UTF-8** (8-bit Unicode Transformation Format) – system kodowania, wykorzystujący od 1 do 4 bajtów do zakodowania pojedynczego znaku, w pełni kompatybilny z ASCII. Jest najczęściej wykorzystywany do przechowywania napisów w plikach i komunikacji sieciowej.

Tablica ASCII ma tylko 128 znaków - do wielu celów to jest zdecydowanie za mało, UTF-8 rozwiązuje ten problem.

Kodowanie zależy od tego o jakim znaku mówimy. Dla odpowiednich przedziałów kodów korzystamy z tabeli:

![alt text](https://i.imgur.com/kS5LBGy.png "Logo Title Text 1")


Tekst do zakodowania: *Proszę zapłacić 5€!*

50 72 6f 73 7a c4 99 20 7a 61 70 c5 82 61 63 69 c4 87 20 35 e2 82 ac 21

Dla przykładu popatrzmy na €:

1. Kod dla € to U+20AC.
2. Jest to przedział między U+0800 a U+FFFF, więc potrzebujemy 3 bajtów. 
3. $20AC_{16} = 0010 0000 1010 1100_2$. 
4. Korzystamy z tabeli w taki sposób, że w miejsce każdego $x$ wstawiamy kolejne bity. 
5. Dostajemy na koniec takie kodowanie: $1110 \space 0010 \space 1000 \space 0010 \space 1010 \space 1100$ 
6. Co konwertujemy do systemu szesnastkowego: $1110 \space 0010 \space 1000 \space 0010 \space 1010 \space 1100 = E2 \space 82 \space AC$