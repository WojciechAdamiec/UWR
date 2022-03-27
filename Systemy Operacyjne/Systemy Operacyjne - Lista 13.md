# Systemy Operacyjne - Lista 13

## Wojciech Adamiec, 310064

### Deklarowane zadania: 3, 4, 5, 7

### Zadanie 1.
:::info
![](https://i.imgur.com/EJkH3KH.pngg)
:::

### Zadanie 2.
:::info
![](https://i.imgur.com/4goQ9hb.png)
:::

### Zadanie 3.
:::info
![](https://i.imgur.com/puvAiIy.png)
:::

---

| P. Num | Event                      | active | waiting | must_wait | block |
| ------ | -------------------------- | ------ | ------- | --------- | ----- |
|        |                            | 0      | 0       | false     | 0     |
| 1      | acquire                    | 1      | 0       | false     | 0     |
| 2      | acquire                    | 2      | 0       | false     | 0     |
| 3      | acquire                    | 3      | 0       | true      | 0     |
| 4      | acquire -> blok. na 6th l. | 3      | 1       | true      | 0     |
| 1      | release                    | 2      | 1       | true      | 0     |
| 2      | release                    | 1      | 1       | true      | 0     |
| 3      | release                    | 0      | 1       | false     | 1     |
| 5      | acquire                    | 1      | 1       | false     | 1     |

5th aquire może teraz wejść przed 4th (zaburzenie FIFO)

---


| P. Num | Event                      | active | waiting | must_wait | block |
| ------ | -------------------------- | ------ | ------- | --------- | ----- |
|        |                            | 0      | 0       | false     | 0     |
| 1      | acquire                    | 1      | 0       | false     | 0     |
| 2      | acquire                    | 2      | 0       | false     | 0     |
| 3      | acquire                    | 3      | 0       | true      | 0     |
| 4      | acquire -> blok. na 6th l. | 3      | 1       | true      | 0     |
| 5      | acquire -> blok. na 6th l. | 3      | 2       | true      | 0     |
| 6      | acquire -> blok. na 6th l. | 3      | 3       | true      | 0     |
| 1      | release                    | 2      | 3       | true      | 0     |
| 2      | release                    | 1      | 3       | true      | 0     |
| 3      | release                    | 0      | 3       | false     | 3     |
| 7      | acquire                    | 1      | 3       | false     | 3     |
| 8      | acquire                    | 2      | 3       | false     | 3     |
| 9      | acquire                    | 3      | 3       | true      | 3     |
| 4      | cont. from blok. na 6th l. | 4      | 2       | false     | 2     |
| 5      | cont. from blok. na 6th l. | 5      | 1       | false     | 1     |
| 6      | cont. from blok. na 6th l. | 6      | 0       | false     | 0     |

Mamy teraz nie tylko zaburzone FIFO, ale jeszcze ilość aktywnych zasobów większą niż dopuszczalna. W dodatku `must_wait` jest źle ustawione.


### Zadanie 4.
:::info
![](https://i.imgur.com/zbqjATI.png)
:::

```c=
#include "csapp.h"

static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

static void randsleep(void) {
  usleep(rand() % 5000 + 5000);
}

#define N 24

static pthread_t td[N];
static sem_t forks[N];
/* TODO: If you need extra shared state, define it here. */
static sem_t eating_philosophers;

void *philosopher(void *id) {
  int right = (intptr_t)id;
  int left = right == 0 ? N - 1 : right - 1;

  for (;;) {
    /* Think */
    randsleep();

    /* TODO: Take forks (without deadlock & starvation) */
    Sem_wait(&eating_philosophers);
    Sem_wait(&forks[right]);
    Sem_wait(&forks[left]);

    /* Eat */
    outc("a" + right);
    randsleep();

    /* TODO: Put forks (without deadlock & starvation) */
    Sem_post(&forks[left]);
    Sem_post(&forks[right]);
    Sem_post(&eating_philosophers);
  }

  return NULL;
}

int main(void) {
  /* TODO: If you need extra shared state, initialize it here. */
  Sem_init(&eating_philosophers, 0, N - 1);

  for (int i = 0; i < N; i++)
    Sem_init(&forks[i], 0, 1);

  for (int i = 0; i < N; i++)
    Pthread_create(&td[i], NULL, philosopher, (void *)(intptr_t)i);

  for (int i = 0; i < N; i++)
    Pthread_join(td[i], NULL);
  
  return EXIT_SUCCESS;
}
```

### Zadanie 5.
:::info
![](https://i.imgur.com/iSxSn3N.png)
:::

```c=
#include "csapp.h"

static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

#define N 12
#define M 6

static struct {
  /* TODO: Put semaphores and shared variables here. */
  int meals_count;
  sem_t mutex;
  sem_t empty;
  sem_t full;
} *shared = NULL;


static void savage(void) {
  for (;;) {
    /* TODO Take a meal or wait for it to be prepared. */

    Sem_wait(&shared->mutex);
    if(shared->meals_count == 0)
    {
      Sem_post(&shared->empty);
      Sem_wait(&shared->full);
    }
    printf("[%d]: eating\n", getpid());
    shared->meals_count--;
    Sem_post(&shared->mutex);

    /* Sleep and digest. */
    usleep(rand() % 1000 + 1000);
  }

  exit(EXIT_SUCCESS);
}

static void cook(void) {
  for (;;) {
    /* TODO Cook is asleep as long as there are meals.
     * If woken up they cook exactly M meals. */

    Sem_wait(&shared->empty);
    printf("[%d]: cooking\n", getpid());
    shared->meals_count = M;
    Sem_post(&shared->full);
  }
}

/* Do not bother cleaning up after this process. Let's assume that controlling
 * terminal sends SIGINT to the process group on CTRL+C. */
int main(void) {
  shared = Mmap(NULL, getpagesize(), PROT_READ|PROT_WRITE, MAP_ANON|MAP_SHARED,
                -1, 0);

  /* TODO: Initialize semaphores and other shared state. */

  Sem_init(&shared->mutex, 1, 1);
  Sem_init(&shared->empty, 1, 0);
  Sem_init(&shared->full, 1, 0);
  shared->meals_count = M;

  for (int i = 0; i < N; i++)
    if (Fork() == 0)
      savage();

  cook();

  return EXIT_SUCCESS;
}
```

### Zadanie 6.
:::info
![](https://i.imgur.com/yjfEQV4.png)
:::

### Zadanie 7.
:::info
![](https://i.imgur.com/jNgLYxt.png)
:::

![](https://i.imgur.com/LIsyTIN.png)

Błędna intuicja:

```python=
def tobacco_smoker():
    repeat:
        paper.wait()
        matches.wait()
        smoke()
        tobacco_smoker_done.signal()
```

Pojawia się tutaj problem: dwóch palaczy bierze po jednym składniku i mamy zakleszczenie.

Rozwiązanie będzie polegało na wprowadzenie 3 wątków popychaczy, którzy będą patrzeć odpowiednio na papier, tabakę lub zapałki, komunikować się ze sobą współdzielonymi zmiennymi i ostatecznie wybudzać odpowiedniego palacza.

```c=
#include "csapp.h"

static __unused void outc(char c) {
  Write(STDOUT_FILENO, &c, 1);
}

static __thread unsigned seed;

// Ingredients semaphores
static sem_t tobacco;
static sem_t matches;
static sem_t paper;

// Smoking proccess semaphore
static sem_t doneSmoking;

// Global variables to hold info about ingredients on table
static bool is_tobacco;
static bool is_matches;
static bool is_paper;

// Smokers semaphores
static sem_t tobacco_smoker;
static sem_t matches_smoker;
static sem_t paper_smoker;

// Lock for pushers
static sem_t pusher;


static void *agent(void *arg) {
  seed = pthread_self();

  while (true) {
    Sem_wait(&doneSmoking);

    int choice = rand_r(&seed) % 3;
    if (choice == 0) {
      Sem_post(&tobacco);
      Sem_post(&paper);
    } else if (choice == 1) {
      Sem_post(&tobacco);
      Sem_post(&matches);
    } else {
      Sem_post(&paper);
      Sem_post(&matches);
    }
  }

  return NULL;
}

/* Tobacco pusher wakes then tobacco is on table */
static void *tobacco_push(void *arg)
{
  while(true)
  {
    Sem_wait(&tobacco);
    Sem_wait(&pusher);

    if (is_paper)
    {
      is_paper = false;
      Sem_post(&matches_smoker);
    }
    else if (is_matches)
    {
      is_matches = false;
      Sem_post(&paper_smoker);
    }
    else
      is_tobacco = true;

    Sem_post(&pusher);
  }

  return NULL;
}

/* Tobacco pusher wakes then paper is on table */
static void *paper_push(void *arg)
{
  while(true)
  {
    Sem_wait(&paper);
    Sem_wait(&pusher);

    if (is_tobacco)
    {
      is_tobacco = false;
      Sem_post(&matches_smoker);
    }
    else if (is_matches)
    {
      is_matches = false;
      Sem_post(&tobacco_smoker);
    }
    else
      is_paper = true;

    Sem_post(&pusher);
  }

  return NULL;
}

/* Tobacco pusher wakes then matches are on table */
static void *matches_push(void *arg)
{
  while(true)
  {
    Sem_wait(&matches);
    Sem_wait(&pusher);

    if (is_paper)
    {
      is_paper = false;
      Sem_post(&tobacco_smoker);
    }
    else if (is_tobacco)
    {
      is_tobacco = false;
      Sem_post(&paper_smoker);
    }
    else
      is_matches = true;

    Sem_post(&pusher);
  }

  return NULL;
}

static void randsleep(void) {
  usleep(rand_r(&seed) % 1000 + 1000);
}

static void make_and_smoke(char smoker) {
  randsleep();
  Sem_post(&doneSmoking);
  outc(smoker);
  randsleep();
}

static void *smokerWithMatches(void *arg) {
  seed = pthread_self();

  while (true) {

    Sem_wait(&matches_smoker);
    make_and_smoke('M');
  }

  return NULL;
}

static void *smokerWithTobacco(void *arg) {
  seed = pthread_self();

  while (true) {

    Sem_wait(&tobacco_smoker);
    make_and_smoke('T');
  }

  return NULL;
}

static void *smokerWithPaper(void *arg) {
  seed = pthread_self();
 
  while (true) {

    Sem_wait(&paper_smoker);
    make_and_smoke('P');
  }

  return NULL;
}

int main(void) {
  Sem_init(&tobacco, 0, 0);
  Sem_init(&matches, 0, 0);
  Sem_init(&paper, 0, 0);

  Sem_init(&doneSmoking, 0, 1);

  // Smokers are locked at the start
  Sem_init(&tobacco_smoker, 0, 0);
  Sem_init(&matches_smoker, 0, 0);
  Sem_init(&paper_smoker, 0, 0);
  
  // No pusher is pushing at the start
  Sem_init(&pusher, 0, 1);

  // There are no ingredients on the table at the start
  is_tobacco = false;
  is_matches = false;
  is_paper = false;

  pthread_t tobacco_pusher, paper_pusher, matches_pusher;
  Pthread_create(&tobacco_pusher, NULL, tobacco_push, NULL);
  Pthread_create(&paper_pusher, NULL, paper_push, NULL);
  Pthread_create(&matches_pusher, NULL, matches_push, NULL);

  pthread_t agentThread;
  Pthread_create(&agentThread, NULL, agent, NULL);

  pthread_t smokerPaperThread, smokerMatchesThread, smokerTobaccoThread;
  Pthread_create(&smokerPaperThread, NULL, smokerWithPaper, NULL);
  Pthread_create(&smokerMatchesThread, NULL, smokerWithMatches, NULL);
  Pthread_create(&smokerTobaccoThread, NULL, smokerWithTobacco, NULL);

  Pthread_join(agentThread, NULL);
  Pthread_join(smokerPaperThread, NULL);
  Pthread_join(smokerMatchesThread, NULL);
  Pthread_join(smokerTobaccoThread, NULL);

  Pthread_join(tobacco_pusher, NULL);
  Pthread_join(paper_pusher, NULL);
  Pthread_join(matches_pusher, NULL);

  return 0;
}
```