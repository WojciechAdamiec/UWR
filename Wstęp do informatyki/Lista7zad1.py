from turtle import*
tracer(0, 1)

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


for x in open('dane.txt'):
    Lista.append(x.split())
for i in range(len(Lista)):
    for j in range(len(Lista[0])):
        kwadrat(i, j, eval(Lista[i][j]))


update()
input()
