from math import sqrt


def lista(n):
    lista_skladana = [x for x in range(2, n + 1) if all([x % i != 0 for i in range(2, int(sqrt(x)) + 1)])]
    return lista_skladana


print(lista(100))
