def nwd(n, m):
    if n < m:
        k = m
        m = n
        n = k
    while m != 0:
        k = n % m
        n = m
        m = k
    return n


def nww(n, m):
    return n*m/nwd(n, m)


def nieskracalne(a, b):
    c = nwd(a, b)
    if c == 1:
        return a, b
    a = a / c
    b = b / c
    return a, b


def test(a, b):
    wynik = a * b
    while b != 0:
        t = b
        b = a % b
        a = t
    return wynik//a


def nwd_lepszy(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


print(nwd_lepszy(12, 16))
