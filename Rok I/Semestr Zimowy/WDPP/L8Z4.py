from random import randint
from turtle import*
grid = [[0 for i in range(100)]for j in range(100)]
pixel = 6
tracer(0, 1)


def kwadrat(x, y, colour):
    pu()
    goto(x * pixel - 300, 300 - y * pixel)
    pd()
    color(colour)
    begin_fill()
    for i in range(4):
        fd(pixel)
        rt(90)
    end_fill()
    pu()


def somsiad(x, y):
    wynik = []
    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= 99 and 0 <= ny <= 99:
            wynik.append((nx, ny))
    return wynik


for i in range(20):
    x, y = randint(0, 99), randint(0, 99)
    grid[x][y] = 1100
average = 0
for i in range(100000):
    x, y = (randint(0, 99), randint(0, 99))
    a = somsiad(x, y)
    for e in a:
        print(e)
        average = average + grid[e[0]][e[1]]
    print(average)
    average = average / (len(a))
    grid[x][y] = average


def szkaluj(i, j):
    a = grid[i][j]
    if a < 40:
        return 'green'
    elif a < 60:
        return 'yellow'
    elif a < 100:
        return 'orange'
    else:
        return 'red'


for j in range(100):
    for i in range(100):
        kwadrat(i, j, szkaluj(i, j))

print(grid)
update()
input()
