#include <stdint.h>
#include <stdio.h>

void zeruj(uint32_t &x, uint8_t k){
    x &= ~(1 << k);
}

void ustaw(uint32_t &x, uint8_t k){
    x |= (1 << k);
}

void neguj(uint32_t &x, uint8_t k){
    x ^= (1 << k);
}

int main(){

    uint32_t a = 7;
    uint32_t b = 2;
    uint32_t c = 2;

    printf("Dla %d (111): \n", a);
    zeruj(a, 2);
    printf("Zeruj 2: %d\n", a);

    printf("Dla 2 (010): \n");
    ustaw(b, 0);
    printf("Ustaw 0: %d\n", b);
    
    printf("Dla 2 (010): \n");
    neguj(c, 2);
    neguj(c, 1);
    printf("Neguj 2, Neguj 1: %d\n", c);

    return 0;
}