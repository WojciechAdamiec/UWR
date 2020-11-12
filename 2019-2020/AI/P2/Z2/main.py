import numpy as np
import queue as qq
from collections import defaultdict

lines = []
line = []

for x in open('zad_input.txt'):
    line = x.strip()
    lines.append(line)


X_SIZE, Y_SIZE = len(line), len(lines)
warehouse = np.zeros((X_SIZE, Y_SIZE), dtype='str')
adjacent = [(0, 1), (1, 0), (-1, 0), (0, -1)]
keeper = (-1, -1)
crates_counter = 0
crates = []
goals = []
starting_state = None


def init():
    global crates, crates_counter, keeper, starting_state
    for i in range(X_SIZE):
        for j in range(Y_SIZE):
            warehouse[i][j] = lines[j][i]
    for j in range(Y_SIZE):
        for i in range(X_SIZE):
            if warehouse[i][j] == 'B' or warehouse[i][j] == '*':
                crates.append((i, j))
            if warehouse[i][j] == 'G' or warehouse[i][j] == '*':
                goals.append((i, j))
            elif warehouse[i][j] == 'K':
                keeper = (i, j)
    crates_counter = len(crates)
    starting_state = tuple([keeper] + crates)
    for j in range(Y_SIZE):
        for i in range(X_SIZE):
            if warehouse[i][j] == 'G' or warehouse[i][j] == '*' or warehouse[i][j] == '+':
                warehouse[i][j] = 'G'
            elif warehouse[i][j] != '.' and warehouse[i][j] != 'W':
                warehouse[i][j] = '.'


def info(state):
    house = np.copy(warehouse)
    if (state[0][0], state[0][1]) in goals:
        house[state[0][0]][state[0][1]] = '+'
    else:
        house[state[0][0]][state[0][1]] = 'K'
    for crate in state[1:]:
        if crate in goals:
            house[crate[0]][crate[1]] = '*'
        else:
            house[crate[0]][crate[1]] = 'B'

    for j in range(Y_SIZE):
        for i in range(X_SIZE):
            print(house[i][j], end='')
        print()


def is_ok(state):
    verdict = True
    for crate in state[1:]:
        if crate not in goals:
            verdict = False
            break
    return verdict


def good(state):
    for crate in state[1:]:
        if crate not in goals:
            l, r, u, d = 0, 0, 0, 0
            if warehouse[crate[0] + 1][crate[1]] == 'W':
                r = 1
            if warehouse[crate[0] - 1][crate[1]] == 'W':
                l = 1
            if warehouse[crate[0]][crate[1] + 1] == 'W':
                d = 1
            if warehouse[crate[0]][crate[1] - 1] == 'W':
                u = 1
            if (r and u) or (r and d) or (d and l) or (l and u):
                return False
    return True


def give_options(state):
    options = []
    for adj in adjacent:
        if warehouse[state[0][0] + adj[0]][state[0][1] + adj[1]] == '.' or warehouse[state[0][0] + adj[0]][state[0][1] + adj[1]] == 'G':
            if (state[0][0] + adj[0], state[0][1] + adj[1]) not in state[1:]:
                options.append(tuple([(state[0][0] + adj[0], state[0][1] + adj[1])] + list(state[1:])))
            else:
                if warehouse[state[0][0] + 2 * adj[0]][state[0][1] + 2 * adj[1]] == '.' or warehouse[state[0][0] + 2 * adj[0]][state[0][1] + 2 * adj[1]] == 'G':
                    if (state[0][0] + 2 * adj[0], state[0][1] + 2 * adj[1]) not in state[1:]:
                        index = -1
                        for ind in range(len(state)):
                            if (state[0][0] + adj[0], state[0][1] + adj[1]) == state[ind]:
                                index = ind
                                break
                        options.append(tuple([(state[0][0] + adj[0], state[0][1] + adj[1])] + list(state[1:index]) + [(state[0][0] + 2 * adj[0], state[0][1] + 2 * adj[1])] + list(state[index + 1:])))
    return options


def bfs(input_state):
    queue = qq.Queue()
    history = {}
    discovered = set()
    queue.put(input_state)
    end = None
    while not queue.empty():
        v = queue.get()
        if is_ok(v):
            end = v
            break
        options = give_options(v)
        for option in options:
            if option not in discovered:
                discovered.add(option)
                if good(option):
                    queue.put(option)
                    history[option] = v
    path = [end]
    while end != starting_state:
        path.append(history[end])
        end = history[end]
    path.reverse()
    return path


def h(state):
    global goals
    heu = 0
    for crate in state[1:]:
        distances = set()
        for goal in goals:
            distances.add(abs(crate[0] - goal[0]) + abs(crate[1] - goal[1]))
        heu += min(distances)
    return heu


def a_star(input_state):
    queue = qq.PriorityQueue()
    history = {}
    visited = set()
    gScore = defaultdict(lambda: np.inf)
    gScore[input_state] = 0
    fScore = defaultdict(lambda: np.inf)
    fScore[input_state] = h(input_state)

    queue.put((fScore[input_state], input_state))
    end = None
    while not queue.empty():
        pack = queue.get()
        v = pack[1]
        if is_ok(v):
            end = v
            break
        visited.add(v)
        options = give_options(v)
        for option in options:
            temp_Gscore = gScore[v] + 1
            if temp_Gscore < gScore[option]:
                history[option] = v
                gScore[option] = temp_Gscore
                fScore[option] = gScore[option] + h(option)
                if option not in visited:
                    queue.put((fScore[option], option))

    path = [end]
    while end != starting_state:
        path.append(history[end])
        end = history[end]
    path.reverse()
    return path


init()
# PATH = (bfs(starting_state))
PATH = (a_star(starting_state))
stringPath = ''
for i in range(len(PATH) - 1):
    first = PATH[i][0]
    second = PATH[i + 1][0]
    change = second[0] - first[0], second[1] - first[1]
    if change == (0, 1):
        stringPath += 'D'
    if change == (0, -1):
        stringPath += 'U'
    if change == (1, 0):
        stringPath += 'R'
    if change == (-1, 0):
        stringPath += 'L'

'''
test = ((1, 1), (1, 2), (3, 3))

print('///////////////////////')
info(test)
print(test)
tests = give_options(test)

for t in tests:
    print('=============')
    print(good(t))
    info(t)
    print(t)
    print('=============')
'''

output = open('zad_output.txt', 'w+')
output.write(stringPath)
