#include <iostream>
#include <type_traits>

using namespace std;

template <typename T, typename U>
bool moveObject(T &a, U &b) {
    if constexpr(is_pointer<T>()) {
        if constexpr(!is_convertible<decltype(*a), U>()) {
            cerr << "Wskaźnik do typu " << typeid(*a).name()
                 << " niekonwertowalny do " << typeid(b).name() << '\n';
            return false;
        } else {
            b = move(*a);
            return true;
        }
    } 
    
    else {
        if constexpr(!is_convertible<T, U>()) {
            cerr << "Typ " << typeid(a).name() << " niekonwertowalny do "
                 << typeid(b).name() << '\n';
            return false;
        } else {
            b = move(a);
            return true;
        }
    }
}

class A {};
class B {};

int main() {
    int *a = new int(7);
    int b = 0;
    moveObject(a, b);
    cout << "a: " << *a << "\nb: " << b << "\n\n";

    int c = 21;
    int d = 0;
    moveObject(c, d);
    cout << "c: " << c << "\nd: " << d << "\n\n";

    float *x = new float(2010.7);
    int y = 0;
    moveObject(x, y);
    cout << "x: " << *x << "\ny: " << y << "\n\n";

    B e;
    A f;
    moveObject(e, f);
    cout << '\n';

    B *g = new B;
    A h;
    moveObject(g, h);
    cout << '\n';

    return 0;
}
