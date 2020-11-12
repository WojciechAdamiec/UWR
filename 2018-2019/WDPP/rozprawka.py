def tower(n):
    for i in range(1, n + 1):
        for j in range(3):
            print((n-i)*" " + (2*i-1)*"#" + (n-i)*" ")


tower(5)

print()


def towers(L):
    w = max(L)
    for i in range(1, w + 1):
        for j in range(3):
            for x in range(len(L)):
                if i <= w - L[x]:
                    print((2*L[x])*" ", sep="", end="")
                else:
                    f = L[x] + i - w
                    if f < 0:
                        f = 0
                    print((L[x] - f)*" " + (2*f - 1)*"#" + (L[x] - f + 1)*" ", sep="", end="")
            print()


towers([4, 7, 2, 1, 3, 3, 2, 4])
