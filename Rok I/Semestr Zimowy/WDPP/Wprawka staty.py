from random import randint
from turtle import*

speed = 'fastest'
stats = {}
for i in range(10):
    stats[i] = 0
for e in range(1000000):
    m = randint(1, 1000)
    x = randint(1, m)
    a = str(x)
    for w in a:
        h = int(w)
        stats[h] = stats[h] + 1
print(stats)

for i in range(10):
    pu()
    goto(-300 + 50 * i, - 200)
    pd()
    for j in range(2):
        fd(30)
        lt(90)
        fd(stats[i] // 1000)
        lt(90)

update()
input()