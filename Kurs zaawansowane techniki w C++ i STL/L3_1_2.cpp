#include <iostream>
#include <limits>
#include <bitset>

using namespace std;

int main() {
    cout << "|||||||||||||\n";
    cout << "Zadanie 1 \n";
    cout << "|||||||||||||\n\n";

    cout << "long long int:\n\n";
    
    long long a = numeric_limits<long long int>::min();
    bitset<64> aa(a);
    long long b = numeric_limits<long long int>::max();
    bitset<64> bb(b);
    cout << "\tMin: " << a << '\n';
    cout << "\tBinarnie: " << aa << '\n';
    cout << "\tMax: " << b << '\n';
    cout << "\tBinarnie: " << bb << '\n';

    cout << "\tBity: " << numeric_limits<long long int>::digits << '\n';
    cout << "\tCyfry dziesiętne: " << numeric_limits<long long int>::digits10 << "\n\n";
    
    cout << "|||||||||||||\n";
    cout << "Zadanie 2 \n";
    cout << "|||||||||||||\n\n";

    cout << "float:\n";
    cout << "\tMin dodatnia: " << numeric_limits<float>::min() << '\n';
    cout << "\tMax dodatnia: " << numeric_limits<float>::max() << '\n';
    cout << "\tEpsilon: " << numeric_limits<float>::epsilon() << '\n';

    cout << "double\n";
    cout << "\tMin dodatnia: " << numeric_limits<double>::min() << '\n';
    cout << "\tMax dodatnia: " << numeric_limits<double>::max() << '\n';
    cout << "\tEpsilon: " << numeric_limits<double>::epsilon() << "\n\n";

    return 0;
}
