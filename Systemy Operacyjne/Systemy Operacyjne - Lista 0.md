# Systemy Operacyjne - Lista 0

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 2, 5, 7, 8

### Zadanie 1.
:::info
![](https://i.imgur.com/EsEIoWB.png)
:::

**Exception**: An exception is an abrupt change in the control flow in response to some change in the processor’s state. After raising an exception specific exception handler takes control of the flow.

![](https://i.imgur.com/qzxRi44.png)

Exceptions can be divided into four classes: interrupts, traps, faults, and aborts.

**Hardware interrupt**: Interrupts occur asynchronously as a result of signals from I/O devices that are external to the processor. Hardware interrupts are asynchronous in the sense that they are not caused by the execution of any particular instruction.

After the current instruction finishes executing, the processor notices that the interrupt pin has gone high, reads the exception number from the system bus, and then calls the appropriate interrupt handler. When the handler returns, it returns control to the next instruction (i.e., the instruction that would have followed the current instruction in the control flow had the interrupt not occurred).

![](https://i.imgur.com/NL9Br8v.png)

Przykłady:

1. Naciśnięcie przycisku klawiatury
2. Poruszenie myszy
3. Otrzymanie danych z karty sieciowej

**Trap**: Traps are intentional exceptions that occur as a result of executing an instruction. Like interrupt handlers, trap handlers return control to the next instruction. The most important use of traps is to provide a procedure-like interface between user programs and the kernel, known as a system call.

![](https://i.imgur.com/wDrF6Lw.png)

Przykłady:

1. fork (tworzenie nowego procesu)
2. read (czytanie z pliku)
3. exit (zakończenie aktualnego procesu)

W jakim scenariuszu wyjątek procesora nie oznacza błędu czasu wykonania programu?

1. Wyjątki asynchroniczne (przerwania sprzętowe)
2. Page fault
3. Syscall

Kiedy pułapka jest generowana w wyniku prawidłowej pracy programu?

1. Syscall
2. Breakpointy (w debugerze)

### Zadanie 2.
:::info
![](https://i.imgur.com/5zeusAt.png)
:::

At system boot time (when the computer is reset or powered on), the operating system allocates and initializes a jump table called an exception table, so that entry k contains the address of the handler for exception k.

![](https://i.imgur.com/CyiV2k9.png)

Some of these numbers are assigned by the designers of the processor. Other numbers are assigned by the designers of the operating system kernel.

At run time (when the system is executing some program), the processor detects that an event has occurred and determines the corresponding exception number k. The processor then triggers the exception by making an indirect procedure call, through entry k of the exception table, to the corresponding handler.

An exception is akin to a procedure call, but with some important differences:

1. As with a procedure call, the processor pushes a return address on the stack before branching to the handler. However, depending on the class of exception, the return address is either the current instruction or the next instruction.
2. The processor also pushes some additional processor state onto the stack that will be necessary to restart the interrupted program when the handler returns. For example, an x86-64 system pushes the EFLAGS register containing the current condition codes, among other things, onto the stack.
3. When control is being transferred from a user program to the kernel, all of these items are pushed onto the kernel’s stack rather than onto the user’s stack.
4. Exception handlers run in kernel mode, so that they have complete access to all system resources.

Once the hardware triggers the exception, the rest of the work is done in software by the exception handler. After the handler has processed the event, it optionally returns to the interrupted program by executing a special “return from interrupt” instruction, which pops the appropriate state back into the processor’s control and data registers, restores the state to user mode if the exception interrupted a user program, and then returns control to the interrupted program.

**Kernel mode**, also known as system mode, is one of the central processing unit (CPU) operating modes. While processes run in kernel mode, they have unrestricted access to the hardware. The other mode is user mode, which is a non-privileged mode for user programs.

Dlaczego osobny stos?

-> Żeby nie odkładać na stos użytkownika zbędnych rzeczy oraz, żeby nie ryzykować przepełnieniem tego stosu.

### Zadanie 3.
:::info
![](https://i.imgur.com/5zWgNTa.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/QYSMbyh.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/mP1rovC.png)
:::

`volatile` oznacza zmienną, która może zmienić wartość niezależnie od kodu, w którym się znajduje. Zmusza kompilator do tego, żeby nie cache'ował zmiennej i żeby przy każdym odwołaniu do niej wczytywał ją z pamięci. 
 
Należy używać tego słowa kluczowego np. gdy mamy wskaźnik na adres pod którym jest zmapowana pamięć jakiegoś urządzenia z którym się komunikujemy.

Przykład:

In this example, the code sets the value stored in foo to 0. It then starts to poll that value repeatedly until it changes to 255:

```c=
static int foo;

void bar(void) {
    foo = 0;

    while (foo != 255)
         ;
}
```
An optimizing compiler will notice that no other code can possibly change the value stored in foo, and will assume that it will remain equal to 0 at all times. The compiler will therefore replace the function body with an infinite loop similar to this:
```c=
void bar_optimized(void) {
    foo = 0;

    while (true)
         ;
}
```
However, foo might represent a location that can be changed by other elements of the computer system at any time, such as a hardware register of a device connected to the CPU. The above code would never detect such a change; without the volatile keyword, the compiler assumes that the current program is the only part of the system that could change the value (which is by far the most common situation).

To prevent the compiler from optimizing code as above, the volatile keyword is used:

```c=
static volatile int foo;

void bar (void) {
    foo = 0;

    while (foo != 255)
        ;
}
```
With this modification the loop condition will not be optimized away, and the system will detect the change when it occurs.

Dzięki `volatile` signal handler może mieć poprawny dostęp do jakiejś zmiennej naszego programu (dokładniej nasz program zawsze będzie czytał wartość zmiennej z pamięci)


Inny przykład: (działa dla CLANG, nie działa dla GCC)
```c=
#include <stdio.h>


int main (void)                 // main class declaration in the code
{
    const volatile int local_value = 10 ; // declaring constant volatile integer variable with assigned value
    int *ptr = ( int* ) &local_value ;
    printf ( " The initial value of the local_value is  : %d \n ", local_value ) ;
    *ptr = 2137 ;  // value to the pointer
    printf ( " The modified value of the local_value is: %d \n ", local_value ) ;
    return 0 ;
}
```

### Zadanie 6.
:::info
![](https://i.imgur.com/0eNDRAz.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/069mdK9.png)
:::

**opendir** SYS_openat(), SYS_fstat(), SYS_brk()
**readdir** SYS_getdents()
**printf** SYS_fstat(), SYS_write()
**closedir** SYS_close()

**opendir** używa brk

**Wywołanie systemowe** (system call): stanowi interfejs między wykonywanym programem a (posiadającym zwykle wyższe uprawnienia) jądrem systemu operacyjnego.

**ltrace -S**: Śledzi i pokazuje wywołania systemowe.

**Wywołanie systemowe brk**: Zmienia wielkość sterty programu.

The brk() and sbrk() functions are used to change dynamically the amount of space allocated for the calling process's data segment. The change is made by resetting the process's break value and allocating the appropriate amount of space. The break value is the address of the first location beyond the end of the data segment. The amount of allocated space increases as the break value increases. Newly allocated space is set to zero. If, however, the same memory space is reallocated to the same process its contents are undefined.

![](https://i.imgur.com/avMTk7V.png)

![](https://i.imgur.com/CpQ9SRs.png)

![](https://i.imgur.com/SWup8YQ.png)


### Zadanie 8.
:::info
![](https://i.imgur.com/3zDNztY.png)
:::

**strace** — narzędzie do analizy kodu badające interakcję programu z jądrem systemu operacyjnego. Śledzi wywołania systemowe oraz sygnały w procesie.

**Standardowe wejście i wyjście**

In computer programming, standard streams are interconnected input and output communication channels between a computer program and its environment when it begins execution.

The three input/output (I/O) connections are called standard input (stdin), standard output (stdout) and standard error (stderr).

Standard input is a stream from which a program reads its input data. The program requests data transfers by use of the read operation.

Standard input is a stream from which a program reads its input data. The program requests data transfers by use of the read operation.

In Unix and Unix-like computer operating systems, a file descriptor (FD, less frequently fildes) is a unique identifier (handle) for a file or other input/output resource, such as a pipe or network socket.

**Ścieżka** - ciąg znaków będący identyfikatorem pliku w drzewiastej strukturze będącej abstrakcją zawartości dysku.

![](https://i.imgur.com/4FTpL3g.png)

Używamy komendy `strace ./2_cat`. Dostajemy listę wywołan systemowych wraz z ich argumentami.

Po włączeniu programu program zatrzyma się na wywołaniu read w celu wczytania znaków (bo argumentem pierwszym jest 0, więc jest to standardowe wejście)

![](https://i.imgur.com/d1llxqm.png)

Po naciścnięciu "enter" jest wywołana procedura write, program wypisuje informacje na standardowe wyjście (kod 1). Zwraca liczbę wczytanych bajtów (wpisane znaki plus znak końca linii) oraz wypisuje odebraną zawartość.

PYTANIE:
Naciśnij kombinację klawiszy «CTRL+D»
kończąc  wejściowy  strumień  danych – co zwróciło **read**?  

Nacisniecie Ctrl+D, które wysyła do terminala komunikat EOF- o zakonczeniu pliku, powoduje ze read zwraca 0, następnie program konczy działanie.


Zmodyfikuj  program  tak,  by  czytał  z  pliku podanego w linii poleceń. Co się stanie, jeśli przekażesz ścieżkę do katalogu zamiast do pliku regularnego?

![](https://i.imgur.com/8lHV7cL.png)



używając open , otwieramy wywołanie read by zamiast używać deskryptora pliku dla standardowego wejscia, używało deskryptora pliku, którego scieżka została podana na wejściu.

Teraz, gdy uruchomimy zmodyfikowany program ze scieżką do pliku jako argumentem - program wypisze zawartość tego pliku.

Jeśli ściezka będzie wskazywała na katalog a nie na plik to wywołanie read zakończy się błędem "read error: Is a directory".

![](https://i.imgur.com/7QbynoW.png)
```bash=
CC = gcc -g
CFLAGS = -Og -Wall
CPPFLAGS = -Iinclude -DLINUX -D_GNU_SOURCE 
LDFLAGS = -Llibapue -lapue

LIBAPUE = libapue/libapue.a 
LIBAPUE_SRC = $(wildcard libapue/*.c)
LIBAPUE_OBJ = $(patsubst %.c,%.o,$(LIBAPUE_SRC))

PROGS =	1_ls 2_cat

all: $(PROGS)

%: %.c $(LIBAPUE)
    $(CC) $(CFLAGS) $(CPPFLAGS) -o $@ $< $(LDFLAGS) $(LDLIBS)

$(LIBAPUE): $(LIBAPUE_OBJ)
    $(AR) rc $@ $^

clean:

	rm -f $(PROGS) *.o *~
	rm -f $(LIBAPUE) $(LIBAPUE_OBJ)

# vim: ts=8 sw=8 noet
```