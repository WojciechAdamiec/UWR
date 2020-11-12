#A


def sumy(L):
    if len(L) == 1:
        return set(L)
    for e in list(L):




print(sumy([1, 2, 3, 4, 5]))






"""
def sumy(L):
    if len(L) == 0:
        yield []
    for i in range(len(L)):
        A = L[:i] + L[i + 1:]
        print(A)
        yield [sum(L)]
        yield sumy(A)
"""
"""
for e in sumy([1,2,3]):
    print(e)
"""
#B


def podciagi(n, a, b):
    L = list(range(a, b + 1))
    if n == 0:
        yield []
        return
    for y in podciagi(n - 1, a, b):
        yield y
        for x in L:
            yield [x] + y


def zadanie(a, b):
    wynik = []
    for c in (podciagi(b - a, a, b)):
        if c not in wynik and all(c[x + 1] >= c[x] for x in range(len(c) - 1)):
            wynik.append(c)
    return wynik

"""
Z = zadanie(3, 7)
for e in Z:
    print(e)
"""