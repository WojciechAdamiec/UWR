from wdi import*
import math


def sito(n):
    L = Array(n)
    for i in range(2, n):
        L[i] = i
    L[0] = 0
    L[1] = 0
    for j in range(2, int(math.sqrt(n)) + 1):
        if j is not 0:
            for k in range(2, n // 2):
                if j * k < n:
                    L[j * k] = 0
    for i in range(n):
        if L[i] is not 0:
            L[i] = 1


sito(100)
