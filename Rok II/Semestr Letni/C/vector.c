#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct vector{
    int* data;
    int size;
    int count;
} vector;


vector* vector_create()
{
    vector* v = (vector *)malloc(sizeof(vector));
	v->data = NULL;
	v->size = 0;
	v->count = 0;
	return v;
}


void vector_add(vector *v, int e)
{
	if (v->size == 0) {
		v->size = 10;
		v->data = malloc(sizeof(int*) * v->size);
	}

	if (v->size == v->count) {
		v->size *= 2;
		v->data = realloc(v->data, sizeof(int*) * v->size);
	}

	v->data[v->count] = e;
	v->count++;
}


int vector_read(vector *v, int index)
{
    if (index >= v->count || index < 0){
        printf("Error: Wrong Index!");
        return index;
    }
	return v->data[index];
}

void vector_remove(vector *v)
{
    if (v->count - 1 < 0){
        printf("Error: Empty Vector!");
        return;
    }
	v->data[v->count] = 0;
	v->count--;
}

void vector_free(vector *v)
{
	free(v->data);
	free(v);
}

int main(void)
{
    vector* v = vector_create();

	vector_add(v, 1);
	vector_add(v, 2);
	vector_add(v, 3);
	vector_add(v, 4);
	vector_add(v, 5);

	int i;
	printf("First test:\n");
	for (i = 0; i < v->count; i++) {
		printf("%d\n", vector_read(v, i));
	}

	vector_remove(v);
	vector_remove(v);

	printf("Second test:\n");
	for (i = 0; i < v->count; i++) {
		printf("%d\n", vector_read(v, i));
	}
	
	printf("\n%d\n", vector_read(v, 0));
	printf("%d\n", vector_read(v, -1));
	printf("%d\n", vector_read(v, 3));
    
    vector_remove(v);
	vector_remove(v);
	vector_remove(v);
	printf("\nNow I am gonna delete element of an empty vector:\n");
	vector_remove(v);
    
	vector_free(v);
    
	return 0;
}