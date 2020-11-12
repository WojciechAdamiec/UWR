from turtle import*
import random
speed = 'fastest'
tile = 10


def kwadrat(x, y, colour):
    pu()
    goto(x * tile - 300, -y * tile + 300)
    pd()
    color(colour[0] / 255, colour[1] / 255, colour[2] / 255)
    begin_fill()
    for i in range(4):
        fd(tile)
        rt(90)
    end_fill()
    pu()


Lista = []
Lista2 = []

for x in open('dane.txt'):
    Lista.append(x.split())


for i in range(len(Lista)):
    for j in range(len(Lista[0])):
        Lista2.append([i, j, eval(Lista[i][j])])


for x in range(len(Lista) * len(Lista[0])):
    r = random.choice(Lista2)
    print(r)
    kwadrat(r[0], r[1], r[2])
    Lista2.remove(r)



update()
input()
