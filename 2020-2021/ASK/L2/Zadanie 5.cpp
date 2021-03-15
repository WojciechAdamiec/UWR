#include <stdio.h>
#include <inttypes.h>
#include <iostream>

long long f3(int x){
    return ((long long)x*3)>>2;
}

int32_t threefourths(int32_t x)
{
    int32_t result = (x >> 1) + (x >> 2);
    int z = (x & 2) >> 1 & (x & 1);
    result += z;
    return result;
}

int main(){
    for(long i = 0x8000000; i <= __INT_MAX__ ; i++){
        if(threefourths(i) != f3(i)){
            std::cout << "DUŻO ŹLE! Dla i= "<< i << "\n";
        }
    }

    std::cout << "DUŻO DOBRZE!";
    return 0;
}
