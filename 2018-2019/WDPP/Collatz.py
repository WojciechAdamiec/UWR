from statistics import median


def F(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


def energy(a):
    i = 0
    while True:
        if a == 1:
            return i
        else:
            a = F(a)
        i = i + 1


def analiza(a, b):
    L = []
    for i in range(a, b + 1):
        L.append(energy(i))
    print("Średnia wynosi: " + str(sum(L) / len(L)))
    print("Mediana wynosi: " + str(median(L)))
    print("Maxymalna energia: " + str(max(L)))
    print("Minimalna energia: " + str(min(L)))


analiza(120, 173)
