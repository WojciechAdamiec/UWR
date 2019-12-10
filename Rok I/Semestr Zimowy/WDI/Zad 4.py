from wdi import*


def binary(n):
    m = n
    length = 0
    while n > 0:
        n = n // 2
        length = length + 1
    A = Array(length)
    i = 0
    while m > 0:
        A[i] = m % 2
        m = m // 2
        i = i + 1
    return A


def palindrom(n):
    for i in range(len(n)//2):
        if n[i] != n[len(n) - 1 - i]:
            return False
    return True


def binary_palindrom(n):
    a = binary(n)
    if palindrom(a):
        return True
    return False


print(binary_palindrom(129))
