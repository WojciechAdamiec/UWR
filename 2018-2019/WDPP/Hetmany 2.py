from wdi import*


def init(n):
    for i in range(n):
        b[i] = -1


def isf(x, y):
    for i in range(x):
        if b[i] - i == y - x or b[i] + i == x + y or b[i] == y:
            return 0
    return 1


def draw(n):
    print()
    for i in range(n):
        print(b[i])
    print()
    for i in range(n):
        for j in range(n):
            if b[j] == i:
                print('x', sep='', end='')
            else:
                print('o', sep='', end='')
        print()


def hetmany(n):
    b[0] = 0
    k = 1
    while k < n and k >= 0:
        b[k] = b[k] + 1
        while b[k] < n and not isf(k, b[k]):
            b[k] = b[k] + 1
        if b[k] < n:
            k = k + 1
        else:
            b[k] = -1
            k = k - 1
    if k == n:
        draw(n)
    else:
        print('brak rozwiazania')


b = Array(10)
init(10)
hetmany(10)

