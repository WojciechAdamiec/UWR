/*
* UWAGA! W poniższym kodzie należy zawrzeć krótki opis metody rozwiązania
*        zadania. Będzie on czytany przez sprawdzającego. Przed przystąpieniem
*        do rozwiązywania zapoznaj się dokładnie z jego treścią. Poniżej należy
*        wypełnić oświadczenie o samodzielnym wykonaniu zadania.
*
* Oświadczam, że zapoznałem(-am) się z regulaminem prowadzenia zajęć
* i jestem świadomy(-a) konsekwencji niestosowania się do podanych tam zasad.
*
* Imię i nazwisko, numer indeksu: Wojciech Adamiec, 310064
*/

        .text
        .globl  addsb
        .type   addsb, @function

/*
* W moim rozwiązaniu używam następującej techniki:
Na liście ćwiczeniowej nr 2 znajduje się sporo 'sztuczek', które można wykorzystać 
w naszym zadaniu. W uczcie programistów na odpowiednich stronach znajdują się pomysły
na to jak dodawać ze sobą równolegle liczby, tak aby nie wpływały one na siebie wzajemnie.
Następnie pozostaje nam już tylko obsłużyć najstarszy bit -- w przypadku overflowa lub
underflowa zastąpić dany bajt MAX lub MIN.
*/

addsb:                                  # Input: x: %rdi, y: %rsi

        /* Przygotowanie masek */
        movq $0x8080808080808080, %rcx  # rcx = m1 mask: first bit
        movq $0x7F7F7F7F7F7F7F7F, %rdx  # rdx = m2 mask: all bits except first
        
        /* Zapisanie x, y */
        movq %rdi, %r11                 # r11 = x
        movq %rsi, %r10                 # r10 = y

        /* Policzenie sum bez najstarszego bitu */
        andq %rdx, %rdi                 # rdi = x & m2
        andq %rdx, %rsi                 # rsi = y & m2
        addq %rsi, %rdi                 # rdi = (x & m2) + (y & m2)

        /* Zapisanie informacji o potencjalnym overflow/underflow */
        movq %rdi, %r9                  # r9  = (x & m2) + (y & m2)
        andq %rcx, %r9                  # r9  = ((x & m2) + (y & m2)) & m1)

        /* Dokończenie liczenia sum dla niepatologicznych przypadków */
        movq %r11, %rax                 # rax = x
        xorq %r10, %rax                 # rax = (x xor y)
        andq %rcx, %rax                 # rax = (x xor y) & m1
        xorq %rdi, %rax                 # rax = ((x xor y) & m1) xor ((x & m2) + (y & m2))

        /* Policzenie x, y zandowanego z m1 */
        andq %rcx, %r11                 # r11 = x & m1 w1
        andq %rcx, %r10                 # r10 = y & m1 w2

        /* Policzenie maski do overflow */
        movq %r9, %rcx                  # rcx = r9              s
        movq %r11, %rdx                 # rdx = x & m1          w1
        orq  %r10, %rdx                 # rdx = ~(x & m1)       ~w1
        notq %rdx                       # rdi = ~(y & m1)       ~w2
        andq %rdx, %rcx                 # rcx = r9 & ~(x & m1)  
        subq %rcx, %rax                 # Poprawiamy najstarsze bity
        movq %rcx, %rdi                 # rdi = r9 & ~(x & m1) & ~(y & m1)
        shrq $7, %rdi                   # rdi = r9 & ~(x & m1) & ~(y & m1) >> 7
        subq %rdi, %rcx                 # gotowa maska do overflow 01111111

        /* Policzenie maski do underflow */
        notq %r9                        # r9  = ~((x & m2) + (y & m2)) & m1)
        andq %r11, %r9                  # r9  = ~((x & m2) + (y & m2)) & m1) & (x & m1)
        andq %r10, %r9                  # r9  = ~((x & m2) + (y & m2)) & m1) & (x & m1) & (y & m1)
        movq %r9, %r10                  # r10 = ~((x & m2) + (y & m2)) & m1) & (x & m1) & (y & m1)
        orq %r9, %rax                   # Poprawiamy najstarsze bity
        shrq $7, %r10                   # r10 = ~((x & m2) + (y & m2)) & m1) & (x & m1) & (y & m1) >> 7
        subq %r10, %r9                  # gotowa maska do underflow
        notq %r9                        # odwrócona maska

        /* Nałożenie na wynik MAX i MIN w przypadku nasycenia */
        orq  %rcx, %rax
        
        andq %r9, %rax
        
        /* ret */
        ret

        .size   addsb, .-addsb
