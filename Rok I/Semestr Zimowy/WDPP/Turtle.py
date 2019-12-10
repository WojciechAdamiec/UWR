import random
from turtle import*
speed = "fastest"


def draw():
    pu()
    goto(-350, 0)
    pd()
    for i in range(30):
        rectangle(5*i + random.randint(0, 50))
        pu()
        forward(15)
        pd()


def rectangle(n):
    for i in range(2):
        forward(10)
        lt(90)
        forward(n)
        lt(90)


draw()
a = int(input("Heh: "))
