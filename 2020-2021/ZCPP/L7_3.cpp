#include <fstream>
#include <iostream>
#include <sstream> 
#include <random>
#include <map>

using namespace std;


class customDistribution {
public:
	map<char, int> dic;
	int size = 0;

	customDistribution(map<char, int> adic) : dic(adic) {
		int aux = 0;
		for (auto &element : dic) {
			size += element.second;
			element.second += aux;
			aux = element.second;
		}
	};

	char getLetter(double seed) {
        char result;
		int roll = (int)(seed * size);
		for (auto element : dic) {
			if (roll <= element.second) {
				result = element.first;
                break;
			}
		}
        return tolower(result);
	}
};


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

	map<char, int> dictionary = {
		{'E',  21912 },
		{'T',  16587 },
		{ 'A', 14810 },
		{ 'O', 14003 },
		{ 'I', 13318 },
		{ 'N', 12666 },
		{ 'S', 11450 },
		{ 'R', 10977 },
		{ 'H', 10795 },
		{ 'D', 7874  },
		{ 'L', 7253  },
		{ 'U', 5246  },
		{ 'C', 4943  },
		{ 'M', 4761  },
		{ 'F', 4200  },
		{ 'Y', 3853  },
		{ 'W', 3819  },
		{ 'G', 3693  },
		{ 'P', 3316  },
		{ 'B', 2715  },
		{ 'V', 2019  },
		{ 'K', 1257  },
		{ 'X', 315   },
		{ 'Q', 205   },
		{ 'J', 188   },
		{ 'Z', 128   }
	};

	random_device rdev;
	mt19937 gen(rdev());

	binomial_distribution<int> bd(11, 0.5);
	uniform_real_distribution<double> ud(0, 1);
	customDistribution cd(dictionary);


	ofstream ofs(filename, ios::out);

	for (int i = 0; i < len; i++) {
		int word_len = bd(gen) + 1;
		string word = "";
		for (int j = 0; j < word_len; j++) {
			word.push_back(cd.getLetter(ud(gen)));
		}
		ofs << word << " ";
		cout << word << "\n";
	}

	ofs.close();

	return 0;
}