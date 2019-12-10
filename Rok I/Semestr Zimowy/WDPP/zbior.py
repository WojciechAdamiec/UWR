import math


def zbior(n):
    L = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0 and pierwsza(i):
            L.append(i)
    return set(L)


def pierwsza(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


print(zbior(2*3*5*7*11*2*8*9))
