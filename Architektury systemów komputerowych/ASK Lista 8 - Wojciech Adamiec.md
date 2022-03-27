# ASK Lista 8 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 3, 4

### Zadanie 1.
:::info
![](https://i.imgur.com/JUZsVdr.png)
:::

**Plik relokowalny** to plik generowany przez kompilator lub assembler podczas komplikacji pliku z kodem źródłowym, może on zostać również utworzony przez konsolidator w wyniku połączenia kilku plików relokowalnych. Są one przeznaczone do późniejszego przetwarzania przez konsolidator w celu uzyskania pliku wykonywalnego lub biblioteki dynamicznej. Mają one rozszerzenie `.o`, a generowane są poleceniem `gcc -o [nazwa].o [nazwa].c`.

Sekcja `.strtab` (string table) przechowuje tablice stringów dla wszystkich referencji, tzn. stringi reprezentujące nazwy symboli. Sekcja `.shstrtab` (section header string table) przechowuje nazwy sekcji.

![](https://i.imgur.com/hE3dCXx.png)
![](https://i.imgur.com/v8OtD5U.png)

### Zadanie 2.
:::info
![](https://i.imgur.com/fy2Apdb.png)
:::

Symbole silne wypierają symbole słabe. Oznacza to, że wywołanie main spowoduje następnie wywołanie `p2`, które zostało zainicjalizowane (z pliku `-b`), co z kolei spowoduje wydrukowanie zmiennej `main`, która również została zainicjalizowana (z pliku `-a`).

Gdybyśmy chcieli przypisać wartość do zmiennej `main` w pliku `-b` to dostaniemy `multiple definition of main`.

Jak w `p2` przypiszemy wartość pod zmienną `main` to przy wykonaniu programu dostaniemy `segmentation fault`.

![](https://i.imgur.com/P7KUDCd.png)

### Zadanie 3.
:::info
![](https://i.imgur.com/VAECCSe.png)
:::

![](https://i.imgur.com/g8GFFE7.png)

Rozwiązuje pierwszy podpunkt. Dla `libm.a` dostaje błąd z jakiegoś powodu.

test.c:
```c=
#include <stdio.h>

int main(){
    printf("Hello world!");
}
```
![](https://i.imgur.com/6RaF1R9.png)

Object dumpy są takie same.

Jeśli chodzi o zawartość to:

![](https://i.imgur.com/oGqbjRL.png)

`test1` jest zauważalnie większy.

Możemy porównać wyniki komendy `readelf -a`:

![](https://i.imgur.com/eTHytT8.png)

Czyli: Tak, flaga `-Og` nie implikuje użycia flagi `-g`.

Co dokładnie się dzieje:
https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html
https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html

![](https://i.imgur.com/ThBItRc.png)

Dostajemy od razu odpowiedź:

![](https://i.imgur.com/vib0DpY.png)

### Zadanie 4.
:::info
![](https://i.imgur.com/8QtJV2T.png)
:::

Błąd występuje przy próbie nadpisania `char* s`. Stała znakowa została wrzucona do sekcji `.rodata` - tylko do odczytu. Stąd błąd, przy próbie:

![](https://i.imgur.com/R9BxmTZ.png)

![](https://i.imgur.com/4lIqwsq.png)

Poprawiamy to w taki sposób -- nie chcemy na stacku mieć tej stałej.

```c=
#include <stdlib.h>
#include <string.h>


char *somestr(void) { 
    char *text = malloc(14);
    memcpy(text, "Hello, world!", strlen("Hello, world!") + 1);
    return text;
}
```

Wtedy nasz string jest `.data`, więc można go edytować.

![](https://i.imgur.com/lYJLcHg.png)

Dostajemy:

![](https://i.imgur.com/JJROcn1.png)

### Zadanie 5.
:::info
![](https://i.imgur.com/uquz38u.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/qmjF6XD.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/HrQnmmZ.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/r0oMECJ.png)
:::
