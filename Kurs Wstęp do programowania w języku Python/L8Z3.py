from collections import*
from copy import copy

L = []

for x in open('slowamale.txt', encoding="utf8"):
    L.append(x.strip())


def sklada(slowo, slownik):
    a = copy(slownik)
    for e in slowo:
        a[e] = a[e] - 1
        if a[e] < 0:
            return False
    return True


def zagadka(nazwisko):
    litery = defaultdict(lambda: 0)
    for i in nazwisko:
        if i is not " ":
            litery[i] = litery[i] + 1

    wynik = []
    for h in range(9, 12):
        A = []
        for e in L:
            if len(e) == h:
                if sklada(e, litery):
                    A.append(e)
        for w in A:
            b = copy(litery)
            for ww in w:
                b[ww] = b[ww] - 1
            for f in L:
                if len(f) == len(nazwisko) - h - 1:
                    if sklada(f, b):
                        wynik.append((w, f))
    return wynik


print(zagadka('wojciech adamiec'))














"""
def zawiera():



def zagadka(nazwisko):
    X = {}
    wynik = []
    for x in nazwisko:
        if x != " ":
            if X[x]:

    print(X)
    for i in L:
        g = list(i)
        if all(g) in X:
            wynik.append(i)
    print(wynik)



zagadka("aaaaabbbbbbeeeeeedddddddooooouuuuuu")
"""
