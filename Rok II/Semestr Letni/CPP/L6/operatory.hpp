#pragma once

#include <cmath>
#include "wyrazenie.hpp"

class Operator1arg : public Wyrazenie {
protected:
	Wyrazenie* prawy;
public:
	Operator1arg(Wyrazenie* w);
	virtual double oblicz() const = 0;
	virtual std::string opis() const = 0;
};

class Sin : public Operator1arg {
public:
	using Operator1arg::Operator1arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Cos : public Operator1arg {
public:
	using Operator1arg::Operator1arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Exp : public Operator1arg {
public:
	using Operator1arg::Operator1arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Ln : public Operator1arg {
public:
	using Operator1arg::Operator1arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Bezwzgl : public Operator1arg {
public:
	using Operator1arg::Operator1arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Przeciw : public Operator1arg {
public:
	Przeciw(Wyrazenie* w);
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Odwrot : public Operator1arg {
public:
	Odwrot(Wyrazenie* w);
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Operator2arg : public Operator1arg {
protected:
	Wyrazenie* lewy;
public:
	Operator2arg(Wyrazenie* lw, Wyrazenie* pw);
	virtual double oblicz() const = 0;
	virtual std::string opis() const = 0;
};

class Dodaj : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Odejmij : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Mnoz : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Dziel : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Logarytm : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Modulo : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};

class Potega : public Operator2arg {
public:
	using Operator2arg::Operator2arg;
	virtual double oblicz() const override;
	virtual std::string opis() const override;
};