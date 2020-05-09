#pragma once
#include <algorithm>
#include <string>
#include <vector>

namespace obliczenia {

	bool dodawanieZakres(int a, int b, int& wynik);
	bool odejmowanieZakres(int a, int b, int& wynik);
	bool mnozenieZakres(int a, int b, int& wynik);

	class wymierne_wyjatek : public std::exception {
	protected:
		std::string info;
	public:
		wymierne_wyjatek();
		wymierne_wyjatek(const char* tresc);
		wymierne_wyjatek(const std::string& tresc);
		virtual const char* co() const throw();
	};

	class dzielenie_przez_0 : public wymierne_wyjatek {
		public:
			dzielenie_przez_0();
			using wymierne_wyjatek::wymierne_wyjatek;

	};

	class poza_zakresem : public wymierne_wyjatek {
		public:
			poza_zakresem();
			using wymierne_wyjatek::wymierne_wyjatek;

	};

	class wymierna
	{
		private:
		int licz, mian;

		int gcd(int a, int b);

		void optymalizacja();

		public:
		wymierna(int a, int b);
		wymierna(int a);
		wymierna(const wymierna &inny);

		friend std::ostream& operator<< (std::ostream &wyjscie, const wymierna &w) throw();
		friend wymierna operator + (const wymierna &a, const wymierna &b) throw(poza_zakresem);
		friend wymierna operator - (const wymierna &a, const wymierna &b) throw(poza_zakresem);
		friend wymierna operator * (const wymierna &a, const wymierna &b) throw(poza_zakresem);
		friend wymierna operator / (const wymierna &a, const wymierna &b) throw(poza_zakresem);
		wymierna operator - () const throw();

		wymierna operator ! () const throw(dzielenie_przez_0);

		wymierna& operator += (const wymierna &a) throw(poza_zakresem);
		wymierna& operator -= (const wymierna &a) throw(poza_zakresem);
		wymierna& operator *= (const wymierna &a) throw(poza_zakresem);
		wymierna& operator /= (const wymierna &a) throw();

		int dajLicz() const;
		int dajMian() const;

		operator double() const throw();
		explicit operator int() const throw();
		
	};
}