#include "wymierne.h"

bool obliczenia::dodawanieZakres(int a, int b, int & wynik)
{
	if (a > INT_MAX - b)
		return true;
	else {
		wynik = a + b;
		return false;
	}
}

bool obliczenia::odejmowanieZakres(int a, int b, int & wynik)
{
	if (a < INT_MIN + b)
		return true;
	else {
		wynik = a - b;
		return false;
	}
}

bool obliczenia::mnozenieZakres(int a, int b, int & wynik)
{
	if (a > INT_MAX / b)
		return true;
	else {
		wynik = a * b;
		return false;
	}
}

int obliczenia::wymierna::gcd(int a, int b)
{
	if (b == 0)
		return a;
	return gcd(b, a % b);
}

void obliczenia::wymierna::optymalizacja()
{
	int gcd = obliczenia::wymierna::gcd(licz, mian);

	if (gcd != 1) {
		licz /= gcd;
		mian /= gcd;
	}
	if (mian < 0) {
		licz = -licz;
		mian = -mian;
	}
}

obliczenia::wymierna::wymierna(int a, int b)
{
	if (b == 0) {
		throw new dzielenie_przez_0;
	}
	licz = a;
	mian = b;
	optymalizacja();
}

obliczenia::wymierna::wymierna(int a)
{
	licz = a;
	mian = 1;
}

obliczenia::wymierna::wymierna(const wymierna & inny)
{
	licz = inny.licz;
	mian = inny.mian;
}

obliczenia::wymierna obliczenia::wymierna::operator-() const throw()
{
	return obliczenia::wymierna(-licz, mian);
}

obliczenia::wymierna obliczenia::wymierna::operator!() const throw(dzielenie_przez_0)
{
	return obliczenia::wymierna(mian, licz);
}

obliczenia::wymierna & obliczenia::wymierna::operator+=(const wymierna & a) throw(poza_zakresem)
{
	*this = *this + a;
	return *this;
}

obliczenia::wymierna & obliczenia::wymierna::operator-=(const wymierna & a) throw(poza_zakresem)
{
	*this = *this - a;
	return *this;
}

obliczenia::wymierna & obliczenia::wymierna::operator*=(const wymierna & a) throw(poza_zakresem)
{
	*this = *this * a;
	return *this;
}

obliczenia::wymierna & obliczenia::wymierna::operator/=(const wymierna & a) throw()
{
	*this = *this / a;
	return *this;
}

int obliczenia::wymierna::dajLicz() const
{
	return licz;
}

int obliczenia::wymierna::dajMian() const
{
	return mian;
}

obliczenia::wymierna::operator double() const throw()
{
	return (double)licz / (double)mian;
}

obliczenia::wymierna::operator int() const throw()
{
	double aux = *this;
	return (int)aux;
}

obliczenia::wymierne_wyjatek::wymierne_wyjatek()
{
	info = "Wymierne blad!";
}

obliczenia::wymierne_wyjatek::wymierne_wyjatek(const char * tresc)
	: info(tresc){}

obliczenia::wymierne_wyjatek::wymierne_wyjatek(const std::string & tresc)
	: info(tresc) {}

const char * obliczenia::wymierne_wyjatek::co() const throw()
{
	return info.c_str();
}

obliczenia::dzielenie_przez_0::dzielenie_przez_0()
{
	info = "Wymierne blad - Dzielenie przez 0";
}

obliczenia::poza_zakresem::poza_zakresem()
{
	info = "Wymierne blad - Poza zakresem";
}

std::ostream & obliczenia::operator<<(std::ostream & wyjscie, const wymierna & w)
{
	int licz = w.dajLicz();
	int mian = w.dajMian();

	std::vector<int> reminders(mian, -1);

	std::string res;
	for (int i = 0; reminders[licz%mian] < 0; i++) {
		reminders[licz%mian] = i;
		res += '0' + (licz * 10 / mian) % 10;
		licz = (licz * 10) % mian;
	}
	int length = reminders[licz%mian];

	std::string _out = std::to_string(licz / mian) + "." + res.substr(0, length) + "(" + res.substr(length) + ")";
	wyjscie << _out;

	return wyjscie;
}

obliczenia::wymierna obliczenia::operator+(const wymierna & a, const wymierna & b) throw(poza_zakresem)
{
	int aux_a, aux_b;
	int licz, mian;

	if (mnozenieZakres(a.dajLicz(), b.dajMian(), aux_a))
		throw new poza_zakresem();
	if (mnozenieZakres(b.dajLicz(), a.dajMian(), aux_b))
		throw new poza_zakresem();
	if (dodawanieZakres(aux_a, aux_b, licz))
		throw new poza_zakresem();

	if (mnozenieZakres(a.dajMian(), b.dajMian(), mian))
		throw new poza_zakresem();

	return obliczenia::wymierna(licz, mian);
}

obliczenia::wymierna obliczenia::operator-(const wymierna & a, const wymierna & b) throw(poza_zakresem)
{
	int aux_a, aux_b;
	int licz, mian;

	if (mnozenieZakres(a.dajLicz(), b.dajMian(), aux_a))
		throw new poza_zakresem();
	if (mnozenieZakres(b.dajLicz(), a.dajMian(), aux_b))
		throw new poza_zakresem();
	if (odejmowanieZakres(aux_a, aux_b, licz))
		throw new poza_zakresem();

	if (mnozenieZakres(a.dajMian(), b.dajMian(), mian))
		throw new poza_zakresem();

	return obliczenia::wymierna(licz, mian);
}

obliczenia::wymierna obliczenia::operator*(const wymierna & a, const wymierna & b) throw(poza_zakresem)
{
	int licz, mian;

	if (mnozenieZakres(a.dajLicz(), b.dajLicz(), licz))
		throw new poza_zakresem();
	if (mnozenieZakres(b.dajMian(), a.dajMian(), mian))
		throw new poza_zakresem();

	return obliczenia::wymierna(licz, mian);
}

obliczenia::wymierna obliczenia::operator/(const wymierna & a, const wymierna & b) throw(poza_zakresem)
{
	return a * !b;
}
