#include <iostream>
#include "wyrazenie.hpp"
#include "operatory.hpp"

int main() {

	// Testujemy tutaj liczby, stale i zmienne
	Wyrazenie* liczba = new Liczba(44);
	Wyrazenie* pi = new Pi();
	Wyrazenie* e = new E();
	Wyrazenie* fi = new Fi();
	Wyrazenie* x = new Zmienna("x");
	Wyrazenie* y = new Zmienna("y");
	Zmienna::dodaj_wart(std::make_pair("x", 13.37));
	Zmienna::dodaj_wart(std::make_pair("y", 2020));

	std::cout << "Testujemy tutaj liczby, stale i zmienne: \n";
	std::cout << liczba->opis() << " = " << liczba->oblicz() << '\n'
		<< pi->opis() << " = " << pi->oblicz() << '\n'
		<< e->opis() << " = " << e->oblicz() << '\n'
		<< fi->opis() << " = " << fi->oblicz() << '\n'
		<< x->opis() << " = " << x->oblicz() << '\n'
		<< y->opis() << " = " << y->oblicz() << '\n';

	// Testujemy tutaj operatory jednoargumentowe
	Wyrazenie* sin1 = new Sin(new Liczba(1));
	Wyrazenie* sin2 = new Sin(new Pi());
	Wyrazenie* sin3 = new Sin(new Liczba(0));

	Wyrazenie* cos1 = new Cos(new Liczba(1));
	Wyrazenie* cos2 = new Cos(new Pi());
	Wyrazenie* cos3 = new Cos(new Liczba(0));

	Wyrazenie* exp = new Exp(new Liczba(3));
	Wyrazenie* ln = new Ln(new Liczba(10));
	
	Wyrazenie* bezwzgl1 = new Bezwzgl(new Liczba(-2));
	Wyrazenie* bezwzgl2 = new Bezwzgl(new Liczba(2));

	Wyrazenie* przeciw1 = new Przeciw(new Liczba(-2));
	Wyrazenie* przeciw2 = new Przeciw(new Liczba(2));

	Wyrazenie* odwrot1 = new Odwrot(new Liczba(2));
	Wyrazenie* odwrot2 = new Odwrot(new Liczba(1.0/2));

	std::cout << "\nTestujemy tutaj operatory jednoargumentowe: \n";
	std::cout << sin1->opis() << " = " << sin1->oblicz() << '\n'
		<< sin2->opis() << " = " << sin2->oblicz() << '\n'
		<< sin3->opis() << " = " << sin3->oblicz() << '\n'
		<< cos1->opis() << " = " << cos1->oblicz() << '\n'
		<< cos2->opis() << " = " << cos2->oblicz() << '\n'
		<< cos3->opis() << " = " << cos3->oblicz() << '\n'
		<< exp->opis() << " = " << exp->oblicz() << '\n'
		<< ln->opis() << " = " << ln->oblicz() << '\n'
		<< bezwzgl1->opis() << " = " << bezwzgl1->oblicz() << '\n'
		<< bezwzgl2->opis() << " = " << bezwzgl2->oblicz() << '\n'
		<< przeciw1->opis() << " = " << przeciw1->oblicz() << '\n'
		<< przeciw2->opis() << " = " << przeciw2->oblicz() << '\n'
		<< odwrot1->opis() << " = " << odwrot1->oblicz() << '\n'
		<< odwrot2->opis() << " = " << odwrot2->oblicz() << '\n';

	// Testujemy tutaj operatory dwuargumentowe
	Wyrazenie* dodaj = new Dodaj(pi, e);
	Wyrazenie* logarytm = new Logarytm(e, new Liczba(7));
	Wyrazenie* odejmij = new Odejmij(pi, e);
	Wyrazenie* modulo = new Modulo(pi, x);
	Wyrazenie* mnoz = new Mnoz(x, y);
	Wyrazenie* potega = new Potega(y, new Liczba(2));
	Wyrazenie* dziel = new Dziel(x, new Liczba(2));

	std::cout << "\nTestujemy tutaj operatory dwuargumentowe: \n";
	std::cout << dodaj->opis() << " = " << dodaj->oblicz() << '\n'
		<< logarytm->opis() << " = " << logarytm->oblicz() << '\n'
		<< odejmij->opis() << " = " << odejmij->oblicz() << '\n'
		<< modulo->opis() << " = " << modulo->oblicz() << '\n'
		<< mnoz->opis() << " = " << mnoz->oblicz() << '\n'
		<< potega->opis() << " = " << potega->oblicz() << '\n'
		<< dziel->opis() << " = " << dziel->oblicz() << '\n';

	std::cin.ignore();

	// Przykladowe wyrazenia:
	std::vector< std::pair<std::string, double> > wart = { std::make_pair("x", 0),std::make_pair("y", 3) };
	Zmienna::ustaw_wart(wart);

	Wyrazenie* w0 = new Dziel(
		new Mnoz(
			new Odejmij(
				new Zmienna("x"),
				new Liczba(1)
			),
			new Zmienna("x")
		),
		new Liczba(2));

	Wyrazenie* w1 = new Dziel(
		new Dodaj(
			new Liczba(3),
			new Liczba(5)
		),
		new Dodaj(
			new Liczba(2),
			new Mnoz(
				new Zmienna("x"),
				new Liczba(7)
			)
		)
	);

	Wyrazenie* w2 = new Odejmij(
		new Dodaj(
			new Liczba(2),
			new Mnoz(
				new Zmienna("x"),
				new Liczba(7)
			)
		),
		new Dodaj(
			new Mnoz(
				new Zmienna("y"),
				new Liczba(3)
			),
			new Liczba(5)
		)
	);

	Wyrazenie* w3 = new Dziel(
		new Cos(
			new Mnoz(
				new Dodaj(
					new Zmienna("x"),
					new Liczba(1)
				),
				new Zmienna("x")
			)
		),
		new Potega(
			new E(),
			new Potega(
				new Zmienna("x"),
				new Liczba(2)
			)
		)
	);

	std::cout << "\nPrzykladowe wyrazenia:: \n" <<
		w0->opis() << '\n' <<
		w1->opis() << '\n' <<
		w2->opis() << '\n' <<
		w3->opis() << '\n';

	std::cin.ignore();

	for (double i = 0; i <= 1.001; i += 0.01) {
		wart[0] = std::make_pair("x", i);
		Zmienna::ustaw_wart(wart);
		std::cout << "\n\t\t\t\t\tx = " << i << '\n' <<
			"\t\t\t\t\ty = " << wart[1].second << '\n' <<
			w0->opis() << "\t\t\t - W0 = " << w0->oblicz() << "\n" <<
			w1->opis() << "\t\t - W1 = " << w1->oblicz() << "\n" <<
			w2->opis() << "\t - W2 = " << w2->oblicz() << "\n" <<
			w3->opis() << "\t - W3 = " << w3->oblicz() << "\n";
	}

	std::cin.ignore();

	return 0;
}
