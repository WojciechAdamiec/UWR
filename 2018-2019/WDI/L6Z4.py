"""
Wartość liczby o zapisie binarnym a[0] ... a[k] jest równa
wartości wielomianu w punkcie 2, takiego że
kolejne współczynniki tego wielomianu odpowiadają 0 i 1
w zapisie binarnym tej liczby.


Przykład:
10(2) = 1010(10)

Odpowiada:

W(x) = 1 * x^3 + 0 * x^2 + 1 * x^1 + 0 * x^0
w punkcie x = 2
"""


def wartosc(a, k):
    w = 0
    for i in range(k + 1):
        w = (a[i]) + w * 2
    return w


a = [1, 0, 0, 1, 0, 1]
k = len(a) - 1

print(wartosc(a, k))
