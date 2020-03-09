#include <cstdio>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <string>
#include <stdexcept>
#include <limits.h>
#include <vector>

bool prime(int64_t number);
int64_t convert(std::string word);
std::vector<int64_t> decay(int64_t number);

int main(int argc, char *argv[]){
    
    if (argc == 1)
        std::cerr << "Give a serie of numbers as argument! \n";
    
    std::vector<std::string> all_args;
    if (argc > 1)
        all_args.assign(argv + 1, argv + argc);
    auto print = [](const int64_t& n) {std::cout << " * " << n;};
    for (auto s : all_args){
        int64_t number = convert(s);
        std::vector<int64_t> vec = decay(number);
        std::cout << number << " = ";
        std::cout << vec[0];
        std::for_each(++vec.begin(), vec.end(), print);
        std::cout << "\n";
    }
}
 
bool prime(int64_t number){
    for (int64_t i=2; i <= floor(sqrt(number)); i++)
        if (number % i == 0)
            return false;
    return true;
}

int64_t convert(std::string word){
    int64_t result = 0;
    bool negative = false;
    int64_t aux = 1;
    if (word[0] == 45){
        negative = true;
        word = word.substr(1);
    }
        
    for (int64_t i = word.length() - 1; i >= 0; i--){
        result = result + aux * (word[i] - 48);
        aux = aux * 10;
    }
    if (result < 0)
        throw std::invalid_argument("");
    if (negative)
        result = - result;
    return result;
}

std::vector<int64_t> decay(int64_t number){
    std::vector<int64_t> result;
    int64_t i = 2;
    if (number == -1){
        result.push_back(-1);
        return result;
    }
    if (number == 1){
        result.push_back(1);
        return result;
    }
    if (number == 0){
        result.push_back(0);
        return result;
    }
    if (number < 0){
        result.push_back(-1);
        number = -number;
    }
    while (number > 1){
        if (prime(i) && number % i == 0){
            result.push_back(i);
            number = number / i;
        }
        else
            i++;
    }
    return result;
}
