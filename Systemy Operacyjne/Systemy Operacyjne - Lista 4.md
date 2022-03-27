# Systemy Operacyjne - Lista 4

## Wojciech Adamiec, 310064

### Deklarowane zadania: 5, 6

### Zadanie 1.
:::info
![](https://i.imgur.com/U7iMvWV.png)
:::

### Zadanie 2.
:::info
![](https://i.imgur.com/z4djyi3.png)
:::

### Zadanie 3.
:::info
![](https://i.imgur.com/PaPHo3X.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/Te6dbZB.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/2L03efO.png)
:::

**Rekord katalogu** - Katalogi to specjalne pliki składające się z rekordów. Każdy rekord to para (nazwa, plik).

**Metadane** - Atrybuty plikum, dane niezwiązane bezpośrednio z jego zawartością. Typ, rozmiar, uprawnienia itp... 

**Dowiązanie** - In computing, a hard link is a directory entry that associates a name with a file in a file system. All directory-based file systems must have at least one hard link giving the original name for each file. The term “hard link” is usually only used in file systems that allow more than one hard link for the same file.

Creating an additional hard link has the effect of giving one file multiple names (e.g. different names in different directories) all of which independently connect to the same data on the disk, none of which depends on any of the others.

Czemu nie można modyfikować katalogów przy pomocy wywołań `read` i `write`?

W przypadku katalogów nie mamy do czynienia z ciągiem znaków, tylko całymi rekordami. Próba czytania lub pisania do katalogów w sposób inny niż przeczytanie rekordu/modyfikacja rekordu nie ma żadnego sensu i może powodować problemy.

Jakim wywołaniem systemowym można wczytać rekord katalogu?

getdirentries
readdir

https://man7.org/linux/man-pages/man3/opendir.3.html
https://man7.org/linux/man-pages/man3/readdir.3.html

Dlaczego zawartość katalogu nie jest posortowana?

Ze względów optymalizacyjnych.

Z czego wynika podana liczba dowiązań (20)?

To są po prostu podkatalogi (oraz `.` `..`)

### Zadanie 6.
:::info
![](https://i.imgur.com/nN6v7T8.png)
:::

TOCTTOU - Time of check to time of use

```c=
#include "csapp.h"

bool f_lock(const char *path) {
    if (access(path, F_OK) == 0)
        return false;
    // Przerwa
    (void)Open(path, O_CREAT|O_WRONLY, 0700);
    return true;
}

void f_unlock(const char *path) {
    Unlink(path);
}
```

Wyścig znajdouje się między sprawdzeniem czy plik istnieje, a jego stworzeniem.

https://www.freebsd.org/cgi/man.cgi?query=open&sektion=2

`If O_EXCL is	set with O_CREAT and the file already exists, open() returns an error.  This may	be used	to implement a simple exclusive access locking mechanism.`

Wersja poprawiona

```c=
#include "csapp.h"

bool f_lock(const char *path) {
    return Open(path, O_CREAT|O_EXCL|O_WRONLY, 0700) >= 0;
}

void f_unlock(const char *path) {
    Unlink(path);
}
```

### Zadanie 7.
:::info
![](https://i.imgur.com/ldLeCs8.pngg)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/dEHhP30.png)
:::
