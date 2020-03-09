#include <math.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>


typedef struct pair {
    int a;
    int b;
} pair;

typedef struct node {
    int type;
    int integer;
    pair p;
    float floating;
    char text[256];
} node;


#define SIZE 100

node queue[SIZE];
int begin = -1;
int end = -1;

pair makePair(int a, int b) {
    pair new;
    new.a = a;
    new.b = b;
    return new;
}

bool isEmpty() {
    if(begin == -1)
        return true;
    return false;
}

bool isFull() {
    if(abs(end - begin) < SIZE - 1)
        return false;
    return true;
}

bool pop() {
    if(isEmpty()) {
        puts("Tried to pop from an empty queue.");
        return false;
    }

    switch(queue[begin].type) {
    case 0:
        printf("%s\n", queue[begin].text);
        break;

    case 1:
        printf("%d\n", queue[begin].integer);
        break;

    case 2:
        printf("(%d,%d)\n", queue[begin].p.a, queue[begin].p.b);
        break;

    case 3:
        printf("%f\n", queue[begin].floating);
        break;

    default:
        puts("Invalid node type.");
    }

    if(begin == end) {
        begin = -1;
        end = -1;
    } else
        begin = (begin + 1) % SIZE;

    return true;
}

bool push() {
    if(isFull()) {
        puts("Tried to push into a full queue.");
        return false;
    }

    puts("Input data type:\n(0 - text, 1 - integer, 2 - pair of integers, 3 - "
         "floating point number)");
    char type;
    scanf(" %c", &type);
    node new;
    char text[256];
    int a, b;
    float f;
    switch(type) {
    case '0':
        puts("Input a string:");
        scanf(" %s", text);
        new.type = 0;
        for(int i = 0; i < 256; i++)
            new.text[i] = text[i];
        break;

    case '1':
        puts("Input integer:");
        scanf(" %d", &a);
        new.type = 1;
        new.integer = a;
        break;

    case '2':
        puts("Input a pair of integers:");
        scanf(" %d %d", &a, &b);
        new.type = 2;
        new.p = makePair(a, b);
        break;

    case '3':
        puts("Input a floating point number:");
        scanf(" %f", &f);
        new.type = 3;
        new.floating = f;
        break;

    default:
        puts("Invalid node type.");
    }

    if(begin == -1) {
        begin = 0;
        end = 0;
    } else
        end = (end + 1) % SIZE;
    queue[end] = new;

    return true;
}

int main(int argc, char *argv[]) {
    int option;
	while (true){
		printf("Press 1 to Pop, 2 to Push \n");
	    scanf(" %d", &option);
		if (option == 1){
			pop();
		}
		else if (option == 2){
			push();
		}
		else{
			printf("Error: Wrong Option!");
		}
	}
	

    return 0;
}
