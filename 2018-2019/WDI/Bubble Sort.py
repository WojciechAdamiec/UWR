import random

t = list(range(100))
random.shuffle(t)
print(t)


def bubblesort():
    again = True
    while again:
        again = False
        for i in range(len(t) - 1):
            if t[i] > t[i + 1]:
                t[i], t[i + 1] = t[i + 1], t[i]
                again = True

#1. Wykona tylko N-1 porównań
#2. Wykona N*N porównań i N(N+1) zamian

bubblesort()
print(t)
