// Wojciech Adamiec
// 310064
// WJAN
#include <stdio.h>



int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    
    for (int j=1; j <= 2020; j++){
        if (j >= a && j <= b){
            if (2020 % j == 0){
                printf("%d ", j);
            }
        }
    }
    return 0;
}
