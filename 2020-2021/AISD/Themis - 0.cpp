// Wojciech Adamiec
// 310064
// SDU

#include <stdio.h>
#include <inttypes.h>


int main()
{
    uint64_t a, b;
    scanf("%" PRIu64, &a);
    scanf("%" PRIu64, &b);

    uint64_t first = a / 2021;

    for (uint64_t j=first; j <= b; j++){
        if (j * 2021 >= a && j * 2021 <= b){
            printf("%" PRIu64 " ", j * 2021);
        }
    }
    return 0;
}
