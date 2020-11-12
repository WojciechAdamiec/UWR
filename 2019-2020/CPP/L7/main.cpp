#include <iostream>
#include "wymierne.h"

using namespace obliczenia;

std::string printWym(const wymierna& r);

int main(int argc, char * argv[])
{
	// Konstruktory
	std::cout << "Testy konstruktora:\n" <<
		"wymierna(2, 3)  = " << wymierna(2, 3) << '\n' <<
		"wymierna(1, 7)  = " << wymierna(1, 7) << '\n';

	// Ostream
	wymierna r1 = wymierna(1, 6);
	wymierna r2 = wymierna(2, 7);
	wymierna r3 = wymierna(37, 300);
	wymierna r4 = wymierna(36, 43);
	std::cout << "\nTest Ostream:\n" <<
		"R1: " << printWym(r1) << "    = " << r1 << '\n' <<
		"R2: " << printWym(r2) << "    = " << r2 << '\n' <<
		"R3: " << printWym(r3) << " = " << r3 << '\n' <<
		"R4: " << printWym(r4) << "  = " << r4 << '\n';


	wymierna t1 = r1 + r2;
	wymierna t2 = r1 - r2;
	wymierna t3 = r1 * r2;
	wymierna t4 = r1 / r2;
	wymierna t5 = -r1;
	wymierna t6 = !t5;
	wymierna t7 = r1;
	t7 += r2;
	wymierna t8 = r1;
	t8 -= r2;
	wymierna t9 = r1;
	t9 *= r2;
	wymierna t10 = r1;
	t10 /= r2;
	std::cout << "\nTesty operatorów:\n" <<
		"R1 + R2  =  " << printWym(t1) << '\n' <<
		"R1 - R2  = " << printWym(t2) << '\n' <<
		"R1 * R2  =  " << printWym(t3) << '\n' <<
		"R1 / R2  =  " << printWym(t4) << '\n' <<
		"-R1      = " << printWym(t5) << '\n' <<
		"!(-R1)   =  " << printWym(t6) << '\n' <<
		"R1 += R2 =  " << printWym(t7) << '\n' <<
		"R1 -= R2 = " << printWym(t8) << '\n' <<
		"R1 *= R2 =  " << printWym(t9) << '\n' <<
		"R1 /= R2 =  " << printWym(t10) << '\n';


	double ct1 = r1;
	int ct2 = (int)r1;
	int ct3 = (int)wymierna(1, 2);
	int ct4 = (int)wymierna(5, 3);
	std::cout << "\nTesty castowania:\n" <<
		r1 << " => double = " << ct1 << '\n' <<
		r1 << " => (int)  = " << ct2 << '\n' <<
		wymierna(1, 2) << " => (int)  = " << ct3 << '\n' <<
		wymierna(5, 3) << "  => (int)  = " << ct4 << '\n';


	std::cout << "\nTesty wyjatkow:\n";
	try {
		std::cout << "wymierna(1,0):\n";
		wymierna(1, 0);
	}
	catch (wymierne_wyjatek* e) {
		std::cout << '\t' << e->co() << '\n';
	}

	try {
		std::cout << printWym(wymierna(INT_MAX - 2, INT_MAX - 4)) << " * " <<
			printWym(wymierna(4, 3)) << ":\n";
		wymierna(INT_MAX - 2, INT_MAX - 4) * wymierna(4, 3);
	}
	catch (wymierne_wyjatek* e) {
		std::cout << '\t' << e->co() << '\n';
	}

	try {
		std::cout << "Niestandardowy wyjatek - test:\n";
		throw new poza_zakresem("Niestandardowy wyjatek!");
	}
	catch (wymierne_wyjatek* e) {
		std::cout << '\t' << e->co() << '\n';
	}

	std::cin.ignore();
	return 0;
}

std::string printWym(const wymierna& r) {
	return std::to_string(r.dajLicz()) + "/" + std::to_string(r.dajMian());
}