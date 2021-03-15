# ASK Lista 1 - Wojciech Adamiec
## Zadania Deklarowane: 1, 2, 3, 5, 6, 7

### Zadanie 1.

:::info
Zmienne i, k spełniają warunek 0<i, k≤31. Napisz fragment kodu, który skopiuje i-ty bit zmiennej x na pozycję k-tą.
:::

```c=
int aux(uint32_t x, uint32_t i, uint32_t k){
    return ((x >> i) & 1) << k | x & ~(1 << k);
}
```

Wizualizacja dla:
```
x = 1011010
i = 1
k = 5
```
Zerujemy k-ty bity:
```c
x & ~(1 << k)
```
```
1: 0100000
2: 1011111
3: 
   1011010
   1011111
&  -------
   1011010
```
Kopiujemy i-ty bit i przechowujemy go z prawej:
```c
((x >> i) & 1)
```
```
1: 1011010
2: 0101101
3: 
   0101101
   0000001
&  -------
   0000001
```
Przesuwamy go na k-tą pozycję:
```c
((x >> i) & 1) << k
```
```
1: 0000001
2: 0100000
```
Robimy OR naszego bitu z resztą:
```c
((x >> i) & 1) << k | x & ~(1 << k)
```
```
1:
   1011010
   0100000
|  -------
   1111010
```

### Zadanie 2.

:::info
Napisz fragment kodu, który wyznaczy liczbę zapalonych bitów w zmiennej x.

UWAGA!Oczekiwana złożoność to O(logn), gdzie n to liczba bitów w słowie. Posłuż się strategią „dziel i zwyciężaj”.
:::

https://en.wikipedia.org/wiki/Hamming_weight

```c=
int aux(uint32_t x){
    uint32_t m1  = 0x55555555; // 01010101010101010101010101010101
    uint32_t m2  = 0x33333333; // 00110011001100110011001100110011
    uint32_t m4  = 0x0f0f0f0f; // 00001111000011110000111100001111
    uint32_t m8  = 0x00ff00ff; // 00000000111111110000000011111111
    uint32_t m16 = 0x0000ffff; // 00000000000000001111111111111111
    
    x = (x & m1 ) + ((x >>  1)  & m1 ); //put count of each 2 bits into those 2 bits  
    x = (x & m2 ) + ((x >>  2)  & m2 ); //put count of each 4 bits into those 4 bits 
    x = (x & m4 ) + ((x >>  4)  & m4 ); //put count of each 8 bits into those 8 bits 
    x = (x & m8 ) + ((x >>  8)  & m8 ); //put count of each 16 bits into those 16 bits 
    x = (x & m16) + ((x >> 16)  & m16); //put count of each 32 bits into those 32 bits
    return x;
}
```
Co się dzieje w pojedynczym kroku:

