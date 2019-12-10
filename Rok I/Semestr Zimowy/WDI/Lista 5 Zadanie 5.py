def fTrec(n, m):
    if n == 0:
        return m
    if m == 0:
        return n
    else:
        return fTrec(n - 1, m) + 2*fTrec(n, m - 1)


print(fTrec(3, 4))
