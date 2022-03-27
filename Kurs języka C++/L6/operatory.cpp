#include "operatory.hpp"

Operator1arg::Operator1arg(Wyrazenie * w) : prawy(w) {
	ustawNawiasy(false);
}

double Sin::oblicz() const {
	return sin(prawy->oblicz());
}

std::string Sin::opis() const {
	return "sin(" + prawy->opis() + ")";
}

double Cos::oblicz() const {
	return cos(prawy->oblicz());
}

std::string Cos::opis() const {
	return "cos(" + prawy->opis() + ")";
}

double Exp::oblicz() const {
	return exp(prawy->oblicz());
}

std::string Exp::opis() const {
	if (prawy->dajNawiasy())
		return "e^(" + prawy->opis() + ")";
	return "e^" + prawy->opis();
}

double Ln::oblicz() const {
	if (((new Bezwzgl(prawy)))->oblicz() <= DBL_EPSILON)
		throw new std::invalid_argument("Error - log argument <= 0.");

	return log(prawy->oblicz());
}

std::string Ln::opis() const {
	return "ln(" + prawy->opis() + ")";
}

double Bezwzgl::oblicz() const {
	return abs(prawy->oblicz());
}

std::string Bezwzgl::opis() const {
	return "|" + prawy->opis() + "|";
}

Przeciw::Przeciw(Wyrazenie * w) : Operator1arg(w) {
	ustawNawiasy(true);
}

double Przeciw::oblicz() const {
	return -prawy->oblicz();
}

std::string Przeciw::opis() const {
	if (prawy->dajNawiasy())
		return "-(" + prawy->opis() + ")";

	return "-" + prawy->opis();
}

Odwrot::Odwrot(Wyrazenie * w) : Operator1arg(w) {
	ustawNawiasy(true);
}

double Odwrot::oblicz() const {
	return 1 / prawy->oblicz();
}

std::string Odwrot::opis() const {
	if (prawy->dajNawiasy())
		return "1 / (" + prawy->opis() + ")";

	return "1 / " + prawy->opis();
}

Operator2arg::Operator2arg(Wyrazenie * lw, Wyrazenie * pw) : lewy(lw), Operator1arg(pw) {
	ustawNawiasy(true);
}

double Dodaj::oblicz() const {
	return lewy->oblicz() + prawy->oblicz();
}

std::string Dodaj::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "(" + lewy->opis() + ") + (" + prawy->opis() + ")";
	else if (lewy->dajNawiasy())
		return "(" + lewy->opis() + ") + " + prawy->opis();
	else if (prawy->dajNawiasy())
		return lewy->opis() + " + (" + prawy->opis() + ")";

	return lewy->opis() + " + " + prawy->opis();
}

double Odejmij::oblicz() const {
	return lewy->oblicz() - prawy->oblicz();
}

std::string Odejmij::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "(" + lewy->opis() + ") - (" + prawy->opis() + ")";
	else if (lewy->dajNawiasy())
		return "(" + lewy->opis() + ") - " + prawy->opis();
	else if (prawy->dajNawiasy())
		return lewy->opis() + " - (" + prawy->opis() + ")";

	return lewy->opis() + " - " + prawy->opis();
}

double Mnoz::oblicz() const {
	return lewy->oblicz() * prawy->oblicz();
}

std::string Mnoz::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "(" + lewy->opis() + ") * (" + prawy->opis() + ")";
	else if (lewy->dajNawiasy())
		return "(" + lewy->opis() + ") * " + prawy->opis();
	else if (prawy->dajNawiasy())
		return lewy->opis() + " * (" + prawy->opis() + ")";

	return lewy->opis() + " * " + prawy->opis();
}

double Dziel::oblicz() const {
	if (((new Bezwzgl(prawy)))->oblicz() < DBL_EPSILON)
		throw new std::invalid_argument("Error - dividing by zero.");

	return lewy->oblicz() / prawy->oblicz();
}

std::string Dziel::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "(" + lewy->opis() + ") / (" + prawy->opis() + ")";
	else if (lewy->dajNawiasy())
		return "(" + lewy->opis() + ") / " + prawy->opis();
	else if (prawy->dajNawiasy())
		return lewy->opis() + " / (" + prawy->opis() + ")";

	return lewy->opis() + " / " + prawy->opis();
}

double Logarytm::oblicz() const {
	if ((new Bezwzgl(lewy))->oblicz() <= DBL_EPSILON)
		throw new std::invalid_argument("Error - log base <= 0.");
	if ((new Bezwzgl(new Odejmij(lewy, new Liczba(1))))->oblicz() <= DBL_EPSILON)
		throw new std::invalid_argument("Error - log base = 1.");
	if ((new Bezwzgl(prawy))->oblicz() <= DBL_EPSILON)
		throw new std::invalid_argument("Error - log argument <= 0.");

	return log(prawy->oblicz()) / log(lewy->oblicz());
}

std::string Logarytm::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "log([" + lewy->opis() + "], [" + prawy->opis() + "])";
	else if (lewy->dajNawiasy())
		return "log([" + lewy->opis() + "], " + prawy->opis() + ")";
	else if (prawy->dajNawiasy())
		return "log(" + lewy->opis() + ", [" + prawy->opis() + "])";

	return "log(" + lewy->opis() + ", " + prawy->opis() + ")";
}

double Modulo::oblicz() const {
	if ((new Bezwzgl(prawy))->oblicz() < DBL_EPSILON)
		throw new std::invalid_argument("Error - dividing by zero in modulo");

	return fmod(lewy->oblicz(), prawy->oblicz());
}

std::string Modulo::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "(" + lewy->opis() + ") % (" + prawy->opis() + ")";
	else if (lewy->dajNawiasy())
		return "(" + lewy->opis() + ") % " + prawy->opis();
	else if (prawy->dajNawiasy())
		return lewy->opis() + " % (" + prawy->opis() + ")";

	return lewy->opis() + " % " + prawy->opis();
}

double Potega::oblicz() const {
	if ((new Bezwzgl(lewy))->oblicz() < DBL_EPSILON && (new Bezwzgl(prawy))->oblicz() < DBL_EPSILON)
		throw new std::invalid_argument("Error - power 0^0.");
	return pow(lewy->oblicz(), prawy->oblicz());
}

std::string Potega::opis() const {
	if (lewy->dajNawiasy() && prawy->dajNawiasy())
		return "(" + lewy->opis() + ")^(" + prawy->opis() + ")";
	else if (lewy->dajNawiasy())
		return "(" + lewy->opis() + ")^" + prawy->opis();
	else if (prawy->dajNawiasy())
		return lewy->opis() + "^(" + prawy->opis() + ")";

	return lewy->opis() + "^" + prawy->opis();
}
