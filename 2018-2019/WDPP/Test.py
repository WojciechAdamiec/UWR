from turtle import*
import random

tracer(0, 1)

pu()
goto(- 300, 0)
pd()

kolory = ['red', 'green', 'blue', 'magenta', 'yellow', 'brown']
for i in range(6):
    fillcolor(random.choice(kolory))
    begin_fill()
    fd(100)
    lt(90)
    fd(100)
    lt(90)
    for i in range(4):
        fd(25)
        lt(90)
        fd(25)
        rt(90)
    end_fill()
    bk(100)
    lt(180)


update()
input()
