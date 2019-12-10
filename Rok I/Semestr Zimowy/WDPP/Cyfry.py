from duze_cyfry import*
import random
from turtle import*
colors = ['blue', 'red', 'magenta', 'green', 'yellow', 'brown', 'grey']
tracer(0, 1)


def draw(n):
    n = str(n)
    c = []
    for e in range(len(n)):
        c.append(random.choice(colors))
    for i in range(5):
        pu()
        goto(-300, 50 - i * 10)
        for j in range(len(n)):
            color = c[j]
            w = int(n[j])
            f = list(daj_cyfre(w)[i])
            print(f)
            for k in range(len(f)):
                if f[k] == '#':
                    print('kwadrat')
                    rectangle(color)
                fd(10)
            fd(10)


def rectangle(color):
    pd()
    fillcolor(color)
    begin_fill()
    for i in range(4):
        fd(10)
        lt(90)
    end_fill()
    pu()


draw(1234567855)
update()
input()
