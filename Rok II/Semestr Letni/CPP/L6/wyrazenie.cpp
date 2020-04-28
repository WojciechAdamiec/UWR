#include "wyrazenie.hpp"

bool Wyrazenie::dajNawiasy() const {
	return nawiasy;
}

void Wyrazenie::ustawNawiasy(bool v) {
	nawiasy = v;
}

Liczba::Liczba() :value(0) {}

Liczba::Liczba(double l) : value(l) {
	if (value < 0)
		ustawNawiasy(true);
	else
		ustawNawiasy(false);
}

double Liczba::oblicz() const {
	return value;
}

std::string Liczba::opis() const {
	std::string out = std::to_string(value);
	return out.erase(out.find_last_not_of('0') + 2, std::string::npos);
}

Stala::Stala(std::string name, double value) : symbol(name), value(value) {
	if (value < 0)
		ustawNawiasy(true);
	else
		ustawNawiasy(false);
}

double Stala::oblicz() const {
	return value;
}

std::string Stala::opis() const {
	return symbol;
}

E::E() : Stala("e", M_E) {}

Pi::Pi() : Stala("pi", M_PI) {}

Fi::Fi() : Stala("fi", (1 + sqrt(5)) / 2) {}

std::vector< std::pair<std::string, double> > Zmienna::values;

Zmienna::Zmienna(std::string name) : name(name) {
	ustawNawiasy(false);
}

double Zmienna::oblicz() const {
	for (std::pair<std::string, double> val : values)
		if (val.first == name)
			return val.second;

	throw new std::out_of_range("Error: No value for variable " + name + ".");
}

std::string Zmienna::opis() const {
	return name;
}

void Zmienna::dodaj_wart(const std::pair<std::string, double>& p) {
	for (std::pair<std::string, double> val : values)
		if (val.first == p.first)
			throw new std::out_of_range("Error: variable " + p.first + " already exixts.");

	values.push_back(p);
}

void Zmienna::ustaw_wart(const std::vector<std::pair<std::string, double>>& w) {
	values = w;
}