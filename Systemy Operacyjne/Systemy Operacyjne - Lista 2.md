# Systemy Operacyjne - Lista 2

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 3, 4, 5

### Zadanie 1.
:::info
![](https://i.imgur.com/qHzLePH.png)
:::

![](https://i.imgur.com/DhmQhVG.png)

Można wyróżnić następujące stany procesu w systemie Linux:

1. **stopped** - proces zatrzymany, może zostać wznowiony przez inny proces, np. proces został zatrzymany w trakcie debugowania i wznowiony może być tylko przez debugger
2. **running state**:
* **ready** - proces załadowany do pamięci, oczekuje na wykonanie przez CPU
* **executing** - proces będący bieżąco wykonywany (a dokładniej jego instrukcje)
3. **zombie** - proces zakończony, jednak dalej znajduje się w tablicy procesów i oczekuje na obsługę zamknięcia przez proces rodzica
4. **uninterruptible** czyli sen nieprzerywalny to stan procesu, w którym proces jest zablokowany i nie obsługuje żadnych sygnałów
5. **interruptible** czyli sen przerywalny to stan procesu, w którym proces jest zablokowany, jednak oczekuje na zdarzenie takie jak koniec operacji I/O, dostępność zasobu lub sygnał z innego procesu

Dwa ostatnie stany różnią się tym, że sen przerywalny reaguje na sygnały, przez które może zostać obudzony, a sen nieprzerywalny nie obsługuje sygnałów.

Ready <-> Executing:

* Zaplanowanie przez scheduler (jądro operacyjne)

Executing -> Zombie:

* Zamknięcie procesu `exit()` (użytkownik)
* otrzymacie SIGKILL/SIGTERM (jądro)
* błąd I/O (sterownik)
* Zamknięcie w przypadku deadlock

Stopped <-> Running:

* Otrzymanie sygnałów SIGSTOP/SIGCONT (użytkownik)

Interruptible/Uninterruptible <-> Ready

* -> Ready: Wydarzenie I/O (wybudzenie przez jądro)
* -> Ready: Sygnał (tylko dla interruptible)
* -> Interruptible/Uninterruptible: Żądanie wykonania I/O

**Zablokowanie sygnału** to określenie na niedostarczenie sygnału do procesu do momentu odblokowania go przez system operacyjny. Proces blokuje sygnał poprzez użycie funkcji:

```c
int sigprocmask(int how, const sigset_t *set, sigset *oldset)
```

**Zignorowanie sygnału** to sytuacja, w której nie została zdefiniowana procedura obsługi konkretnego sygnału.

Sygnału SIGKILL nie da się zablokować, a zignorowanie tego sygnału spowoduje zabicie procesu.

### Zadanie 2.
:::info
![](https://i.imgur.com/dR4NG1b.png)
:::

### Zadanie 3.
:::info
![](https://i.imgur.com/DF5WxQ8.png)
:::

**Fork**:

Najważniejszym zasobem dziedziczonym z procesu rodzica do procesu potomnego (dziecka) są pliki. Wszystkie deskryptory plików, które zostały otwarte w rodzicu są duplikowane w dziecku tj. używają tego samego wpisu tabeli plików dla każdego otwartego deskryptora.

Równie ważne jest aby rodzic i dziecko korzystali z tego samego offsetu pliku, ponieważ w momencie kiedy oba procesy zapisują na standardowe wyjście to jeśli wyjście standardowe rodzica zostanie przekierowane to ważne jest, aby offset pliku rodzica był aktualizowany przez dziecko, kiedy dziecko zapisuje na standardowe wyjście.

![](https://i.imgur.com/9tPu0Tr.png)

**Execve**:

When a process calls one of the exec functions, that process is completely replaced by the new program, and the new program starts executing at its main function. The process ID does not change across an exec, because a new process is not created; exec merely replaces the current process — its text, data, heap, and stack segments — with a brand-new program from disk.

![](https://i.imgur.com/RKrsaOn.png)

The handling of open files depends on the value of the `close-on-exec` flag for each descriptor.

```c=
int main() {	
  printf("Test");
  fork();
  return 0;
}
```

W zależności od kompilatora powyższy program może wypisać `test` raz albo dwa razy.

Przed jego wywołaniem należy opróżnić bufory `stdio`, ponieważ chcemy uniknąć kilkukrotnego wypisywania danych.

Co jądro robi z konfiguracją zainstalowanych procedur obsługi sygnałow?

-> W trakcie `execve` jądro przywraca domyślną obsługę wyłapywanych sygnałów. Jeżeli program wywołuje `execve` to cały jego kod i dane są zwalniane z pamięci, więc nie można ich już używać do obsługi sygnału.
### Zadanie 4.
:::info
![](https://i.imgur.com/cwj47SM.png)
:::

Polecenie `man` daje wzgląd w manuala.

1. `kill` wysyła `TERM`.
2. `pkill` wysyła `SIGTERM`.
3. `xkill`: This command does not provide any warranty that the application whose connection to the X server is closed will abort nicely, or even abort at all. All this command does is to close the connection to the X server. Many existing applications do indeed abort when their connection to the X server is closed, but some can choose to continue.

Polecenia te wykonuje się w taki sposób:

```
$ kill [pid]
$ pkill [process name]
$ xkill (po czym wybiera się okno, które zabijamy)
```
Warto dodać, że po kilkukrotnym uruchomieniu xeyes (np. dla 5 działających procesów jednocześnie) pkill xeyes zabije wszystkie te procesy.

Wykonując CTRL+Z wywołujemy sygnał SIGTSTP (lekko się różni od SIGSTOP) na programie xeyes, wznawiamy jego działanie przez fg lub bg (zależy czy chcemy aby działało w tle, czy nie).

**Sygnały oczekujące** to sygnały, których dostarczenie jest wstrzymane do momentu wyjścia przez proces z nieprzerywalnego snu.

Sygnały `SIGUSR1`, `SIGUSR2`, `SIGHUP` i `SIGINT` wysyłamy w procedurze `kill -[sygnał] [pid]`. W pliku `/proc/pid/status` znajdują się pola dotyczące sygnałów:

* `SigQ` Liczba oczekujących sygnałów dla procesu i jego podprocesów.
* `SigPnd`, `ShdPnd` Maski sygnałów oczekujących.
* `SigBlk`, `SigIgn`, `SigCgt` to maski sygnałów blokowanych, ignorowanych oraz złapanych.

Po uruchomieniu xeyes możemy sprawdzić maski przez `cat /proc/[pid]/status`, klikamy `CTRL+Z`, żeby wysłać sygnał `SIGTSTP`, a następnie wywołujemy kolejno:

```
$ kill -SIGUSR1 [pid]
$ cat /proc/[pid]/status
$ kill -SIGUSR2 [pid]
$ kill -SIGHUP [pid]
$ kill -SIGINT [pid]
```

Jako pierwszy zostanie dostarczony `SIGHUP`.

### Zadanie 5.
:::info
![](https://i.imgur.com/yZ6LlbF.png)
:::
```c=
/* See LICENSE file for copyright and license details. */

#include <sys/types.h>
#include <sys/wait.h>

#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define LEN(x)	(sizeof (x) / sizeof *(x))
#define TIMEO	30

static void sigpoweroff(void);
static void sigreap(void);
static void sigreboot(void);
static void spawn(char *const []);

static struct {
	int sig;
	void (*handler)(void);

} sigmap[] = {
	{ SIGUSR1, sigpoweroff },
	{ SIGCHLD, sigreap     },
	{ SIGALRM, sigreap     },
	{ SIGINT,  sigreboot   },
};

#include "config.h"

static sigset_t set;

int main(void)
{
	int sig;
	size_t i;

	if (getpid() != 1)
		return 1;

	chdir("/");
	sigfillset(&set); # Pobranie sygnałów z systemu
	sigprocmask(SIG_BLOCK, &set, NULL);
	spawn(rcinitcmd); # Rozruch systemu
	while (1) {
		alarm(TIMEO); # Za 30 sekund dostane sygnał alarm
		sigwait(&set, &sig); # Czekam na sygnały z setu
		for (i = 0; i < LEN(sigmap); i++) {
			if (sigmap[i].sig == sig) {
				sigmap[i].handler();
				break;
			}
		}
	}
	/* not reachable */
	return 0;
}

static void
sigpoweroff(void)
{
	spawn(rcpoweroffcmd);
}

static void
sigreap(void)
{
	while (waitpid(-1, NULL, WNOHANG) > 0)
		;
	alarm(TIMEO);
}

static void
sigreboot(void)
{
	spawn(rcrebootcmd);
}

static void
spawn(char *const argv[])
{
	switch (fork()) {
	case 0:
		sigprocmask(SIG_UNBLOCK, &set, NULL);
		setsid();
		execvp(argv[0], argv);
		perror("execvp");
		_exit(1);
	case -1:
		perror("fork");
	}
}
```
**setsid()** creates a new session if the calling process is not a
       process group leader.  The calling process is the leader of the
       new session (i.e., its session ID is made the same as its process
       ID).  The calling process also becomes the process group leader
       of a new process group in the session (i.e., its process group ID
       is made the same as its process ID).

       The calling process will be the only process in the new process
       group and in the new session.
**sigfillset()** function shall initialize the signal set pointed
       to by set, such that all signals defined in this volume of
       POSIX.1‐2017 are included.
       
**sigprocmask()** is used to fetch and/or change the signal mask of
       the calling thread.  The signal mask is the set of signals whose
       delivery is currently blocked for the caller.
       
**sigwait()** function suspends execution of the calling thread
       until one of the signals specified in the signal set set becomes
       pending.  The function accepts the signal (removes it from the
       pending list of signals), and returns the signal number in sig.
       
### Zadanie 6.
:::info
![](https://i.imgur.com/pPehzj3.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/jN8BS7R.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/QNEsOJt.png)
:::
