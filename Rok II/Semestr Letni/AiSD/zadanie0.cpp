#include <cstdio>
#include <algorithm>


int main(){
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    
    if (a > b){
        std::swap(a, b);
    }

    for (;a <= b; a++){
        printf("%d\n", a);
    }
}
