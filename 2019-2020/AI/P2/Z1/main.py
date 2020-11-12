import random
import numpy as np

file = open('zad_input.txt', encoding='UTF-8')

opt_dist_memory = {}


lines = file.readlines()
X, Y = map(int, lines[0].split())
heights = [list(map(int, line.split())) for line in lines[1: X+1]]
widths = [list(map(int, line.split())) for line in lines[1+X: X+Y+1]]


matrix = np.zeros((X, Y), dtype='int8')

# print(X, Y)
# print(heights, widths)


def info(mat):
    print('=================')
    print(mat)
    print('=================')


def init():
    for x in range(X):
        for y in range(Y):
            matrix[x][y] = 0


def opt_dist(array, D):
    array = list(array)
    global opt_dist_memory
    test = (tuple(array), tuple(D))
    if test in opt_dist_memory:
        return opt_dist_memory[test]

    array = [0] + array
    mat = [[np.inf for i in range(len(array) + 1)] for j in range(len(D) + 1)]

    for j in range(len(array) + 1):
        mat[0][j] = sum(array[0:j])

    for i in range(1, len(D) + 1):
        for j in range(sum(D[0:i]) + i, len(array) + 1):
            mat[i][j] = min(mat[i][j],\
                            mat[i][j - 1] + array[j - 1],\
                            mat[i - 1][j - D[i - 1] - 1] + D[i - 1]\
                            - sum(array[j - D[i - 1]: j]) + array[j - D[i - 1] - 1])

    result = mat[len(D)][len(array)]
    opt_dist_memory[test] = result
    return result


def is_ok():
    for row in range(X):
        if opt_dist(matrix[row], heights[row]):
            return False
    for column in range(Y):
        temp = matrix[:, column]
        if opt_dist(temp, widths[column]):
            return False
    return True


def wrong_column():
    wrongs = []
    for index in range(Y):
        array = matrix[:, index]
        if opt_dist(array, widths[index]):
            wrongs.append(index)
    if wrongs:
        return random.choice(wrongs)
    return -1


def wrong_row():
    wrongs = []
    for index in range(X):
        array = matrix[index]
        if opt_dist(array, heights[index]):
            wrongs.append(index)
    if wrongs:
        return random.choice(wrongs)
    return -1


def work():

    def sub_work():
        i = 0
        while i < 200000 and (not is_ok()):
            roll = random.random()
            if roll >= 0:
                index = wrong_column()
                if roll < 0.02:
                    randX = random.randint(0, X - 1)
                    randY = random.randint(0, Y - 1)
                    if matrix[randX][randY] == 1:
                        matrix[randX][randY] = 0
                    else:
                        matrix[randX][randY] = 1
                elif index != -1:
                    virtual = matrix.copy()
                    options = np.zeros(X, dtype='int8')
                    change = opt_dist(virtual[:, index], widths[index])
                    for j in range(X):
                        aux = opt_dist(virtual[j], heights[j])
                        if virtual[j, index] == 1:
                            virtual[j, index] = 0
                        else:
                            virtual[j, index] = 1
                        options[j] = (change - opt_dist(virtual[:, index], widths[index])) +\
                                     (aux - opt_dist(virtual[j], heights[j]))
                        if virtual[j, index] == 1:
                            virtual[j, index] = 0
                        else:
                            virtual[j, index] = 1
                    maximum = max(options)
                    to_roll = []
                    for w in range(len(options)):
                        if options[w] == maximum:
                            to_roll.append(w)
                    winner = random.choice(to_roll)
                    if matrix[winner, index] == 1:
                        matrix[winner, index] = 0
                    else:
                        matrix[winner, index] = 1
            else:
                index = wrong_row()
                if index != -1:
                    pass
            i += 1

    sub_work()
    while not is_ok():
        init()
        sub_work()


work()

'''
s = '.###.......#.#......####.........#.###.....######.....######'
for x in range(6):
    for i in range(10):
        if s[10 * x + i] == '#':
            matrix[x][i] = 1
'''
'''
info(matrix)
if is_ok():
    print('OK')
'''

f = open('zad_output.txt', 'w+')
for i in range(X):
    for j in range(Y):
        if matrix[i][j]:
            f.write('#')
        else:
            f.write('.')
    f.write('\n')
f.close()
