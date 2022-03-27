# ASK Lista 13 - Wojciech Adamiec
## Zadania Deklarowane: 1

### Zadanie 1.
:::info
![](https://i.imgur.com/UYh3Jte.png)
:::

**predyktor skoków** - obwód cyfrowy w procesorze, którego zadaniem jest zgadnąć, w którą stronę pójdzie gałąź. 

Q: W jaki sposób procesor przetwarza skoki warunkowe?
A: Nowoczesne procesory potrafią przetwarzać instrukcje szybciej, niż one się wykonują. Dlatego przy napotkaniu brancha procesor spekuluje czy warunek zajdzie, wybiera jakąś opcję i przetwarza instrukcje dalej, ale bez modyfikowania fizycznych rejestrów czy pamięci.
Jeśli procesor zgadł to commituje instrukcje do pamięci i rejestrów. 
Jeśli nie to musi odrzucić wykonane instrukcje i wrócić do miejsca rozgałęzienia w pamięci. 


Q: W jakim celu procesor używa predyktora skoków?
A: Procesor potrafi przetwarzać instrukcje szybciej, niż one się wykonują, dlatego w przypadku rozgałęzienia musi spekulować, która z gałęzi się wykona. 

Q: Co musi zrobić, jeśli skok zostanie źle przewidziany? 
A: Musi odrzucić wykonane instrukcje i wrócić do miejsca rozgałęzienia w pamięci. To kosztowna operacja, ~$20$ cykli 

Q: Które skoki warunkowe warto zoptymalizować do instrukcji `cmov`? 
A: Te, które są często używane i kompilator ma problem z ich przewidywaniem

Przepisz poniższy kod tak żeby w linii 4 kompilator nie użył skoku warunkowego: 

```c=
 void merge1(long src1[], long src2[], long dest[], long n) {
     long i1 = 0, i2 = 0;
     while (i1 < n && i2 < n)
         *dest++ = src1[i1] < src2[i2] ? src2[i1++] : src2[i2++];
 }
```

```c=
 void merge2(long src1[], long src2[], long dest[], long n) {
    long i1 = 0, i2 = 0;
    while (i1 < n && i2 < n) {
        long v1 = src2[i1];
        long v2 = src2[i2];
        bool cond = v1 < v2;
        *dest++ = cond ? v1 : v2;
        i1 += cond;
        i2 += (1-cond);
    }
}
```

### Zadanie 2.
:::info
![](https://i.imgur.com/NpP4CSP.png)
:::

### Zadanie 3.
:::info
![](https://i.imgur.com/85oHgfc.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/iwOymM7.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/Be8H8tT.png)
:::

**wirtualna przestrzeń adresowa** - Zestaw zakresów adresów pamięci (wirtualnych), które system operacyjny udostępnia procesowi.

Przy pomocy polecenia `ps -e -o pid,rss,vsz,cmd` wydrukuj listę wszystkich procesów
wraz z zadeklarowanym rozmiarem wirtualnej przestrzeni adresowej

Oblicz rozmiar pamięci wirtualnej używanej przez wszyskie procesy
![](https://i.imgur.com/TTtrCqj.png)

Na podstawie wydruku polecenia `free` określ bieżące użycie i całkowity rozmiar pamięci fizycznej

![](https://i.imgur.com/ib51RNt.png)
Bieżące użycie: $3897872$ bajtów
Całkowity rozmiar: $16268620$ bajtów

Wyjaśnij w jaki sposób stronicowanie na żądanie i współdzielenie pamięci pozwalają systemowi opreacyjnemu na oszczędne zarządzanie pamięcią fizyczną

**stronicowanie na żądanie** - System operacyjny kopiuje stronę z dysku do pamięci tylko jeśli proces zażądał tej strony. Dzięki temu nie ładujemy stron, które nie są używane.
**współdzielenie pamięci** - Jeden proces wystawia segment pamięci, która może być widziana przez inne procesy, służy do komunikacji, pozwala na dostęp do tych samych zasobów wielu procesom, co zapobiega kopiowaniu tych samych danych. 

### Zadanie 6.
:::info
![](https://i.imgur.com/4Zi6Twp.png)
:::