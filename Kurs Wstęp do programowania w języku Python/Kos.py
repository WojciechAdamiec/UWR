def T(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return T(n//2) + 1
    return T((n + 1)//2) + 1


for i in range(1, 100):
    print(T(i))
