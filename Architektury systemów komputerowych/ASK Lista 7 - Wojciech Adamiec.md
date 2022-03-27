# ASK Lista 7 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 3, 4, 6

### Zadanie 1.
:::info
![](https://i.imgur.com/AkRiNEA.png)
:::

Zauważmy, że chcąc dostać się do $t$ w strukturze $str2$ wykonujemy `move` na adresie `(%rsi + 8)`. Oznacza to, że `char array[B]` ma co najwyżej 8 bajtów. Jednocześnie wiemy, że gdyby ten array miał 4 lub mniej bajtów to $t$ nie musiałoby znajdować się na 8 bajcie, tylko na 4 (wyrównanie dla inta to 4 bajty).

Z tego wnioskujemy, że $B \in \{5, 6, 7, 8\}$.

Teraz zobaczmy na `movq %rax, 184(%rdi)`, który odpowiada dostaniu się do `long y` w strukturze $str1$. Wiemy, że wyrównanie jest mniejsze od 8 bajtów (long) i jednocześnie wiemy, że rozmiar `int x[A][B]` jest równy $4\cdot A \cdot B$.

Oznacza to, że rozmiar tej tablicy jest z przedziału $178 \leq 4 \cdot A \cdot B \leq 184$. Co po przekształceniu daje $45 \leq A \cdot B \leq 46$. Wiedząc, że $A, B$ są naturalne wnioskujemy, że $AB \in \{45, 46\}$.

Mamy teraz dwa więzy:

1. $B \in \{5, 6, 7, 8\}$
2. $AB \in \{45, 46\}$

Zachłannie szukamy rozwiązania i okazuje się, że jedyne rozwiązanie mamy dla:

1. $A = 9$
2. $B = 5$

Co rozwiązuje nasze zadanie.

### Zadanie 2.
:::info
![](https://i.imgur.com/KbR7QiR.png)
:::

Zauważmy na początu, że funkcja `store_elem` zwraca nam rozmiar tablicy $A$. Ten rozmiar jest stałą równą $3640$. Jednocześnie wiemy, że rozmiar typu `long` to $8$. Z tego wnioskujemy, że: $R \cdot S \cdot T = 3640 / 8 = 455$.

Teraz analizujemy kod assembly. Wiemy, że funkcja chce się dostać do elementu tablicy $A$ o indeksie `[i][j][k]`.

```
store_elem:
    leaq (%rsi,%rsi,2),%rax   // rax = 3*j
    leaq (%rsi,%rax,4),%rax   // rax = (4*3+1)*j = 13j
    movq %rdi,%rsi            // rsi = i
    salq $6,%rsi              // rsi = 64*i
    addq %rsi,%rdi            // rdi = 65*i
    addq %rax,%rdi            // rdi = 65i + 13j
    addq %rdi,%rdx            // rdx = 65i + 13j + k
    movq A(,%rdx,8),%rax      // rax = A + 8(65i + 13j + k)
    movq %rax,(%rcx)
    movq $3640,%rax
    ret
```

Widzimy, że dostanie się do tego elementu dzieje się za pomocą równania $A + 8(65i + 13j + k)$.

Z tego wnioskujemy, że rozmiar jednego elementu zewnętrznej tablicy (i jednocześnie rozmiar środkowej tablicy) wynosi $65 \cdot 8$ bajtów. Znając rozmiar całej tablicy $A$ wnioskujemy z tego:

$R = 455 / 65 = 7$

Wiemy, że rozmiar środkowej tablicy to $65 \cdot 8$. Jednocześnie rozmiar wewnętrznej tablicy to $13 \cdot 8$ Z tego wiemy, że wewnętrznych tablic jest:

$S = 65 / 13 = 5$

Wystarczy teraz znaleźć brakujący element:

$T = 455 / (5 \cdot 7) = 13$

Czyli rozwiązanie to:

$R = 7$
$S = 5$
$T = 13$

### Zadanie 3.
:::info
![](https://i.imgur.com/cwi41af.png)
:::

```=
test:
    movl   0x120(%rsi),   %ecx              # %ecx = *(%rsi+0x120) // n = bp->last
    addl   (%rsi),        %ecx              # %ecx = %ecx + *%rsi  // n += bp->first
                                            # %ecx = n
    leaq   (%rdi,%rdi,4), %rax              # %rax = 5 * i
    leaq   (%rsi,%rax,8), %rax              # %rax = %rsi + 8*5*i = %rsi + 40i
    
    movq   0x8(%rax),     %rdx              # %rdx = *(%rsi + 40i + 8)
                                            # %rdx = idx i-tej struktury a_struct w tablicy a
    movslq %ecx,          %rcx              # (long)(%rcx) czyli (long)n
                                            # rcx = n
    movq   %rcx,          0x10(%rax,%rdx,8) # *(%rax + 8 + 8 + 8 * %rdx) = n 
                                            # czyli x[idx] = n
    retq
```

Na początku zauważamy, że aby dostać się do `last` musimy przejść do $288$ bajtu.

Teraz zauważamy, że chcąc dostać się do i-tego a_struct'a w tablicy $a$ wykonujemy operację $40 \cdot i$, to znaczy, że rozmiar pojednczej a-struktury w tablicy $a$ jest równy $40$ (być może w tych bajtach jest jakiś padding).

Następnie zauważamy, że chcąc dostać się do pola `idx` i-tej a-struktury robimy dereferencję na adresie $rsi + 40\cdot i + 8$ : to jest początek b-struktury + $8$ bajtów (first $4$ bajtowy + $4$ bajty paddingu) + $40\cdot i$, żeby dostać się do i-tej a-struktury.

Z tego wnioskujemy, że:

$288 - 4 - 4 = 280$ to jest rozmiar całej tablicy $a$. Jednocześnie wiemy, że rozmiar pojedycznej a-struktury jest równy $40$.

$280/40 = 7$ i jest to dla nas bardzo wygodne, bo skoro dostajemy dzielenie bez reszty to wiemy, że nie ma po tablicy żadnego paddingu. Jednocześnie wiemy, że szukana wartość $CNT = 7$.

Teraz skupmy się na architekturze a-struktury. Domyślamy się, że ma ona postać:

```c=
typedef struct{
    type idx;
    type x[size];
}a_struct;
```

Zauważmy, że chcą zrobić przypisanie do idx-sowego indeksu tablicy $x$ wartości $n$ my robimy dereferencje na: $rax + 8 + 8 + 8 \cdot rdx$.

Z tego $rax + 8$ wskazuje na początek i-tej a-struktury.
Kolejne $+8$ przesuwa nas do tablicy $x$.
Następnie chcąc dostać się idx-owego indeksu tej tablicy robimy $8 \cdot rdx$.

Wnioskujemy z tego, że tablica $x$ jest typu `long`. Jednocześnie wiemy, że zaczyna się ona po 8 bajtach, co sugeruje nam, że pole `idx` również jest typu `long`.

Rozmiar a-struktury to $40$. Wiemy, że $8$ bajtów idzie na `idx`, więc zostaje $32$ bajty na tablice $x$. Stąd wnioskujemy, że rozmiar tej tablicy to $4$.

Podsumowując dostajemy:

$CNT = 7$
```c=
typedef struct{
    long idx;
    long x[4];
}a_struct;
```

### Zadanie 4.
:::info
![](https://i.imgur.com/ZLHvffi.png)
:::

Unia to taki typ danych co przechowuje na raz jedną ze struktur. Rozmiar uni to rozmiar największej struktury, którą może przechowywać - w naszym przypadku to jest tak czy siak $16$ bajtów.

```c=
union elem * proc(union elem * parent){
    union elem child = *parent->e2.next;  // 12, 13
    long p = *child.e1.p;                 // 14
    p -= parent->e1.y;                    // 15
    child.e2.x = p;                       // 16
    return parent->e2.next;               // 12, 17
}
```

### Zadanie 5.
:::info
![](https://i.imgur.com/f9ppLd2.png)
:::

### Zadanie 6.
:::info
![](https://i.imgur.com/9wcukMr.png)
:::

```=
puzzle6:                       // Input: %rdi : P* s, %xmm0 : float x
    movq    (%rdi), %rdx                    // rdx : s->n
    leaq    8(%rdi), %rcx                   // rcx : s->tab
    xorl    %eax, %eax                      // rax : i = 0
    vxorps  %xmm1, %xmm1, %xmm1             // xmm1: acc = 0
    vmovss  .LC1(%rip), %xmm2               // xmm2: power = 1
.L2: 
    cmpq    %rdx, %rax                      // If (i > s->n)  
    jge    .L5                              // goto .L5
    
    vfmadd231ss (%rcx,%rax,4), %xmm2, %xmm1 // acc += power * s->tab[i]
    incq    %rax                            // i++
    vmulss  %xmm0, %xmm2, %xmm2             // power *= x
    jmp     .L2
.L5:  
    vmovaps %xmm1, %xmm0                    // Return acc
    ret
.LC1: 
    .long   0x3f800000                      // 1 (stała, float)
```

```c=
float puzzle6(struct P * s, float x){
    float acc   = 0;
    float power = 1;
    
    for(int i = 0; i < s->n; i++){
        acc += power * s->tab[i];
        power *= x;
    }
    
    return acc; 
}
```

Wiemy, że szukana struktura ma postać:

```c=
typedef struct P{
    type1 n;
    type2 p[N];
}s;
```

Wiemy, że `type1` ma 8 bajtów. Stąd domyślamy się, że chodzi o `long`. Operacje na elementach tablicy $p$ wymagają od zmiennych bycia typem `float`. Stąd dostajemy:

```c=
typedef struct P{
    long n;
    float p[N];
}s;
```

### Zadanie 7.
:::info
![](https://i.imgur.com/iFzQIg3.png)
:::

### Zadanie 8.
:::info
![](https://i.imgur.com/9mJ73pa.png)
:::