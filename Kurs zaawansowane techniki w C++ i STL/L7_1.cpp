#include <algorithm>
#include <iostream>
#include <random>
#include <deque>

using namespace std;

// Fisher - Yates shuffle Algorithm
template <typename Collection>
void permutation(Collection &c) {
    random_device rdev;
    mt19937 gen(rdev());
    for(unsigned i = c.size() - 1; i >= 1; i--) {
        uniform_int_distribution<unsigned> dist(0, i);
        unsigned j = dist(gen);
        std::swap(c[j], c[i]);
    }
}

void tester2(){
    deque<int> test;
    test.push_back(1);
    test.push_back(2);
    test.push_back(3);
    permutation(test);
    for (auto i: test){
        cout << i << " ";
    }
    cout << "\n";
}

void tester1(){
    string text = "CMENTARZ";
    
    permutation(text);
    cout << text << '\n';
}
int main() {
    
    for(int i = 0; i < 10; i++){
        tester1();
    }

    for(int i = 0; i < 10; i++){
        tester2();
    }

    return 0;
}