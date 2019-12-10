from wdi import*


def nwd(n, m):
    if n < m:
        k = m
        m = n
        n = k
    while m > 0:
        n = n % m
        k = n
        n = m
        m = k
    return n


def nwd_long(n, a):
    rez = 0
    for i in range(n):
        rez = nwd(rez, a[i])
    return rez


N = 3
A = Array(N)
A[0] = 2*3*4*5*17
A[1] = 2*3*4*5*7
A[2] = 2*3*5*13

print(nwd_long(3, A))
