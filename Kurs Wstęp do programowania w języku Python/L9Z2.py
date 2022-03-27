from turtle import*
import random
tracer(0, 1)


def fractal(n):
    if n <= 0:
        return
    for i in range(n):
        color(random.choice(['red', 'black', 'blue', 'magenta']))
        fd(n)
        rt(360/n)
        bk(n)
    fd(- n // 2)
    return fractal(int(n * 2/3))


fractal(180)
update()
input()

