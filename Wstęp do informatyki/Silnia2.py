def silnia(n):
    i = 2
    while n != 0:
        print(n % i)
        n = n // i
        i = i + 1


silnia(100)
