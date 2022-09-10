#include <fstream>
#include <iostream>
#include <random>

using namespace std;

int main() {
	random_device rdev;
	mt19937 gen(rdev());

	uniform_real_distribution<double> ud(0, 10);
	binomial_distribution<int> bd(20, 0.5);
	normal_distribution<double> nd(0.5, 0.1);

	ofstream ofs1("../uniform.csv", ios::out);
	ofstream ofs2("../binomial.csv", ios::out);
	ofstream ofs3("../normal.csv", ios::out);

	for (int i = 0; i < 1000; ++i) {
		ofs1 << ud(gen) << '\n';
		ofs2 << bd(gen) << '\n';
		ofs3 << nd(gen) << '\n';
	}

	ofs1.close();
	ofs2.close();
	ofs3.close();

	return 0;
}