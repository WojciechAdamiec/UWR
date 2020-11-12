import random
import numpy as np

file = open('zad5_input.txt', encoding='UTF-8')
first = file.readline().strip()

SIZE = int(first[0]), int(first[-1])


vertical = []
horizontal = []


for i in range(SIZE[0]):
    line = file.readline()
    vertical.append(int(line))

for j in range(SIZE[1]):
    line = file.readline()
    horizontal.append(int(line))


matrix = np.zeros(SIZE, dtype='int8')


def info(mat):
    print('=================')
    print(mat)
    print('=================')


def init():
    for x in range(SIZE[0]):
        for y in range(SIZE[0]):
            matrix[x][y] = 0
    for i in range(SIZE[0]):
        for j in range(vertical[i]):
            matrix[i][j] = 1


def opt_dist(array, D):
    length = len(array)
    start = 0
    end = D - 1
    best = 0
    ones = 0
    for i in range(length - D + 1):
        aux = 0
        for j in range(start, end + 1):
            if array[j]:
                aux += 1
        if aux > best:
            best = aux
        start += 1
        end += 1
    for element in array:
        if element:
            ones += 1
    # print(array, D, D - 2 * best + ones)
    return D - 2 * best + ones


def is_ok():
    for i in range(SIZE[0]):
        if opt_dist(matrix[i], vertical[i]):
            return False
    for j in range(SIZE[1]):
        temp = matrix[:, j]
        if opt_dist(temp, horizontal[j]):
            return False
    return True


def wrong_column():
    wrongs = []
    for index in range(SIZE[1]):
        array = matrix[:, index]
        if opt_dist(array, horizontal[index]):
            wrongs.append(index)
    if wrongs:
        return random.choice(wrongs)
    return -1


def wrong_row():
    wrongs = []
    for index in range(SIZE[0]):
        array = matrix[index]
        if opt_dist(array, vertical[index]):
            wrongs.append(index)
    if wrongs:
        return random.choice(wrongs)
    return -1


def work():

    def sub_work():
        i = 0
        while i < 5000 and (not is_ok()):
            if random.random() > 0.5:
                index = wrong_column()
                if index != -1:
                    virtual = matrix.copy()
                    options = np.zeros(SIZE[0], dtype='int8')
                    change = opt_dist(virtual[:, index], horizontal[index])
                    for j in range(SIZE[0]):
                        aux = opt_dist(virtual[j], vertical[j])
                        if virtual[j, index] == 1:
                            virtual[j, index] = 0
                        else:
                            virtual[j, index] = 1
                        options[j] = (change - opt_dist(virtual[:, index], horizontal[index])) +\
                                     (aux - opt_dist(virtual[j], vertical[j]))
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
"""
s = '##.....##.....##############.....##.....##.....##'
for x in range(7):
    for i in range(7):
        if s[7 * x + i] == '#':
            matrix[x][i] = 1
"""
'''
print(vertical, horizontal)

info(matrix)
if is_ok():
    print('OK')
'''
f = open('zad5_output.txt', 'w+')
for i in range(SIZE[0]):
    for j in range(SIZE[1]):
        if matrix[i][j]:
            f.write('#')
        else:
            f.write('.')
    f.write('\n')
f.close()
