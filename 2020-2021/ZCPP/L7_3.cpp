#include <fstream>
#include <iostream>
#include <sstream> 
#include <random>

using namespace std;


int main(int argc, char** argv) {

	string filename;
	int len;

	if (argc >= 3) {
		filename = argv[1];
		len = stoi(argv[2]);
	}
	else {
		filename = "test.txt";
		len = 10;
	}
	cout << "Filename: " << filename << "\n";

    // std::discrete_distribution
    char letters[26] = {
        'E',
        'T',
        'A',
        'O',
        'I',
        'N',
        'S',
        'R',
        'H',
        'D',
        'L',
        'U',
        'C',
        'M',
        'F',
        'Y',
        'W',
        'G',
        'P',
        'B',
        'V',
        'K',
        'X',
        'Q',
        'J',
        'Z'
    };

	random_device rdev;
	mt19937 gen(rdev());

	binomial_distribution<int> bd(11, 0.5);
	uniform_real_distribution<double> ud(0, 1);
    discrete_distribution<int> dis({
        21912,
        16587,
        14810,
        14003,
        13318,
        12666,
        11450,
        10977,
        10795,
        7874,
        7253,
        5246,
        4943,
        4761,
        4200,
        3853,
        3819,
        3693,
        3316,
        2715,
        2019,
        1257,
        315,
        205,
        188,
        128
    });

	ofstream ofs(filename, ios::out);

	for (int i = 0; i < len; i++) {
		int word_len = bd(gen) + 1;
		string word = "";
		for (int j = 0; j < word_len; j++) {
			word.push_back(letters[dis(gen)]);
		}
		ofs << word << " ";
		cout << word << "\n";
	}

	ofs.close();

	return 0;
}