# Systemy Operacyjne - Lista 3

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 2, 3, 5

### Zadanie 1.
:::info
![](https://i.imgur.com/jX3FJga.png)
:::

**Sesja** to pewna liczba grup procesów podłączonych do tego
samego terminala sterującego.

**Terminal sterujący** może należeć do co najwyżej jednej sesji
– można wyświetlić bieżący poleceniem ‘tty’.

**Liderem sesji** jest z reguły proces powłoki. Żeby zostać
liderem sesji należy utworzyć sesję setsid i ustalić terminal
sterujący tcsetsid.

Jeśli powłoka zostanie odłączona od terminala, to dostanie
SIGHUP i zdecyduje co zrobić z procesami, którymi zarządza.

Zewnętrzny terminal:

`strace -e trace=signal xterm -e 'bash -i'`

Wewnątrz nowego terminala:

`sleep 1000 &`
`ps ax -o pid,ppid,sid,command`
`kill -SIGKILL 0`

Zewnętrzny terminal:

`ps ax -o pid,ppid,sid,command | grep sleep`
`cat /proc/[pid]/cmdline`

Zostaje wysłany SIGHUP.

W wariancie zabicia emulatora zamiast tego zostaje wysłany SIGKILL (sleep umiera).


### Zadanie 2.
:::info
![](https://i.imgur.com/DnlkVKR.png)
:::

https://man.netbsd.org/termios.4

For canonical input — You type a line of input; if you make a mistake, you use the erase character (default is Backspace, usually; sometimes Delete) to erase the previous character. If you mess up completely, you can cancel the whole line with the line kill character (not completely standardized, often Control-X). The entire line is gathered and edited up until the end of line character — Return — is pressed. Thereupon, the whole line is made available to waiting programs. Depending on the read() system calls that are outstanding, the whole line will be available to be read (by one or more calls to read()).

For non-canonical input — think vi or vim or whatever — you press a character, and it is immediately available to the program. You aren't held up until you hit return. The system does no editing of the characters; they are made available to the program as soon as they are typed. It is up to the program to interpret things appropriately. Now, vim does do a number of things that look a bit like canonical input. For example, backspace moves backwards, and in input mode erases what was there. But that's because vim chooses to make it behave like that.

Jak konfigurację terminala powinien zmienić program na czas wpisywania hasła przez użytkownika?

-> Opcję echoing, po to, aby wpisane hasło nie zostało od razu przesłane do kolejki wyjściowej.

![](https://i.imgur.com/2VV5fju.png)

### Zadanie 3.
:::info
![](https://i.imgur.com/K6O36CI.png)
:::

Sygnały związane z **zarządzaniem zadaniami**:

* intr wysyła sygnał przerwania
* quit wysyła sygnał zamknięcia
* swtch włącza inną warstwę powłoki
* start/stop wznawia/wstrzymuje wyświetlanie
* susp wysyła sygnał stop

Sygnały związane z **edycją wiersza**:

* erase kasuje ostatni wprowadzony znak,
* kill kasuje cały wiersz
* eof wysyła znak końca pliku (końca wejścia)
* eol/eol2 wysyła znak końca wiersza
* werase kasuje ostatnie wprowadzone słowo
* rprnt powtarza bieżący wiersz
* lnext Receipt of this character causes the next character to be taken literally.

https://man7.org/linux/man-pages/man4/tty_ioctl.4.html

The size of a terminal is kept in kernel-internal structure, and can be queried by the TIOCGWINSZ and set by TIOCSWINSZ ioctls.

Each time the window size is set via TIOCSWINSZ (eg. by xterm when its GUI window was resized) the kernel will send a SIGWINCH signal to the foreground process group of that terminal.

A program like vi catches that signal and updates its idea of the window size via TIOCGWINSZ.

The window size is usually set by the program driving the master end of a pseudo-tty (like xterm or sshd) but any process able to open the tty (whether in read-only or write-only mode) can do it.

A command line interface to those ioctls is via the stty program. (eg. stty cols 80 rows 40). This is useful with real serial terminals, which have no inherent size, and no standard way to pass that info through.

### Zadanie 4.
:::info
![](https://i.imgur.com/6dvPiTY.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/i2jr6yA.png)
:::

1. Łatwo
2. Ctrl + Z -> SIGTSTP; bg
3. To służy do zatrzymania/wznowienia outputu, a nie programu.
4. SIGTTIN (sprawdzamy za pomocą strace). When any process in a background job tries to read from the terminal, all of the processes in the job are sent a SIGTTIN signal. The default action for this signal is to stop the process.
5. Ta konfiguracja odpowiada za stopowanie procesów tła, które chcą coś wypisać w terminalu.

### Zadanie 6.
:::info
![](https://i.imgur.com/b8WSTll.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/g8cOYzc.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/XCXgX9e.png)
:::
