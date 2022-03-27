from math import gcd


def skroc(u):
    if u[1] < 0:
        u[1] = -1 * u[1]
        u[0] = -1 * u[0]
    x = gcd(u[0], u[1])
    if x != 1:
        u[0] = u[0] // x
        u[1] = u[1] // x
    return [u[0], u[1]]


def utworz():
    print('Podaj licznik: ', end='')
    a = int(input())
    print('Podaj mianownik: ', end='')
    b = int(input())
    if b == 0:
        return 'Error, division with 0'
    return skroc([a, b])


def dodawanie(u1, u2):
    return skroc([u1[0] * u2[1] + u1[1] * u2[0], u1[1] * u2[1]])


def mnozenie(u1, u2):
    return skroc([u1[0] * u2[0], u1[1] * u2[1]])


def odejmowanie(u1, u2):
    u3 = [-1 * u2[0], u2[1]]
    return dodawanie(u1, u3)


def dzielenie(u1, u2):
    u3 = [u2[1], u2[0]]
    return mnozenie(u1, u3)


def dodaj(u1, u2):
    x = dodawanie(u1, u2)
    u1[0] = x[0]
    u1[1] = x[1]


def odejmij(u1, u2):
    x = odejmowanie(u1, u2)
    u1[0] = x[0]
    u1[1] = x[1]


def pomnoz(u1, u2):
    x = mnozenie(u1, u2)
    u1[0] = x[0]
    u1[1] = x[1]


def podziel(u1, u2):
    x = dzielenie(u1, u2)
    u1[0] = x[0]
    u1[1] = x[1]

