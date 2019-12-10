from turtle import*
import math
import random
speed = 'fastest'
tracer(0, 1)
r = False


def square(pos, colour):
    pu()
    goto(grid*pos[0] - 200, -grid*pos[1] + 200)
    pd()
    begin_fill()
    color('black', colour)
    for i in range(4):
        fd(grid)
        rt(90)
    end_fill()
    A[pos[0]][pos[1]] = (True, colour)
    pu()


def zero(loc, colour):
    global r
    if any(A[loc[0] + i - 2][loc[1] - 6 + j][1] == colour for i in range(1, 8) for j in range(1, 8)):
        r = True
        return
    if A[loc[0] + 1][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 3][0]:
        r = True
        return
    if A[loc[0] + 4][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0] + 4][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 4][loc[1] - 3][0]:
        r = True
        return
    print(loc, colour)
    pu()
    square((loc[0] + 1, loc[1]), colour)
    square((loc[0] + 2, loc[1]), colour)
    square((loc[0] + 3, loc[1]), colour)
    square((loc[0] + 1, loc[1] - 4), colour)
    square((loc[0] + 2, loc[1] - 4), colour)
    square((loc[0] + 3, loc[1] - 4), colour)
    square((loc[0], loc[1] - 1), colour)
    square((loc[0], loc[1] - 2), colour)
    square((loc[0], loc[1] - 3), colour)
    square((loc[0] + 4, loc[1] - 1), colour)
    square((loc[0] + 4, loc[1] - 2), colour)
    square((loc[0] + 4, loc[1] - 3), colour)
    for i in range(1, 4):
        for j in range(1, 4):
            A[loc[0] + i][loc[1] - 4 + j] = (True, 'white')
    update()


def one(loc, colour):
    global r
    if any(A[loc[0] + i - 2][loc[1] - 6 + j][1] == colour for i in range(1, 8) for j in range(1, 8)):
        r = True
        return
    if A[loc[0]][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 3][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 3][0]:
        r = True
        return
    print(loc, colour)
    pu()
    square((loc[0], loc[1]), colour)
    square((loc[0] + 1, loc[1]), colour)
    square((loc[0] + 2, loc[1]), colour)
    square((loc[0] + 1, loc[1] - 1), colour)
    square((loc[0] + 1, loc[1] - 2), colour)
    square((loc[0] + 1, loc[1] - 3), colour)
    square((loc[0] + 1, loc[1] - 4), colour)
    square((loc[0], loc[1] - 3), colour)
    update()


def six(loc, colour):
    global r
    if any(A[loc[0] + i - 2][loc[1] - 6 + j][1] == colour for i in range(1, 8) for j in range(1, 8)):
        r = True
        return
    if A[loc[0] + 1][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 3][0]:
        r = True
        return
    if A[loc[0] + 4][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1] - 2][0]:
        r = True
        return
    print(loc, colour)
    pu()
    square((loc[0] + 1, loc[1]), colour)
    square((loc[0] + 2, loc[1]), colour)
    square((loc[0] + 3, loc[1]), colour)
    square((loc[0] + 1, loc[1] - 4), colour)
    square((loc[0] + 2, loc[1] - 4), colour)
    square((loc[0] + 3, loc[1] - 4), colour)
    square((loc[0], loc[1] - 1), colour)
    square((loc[0], loc[1] - 2), colour)
    square((loc[0], loc[1] - 3), colour)
    square((loc[0] + 4, loc[1] - 1), colour)
    square((loc[0] + 3, loc[1] - 2), colour)
    square((loc[0] + 2, loc[1] - 2), colour)
    square((loc[0] + 1, loc[1] - 2), colour)
    for i in range(1, 4):
        for j in range(1, 4):
            A[loc[0] + i][loc[1] - 4 + j] = (True, 'white')
    update()


def eight(loc, colour):
    global r
    if any(A[loc[0] + i - 2][loc[1] - 6 + j][1] == colour for i in range(1, 8) for j in range(1, 8)):
        r = True
        return
    if A[loc[0] + 1][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1]][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1] - 4][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0]][loc[1] - 3][0]:
        r = True
        return
    if A[loc[0] + 4][loc[1] - 1][0]:
        r = True
        return
    if A[loc[0] + 1][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 2][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 3][loc[1] - 2][0]:
        r = True
        return
    if A[loc[0] + 4][loc[1] - 3][0]:
        r = True
        return
    print(loc, colour)
    pu()
    square((loc[0] + 1, loc[1]), colour)
    square((loc[0] + 2, loc[1]), colour)
    square((loc[0] + 3, loc[1]), colour)
    square((loc[0] + 1, loc[1] - 4), colour)
    square((loc[0] + 2, loc[1] - 4), colour)
    square((loc[0] + 3, loc[1] - 4), colour)
    square((loc[0], loc[1] - 1), colour)
    square((loc[0], loc[1] - 3), colour)
    square((loc[0] + 4, loc[1] - 1), colour)
    square((loc[0] + 4, loc[1] - 3), colour)
    square((loc[0] + 1, loc[1] - 2), colour)
    square((loc[0] + 2, loc[1] - 2), colour)
    square((loc[0] + 3, loc[1] - 2), colour)
    for i in range(1, 4):
        for j in range(1, 4):
            A[loc[0] + i][loc[1] - 4 + j] = (True, 'white')
    update()


def numbers():
    a = random.randint(0, 35)
    b = random.randint(0, 35)
    c = random.choice(['blue', 'yellow', 'grey', 'red', 'green'])
    return (a, b), c


size = 45
grid = 10
A = [[(False, 'white') for i in range(size)] for j in range(size)]

pu()
i = 1

while i <= 40:
    info = numbers()
    x = random.randint(0, 3)
    if x == 0:
        zero((info[0][0], info[0][1]), info[1])
    elif x == 1:
        one((info[0][0], info[0][1]), info[1])
    elif x == 2:
        six((info[0][0], info[0][1]), info[1])
    else:
        eight((info[0][0], info[0][1]), info[1])
    if not r:
        i = i + 1
    else:
        r = False


update()
print('koniec')
x = input()

"""
Nie ma wszystkich cyfr, ale to tylko mechaniczna czynność, żeby je dopisać"
"""
