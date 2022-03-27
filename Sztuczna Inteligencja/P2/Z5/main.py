import numpy as np
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
archives = {}
goals = []
commandos = []
starting_state = ()
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


def move(state, step):
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


def preprocessing():
    global archives
    for goal in goals:
        visited = set()
        depth = 0
        queue = qq.Queue()
        queue.put((goal, depth))
        visited.add(goal)
        while not queue.empty():
            v, dep = queue.get()
            if v not in archives or archives[v] > dep:
                archives[v] = dep
            for adj in adjacent:
                moved = v[0] + adj[0], v[1] + adj[1]
                if field[moved[0]][moved[1]] != '#':
                    if moved not in visited:
                        visited.add(moved)
                        queue.put((moved, dep + 1))


def h(state):
    smalls = set()
    for com in state:
        smalls.add(archives[com])
    return max(smalls)


def work():
    global starting_state, current, end, archives
    preprocessing()
    current = starting_state

    queue = qq.PriorityQueue()
    history = {}
    visited = set()
    gScore = defaultdict(lambda: np.inf)
    gScore[current] = 0
    fScore = defaultdict(lambda: np.inf)
    fScore[current] = h(current)

    queue.put((fScore[current], current))
    end = None
    while not queue.empty():
        pack = queue.get()
        v = pack[1]
        if is_ok(v):
            end = v
            break
        visited.add(v)
        for adj in adjacent:
            new_v = move(v, adj)
            temp_Gscore = gScore[v] + 1
            if temp_Gscore < gScore[new_v]:
                history[new_v] = v, direction[adj]
                gScore[new_v] = temp_Gscore
                fScore[new_v] = gScore[new_v] + h(new_v)
                if new_v not in visited:
                    queue.put((fScore[new_v], new_v))

    path = ''
    while end != starting_state:
        path += history[end][1]
        end = history[end][0]

    return path[len(path)::-1]


init()
outcome = work()

'''
ver = starting_state
info(ver)
inc = 0
for t in outcome:
    inc += 1
    ver = move(ver, rev_direction[t])
    print('Num: ', inc)
    info(ver)
'''
file = open('zad_output.txt', 'w+')
file.write(outcome)
