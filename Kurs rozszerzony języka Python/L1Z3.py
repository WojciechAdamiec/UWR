print("Python Zaawansowany: Lista 1; Zadanie 3")
print()


def romb(n):
    for i in range(n + 1):
        print(' ' * (n - i), (2 * i - 1) * 'X', ' ' * (n - i))
    for i in range(n - 1):
        print(' ' * (i + 1), (2 * (n - i) - 3) * 'X', ' ' * (i + 1))


romb(7)

