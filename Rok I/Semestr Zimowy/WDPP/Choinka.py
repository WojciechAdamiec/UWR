from turtle import*
import math
speed = 'fastest'


def triangle(n, colour):
    color('black', (colour/16, 1 - colour/5, 0))
    begin_fill()
    for i in range(3):
        fd(n)
        lt(120)
    end_fill()


pu()
goto(0, -300)
pd()
for i in range(1, 6):
    triangle(40*(6 - i), i)
    pu()
    fd(20*(6 - i))
    lt(90)
    fd(20*(6 - i)*math.sqrt(3))
    rt(90)
    bk(20*(6 - i - 1))
    pd()


x = input()
