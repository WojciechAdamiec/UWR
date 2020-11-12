#include <iostream>
#include <string>
#include <vector>

std::string bin2rom(int x) {
	const std::vector<std::pair<int, std::string>> rome = {
		{1000, "M"},
		{900, "CM"}, {500, "D"}, {400, "CD"}, {100, "C"},
		{90, "XC"}, {50, "L"}, {40, "XL"}, {10, "X"},
		{9, "IX"}, {5, "V"}, {4, "IV"}, {1, "I"}
	};
	std::string result = "";
	int i = 0;
	while (x > 0) {
		while (i < rome.size() - 1 && rome[i].first > x)
			i++;

		result += rome[i].second;
		x -= rome[i].first;
	}
	return result;
}

int main(int argc, char **argv) {
	int n;
	for (int i = 1; i < argc; i++) {
		try {
			n = std::stoi(argv[i]);
			if (n < 1 || n > 3999)
				throw std::logic_error("Out of range");

			std::cout << bin2rom(n) << "\n";
		}
		catch (const std::exception &E) {
			std::clog << "Wrong argument number: " << i << ": " << argv[i]
				<< " : " << E.what() << "\n";
		}
	}
	return 0;
}