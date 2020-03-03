import queue as qq
import numpy as np
# import pudb; pudb.set_trace()

lines = []
data = []
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for x in open('zad1_input.txt', encoding='UTF-8'):
    lines.append(x.strip())
for i in range(len(lines)):
    alf = -1
    player = lines[i][0:5]

    cor1 = lines[i][6:8]
    for j in range(len(letters)):
        if letters[j] == cor1[0]:
            alf = j
    num = int(cor1[1]) - 1
    white_king = alf, num

    cor2 = lines[i][9:11]
    for j in range(len(letters)):
        if letters[j] == cor2[0]:
            alf = j
    num = int(cor2[1]) - 1
    white_tower = alf, num

    cor3 = lines[i][12:14]
    for j in range(len(letters)):
        if letters[j] == cor3[0]:
            alf = j
    num = int(cor3[1]) - 1
    black_king = alf, num

    data.append((player, white_king, white_tower, black_king))


adjacent = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]


def black_king_check(state, pos):
    tower = state[2]
    king = state[1]
    wrong_places = [king]

    for adj in adjacent:
        wrong_places.append((king[0] + adj[0], king[1] + adj[1]))

    if pos == tower and tower not in wrong_places:
        return True

    if pos[0] == tower[0]:
        if king[0] != pos[0]:
            for ver in range(8):
                wrong_places.append((tower[0], ver))
        else:
            for ver in range(8):
                if king[1] > max(tower[1], pos[1]) or king[1] < min(tower[1], pos[1]):
                    wrong_places.append((tower[0], ver))
    if pos[1] == tower[1]:
        if king[1] != pos[1]:
            for hor in range(8):
                wrong_places.append((hor, tower[1]))
        else:
            for hor in range(8):
                if king[0] > max(tower[0], pos[0]) or king[0] < min(tower[0], pos[0]):
                    wrong_places.append((hor, tower[1]))

    if pos in wrong_places:
        return False
    return True


def checkmate(state):
    pos = state[3]
    if not black_king_check(state, pos):
        for adj in adjacent:
            if (0 <= pos[0] + adj[0] <= 7) and (0 <= pos[1] + adj[1] <= 7):
                if black_king_check(state, (pos[0] + adj[0], pos[1] + adj[1])):
                    return False
        # print('Checkmate!')
        return True
    return False


def possibilities(state):
    new_states = set()
    potential_positions = []
    # print('Entering possibilities: ' + state.player)
    if state[0] == 'black':
        # options for black_king
        pos = state[3]
        for adj in adjacent:
            if (0 <= pos[0] + adj[0] <= 7) and (0 <= pos[1] + adj[1] <= 7):
                potential_positions.append((pos[0] + adj[0], pos[1] + adj[1]))
        # print(potential_positions, ' : ', pos)
        for position in potential_positions:
            if black_king_check(state, position):
                new_states.add(('white', state[1], state[2], position))
    elif state[0] == 'white':
        # options for white_king
        pos = state[1]
        tower = state[2]
        black = state[3]
        for adj in adjacent:
            if (0 <= pos[0] + adj[0] <= 7) and (0 <= pos[1] + adj[1] <= 7):
                potential_positions.append((pos[0] + adj[0], pos[1] + adj[1]))
        wrong_places = [tower, black]
        for adj in adjacent:
            wrong_places.append((black[0] + adj[0], black[1] + adj[1]))
        for place in potential_positions:
            if place not in wrong_places:
                new_states.add(('black', place, state[2], state[3]))

        # options for white_tower
        wrong_places = [tower, black, pos]
        possible_places = []
        for ver in range(8):
            possible_places.append((tower[0], ver))
        for hor in range(8):
            possible_places.append((hor, tower[1]))

        if pos[0] == tower[0]:
            for ver in range(8):
                if (ver > pos[1] > tower[1]) or (ver < pos[1] < tower[1]):
                    wrong_places.append((tower[0], ver))

        if pos[1] == tower[1]:
            for hor in range(8):
                if (hor > pos[0] > tower[0]) or (hor < pos[0] < tower[0]):
                    wrong_places.append((hor, tower[1]))

        for place in possible_places:
            if place not in wrong_places:
                new_states.add(('black', pos, place, black))

    return new_states


def find(first_state):
    queue = qq.Queue()
    dead = set()
    node = (None, first_state)

    while not checkmate(node[1]):
        # print('Cycle!')
        if node[1][2] != node[1][3]:
            new_states = possibilities(node[1])
            for possibility in new_states:
                if possibility not in dead:
                    dead.add(possibility)
                    queue.put((node, possibility))
        node = queue.get()

    history = []
    while node[0]:
        history.append(node[1])
        node = node[0]
    history.append(first_state)
    history.reverse()
    return history


def info(state):
        rendered_map = np.zeros((8, 8), dtype=int)
        print()
        print('=======')
        print(state[0])
        print()
        rendered_map[state[1][1], state[1][0]] = 1
        rendered_map[state[2][1], state[2][0]] = 2
        rendered_map[state[3][1], state[3][0]] = 3
        print('X A B C D E F G H')
        for i in range(1, 9):
            print(i, end=' ')
            for j in range(8):
                print(rendered_map[i - 1][j], end=' ')
            print()
        print()


for state in data:
    history = find(state)
    print()
    print(state, 'Length: ' + str(len(history) - 1))
    for turn in history:
        info(turn)
