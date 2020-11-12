#pragma once
#define _USE_MATH_DEFINES
#include <cmath>
#include "wyrazenie.hpp"
#include <string>
#include <vector>

class Wyrazenie {
protected:
	bool nawiasy;
public:
	bool dajNawiasy() const;
	void ustawNawiasy(bool v);
	virtual double oblicz() const = 0;
	virtual std::string opis() const = 0;
};

class Liczba : public Wyrazenie {
protected:
	const double value;
public:
	Liczba();
	Liczba(double l);

	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Stala : public Wyrazenie {
protected:
	const std::string symbol;
	const double value;
public:
	Stala(std::string name, double value);

	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class E : public Stala {
public:
	E();
};

class Pi : public Stala {
public:
	Pi();
};

class Fi : public Stala {
public:
	Fi();
};

class Zmienna : public Wyrazenie {
private:
	static std::vector< std::pair<std::string, double> > values;
	const std::string name;
public:
	Zmienna(std::string name);

	virtual double oblicz() const override;
	virtual std::string opis() const override;

	static void dodaj_wart(const std::pair<std::string, double>& p);
	static void ustaw_wart(const std::vector< std::pair<std::string, double> >& w);
};