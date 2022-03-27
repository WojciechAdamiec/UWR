# Systemy Operacyjne - Lista 1

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 2, 3, 4, 6, 7

### Zadanie 1.
:::info
![](https://i.imgur.com/276lBD2.png)
:::

Każdy proces posiada swojego **rodzica** (oprócz init, którego rodzicem jest kernel ppid 0), który utworzył **dziecko** przy pomocy fork(). Każdy proces posiada również swój **identyfikator procesu (PID)**, a więc unikalną liczbę, dzięki której łatwiej jest go zidentyfikować. **Identyfikatorem grupy procesów (PGID)** oznacza się zbiór jednego lub większej ilości procesów, które mogą razem otrzymywać sygnały. **Identyfikator rodzica (PPID)** to identyfikator procesu, który za pomocą fork() utworzył procesy dzieci. **Właściciel** to użytkownik, który uruchomił proces i posiada pełne uprawnienia do kontrolowania ich, np. zatrzymywania lub zabijania. **Wątki jądra** to wątki wykonujące kod jądra, nie są one powiązane z procesami z przestrzeni użytkownika, nie używają również pamięci użytkownika (gdy dodamy vsz do tabeli polecenia ps -eo ... zobaczymy 0 (KiB) dla procesów root). W kolumnie STAT oznacza je litera I. Wywołanie ps bez argumentów sprawi, że wypisana zostanie lista procesów w bieżącej sesji.

Aby dowiedzieć się jakie znaczenie mają poszczególne znaki w kolumnie STAT, używamy man ps i szukamy tego, co nas interesuje:

```
PROCESS STATE CODES
   Here are the different values that the s, stat and state output specifiers 
   (header "STAT" or "S") will display to describe the state of a process:

       D    uninterruptible sleep (usually IO)
       I    Idle kernel thread
       R    running or runnable (on run queue)
       S    interruptible sleep (waiting for an event to complete)
       T    stopped by job control signal
       t    stopped by debugger during the tracing
       W    paging (not valid since the 2.6.xx kernel)
       X    dead (should never be seen)
       Z    defunct ("zombie") process, terminated but not reaped by its parent

   For BSD formats and when the stat keyword is used, 
   additional characters may be displayed:

       <    high-priority (not nice to other users)
       N    low-priority (nice to other users)
       L    has pages locked into memory (for real-time and custom IO)
       s    is a session leader
       l    is multi-threaded (using CLONE_THREAD, like NPTL pthreads do)
       +    is in the foreground process group
```

Wątki jądra można rozpoznąc po `vsz` mającym wartość 0 (kolejna kolumna w `ps` wspomniana wcześniej) oraz po tym, że `cmd` jest w nawiasach kwadratowych, tzn. nie jest znana nazwa polecenia, które je utworzyło. Wątki w pstree można rozpoznać po sposobie zapisu ich nazw: `n*[{name}]` to grupa n wątków.

An unintentionally orphaned process is created when its parent process crashes or terminates. Unintentional orphan processes can be avoided using the process group mechanism.

In a POSIX-conformant operating system, a process group denotes a collection of one or more processes. Among other things, a process group is used to control the distribution of a signal; when a signal is directed to a process group, the signal is delivered to each process that is a member of the group.

Wątki jądra mają ppid = 2 (**kthreads**) -- jednoznaczna metoda.

### Zadanie 2.
:::info
![](https://i.imgur.com/PMk4g5z.png)
:::

**Sierota** - Proces, któremu umarł rodzic.

Jak jądro reaguje na proces, który staje się sierotą?

Podpina proces pod proces `init`, który będzie odpowiedzialny za jego grzebanie.

**Zombie** - Proces, którego wykonanie się zakończyło, ale proces nie został pogrzebany (dalej jest w tabeli procesów).

![](https://i.imgur.com/Mrf693b.png)

Zombie proces grzebie się za pomocą syscalla `wait`.

![](https://i.imgur.com/4iKWGsM.png)

Dlaczego proces nie może sam siebie pogrzebać?

Każdy proces ma przyporządkowany stos kernela. Normalnie stos kernela rodzica służy do pogrzebania procesu dziecka (między innymi zwolnienie stosu kernela dziecka). Gdyby proces miałby się sam pogrzebać to musiałbyć użyć stosu kernela do zwolnienia tego samego stosu kernela co jest niemożliwe.

**Stan procesu** - Running, waiting, stopped, zombie.

Co mogłoby się stać, gdyby dziecko mogło czekać na zmianę stanu swojego rodzica?

Mogłoby dojść do nieskończonej pętli wzajemnych `waitów`.

Co mogłoby się stać, gdyby dziecko miało dwóch rodziców?

Mógłby być problem przy grzebaniu, gdyby oboje czekali na status dziecka. Po pierwszym odczycie dziecko może zostać pogrzebane.

### Zadanie 3.
:::info
![](https://i.imgur.com/TU6ivuO.png)
:::

The proc filesystem is a pseudo-filesystem which provides an interface to kernel data structures.

**Argumenty programu** - Zmienne przekazywane do programu w momencie wykonania.

**Zmienne środowiskowe** - Niejawne zmienne programu, opakowane nieco inaczej niż argumenty. Wartości zmiennych ustawiane poza programem.

cmdline - arguemnty
environ - zmienne środowiskowe

Uid - User ID
Gid - Group ID
Groups - Supplementary group list. To lista grup uzupełniających dziedziczonych po rodzicu, mówią one jakie uprawnienia ma proces
VmPeak - Maksymalny rozmiar pamięci wirtualnej
VmSize - Aktualny rozmiar pamięci wirtualnej
VmRSS - Size of memory portions. Wielkość fizycznej pamięci, która aktualnie jest używana.
Threads - Number of threads
Voluntary_ctxt_switches - Number of voluntary context switches
Nonvoluntary_ctxt_switches - Number of non voluntary context switches

In computing, a context switch is the process of storing the state of a process or thread, so that it can be restored and resume execution at a later point.

Voluntary - przez użytkownika.
Non-voluntary - przez system.

### Zadanie 4.
:::info
![](https://i.imgur.com/aDKr3Hs.png)
:::

Szukamy `ps ax | grep X`.

Znajduje coś takiego:

![](https://i.imgur.com/xJcFcWl.png)

Stack widać od razu. Stertę trzeba za pomocą pliku `/proc/pid/maps`.

**Segmenty programu** - Spójne bloki pamięci o jednolitym przeznaczeniu i atrybutach z punktu widzenia procesu ładowania i uruchamiania programu.

![](https://i.imgur.com/rMEHiOj.png)

**Pamięć anonimowa** - Pamięć niebędąca powiązana z żadnym plikiem ani obiektem. Powszechnym anonimowym mapowaniem jest stos i sterta wspomniane powyżej. Jest ona oznaczona jako [anon].

**Pliki odwzrorowane w pamięć** - (ang. memory-mapped file) to segment pamięci wirtualnej mający bezpośrednie mapowanie co do bajta z jakimś plikiem lub zasobem. Biblioteki współdzielone. Dzięki temu unika się stosowania funkcji systemowych na plikach takich jak read() lub write(), gdyż proces adresuje plik bezpośrednio. Plik może być traktowany jak ciągły obszar w pamięci procesu, dostępny poprzez bezpośrednie operacje pobrania i podstawienia wartości. Wszystkie modyfikacje dokonane w pamięci są później zapisywane na dysku. Znaleźć je można w Mapping jako pliki *.so.

### Zadanie 5.
:::info
![](https://i.imgur.com/wDAP5cM.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/adymH39.png)
:::

**Real** is wall clock time - time from start to finish of the call. This is all elapsed time including time slices used by other processes and time the process spends blocked (for example if it is waiting for I/O to complete). - jest to rzeczywisty czas od uruchomienia do zwrócenia wyniku

**User** is the amount of CPU time spent in user-mode code (outside the kernel) within the process. This is only actual CPU time used in executing the process. Other processes and time the process spends blocked do not count towards this figure. - czas wykorzystywania CPU przez program będąc w user-mode

**Sys** is the amount of CPU time spent in the kernel within the process. This means executing CPU time spent in system calls within the kernel, as opposed to library code, which is still running in user-space. Like 'user', this is only CPU time used by the process. - Czas wykorzystania CPU przez program w trybie kernel-mode (syscalle)

Czemu suma czasów user i sys(a) nie jest równa real(b) real mierzy czas rzeczywisty od początku, a User oraz Real mierzą tylko czas wykorzystania procesora i nie uwzględniaja czasu oczekiwania na IO lub przerw w działaniu.

Czemu suma czasów user i sys(a) może być większa od real? Jeśli Proces wykorzystuje kilka wątków procesora(~procesorów), wtedy usr oraz sys sumują się z każdego użytego wątka procesora(~procesora).

`ulimit -t` The maximum amount of cpu time in seconds.

`echo$?` - zwraca kod wyjścia ostatniego polecenia

### Zadanie 7.
:::info
![](https://i.imgur.com/m0tEYN5.png)
:::

**Kopiowanie przez referencje** - kopia wskaźnika, a nie zawartości pliku.

**Pozycja kursora** - offset przy czytaniu/pisaniu.



### Zadanie 8.
:::info
![](https://i.imgur.com/zuJaYfu.png)
:::
