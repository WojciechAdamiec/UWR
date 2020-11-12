#include <stdio.h>
#define MAXSIZE 100000
 
struct stack
{
    int stk[MAXSIZE];
    int top;
};
typedef struct stack STACK;
STACK s;
 
void push(int element);
int  pop(void);
void display(void);


int main()
{
    s.top = -1;
    int len;
    scanf("%d", &len);
    char array[len];
    scanf("%s", array);
    
    for(int i = len - 1; i >= 0; i--){
        // printf("i: %d array[i]: %d \n", i, array[i] - 48);
        // display();
        if (array[i] >= '0' && array[i] <='9'){
            push(array[i] - 48);
        }
        else{
            int a = pop();
            int b = pop();
            if (array[i] == '+'){
                push(a + b);
            }
            if (array[i] == '-'){
                push(a - b);
            }
            if (array[i] == '*'){
                push(a * b);
            }
        }
    }
    
    printf("%d", pop());

    return 0;
}


void push (int element)
{
    int num;
    if (s.top == (MAXSIZE - 1))
    {
        printf ("Stack is Full\n");
        return;
    }
    else
    {
        // printf ("Enter the element to be pushed\n");
        num = element;
        s.top = s.top + 1;
        s.stk[s.top] = num;
    }
    return;
}
/*  Function to delete an element from the stack */
int pop ()
{
    int num;
    if (s.top == - 1)
    {
        printf ("Stack is Empty\n");
        return (s.top);
    }
    else
    {
        num = s.stk[s.top];
        // printf ("poped element is = %dn", s.stk[s.top]);
        s.top = s.top - 1;
    }
    return(num);
}
/*  Function to display the status of the stack */
void display ()
{
    int i;
    if (s.top == -1)
    {
        printf ("Stack is empty\n");
        return;
    }
    else
    {
        printf ("\n The status of the stack is \n");
        for (i = s.top; i >= 0; i--)
        {
            printf ("%d\n", s.stk[i]);
        }
    }
    printf ("\n");
}