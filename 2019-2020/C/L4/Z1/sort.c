#include "bst.h"
#include <stdio.h>
#include <stdlib.h>

int main() {
	Node* tree = NULL;
	for (int i = 0; i < 106; i++) {
		add(&tree, rand());
	}
	printf("height: %d \n", height(tree));
	info(tree);
}
