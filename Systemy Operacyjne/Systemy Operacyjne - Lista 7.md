# Systemy Operacyjne - Lista 7

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1

### Zadanie 1.
:::info
![](https://i.imgur.com/gpBR2me.png)
:::

**Odwzorowanie plików w pamięć** (ang. memory-mapped files) to zmapowanie obszaru pliku lub zasobu plikopodobnego do pamięci wirtualnej procesu. Po zmapowaniu pliku, do jego zawartości można dostać się bezpośrednio poprzez operowanie na jego bajtach w odpowiadającym obszarze pamięci. Strony są automatycznie ładowane z pliku, gdy zajdzie taka potrzeba.

**Odwzorowanie pamięci anonimowej** (ang. anonymous mappings) to mapowanie, które nie ma odpowiadającego pliku, a strony mapowania są zainicjalizowane zerami.

**Odwzorowanie prywatne** (MAP_PRIVATE) działa tak, że modyfikacje zawartości odwzorowania nie są widoczne dla innych procesów, a dla odwzorowań plików w pamięć - nie są zapisywane do pliku. Jądro obsługuje ją leniwie – poprzez tworzenie kopii strony przy próbie zapisu. Dzięki temu zmiany są widoczne tylko w procesie, który je wykonał.

**Odwzorowanie dzielone** (MAP_SHARED) sprawia, że modyfikacje zawartości odwzorowania są widoczne dla innych procesów dzielących to odwzorowanie oraz w przypadku odwzorowań plików w pamięć, są zapisywane do plików. Pamięć odzworowana może być dzielona z odwzorowaniami w innych procesach (wpisy tabeli stron każdego procesu wskazują na to samo miejsce w pamięci RAM) na dwa sposoby: dwa procesy odwzorowują ten sam obszar pliku lub poprzez fork(2) (dziecko dziedziczy wszystkie odwzorowania rodzica).

**Czy pamięć obiektów odwzorowanych w pamięć prywantnie może być współdzielona?**

![](https://i.imgur.com/YlWp7AU.png)
![](https://i.imgur.com/ROe3Ama.png)

**Czemu można tworzyć odwzorowania plików urządzeń blokowych w pamięć, a znakowych nie?**

Urządzenia znakowe operują na pojedynczych znakach, odwzorowanie ich w pamieci nie ma więc sensu. (nie ma bufora do zmapowania).

As this device acts like a file – programs can do almost everything except seeking. Every file operation on this object commands the driver to do something inside the Linux kernel and start reading some data from the hardware.

### Zadanie 2.
:::info
![](https://i.imgur.com/cmQfEVF.png)
:::

![](https://i.imgur.com/CGkveAZ.png)

**Prywatne odwzorowanie pliku**: głównym zastosowaniem jest zainicjalizowanie obszaru pamięci z zawartości pliku, np. inicjalizacja sekcji text lub data procesu z pliku wykonywalnego lub biblioteki współdzielonej.

**Prywatne odwzorowanie anonimowe**: alokacja nowej pamięci (pustej, tzn. wypełnionej zerami) dla procesu, np. używając malloc(3), który wykorzystuje mmap(2).

**Dzielone odwzorowanie pliku**: Przy I/O dla plików dostarczana jest alternatywa dla używania read(2) oraz write(2), umożliwienie szybkiej komunikacji międzyprocesowej (IPC) dla procesów niepowiązanych ze sobą

**Dzielone odzworowanie anonimowe**: umożliwienie szybkiej komunikacji międzyprocesowej (IPC) dla procesów powiązanych ze sobą

**Co się dzieje z odwzorowaniami przy `fork`?**:
Są współdzielone na zasadzie *copy on write*.

**Co się dzieje z odwzorowaniami przy `execve`?**:

![](https://i.imgur.com/t0A9Ir6.png)

**Pokaż jak tworzyć odwzorowania przy użyciu `mmap`**:

https://man7.org/linux/man-pages/man2/mmap.2.html

```c=
void *mmap(void *addr, size_t length, int prot, int flags,
           int fd, off_t offset);
           
// prywatne odwzorowanie pliku
void *private_file = mmap(NULL, [size], [prot], MAP_PRIVATE | MAP_FILE, [fd], [offset]);
// prywatne odwzorowanie anonimowe
void *private_anon = mmap(NULL, [size], [prot], MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
// dzielone odwzorowanie pliku
void *shared_file = mmap(NULL, [size], [prot], MAP_SHARED | MAP_FILE, [fd], [offset]);
// dzielone odwzorowanie anonimowe
void *shared_anon = mmap(NULL, [size], [prot], MAP_SHARED | MAP_ANONYMOUS, -1, 0);
```

**W jaki sposób jądro zwiększa rozmiar stosu do ustalonego limitu?**:

TODO

**Kiedy jądro wyśle sygnał SIGBUS do procesu posiadającego odwzorowanie pliku w pamięć?**:

Z manuala `mmap`:

SIGBUS Attempted access to a page of the buffer that lies beyond the end of the mapped file.

Idiotoodporny obrazek:

![](https://i.imgur.com/HdmDOCw.png)


### Zadanie 3.
:::info
![](https://i.imgur.com/4axSIyo.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/qOjeXmF.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/NB5mzbJ.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/1RkWvFo.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/Q6SObbW.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/euBUaVH.png)
:::