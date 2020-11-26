#include <iostream>
#include <cmath>
#include <functional>
 
template <typename A, typename B, typename C>
std::function<C(A)> compose(std::function<C(B)> f, std::function<B(A)> g) {
    return [f, g](A x) { return f(g(x)); };
}

template <typename A, typename B, typename C>
std::function<void(A)> stepCompose(std::function<C(A)> f, std::function<B(A)> g) {
    return [f, g](A x) {f(x); g(x);};
}

int main() {
    std::function<double(double)> f = sin;
    std::function<double(double)> g = asin;

    std::function<double(double)> a = [] (double x) {return x * x;};
    std::function<double(double)> b = [] (double x) {return sqrt(x);};

    for (int i=0; i < 10; i += 1)
        std::cout << "sin: " << f(0.1 * i) << " compose: " << compose(f, g)(0.1 * i) << std::endl;

    for (int i=0; i < 10; i += 1)
        std::cout << "power: " << a(i) << " compose: " << compose(a, b)(i) << std::endl;

    std::function<double(double)> f1 = [] (double x) {double res = x * x; std::cout << "f1: " << res << "\n"; return res;};
    std::function<double(double)> f2 = [] (double x) {double res = sqrt(x); std::cout << "f2: " << res << "\n"; return res;};
    std::function<double(double)> f3 = [] (double x) {double res = x - 100; std::cout << "f3: " << res << "\n"; return res;};
    
    stepCompose(f1, stepCompose(f2, f3))(36.0);

    return 0;
}