![alt text](https://i.imgur.com/7m8ViLH.png "")

Jak wygląda całość algorytmu:

![alt text](https://i.imgur.com/TvBsipy.png "")

### Zadanie 3.

:::info
Podaj rozmiar w bajtach poniższych struktur przyjmując, że wskaźnik jest 32-bitowy. Pod jakim przesunięciem,  względem  początku  struktury,  znajdują  się  poszczególne  pola?  Jak  zreorganizować  pola struktury, by zajmowała mniej miejsca? Z czego wynika takie zachowanie kompilatora?

```c=
struct A{        
    int8_t a;
    void *b;
    int8_t c;
    int16_t d;
};
    
struct B {
    uint16_t a;
    double b;
    void *c;
};
```
:::

Poszczególne typy zajmują różną ilość bajtów w pamięci. Jednocześnie w procesorze słowo maszynowe ma długość 32/64 bity. Żeby móc operować optymalnie na danych, procesor chce mieć je zapisane na jak najmniejszej ilości słów maszynowych. (np. Dla 32 bitowego słowa maszynowego: 1 słowo maszynowe - 1 int32; 1 słowo maszynowe - 2 int16).

W języku C jest tzw. Padding, który zapewnia *poprawne* ułożenie danych w pamięci. Chcemy, aby dane długości $k$ bajtów miały adres, który jest wielokrotnością $k$. Podobnie dla struktur chcemy, aby miały one adres, który jest wielokrotnością rozmiaru największej składowej.

```c=
struct A{        
    int8_t a;    1 bajt
    ...          3 bajty wyrównania
    void *b;     4 bajty
    int8_t c;    1 bajt
    ...          1 bajt wyrównania
    int16_t d;   2 bajty
}

rozmiar A: 12 bajtów
    
struct B {
    uint16_t a;    2 bajty
    ...            6 bajtów wyrównania
    double b;      8 bajtów
    void *c;       4 bajty
    ...            4 bajty wyrównania
};

rozmiar B: 24 bajtów
```
Wersja zoptymalizowana:

```c=
struct A{
    void *b;     4bajty
    int16_t d;   2bajty
    int8_t a;    1bajt
    int8_t c;    1bajt
}
rozmiar A: 8 bajtów
    
struct B {
    double b;      8bajtów
    void *c;       4bajty
    uint16_t a;    2bajty
    ...            2bajty wyrównania
};
rozmiar B: 16 bajtów
```

### Zadanie 4.

### Zadanie 5.

:::info
Zmienne  «a»,  «b»  i  «c»  to  wskaźniki na  tablice  elementów  typu «uint32_t».  Przetłumacz, krok po kroku, poniższe dwie instrukcje złożone zapisane w języku C na kod trójkowy:
s += b[j+1] + b[\-\-j];
a[i++] -= * b * (c[j*2] + 1);
:::

```=c
s += b[j+1] + b[--j];

t1 := j + 1;   // j+1
t1 := t1 * 4;  // liczymy adres w bajtach
t1 := b + t1;
add1 := *t1;   // add1 = b[j+1]

 j := j - 1;   // --j
t2 := j * 4;   // liczymy adres w bajtach
t2 := b + t2;
add2 := *t2;   // add2 = b[--j]
 
s := s + add1;
s := s + add2;
```

```=c
a[i++] -= *b * (c[j*2] + 1);

t1 := i * 4;
 i := i + 1;  // i++
t1 := t1 + a  // liczymy adres w bajtach
 l := *t1

p1 := *b;     // p1=*b

t2 := j * 2;  // j*2
t2 := t2 * 4; 
t2 := c + t2; // liczymy adres w bajtach
p2 := *t2;    // p2 = c[j*2]
p2 := p2 + 1; // p2 = c[j*2] + 1
 p := p1 * p2;// p = *b * (c[j*2] + 1)
*t1 := l - p; // a[i++] -= *b * (c[j*2] + 1);
```

### Zadanie 6.

:::info
Z punktu widzenia procesora wszystkie wskaźniki są tożsame z liczbami całkowitymi. W trakcie generowania kodu wynikowego kompilator musi przetłumaczyć instrukcje wyboru pola struktury lub wariantu unii «x->k» i «x.k» oraz indeksowania tablic «a[i]» na prostsze instrukcje.

Przetłumacz, krok po kroku, poniższą instrukcję zapisaną w języku C na kod trójkowy. Trzeba pozbyć się typów złożonych, wykonać odpowiednie obliczenia na wskaźnikach, a wszystkie dostępy do pamięci realizować wyłącznie instrukcjami «x:=*y» lub «*x:=y». Zmienne «us» i «vs» są typu «struct A *» (patrz zad. 3).

vs->d = us[1].a + us[j].c;
:::
vs->d = us[1].a + us[j].c

```c=
struct A{        
    int8_t a;    1 bajt
    ...          3 bajty wyrównania
    void *b;     4 bajty
    int8_t c;    1 bajt
    ...          1 bajt wyrównania
    int16_t d;   2 bajty
}
```
rozmiar A: 12 bajtów
```=c
i := 1
t1 := i * 12
t1 := us + t1
t1 := *t1   // us[1].a

t2 := j * 12
t2 := us + t2
t2 := t2 + 8
t2 := *t2   // us[j].c

t3 := vs + 10 // vs->d

*t3 := t1 + t2  // vs->d = us[1].a + us[j].c
```

### Zadanie 7.

:::info
Przetłumacz, krok po kroku, poniższą procedurę napisaną w języku C na kod trójkowy. Oznacz **bloki podstawowe** i narysuj **graf przepływu** sterowania.

```c=
void insertion_sort(int arr[], int length){
    int j, temp;
    for (int i = 0; i < length; i++){
        j = i;
        while (j > 0 && arr[j] < arr[j - 1]){
            temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j-1] = temp;
            j--;
        }
    }
}
```
:::
Legenda:
```
x = a[i] to t = a + i; x = *t
a[i] = x to t = a + i; *t = x
```
```=
            i = 0                                  # B1
FOR:        if i == length goto END                # B2
            j = i                                  # B3
WHILE:      if j <= 0 goto WHILE END               # B4
            j1 = j * 4                             # B5
            con1 = arr[j1]
            j2 = j1 - 4
            con2 = arr[j2]
            if con1 >= con2 goto WHILE END
            temp1 = arr[j1]                        # B6
            temp2 = arr[j2]
            arr[j1] = temp2
            arr[j2] = temp1
            j = j - 1
            goto WHILE
WHILE END:  i = i + 1                              # B7
            goto FOR
END:                                               # B8
```

**Blok podstawowy** to taki ciąg instrukcji, który ma tylko jedno wejście i tylko jedno wyjście, przy czym wejście do bloku znajduje się na jego początku, a wyjście na końcu.

**Graf przepływu sterowania** -- Graf, gdzie wierzchołkami są bloki podstawowe, a skierowane krawędzie wskazują powiązania między blokami.

![alt text](https://i.imgur.com/1T37fDN.png "Graf")



### Zadanie 8.