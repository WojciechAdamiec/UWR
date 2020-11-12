#include "bst.h"

typedef struct node{
	int value;
	struct node* left;
	struct node* right;
} Node;

Node* new_node(int v) {
	Node* n = (Node*)malloc(sizeof(Node));
	n->value = v;
	n->left = NULL;
	n->right = NULL;
	return n;
}

void add(Node **t, int x) {
	if (*t == NULL) {
		*t = new_node(x);
	}
	else if (x < (*t)->value) {
		add(&(*t)->left, x);
	}
	else {
		add(&(*t)->right, x);
	}
}

Node* search(Node* t, int x) {
	if (t == NULL || t->value == x) {
		return t;
	}
	if (t->value < x) {
		return search(t->right, x);
	}
	return search(t->left, x);
}

int height(Node* t) {
	if (t == NULL) {
		return 0;
	}
	int height_left = height(t->left);
	int height_right = height(t->right);
	if (height_left > height_right) {
		return 1 + height_left;
	}
	else {
		return 1 + height_right;
	}
}

void info(Node* t) {
	if (t != NULL) {
		info(t->left);
		printf("%d \n", t->value);
		info(t->right);
	}
}

Node* minimum(Node* t)
{
	Node* current = t;

	while (current && current->left != NULL)
		current = current->left;

	return current;
}

Node* removeValue(Node *t, int x)
{
	if (t == NULL) return t;
 
	if (x < t->value)
		t->left = removeValue(t->left, x);

	else if (x > t->value)
		t->right = removeValue(t->right, x);

	else
	{
		if (t->left == NULL)
		{
			Node *temp = t->right;
			free(t);
			return temp;
		}
		else if (t->right == NULL)
		{
			Node *temp = t->left;
			free(t);
			return temp;
		}

		Node* temp = minimum(t->right);

		t->value = temp->value;

		t->right = removeValue(t->right, temp->value);
	}
	return t;
}
