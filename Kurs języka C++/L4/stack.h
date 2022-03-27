#pragma once
#include <string>
#include <iostream>
#include <algorithm>

class stack {

	private: 
		std::string* data;
		int capacity;
		int pointer;

	public:
		// Standard Methods:
		void put(std::string element);
		std::string pop();
		std::string look();
		int size();
		void print();

		// Constructors / Destructors:
		stack();
		stack(int capacity);
		stack(std::initializer_list<std::string> list);
		stack(const stack & toCopy);
		stack(stack && toMove);
		~stack();

		// Additional methods:
		stack reverse();

		// Assignments:

		stack & operator= (const stack & old);
		stack & operator= (stack && old);
		
};