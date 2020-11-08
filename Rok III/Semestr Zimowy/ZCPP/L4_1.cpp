#include <iostream>
#include <vector>
#include <set>
#include <list>

using namespace std;

int main() {

	// Zadanie 1 //

	vector<double> x;
	list<string> y;
	set<int> z;

	x.push_back(1.0);
	x.push_back(4.0);
	x.push_back(1.0);
	x.push_back(0.0);

	y.push_back("Jeszcze");
	y.push_back("Polska");
	y.push_back("nie");
	y.push_back("zginęła");

	z.insert(1);
	z.insert(3);
	z.insert(7);
	z.insert(2);

	// Wypisz wszystkie wartości z zadanego zakresu (większe od a i mniejsze od b).

	template <typename Container>
	void printIfInRange(const Container &c,
						const typename Container::value_type &a,
						const typename Container::value_type &b) {
		auto lambda = [&](auto x) {
			if (x > a && x < b)
				cout << '\t' << x << '\n';
		};
		for_each(c.begin(), c.end(), lambda);
	}

	return 0;
}
