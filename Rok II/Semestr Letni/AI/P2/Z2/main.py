import numpy as np
import queue as qq

lines = []
line = []

for x in open('zad_input.txt'):
    line = x.strip()
    lines.append(line)


X_SIZE, Y_SIZE = len(line), len(lines)
warehouse = np.zeros((X_SIZE, Y_SIZE), dtype='str')
adjacent = [(0, 1), (1, 0), (-1, 0), (0, -1)]
result = ''
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


def give_options(state):
    options = []
    for adj in adjacent:
        if warehouse[state[0][0] + adj[0]][state[0][1] + adj[1]] == '.' or warehouse[state[0][0] + adj[0]][state[0][1] + adj[1]] == 'G':
            if (state[0][0] + adj[0], state[0][1] + adj[1]) not in state[1:]:
                options.append(tuple([(state[0][0] + adj[0], state[0][1] + adj[1])] + list(state[1:])))
            else:
                if warehouse[state[0][0] + 2 * adj[0]][state[0][1] + 2 * adj[1]] == '.' or warehouse[state[0][0] + 2 * adj[0]][state[0][1] + 2 * adj[1]] == '.':
                    if (state[0][0] + 2 * adj[0], state[0][1] + 2 * adj[1]) not in state[1:]:
                        index = -1
                        for ind in range(len(state)):
                            if (state[0][0] + adj[0], state[0][1] + adj[1]) == state[ind]:
                                index = ind
                                break
                        options.append(tuple([(state[0][0] + adj[0], state[0][1] + adj[1])] + list(state[1:index]) + [(state[0][0] + 2 * adj[0], state[0][1] + 2 * adj[1])] + list(state[index + 1:])))
    return options


def bfs(input_state):
    state = input_state
    visited = set()
    visited.add(state)
    queue = qq.Queue()
    queue.put(state)
    while not queue.empty():
        options = give_options(state)
        for opt in options:
            if opt not in visited:
                visited.add(opt)
                queue.put(opt)
        state = queue.get()
        print(state)
    print('final: ', state)


init()
bfs(starting_state)
print(not is_ok(((1, 1), (1, 3), (2, 1))))

output = open('zad_output.txt', 'w+')
output.write(result)
