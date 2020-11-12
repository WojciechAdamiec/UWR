import numpy as np
import random
import time
import copy
import math
import os
import subprocess

MAX = 1
MIN = 0
SIZE = 8
TIME = 1


def build_board():
    board = np.full((SIZE, SIZE), 7, dtype='int8')
    board[3][3] = MAX
    board[4][4] = MAX
    board[3][4] = MIN
    board[4][3] = MIN
    return board


class State:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self, board, fields, player, parent, move):

        self.board = board
        self.fields = fields
        self.player = player
        self.opponent = 1 - player
        self.parent = parent
        self.move = move
        self.children = []
        self.wins = 0
        self.played_games = 1

    def __str__(self):
        draw = []
        for i in range(SIZE):
            res = []
            for j in range(SIZE):
                b = self.board[i][j]
                if b == 7:
                    res.append('.')
                elif b == MAX:
                    res.append('#')
                elif b == MIN:
                    res.append('o')
            draw.append(''.join(res))
        return '\n'.join(draw)

    def moves(self):
        res = []
        for (x, y) in self.fields:
            if any(self.can_beat(x, y, direction) for direction in State.dirs):
                res.append((x, y))
        if not res:
            return [None]
        return res

    def can_beat(self, x, y, d):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == self.opponent:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == self.player

    def get(self, x, y):
        if 0 <= x < SIZE and 0 <= y < SIZE:
            return self.board[y][x]
        return None

    def do_move(self, move):

        board = copy.deepcopy(self.board)
        fields = copy.deepcopy(self.fields)
        if move:
            x, y = move
            x0, y0 = move
            board[y][x] = self.player
            fields -= set([move])
            for dx, dy in State.dirs:
                x, y = x0, y0
                to_beat = []
                x += dx
                y += dy
                while self.get(x, y) == self.opponent:
                    to_beat.append((x, y))
                    x += dx
                    y += dy
                if self.get(x, y) == self.player:
                    for (nx, ny) in to_beat:
                        board[ny][nx] = self.player
        return State(board, fields, self.opponent, self, move)

    def terminal(self):
        a = [x for x in self.moves() if x is not None]
        if not a:
            s = State(self.board, self.fields, self.opponent, self, None)
            opp_moves = s.moves()
            return not [y for y in opp_moves if y is not None]
        return False


class Board:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    def __init__(self, player):

        self.player = player
        self.board = build_board()
        self.fields = set()
        for j in range(SIZE):
            for i in range(SIZE):
                if self.board[i][j] == 7:
                    self.fields.add((i, j))

        self.state = State(self.board, self.fields, self.player, None, None)

        self.N = 0  # TOTAL NUMBER OF PLAYED GAMES

    def __str__(self):
        return self.board.__str__()

    def random_move(self, state):
        moves = state.moves()
        if moves is None:
            return None
        return random.choice(moves)

    def result(self, board):
        balance = 0
        for y in range(SIZE):
            for x in range(SIZE):
                b = board[y][x]
                if b == MAX:
                    balance += 1
                elif b == MIN:
                    balance -= 1
        return balance

    def random_game(self, root):
        state = State(copy.deepcopy(root.board), copy.deepcopy(root.fields), root.player, None, None)
        while True:
            move = self.random_move(state)
            state = state.do_move(move)
            if state.terminal():
                if self.result(state.board) > 0:
                    return MAX
                return MIN

    def UCB(self, state):
        q = math.sqrt(math.log(self.N) / state.played_games)
        return state.wins / state.played_games + q

    def monte_carlo(self, root):

        start_time = time.time()
        while time.time() - start_time < TIME:
            self.N += 1
            leaf = self.selection(root)
            self.expansion(leaf)
            winner = self.simulation(leaf)
            self.backpropagation(leaf, winner, root)

        best_child = min(root.children, key=lambda s: s.wins)
        return best_child

    def selection(self, root):
        state = root
        while state.children:
            state = max(state.children, key=lambda s: self.UCB(s))
        return state

    def expansion(self, leaf):
        for move in leaf.moves():
            leaf.children.append(leaf.do_move(move))

    def simulation(self, leaf):
        return self.random_game(leaf)

    def backpropagation(self, leaf, winner, root):
        node = leaf
        while True:
            node.played_games += 1
            if node.player == winner:
                node.wins += 1
            if node == root:
                break
            node = node.parent

    def play(self):
        '''
        print(self.state.player)
        print(self.state)
        print('=============')
        '''
        while True:

            if self.state.player == MAX:
                self.state = self.monte_carlo(self.state)

            else:
                move = self.random_move(self.state)
                self.state = self.state.do_move(move)
            '''
            print(self.state.player)
            print(self.state)
            print('=============')
            '''
            if self.state.terminal():
                res = self.result(self.state.board)
                if res > 0:
                    return MAX
                elif res < 0:
                    return MIN
                else:
                    return -1


if __name__ == "__main__":

    rounds = 10

    max_victories = 0
    min_victories = 0
    ties = 0

    player = 0

    for i in range(rounds):
        b = Board(player)
        info = ""
        # time_start = time.time()
        result = b.play()
        # print(time.time() - time_start)
        if result == MAX:
            max_victories += 1
            info += "MAX_victory!"

        elif result == MIN:
            min_victories += 1
            info += "MIN_victory!"
        else:
            ties += 1
            info += "TIE!"
        print(info)
        player = 1 - player

    print("Total results:")
    print("MAX:", max_victories, "TIES:", ties, "MIN:", min_victories)

