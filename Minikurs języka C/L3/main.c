#include <stdio.h>


int next(int* t, int index){
    int i = index;
    while(t[i] == 'X')
        i++;
    return i;
}


int main()
{
    int l;
    scanf("%d", &l);
    char array[l];
    scanf("%c");
    gets(array);
    
    int i = l - 1;
    while (i < 0){
        for (int j = 0; j < l; j++)
            printf("%c", array[j]);
        printf(" \n i: %d \n", i);
        
        if (array[i] == '+'){
            int aux1 = next(array, i + 1);
            printf("aux: %d \n", aux1);
            int a = array[aux1];
            array[aux1] = 'X';
            aux1 = next(array, i + 2);
            printf("aux: %d \n", aux1);
            int b = array[aux1];
            array[aux1] = 'X';
            array[i] = a + b;
        }
        if (array[i] == '-'){
            int aux2 = next(array, i + 1);
            int a = array[aux2];
            array[aux2] = 'X';
            aux2 = next(array, i + 2);
            int b = array[aux2];
            array[aux2] = 'X';
            array[i] = a - b;
        }
        if (array[i] == '*'){
            int aux3 = next(array, i + 1);
            int a = array[aux3];
            array[aux3] = 'X';
            aux3 = next(array, i + 2);
            int b = array[aux3];
            array[aux3] = 'X';
            array[i] = a * b;
        }
        i--;
    }
    printf("%d", array[0]);
    return 0;
}
