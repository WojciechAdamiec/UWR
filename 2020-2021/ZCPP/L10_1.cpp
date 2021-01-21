#include <iomanip>
#include <iostream>
#include <iterator>
#include <sstream>
#include <vector>
#include <math.h>

int main() {
    std::string input;
    std::getline(std::cin, input);

    std::istringstream iss(input);

    std::vector<double> vec(std::istream_iterator<double>(iss), {});

    std::cout << std::fixed << std::setprecision(3);

    double mean = 0.0;
    double sd = 0.0;
    
    for(auto i : vec){
        mean += i;
    }
    mean = mean / vec.size();

    for(auto i : vec){
        sd += (i - mean) * (i - mean);
    }
    sd = sqrt(sd / vec.size());

    std::cout << "mean:               " << mean << '\n';
    std::cout << "standard deviation: " << sd << '\n';

    return 0;
}
