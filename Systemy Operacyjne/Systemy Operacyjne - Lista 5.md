# Systemy Operacyjne - Lista 5

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 3, 4, 6, 7

### Zadanie 1.
:::info
![](https://i.imgur.com/yKkhjcD.png)
:::

**Jednokierunkowość pipe'a** - Komunikacja odbywa się tylko w jedną stronę. Pierwszy proces ustawia pipe jak swoje wyjście, drugi proces ustawia pipe jako swoje wejście.

![](https://i.imgur.com/LBipgiV.png)

**Bufor** - Pudełko na dane w komunikacji za pomocą rury. Jeśli rura jest przepełniona to próba napisania do niej uśpi proces piszący do czasu zwolnienia rury. Podobnie próba odczytania danych z pustej rury uśpi proces czytający do czasu zapełnienia rury.

Operacja `write` na rurze daje nam gwarancję atomowego zapisu - dzięki temu jeśli dwa procesy piszą do tej samej rury, to dopóki długość wiadomości nie przekracza rozmiaru bufora wiadomości nie będą przeplatane.

Jeśli dowolny proces potoku będzie chciał pisać do rury, z której nikt nie czyta lub przeczytać z rury, do której nikt nie piszę wówczas zostanie do niego wysłany sygnał `SIGPIPE`.

Short count - Gdy read przeczyta mniej bajtów niż zamierzał.

Short count jest możliwy tylko przy `read`, kiedy zabraknie danych do przeczytania. Przy `write` nie może wystąpić short count bo zapisy są atomowe.

Jak połączyć rodzica i dziecko rurą, która została utworzona po uruchomieniu dziecka?

Można to zrobić za pomocą rury nazwanej.

`mkfifo rura`
`cat /dev/random > rura & cat < rura`
### Zadanie 2.
:::info
![](https://i.imgur.com/CpnZMth.png)
:::

### Zadanie 3.
:::info
![](https://i.imgur.com/apHnQR6.png)
:::

![](https://i.imgur.com/JnvJFFV.png)

**Nieużytek** to nieużywany fragment reprezentacji katalogu.

**Kompaktowanie** to operacja, która zmniejsza rozmiar katalogu - usuwane są nieużytki. Opłaca się ją robić, gdy wiadomo, że w danym katalogu jest dużo nieużytków, czyli zystamy na tej operacji dużo miejsca.

**Dodawanie pliku**: Trzeba przejrzeć cały katalog, żeby sprawdzić, czy jest dany plik w tym katalogu. Jeśli nie ma miejsca, wykonywane jest kompaktowanie.

**Usuwanie pliku**: Przegląda się cały katalog, żeby wiedzieć, czy jest plik. Po usunięciu pliku miejsce, gdzie był ten plik staje się nieużytkiem, pliki nie są od razu przesuwane, lecz przestawiany jest wskaźnik przy poprzednim pliku (entry size).

### Zadanie 4.
:::info
![](https://i.imgur.com/qYI22hQ.png)
:::

**Ścieżka bezwzględna** - ścieżka zaczynająca się od katalogu `/`.

**I-węzeł** - struktura przechowująca metadane pliku. Zawiera wskaźniki na bloki danych.

Algorytm trawersuje od i-węzła 2 -- czyli od katalogu `/`.

![](https://i.imgur.com/saM0N34.png)

![](https://i.imgur.com/W8uGIsX.png)

W i-węźle znajduje się struktura wskaźników (drzewiasta). Dzięki temu sterownik systemu pliku wie gdzie szukać i-tego bajtu pliku.

### Zadanie 5.
:::info
![](https://i.imgur.com/d97NZuw.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/YN0K9gg.png)
:::

```c=
#include "csapp.h"

typedef struct {
  int read;
  int write;
} pipe_t;

static inline pipe_t MakePipe(void) {
  int fds[2];
  Pipe(fds);
  return (pipe_t){.read = fds[0], .write = fds[1]};
}

static inline void CloseReadEnd(pipe_t p) {
  Close(p.read);
}

static inline void CloseWriteEnd(pipe_t p) {
  Close(p.write);
}

static bool ReadNum(pipe_t p, long *valp) {
  return Read(p.read, valp, sizeof(long)) == sizeof(long);
}

static bool WriteNum(pipe_t p, long val) {
  return Write(p.write, &val, sizeof(long)) == sizeof(long);
}

static noreturn void generator(pipe_t out, long maxprime) {
  for (long n = 2; n <= maxprime; n++)
    WriteNum(out, n);
  exit(EXIT_SUCCESS);
}

static void filter(pipe_t in, pipe_t out, long prime) {
  long num;
  while (ReadNum(in, &num)) {
    if (num % prime != 0)
      WriteNum(out, num);
  }
}

static noreturn void filter_chain(pipe_t in) {
  long prime;

  /* TODO: Something is missing here! */

  /* Read number from pipe */
  int left = ReadNum(in, &prime);

  /* If no more numbers in buffer */
  if (left == 0){
    exit(EXIT_SUCCESS);
  }

  printf("%ld\n", prime);
  fflush(stdout);
    
  pipe_t out = MakePipe();
  if (Fork()){
    /* Parent */
    CloseWriteEnd(out);
    CloseReadEnd(in);
    filter_chain(out);
    Wait(NULL);
  }
  else{
    /* Child */
    CloseReadEnd(out);
    filter(in, out, prime);
  }
  
  exit(EXIT_SUCCESS);
}

int main(int argc, char *argv[]) {
  if (argc != 2)
    app_error("Usage: %s [MAXPRIME]", argv[0]);

  long maxprime = atol(argv[1]);

  if (maxprime < 2 || maxprime > 10000)
    app_error("Give maximum prime number in range from 2 to 10000!");

  /* Spawn generator. */
  pipe_t gen_pipe = MakePipe();
  if (Fork()) { /* parent */
    CloseWriteEnd(gen_pipe);
  } else { /* child */
    CloseReadEnd(gen_pipe);
    generator(gen_pipe, maxprime);
  }

  /* Spawn filter chain. */
  if (Fork()) { /* parent */
    CloseReadEnd(gen_pipe);
  } else { /* child */
    filter_chain(gen_pipe);
  }

  /* Wait to reap children. */
  for (int i = 0; i < 2; i++)
    Wait(NULL);

  return 0;
}
```

![](https://i.imgur.com/gp34Lhv.png)

### Zadanie 7.
:::info
![](https://i.imgur.com/nwfIZQc.png)
:::

```c=
#include "csapp.h"

typedef struct {
  int child_fd;
  int parent_fd;
} sockpair_t;

static sockpair_t MakeSocketPair(void) {
  int sv[2];
  Socketpair(AF_UNIX, SOCK_STREAM, 0, sv);
  return (sockpair_t){.child_fd = sv[0], .parent_fd = sv[1]};
}

static bool MaybeReadNum(int fd, int *num_p) {
  return Read(fd, num_p, sizeof(int)) == sizeof(int);
}

static int ReadNum(int fd) {
  int num;
  if (Read(fd, &num, sizeof(int)) < sizeof(int))
    app_error("ReadNum error");
  return num;
}

static void WriteNum(int fd, int num) {
  if (Write(fd, &num, sizeof(int)) < sizeof(int))
    app_error("WriteNum error");
}

static void SendElem(int parent_fd, int child_fd, int nelem) {
  WriteNum(child_fd, nelem);
  for (int i = 0; i < nelem; i++)
    WriteNum(child_fd, ReadNum(parent_fd));
}

static void Merge(int left_fd, int right_fd, int parent_fd) {
  bool has_left = true;
  bool has_right = true;
  int left = ReadNum(left_fd);
  int right = ReadNum(right_fd);

  do {
    if ((has_left && has_right) ? left < right : has_left) {
      WriteNum(parent_fd, left);
      has_left = MaybeReadNum(left_fd, &left);
    } else {
      WriteNum(parent_fd, right);
      has_right = MaybeReadNum(right_fd, &right);
    }
  } while (has_left || has_right);
}

static void Sort(int parent_fd) {
  int nelem = ReadNum(parent_fd);

  if (nelem < 2) {
    WriteNum(parent_fd, ReadNum(parent_fd));
    Close(parent_fd);
    return;
  }

  sockpair_t left = MakeSocketPair();
  /* TODO: Spawn left child. */

  /* Child */
  if (Fork() == 0){

    Close(left.parent_fd);
    Close(parent_fd);

    Sort(left.child_fd);
    exit(0);
  }

  Close(left.child_fd);

  sockpair_t right = MakeSocketPair();
  /* TODO: Spawn right child. */

  if (Fork() == 0){
    Close(left.parent_fd);
    Close(right.parent_fd);
    Close(parent_fd);

    Sort(right.child_fd);
    exit(0);
  }

  Close(right.child_fd);

  /* TODO: Send elements to children and merge returned values afterwards. */

  const int32_t left_half = nelem / 2;
  const int32_t right_half = nelem - left_half;

  SendElem(parent_fd, left.parent_fd, left_half);
  SendElem(parent_fd, right.parent_fd, right_half);

  Merge(left.parent_fd, right.parent_fd, parent_fd);

  Close(parent_fd);
  Close(left.parent_fd);
  Close(right.parent_fd);
  
  /* Wait for both children. */
  Wait(NULL);
  Wait(NULL);
}

static int GetNumber(void) {
  char buf[20];
  if (fgets(buf, sizeof(buf), stdin) == NULL)
    app_error("GetNumber error");
  return strtol(buf, NULL, 10);
}

int main(void) {
  sockpair_t sort = MakeSocketPair();

  if (Fork()) {
    /* parent */
    int nelem = GetNumber();
    if (nelem < 2)
      app_error("Number of sorted elements must be at least 2!\n");
    Close(sort.child_fd);

    /* Write unsorted numbers to mergesort */
    WriteNum(sort.parent_fd, nelem);
    for (int i = 0; i < nelem; i++)
      WriteNum(sort.parent_fd, GetNumber());

    /* Read sorted numbers from mergesort */
    int prev = INT_MIN;
    for (int i = 0; i < nelem; i++) {
      int elem = ReadNum(sort.parent_fd);
      fprintf(stderr, "%d\n", elem);
      assert(prev <= elem);
      prev = elem;
    }
    Close(sort.parent_fd);

    Wait(NULL);
  } else {
    /* child */
    Close(sort.parent_fd);
    Sort(sort.child_fd);
  }

  return 0;
}
```
![](https://i.imgur.com/axIvDW3.png)
![](https://i.imgur.com/esRi6qi.png)
![](https://i.imgur.com/Q4iJFoR.png)
