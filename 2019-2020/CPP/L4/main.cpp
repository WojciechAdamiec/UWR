#include "stack.h"

using namespace std;

void printMan();

int main() {
	
	cout << "Constructor tests: Empty constructor:\n";
	// Empty constructor
	stack *stack1 = new stack();

	cout << "\nInitializer_list constructor:\n";
	// Initializer_list constructor
	stack *stack2 = new stack{ "1", "2", "3", "4", "5", "6" };
	stack2->print();
	
	cout << "\nCopying constructor: \n";
	// Copying constructor
	stack *stack3 = new stack(*stack2);
	stack3->print();
	
	cout << "\nMoving constructor: \n";
	// Moving constructor
	stack *stack4 = new stack(std::move(*stack3));
	stack4->print();
	cout << "\nMoved stack:\n";
	stack3->print();

	
	delete stack1;
	delete stack2;
	delete stack3;
	delete stack4;

	cin.ignore();

	// Konstruktor z int
	stack *LIFO = new stack(5);

	bool loop = true;
	char input;
	string s;
	int cap;

	printMan();
	for (int i = 0; i < 20; i++)
		cout << '\n';

	while (loop) {
		std::cout << '\n';
		std::cin >> input;
		try {
			switch (input) {
			case 'q':
				std::cout << "Give stack's maximum capacity: \n";
				std::cin >> cap;
				delete LIFO;
				LIFO = new stack(cap);
				std::cout << "Created stack of capacity: " << cap << "\n";
				break;

			case 'w':
				std::cout << "Give a new element to put.\n";
				std::cin >> s;
				LIFO->put(s);
				std::cout << "Text: " << s << " has been added to stack.\n";
				break;

			case 'e':
				std::cout << "Removed element: " << LIFO->pop() << "\n";
				break;

			case 'r':
				std::cout << "Last element of a stack: " << LIFO->look() << "\n";
				break;

			case 't':
				std::cout << "Number of elements in stack: " << LIFO->size() << "\n";
				break;

			case 'y':
				LIFO->print();
				break;

			case 'u':
				loop = false;
				break;

			default:
				std::cout << "Wrong command, try again.\n\n";
				printMan();
			}
		}
		catch (exception &e) {
			cout << "Error - " << e.what() << "\n";
		}
	}

	delete LIFO;
	std::cin.ignore();
	
	return 0;
}

void printMan() {
	std::cout << "Type the next command.\n"
		"Avaiable commands:\n"
		"q - Create new stack\n"
		"w - Put element to stack\n"
		"e - Pop last element\n"
		"r - Look at the last element\n"
		"t - Stack size\n"
		"y - Print all elements of stack\n"
		"u - End program\n";
}