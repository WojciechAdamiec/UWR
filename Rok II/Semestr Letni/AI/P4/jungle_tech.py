start_down = """
..#1#..
...#...
.......
.~~.~~.
.~~.~~.
.~~.~~.
.......
...#...
..#2#..
"""

start_up = """
L.....T
.D...C.
R.J.W.E
.......
.......
.......
e.w.j.r
.c...d.
t.....l
"""


def base(player):
    return player


GRASS = 2
WATER = 3
TRAP = 3


# RAT
def rat(player):
    if player == 0:
        return 1
    if player == 1:
        return -1
    print('RAT ERROR')


# CAT
def cat(player):
    if player == 0:
        return 2
    if player == 1:
        return -2
    print('CAT ERROR')


# DOG
def dog(player):
    if player == 0:
        return 3
    if player == 1:
        return -3
    print('DOG ERROR')


# WOLF
def wolf(player):
    if player == 0:
        return 4
    if player == 1:
        return -4
    print('WOLF ERROR')


# PANTHER
def panther(player):
    if player == 0:
        return 5
    if player == 1:
        return -5
    print('PANTHER ERROR')


# TIGER
def tiger(player):
    if player == 0:
        return 6
    if player == 1:
        return -6
    print('TIGER ERROR')


# LION
def lion(player):
    if player == 0:
        return 7
    if player == 1:
        return -7
    print('LION ERROR')


# ELEPHANT
def elephant(player):
    if player == 0:
        return 8
    if player == 1:
        return -8
    print('ELEPHANT ERROR')