#include <algorithm>
#include <fstream>
#include <iostream>
#include <iterator>
#include <vector>
#include <numeric>

int totient(int n) {
    int count = 0;
    for(int i = 1; i <= n; i++) {
        if(std::gcd(i, n) == 1)
            count++;
    }
    return count;
}

int main() {
    int k;
    std::cin >> k;

    std::vector<int> totients;
    for(int i = 1; i <= k; i++)
        totients.push_back(totient(i));


    std::ofstream of("phi.txt");
    std::ostream_iterator<int> osit(of, "; ");

    std::copy(totients.begin(), totients.end(), osit);

    return 0;
}
