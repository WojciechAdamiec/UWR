# Systemy Operacyjne - Lista 12

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 2, 6, 8

### Zadanie 1.
:::info
![](https://i.imgur.com/qfT2cE6.png)
:::

`__thread()` powoduje, że każdy wątek dostaje swoją instancje.

**Zmienna współdzielona**

Zmienna, do której referencję robią co najmniej dwa różne wątki.

**Wyścig**

Sytuacja, gdy finalny stan programu może zależeć od przeplotu wątków.

---

Zmienne:
* myid - dzielona, bo przekazujemy adres do pthread_create
* strtab - globalna zmienna dzielona przez wszystkie wątki
* vargp - ten sam adres co myid, współdzielona
* cnt - dzielone przez wszystkie `thread()`, bo lokalna, statyczna
* argc - nie jest współdzielona
* argv[0] - przypisywane do zmiennej strtab, więc dzielone

Wyścigi:
* cnt - jak na wykładzie (load, update, store jest sekcją krytyczną)
* myid - myid: zanim w `thread()` nastąpi przypisane wartości do własnej instancji zmiennej `myid`, w main wartość `myid` może ulec zmianie. W wyniku tego możemy dosktać kilka wątków o takiej samej wartości `myid`

### Zadanie 2.
:::info
![](https://i.imgur.com/A44lB63.png)
:::

**Sekcja krytyczna**

Fragment kodu, w którym proces robi dostęp/update do danych, które są współdzielone przez przynajmniej jeden inny proces. Dla poprawnego działania programu musimy mieć pewność, że żadne dwa procesy nie są jednocześnie w tej samej sekcji krytycznej.

Rozwiązanie problemu sekcji krytycznej musi spełniać następujące wymagania:

1. **Mutual exclusion** Jeśli jakiś proces jest w sekcji krytycznej, to żaden inny proces nie może być w sekcji krytycznej.
2. **Progress** Jeśli żaden proces nie jest w sekcji krytycznej i jakieś procesy chcą wejść do sekcji krytycznej to wtedy jeden z nich do niej wejdzie. 
3. **Bounded waiting** Żaden proces nie może czekać w nieskończoność na wejście do sekcji krytycznej.

**Wyłączanie przerwań**

(ang. interrupt disable) to sposób rozwiązania problemu sekcji krytycznych. Polega ono na wyłączeniu obsługi przerwań w momencie, gdy proces wchodzi do swojej sekcji krytycznej, a następnie po włączeniu obsługi przerwań, gdy proces z niej wyjdzie. Działa to dlatego, że zmiana procesu odbywa się tylko poprzez przerwania, a więc wyłączając przerwania pozbawiamy możliwość zmiany procesu w trakcie wykonywania sekcji krytycznej.

Dlaczego to jest kiepski pomysł?

Here, the trouble manifests in numerous ways: a greedy program could call `lock()` at the beginning of its execution and thus monopolize the processor; worse, an errant or malicious program could call `lock()` and go into an endless loop. In this latter case, the OS never regains control of the system, and there is only one recourse: restart the system. Using interrupt disabling as a generalpurpose synchronization solution requires too much trust in applications.

Second, the approach does not work on multiprocessors. If multiple
threads are running on different CPUs, and each try to enter the same
critical section, it does not matter whether interrupts are disabled; threads will be able to run on other processors, and thus could enter the critical section. As multiprocessors are now commonplace, our general solution will have to do better than this.

Third, turning off interrupts for extended periods of time can lead to interrupts becoming lost, which can lead to serious systems problems. Imagine, for example, if the CPU missed the fact that a disk device has finished a read request. How will the OS know to wake the process waiting for said read?

**Prawo Amdahla**

![](https://i.imgur.com/jslL8nI.png)
![](https://i.imgur.com/lwdvnsP.png)

**Blokowanie dronoziarniste**

(ang. fine-grained locking) to sposób pracy przy sekcjach krytycznych. Polega on na wydzielaniu pojedynczych zmiennych i struktur, a następnie utworzeniu dla każdej z nich osobnej blokady. Dzięki temu, przy wielu sekcjach krytycznych wiemy, że w każdej z nich przebywa tylko jeden proces, a więc wiele procesów może wykonywać operacje ze swoich sekcji krytycznych. W ten sposób zwiększamy możliwość zrównoleglenia danych partii programu.

### Zadanie 3.
:::info
![](https://i.imgur.com/46qnrSk.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/ffVsWFE.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/28Q8H6z.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/pm8eYkO.png)
:::

Na początku:
```
    turn = 0
    blocked[0] = false
    blocked[1] = false
```
`P(1)` wykonuje linie: 6, 7, 8
Mamy zatem:
```
    turn = 0
    blocked[0] = false
    blocked[1] = true
```
Teraz następną instrukcją dla `P(1)` będzie 10 (bo `blocked[1-1] == false`)

Teraz `P(0)` wykonuje linie: 6, 7, 12 (wchodzi w sekcję krytyczną)
Mamy zatem:
```
    turn = 0
    blocked[0] = true
    blocked[1] = true
```
Wracamy do `P(1)`. Robimy linię 10, 7 i następnie 12 (bo `turn == id`), czyli wchodzimy w sekcję krytyczną.

Dwa procesy nie mogą równocześnie być w sekcji krytycznej.

### Zadanie 7.
:::info
![](https://i.imgur.com/vQYKrwi.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/4uwGj5m.png)
:::

**P: Proberen V: Verhogen**

**Semafor zliczający**
Semafor, który przyjmuje wartości całkowite nieujemne. Jest licznikiem zestawu dostępnych zasobów.

**Semafor binarny**
Semafor, który przyjmuje wartości 0 lub 1.

- Niech $t_1, t_2, t_3, t_4$ to wątki, które będą korzystać z dwóch zasobów.
- Start programu, inicjalizacja **csem**
    - $mutex = 1$
    - $delay = 0$
    - $count = 2$
- Uruchamiamy wątki $t_1, t_2, t_3, t_4$
- $t_1.P()$, nie zostaje zablokowany
    - $mutex = 1$
    - $delay = 0$
    - $count = 1$
- $t_2.P()$, nie zostaje zablokowany
    - $mutex = 1$
    - $delay = 0$
    - $count = 0$
- $t_3.P()$, brak wolnych zasobów -- blokada
    - $mutex = 1$
    - $delay = 0$
    - $count = -1 \Rightarrow t_3$ zablokowany na $P(delay)$
- $t_4.P()$, brak wolnych zasobów -- blokada
    - $mutex = 1$
    - $delay = 0$
    - $count = -2 \Rightarrow t_4$ zablokowany na $P(delay)$
- $t_1.V()$, kończy działanie
    - $mutex = 1$
    - $delay = 1$
    - $count = -1$ &nbsp;:warning: zwolnienie zasobu nie oznacza, że inny wątek go przejmie
- $t_2.V()$, kończy działanie
    - $mutex = 1$
    - $delay = 1$
    - $count = 0$ &nbsp;&nbsp;&nbsp;&nbsp;:warning: zwolniliśmy dwa zasoby, a ilość uśpionych wątków to dalej 2
- $t_3$ zostaje wznowiony, program wraca z $P(delay)$, $t_3$ otrzymuje dostęp do zasobu
    - $mutex = 1$
    - $delay = 0$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:warning: istnieje 1 wolny zasób i uśpiony proces, ale nigdy się nie wybudzi
    - $count = 0$ &nbsp;&nbsp;&nbsp;&nbsp; :warning: istnieje 1 wolny zasób
- $t_3$ wywołuje $V()$, kończy działanie
    - $mutex = 1$
    - $delay = 0$ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:warning: $count > 0 \Rightarrow delay = 0$
    - $count = 1$ &nbsp;&nbsp;&nbsp;&nbsp; :warning: istnieją 2 wolne zasoby

### Zadanie 9.
:::info
![](https://i.imgur.com/32RETOc.png)
:::
