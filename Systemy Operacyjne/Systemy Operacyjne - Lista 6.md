# Systemy Operacyjne - Lista 6

## Wojciech Adamiec, 310064

### Deklarowane zadania: 1, 5, 7

### Zadanie 1.
:::info
![](https://i.imgur.com/kcmQ8YA.png)
:::

**Tożsamość procesu** to zbiór identyfikatorów użytkowników i grup powiązanych z danym procesem.

`ruid` - real user id - właściciel procesu.

`euid` - effective user id - system operacyjny patrzy na to id w procesie podejmowania decyzji o pozwoleniu na wykonanie rzeczy. (możemy chcieć tymczasowo przyjąć tożsamość innego usera, np. roota)

`suid` - saved user id - kiedy uprzywilejowany proces wykonuje jakieś nieuprzywilejowane zadania musimy zmienić efektywne id (jednocześnie zapisując poprzednie w saved user id). Po zakończeniu działań efektywne id zostanie przywrócone do stanu zapisanego w saved user id.

Stan początkowy:

`ruid` = 1000, `euid` = 0, `suid` = 0

1. setuid(2000) -> `ruid` = 2000, `euid` = 2000, `suid` = 2000

:::success
The setuid() system call sets the real and	effective user IDs and the saved set-user-ID of the current process to the specified value.

The setuid() system call is permitted if the specified	ID is equal to the real user ID or the effective user	ID of the process, or if the effective user ID is that of the super user.
:::

2. setreuid(-1, 2000) -> `ruid` = 1000, `euid` = 2000, `suid` = 2000

:::success

The real and effective user IDs of	the current process are	set according to the arguments.	If ruid	or euid	is -1, the current uid is filled in by the system.

Unprivileged users may change the real user ID to the	effec-tive user ID and vice-versa; only the super-user may make other changes.

If the real user ID is changed (i.e. ruid is not -1) or the effective user ID is changed to something other than the real user ID, then the saved user ID will be set to the effective user ID.
:::

3. seteuid(2000) -> `ruid` = 1000, `euid` = 2000, `suid` = 0

:::success
The seteuid() system call (setegid()) sets	the effective user ID (group ID) of the	current	process.
:::

4. setresuid(-1, 2000, 3000) -> `ruid` = 1000, `euid` = 2000, `suid` = 3000

:::success
The setresuid() system call sets the real,	effective and saved user IDs of	the current process. The analogous setresgid() sets the real, effective and saved group IDs.

Privileged processes may set these IDs to arbitrary values.

Passing -1 as an argument causes the corresponding value to remain unchanged.
:::


Proces z tożsamością `ruid=0`, `euid=1000`, `suid=1000` nie jest uprzywilejowany, bo effective user ID wynosi 1000.

### Zadanie 2.
:::info
![](https://i.imgur.com/6U12A53.png)
:::

### Zadanie 3.
:::info
![](https://i.imgur.com/crIICCi.png)
:::

### Zadanie 4.
:::info
![](https://i.imgur.com/D3RjdjL.png)
:::

### Zadanie 5.
:::info
![](https://i.imgur.com/1FheoYo.png)
:::

    All  functions  registered with atexit(3) and on_exit(3) are called, in
       the reverse order of their registration.  (It is possible  for  one  of
       these  functions  to  use  atexit(3) or on_exit(3) to register an addi‐
       tional function to be executed during exit processing; the  new  regis‐
       tration  is  added to the front of the list of functions that remain to
       be called.)  If one of these functions does not return (e.g., it  calls
       _exit(2),  or  kills  itself with a signal), then none of the remaining
       functions is called, and further exit processing (in particular, flush‐
       ing  of  stdio(3) streams) is abandoned.  If a function has been regis‐
       tered multiple times using atexit(3) or on_exit(3), then it  is  called
       as many times as it was registered.

       All  open  stdio(3)  streams  are flushed and closed.  Files created by
       tmpfile(3) are removed.

Problemy z buforami

* _exit(2) - Właściciel buforów znika, więc to co jest w buforze może się nie wypisać
* fork(2) - proces dziecko używa tego samego bufora co rodzic, więc zawartość zawartośc bufora może zostać wypisana ponownie.
* execve(2) - program otrzymuje nowe bufory, więc tak samo jak przy _exit(2), może sie nie wypisać to co chcieliśmy wypisać przed execve(2)

Jak zapobiegać tym problemom:

-> Za pomocą `fflush`.

Strategie buforowania:

* pliki terminala - buforowanie liniami (dopóki nie napotkamy ‘\n’, albo końca bufora)
* pliki dyskowe - buforowanie pełne (dopóki bufor nie jest zapełniony)
* stderr - niebuforowane; w przypadku obsługi błędów, chcemy je widzieć od razu

Aby poprawnie opróżnić wszystkie bufory przed zamknięciem programu, powinniśmy w procedurze obsługi sygnału SIGINT użyć `tcflush()`

### Zadanie 6.
:::info
![](https://i.imgur.com/GH1xdNu.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/L9vXFPR.png)
:::

```c=
#include "csapp.h"

static const char *uidname(uid_t uid) {
  /* TODO: Something is missing here! */

  struct passwd *pw = getpwuid(uid);
  return pw->pw_name;

}

static const char *gidname(gid_t gid) {
  /* TODO: Something is missing here! */

  struct group *gr = getgrgid(gid);
  return gr->gr_name;
}

static int getid(uid_t *uid_p, gid_t *gid_p, gid_t **gids_p) {
  gid_t *gids = NULL;
  int group_number;

  /* TODO: Something is missing here! */

  *uid_p = getuid();
  *gid_p = getgid();
  group_number = getgroups(0, NULL);
  gids = malloc(group_number * sizeof(gid_t));
  getgroups(group_number, gids);


  *gids_p = gids;
  return group_number;
}

int main(void) {
  uid_t uid;
  gid_t *gids, gid;
  int groups = getid(&uid, &gid, &gids);

  printf("uid=%d(%s) gid=%d(%s) ", uid, uidname(uid), gid, gidname(gid));
  printf("groups=%d(%s)", gids[0], gidname(gids[0]));
  for (int i = 1; i < groups; i++)
    printf(",%d(%s)", gids[i], gidname(gids[i]));
  putchar('\n');

  free(gids);

  return 0;
}
```