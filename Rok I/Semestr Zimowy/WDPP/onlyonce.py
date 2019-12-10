def take_second(elem):
    return elem[1]


def only_once(n):
    L = []
    for i in range(len(n)):
        L.append((n[i], i))
    L.sort()
    a = L[0][0]
    e = 1
    while e <= len(L) - 1:
        if L[e][0] == a:
            L.remove(L[e])
            e = e - 1
        a = L[e][0]
        e = e + 1
    L.sort(key=take_second)
    X = []
    for i in range(len(L)):
        X.append(L[i][0])
    return X


print(only_once([1, 3, 5, 6, 2, 4, 2, 9, 7, 1, 2, 2, 6]))
