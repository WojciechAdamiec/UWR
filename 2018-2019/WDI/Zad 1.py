def pierwsze_a(n):
    if n % 2: return n
    return -n


def pierwsze_b(n):
    wynik = 0
    for i in range(1, n + 1):
        if i % 2:
            wynik = wynik + 1/i
        else:
            wynik = wynik - 1/i
    return wynik


def pot(a, b):
    rez = 1
    while b > 0:
        if b % 2:
            rez = rez * a
        b = b // 2
        a = a * a
    return rez


"""
Aby uzyskać a^b wystarczy wymnożyć potęgi a odpowiadające
jedynkom w binarnej reprezentacji liczby b
"""


def pierwsze_c(n, x):
    wynik = 0
    for i in range(1, n + 1):
        wynik = wynik + i*pot(x, i)
    return wynik


def pierwsze_c_beta(n, x):
    wynik = 0
    pow = x
    for i in range(1, n + 1):
        wynik = wynik + i * pow
        pow = pow * x
    return wynik


def schemat_hornera(n, x):
    suma = 0
    i = n
    while i >= 1:
        suma = (suma + i) * x
        i = i - 1
    return suma


n = 7
x = 3

print(pierwsze_c(n, x))
print(pierwsze_c_beta(n, x))
print(schemat_hornera(n, x))
