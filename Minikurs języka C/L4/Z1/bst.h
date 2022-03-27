#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

typedef struct node Node;

Node* new_node(int v);
void add(Node **t, int x);
Node* search(Node* t, int x);
int height(Node* t);
void info(Node* t);
Node* minimum(Node* t);
Node* removeValue(Node*t, int x);
