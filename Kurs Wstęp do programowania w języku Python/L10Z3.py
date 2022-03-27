from random import randint


def solve(zagadka):
    wynik = {}
    for e in zagadka:
        if e not in [' ', '=', '+']:
            wynik[e] = str(randint(1, 9))
        else:
            wynik[e] = e
    szyfr = ''.join([wynik[x] for x in zagadka])
    A = szyfr.split('=')
    a = eval(A[0])
    b = eval(A[1])
    print(a)
    print(b)
    if a == b:
        return wynik
    else:
        return solve(zagadka)


print(solve('DUPA + KIJ = MAMA'))
