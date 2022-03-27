#include <iostream>
#include <chrono>
#include <random>

using namespace std;

random_device rd;
mt19937 gen(rd());
uniform_real_distribution<double> dist(0.5, 2.0);

void fillMatrix(const int n, double **mat) {
    for(int i = 0; i < n; i++)
        for(int j = 0; j < n; j++)
            mat[i][j] = dist(gen);
}

void multiply(double **mat, double **res, const int N)
{
    int i, j, k;
    for (i = 0; i < N; i++) {
        for (j = 0; j < N; j++) {
            res[i][j] = 0;
            for (k = 0; k < N; k++)
                res[i][j] += mat[i][k] * mat[k][j];
        }
    }
}

void lap(const int N){
    double **a = new double *[N];
    for(int i = 0; i < N; i++)
        a[i] = new double[N];

    fillMatrix(N, a);

    double **b = new double *[N];
    for(int i = 0; i < N; i++)
        b[i] = new double[N];

    multiply(a, b, N);
}

double test(const int n, const int runs) {
    double sum = 0;
    for(int i = 0; i < runs; i++) {
        auto t1 = chrono::high_resolution_clock::now();
        lap(n);
        auto t2 = chrono::high_resolution_clock::now();
        auto d = chrono::duration_cast<chrono::microseconds>(t2 - t1).count();
        sum += d;
    }
    return sum / runs;
}

int main() {
    
    const int N1 = 100;
    const int N2 = 1000;
    const int N3 = 10000;

    cout << "Czas dla 10:   " << test(N1, 20) / 1000 << "ms \n";
    cout << "Czas dla 100:  " << test(N2, 2) / 1000 << "ms \n";
    cout << "Czas dla 1000: " << test(N3, 1) / 1000 << "ms \n";

    return 0;
}
