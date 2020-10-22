#include <cmath>
#include <iostream>
#include <memory>
#include <random>

using namespace std;

const int N = 8;
const int M = 20;

random_device rd;
uniform_int_distribution<int> dist(0, 1);

class Prosta
{ 
    public: 
    uint64_t licznik;

    Prosta(){licznik = 1;}
    void info(){
        std::cout << "\n" << licznik;
    }
    void update(){licznik++;}
    virtual ~Prosta()
    {
        std::cerr << "Licznik zniszczony: " << licznik << "\n";
    }
};

void operate(unique_ptr<Prosta[]> cel, int i, int n = 1){
    if (i <= 0){
        return;
    }
    for (int x = 0; x < sizeof(cel); x++){
        if (dist(rd) != 0){
            cel[x].update();
        }
    }
    operate(move(cel), i - 1, n + 1);
}

int main() {
    unique_ptr<Prosta[]> test = make_unique<Prosta[]>(N);
    operate(move(test), M);
    /*
    for (int j = 0; j < N; j++){
        cout << j;
        test[j].info();
    }
    */
    return 0;
}