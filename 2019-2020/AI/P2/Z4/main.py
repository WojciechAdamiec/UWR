import numpy as np
from random import choice
import queue as qq
from collections import defaultdict

lines = []
line = []

for x in open('zad_input.txt'):
    line = x.strip()
    lines.append(line)


X_SIZE, Y_SIZE = len(line), len(lines)
field = np.zeros((X_SIZE, Y_SIZE), dtype='str')
direction = {(0, 1): 'D',
             (1, 0): 'R',
             (-1, 0): 'L',
             (0, -1): 'U'}

rev_direction = {'D': (0, 1),
                 'R': (1, 0),
                 'L': (-1, 0),
                 'U': (0, -1)}
opp = {'U': 'D',
       'L': 'R',
       'R': 'L',
       'D': 'U'}

adjacent = [(0, 1), (1, 0), (-1, 0), (0, -1)]
goals = []
commandos = []
starting_state = ()
outcome = ''
phase = 0


def init():
    global starting_state
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            field[i][j] = lines[j][i]
    for j in range(Y_SIZE):
        for i in range(X_SIZE):
            if field[i][j] == 'S' or field[i][j] == 'B':
                commandos.append((i, j))
            if field[i][j] == 'G' or field[i][j] == 'B':
                goals.append((i, j))
    for j in range(Y_SIZE):
        for i in range(X_SIZE):
            if field[i][j] == 'S':
                field[i][j] = ' '
            elif field[i][j] == 'B':
                field[i][j] = 'G'
    starting_state = tuple(commandos)


def info(state):
    battle = np.copy(field)
    for commando in state:
        if battle[commando[0]][commando[1]] == 'G':
            battle[commando[0]][commando[1]] = 'B'
        else:
            battle[commando[0]][commando[1]] = 'S'
    for j in range(Y_SIZE):
        for i in range(X_SIZE):
            print(battle[i][j], end='')
        print()
    print()
    print('=============================')
    print()


def is_ok(state):
    for com in state:
        if com not in goals:
            return False
    return True


def move(state, step, track=False):
    global outcome
    if track:
        outcome += direction[step]
    global field
    commando = set()
    for com in state:
        if field[com[0] + step[0]][com[1] + step[1]] != '#':
            if (com[0] + step[0], com[1] + step[1]) not in commando:
                commando.add((com[0] + step[0], com[1] + step[1]))
        else:
            if (com[0], com[1]) not in commando:
                commando.add((com[0], com[1]))
    return tuple(commando)


def work():
    global starting_state, counter, current, outcome
    current = starting_state
    counter = 0

    def phase_1():
        global starting_state, current, counter, outcome

        for i in range(max(X_SIZE, Y_SIZE) - 5):
            if counter > 112:
                return
            counter += 1
            current = move(current, (-1, 0), True)

            counter += 1
            current = move(current, (0, -1), True)

        if len(current) <= 3:
            return

        for i in range(max(X_SIZE, Y_SIZE) - 2):
            if counter > 112:
                return
            counter += 1
            current = move(current, (-1, 0), True)

            counter += 1
            current = move(current, (0, 1), True)

        if len(current) <= 3:
            return

        for i in range(max(X_SIZE, Y_SIZE) - 2):
            if counter > 112:
                return
            counter += 1
            current = move(current, (1, 0), True)

            counter += 1
            current = move(current, (0, 1), True)

        if len(current) <= 3:
            return

        for i in range(max(X_SIZE, Y_SIZE) - 2):
            if counter > 112:
                return
            counter += 1
            current = move(current, (1, 0), True)

            counter += 1
            current = move(current, (0, -1), True)

    def phase_2():
        global current, outcome, phase
        current = tuple(sorted(list(current)))
        start = current
        visited = set()
        history = {}
        queue = qq.Queue()
        queue.put(current)
        visited.add(current)
        while not queue.empty():
            v = queue.get()
            if is_ok(v):
                current = v
                break
            for adj in adjacent:
                moved = tuple(sorted(list(move(v, adj))))
                if moved not in visited:
                    visited.add(moved)
                    queue.put(moved)
                    history[moved] = (v, direction[adj])
        if queue.empty():
            print('QUEUE EMPTY!')
        bfs_string = ''
        while current != start:
            bfs_string += history[current][1]
            current = history[current][0]
        bfs_string = bfs_string[len(bfs_string)::-1]
        phase = len(outcome)
        outcome = outcome + bfs_string

    phase_1()
    phase_2()


init()
work()
'''
ver = starting_state
info(ver)
inc = 0
for t in outcome:
    inc += 1
    ver = move(ver, rev_direction[t])
    print('Phase: ', phase, 'Num: ', inc)
    info(ver)
'''
file = open('zad_output.txt', 'w+')
file.write(outcome)
