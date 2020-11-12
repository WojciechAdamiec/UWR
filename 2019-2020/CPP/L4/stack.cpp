#include "stack.h"

void stack::put(std::string element)
{
	if (pointer >= capacity) {
		throw std::exception("Stack full!");
	}
	data[pointer] = element;
	pointer++;
}

std::string stack::pop()
{
	if (pointer == 0) {
		throw std::exception("Stack empty!");
	}
	pointer--;
	return data[pointer];
}

std::string stack::look()
{
	if (pointer == 0) {
		throw std::exception("Stack empty!");
	}
	return data[pointer - 1];
}

int stack::size()
{
	return pointer;
}

void stack::print()
{
	for (int i = 0; i < pointer; i++) {
		std::cout << data[i] << ", ";
	}
}

stack::stack()
{
	capacity = 1;
	pointer = 0;
	data = new std::string[capacity];
}

stack::stack(int capacity)
{
	if (capacity > 100 || capacity < 1) {
		throw std::exception("Wrong Capacity!");
	}
	this->capacity = capacity;
	this->pointer = 0;
	data = new std::string[capacity];
}

stack::stack(std::initializer_list<std::string> list)
{
	capacity = list.size();
	pointer = capacity;
	data = new std::string[capacity];
	auto it = list.begin();

	for (int j = 0; it != list.end(); j++, it++) {
		data[j] = *it;
	}
}

stack::stack(const stack & toCopy) : stack(toCopy.capacity)
{
	pointer = toCopy.pointer;
	for (int j = 0; j < capacity; j++) {
		data[j] = toCopy.data[j];
	}
}

stack::stack(stack && toMove)
{
	capacity = toMove.capacity;
	pointer = toMove.pointer;
	data = toMove.data;
	toMove.capacity = 0;
	toMove.pointer = -1;
	toMove.data = nullptr;
}

stack::~stack()
{
	delete[] data;
}

stack stack::reverse()
{
	stack newStack = *this;
	std::reverse(data, data + newStack.pointer);

	return newStack;
}

stack & stack::operator=(const stack & old)
{
	if (&old == this) {
		return *this;
	}
	delete[] data;
	data = nullptr;
	pointer = old.pointer;
	data = new std::string[capacity];

	for (int j = 0; j < capacity; j++) {
		data[j] = old.data[j];
	}
	return *this;
}

stack & stack::operator=(stack && old)
{
	if (&old == this) {
		return *this;
	}
	delete[] data;
	data = nullptr;
	capacity = old.capacity;
	pointer = old.pointer;
	data = old.data;
	old.capacity = 0;
	old.pointer = -1;
	old.data = nullptr;
	return *this;
}
