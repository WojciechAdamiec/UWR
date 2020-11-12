from wdi import*


def zapis(n):
    wynik = 0
    tab = Array(10)
    while n > 0:
        tab[n % 10] += 1
        n = n // 10
    for i in range(10):
        if tab[i] != 0:
            wynik += 1
    return wynik


def osiem(n):
    a = n
    i = 0
    while a > 0:
        i = i + 1
        a = a // 10
    tab = Array(i)
    i = 0
    while n > 0:
        tab[i] = n % 10
        n = n // 10
        i = i + 1
    for j in range(len(tab) // 2):
        if tab[j] != tab[len(tab) - 1 - j]:
            return False
    return True
