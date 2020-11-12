#include "bst.h"

int main() {
	Node* tree = NULL;
	add(&tree, 10);
	for (int i = 20; i > 0; i -= 2) {
		add(&tree, i);
	}
	
	info(tree);
	if (search(tree, 10)) {
		printf("OK!\n");
	}
	if (search(tree, 11)) {
		printf("Not OK!\n");
	}

	// Height should be 7:
	printf("=============== \n");
	printf("Height: %d \n", height(tree));

	// Tests for an empty tree
	printf("=============== \n");
	Node* birch = NULL;
	search(birch, 10);
	removeValue(birch, 10);

	// Tests for removeValue
	printf("=============== \n");
	Node* oak = NULL;
	add(&oak, 50);
	add(&oak, 30);
	add(&oak, 20);
	add(&oak, 40);
	add(&oak, 70);
	add(&oak, 60);
	add(&oak, 80);
	printf("=============== \n");
	info(oak);
	removeValue(oak, 30);
	removeValue(oak, 70);
	removeValue(oak, 60);
	removeValue(oak, 60);
	printf("=============== \n");
	info(oak);
	printf("=============== \n");

	// Tests for resuability
	Node* ash = NULL;
	info(ash);
	add(&ash, 17);
	removeValue(ash, 17);
	add(&ash, 123);
	info(ash);
}
