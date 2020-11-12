#include <iostream>
#include <limits>
#include <ratio>

using namespace std;

template <int N>
class harm : public std::ratio_add<std::ratio<1, N>, harm<N - 1>> {};

template <>
class harm<1> : public std::ratio<1, 1> {};

int main() {
    
    using har1 = harm<1>;
    using har2 = harm<2>;
    using har3 = harm<3>;
    using har4 = harm<4>;
    using har10 = harm<10>;
    using har40 = harm<40>;
    using har46 = harm<46>;

    cout << "har1: " << har1::num << "/" << har1::den << '\n';
    cout << "har2: " << har2::num << "/" << har2::den << '\n';
    cout << "har3: " << har3::num << "/" << har3::den << '\n';
    cout << "har4: " << har4::num << "/" << har4::den << '\n';

    cout << "har10: " << har10::num << "/" << har10::den << '\n';
    cout << "har40: " << har40::num << "/" << har40::den << '\n';
    cout << "har46: " << har46::num << "/" << har46::den << '\n';
    cout << "\nhar46 to ostatnia możliwa liczba harmoniczna!";

    return 0;
}
