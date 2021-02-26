#include <stdint.h>
#include <stdio.h>

bool is_power(uint32_t x){
    return !(x & (x - 1));
}

int main(){

    printf("27  : %d\n", is_power(27));
    printf("32  : %d\n", is_power(32));
    printf("15  : %d\n", is_power(15));
    printf("1024: %d\n", is_power(1024));
    printf("7   : %d\n", is_power(7));
    return 0;
}