print("Python Zaawansowany: Lista 1; Zadanie 5")
print()


def rozkład(n):
    i = 2
    outcome = []
    while n > 1:
        if not n % i:
            if not outcome:
                outcome.append([i, 1])
            elif outcome[-1][0] == i:
                outcome[-1][1] = outcome[-1][1] + 1
            else:
                outcome.append([i, 1])
            n = n // i
        else:
            i = i + 1
        #print(f'n: {n} i: {i}')
    return outcome


print(rozkład(756))
