from wdi import*


def ilo_cyfrowa(n):
    A = Array(10)
    a = str(n)
    k = 0
    for i in range(len(a)):
        A[int(a[i])] = A[int(a[i])] + 1
    for i in range(10):
        if A[i] > 0:
            k = k + 1
    return k


print(ilo_cyfrowa(133))
