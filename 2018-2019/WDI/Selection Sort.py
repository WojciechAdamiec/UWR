import random

t = list(range(100))
random.shuffle(t)
print(t)


def minimum(n):
    mini = n
    for i in range(n, 100):
        if t[i] < t[mini]:
            mini = i
    return mini
# Ilość porównań jest zawsze N(N+1)//2
# Ilość przestawien N


def selectionsort():
    for i in range(100):
        x = minimum(i)
        t[i], t[x] = t[x], t[i]


def selectionsort2(L):
    for i in range(len(L)):
        mini = i
        for j in range(i, len(L)):
            if L[j] < L[mini]:
                mini = j
        t[i], t[mini] = t[mini], t[i]



selectionsort()
print(t)
