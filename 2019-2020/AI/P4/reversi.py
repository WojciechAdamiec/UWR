import numpy as np
import random
import time
import json
import copy
import math
from os.path import exists


class Board:
    dirs = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    SIZE = 8

    # Parameters for heuristic function
    HEU_ARCH = 1
    HEU_CORN = 8000
    HEU_CLO = 3800
    HEU_EDGE = 1000

    scores = None
    scores_games = 1

    def __init__(self):
        if not exists("game_data.json"):
            game_data = {
                "scores": np.zeros(
                    (Board.SIZE ** 2 + 20, Board.SIZE, Board.SIZE), dtype=int
                ).tolist(),
                "scores_games": 1,
            }
            with open("game_data.json", "w") as data:
                data.write(json.dumps(game_data, indent=2))

        with open("game_data.json", "r") as file:
            json_data = json.loads(file.read())
            Board.scores = json_data["scores"]
            Board.scores_games = json_data["scores_games"]
            for r in range(Board.SIZE ** 2 + 20):
                for x in range(Board.SIZE):
                    for y in range(Board.SIZE):
                        Board.scores[r][x][y] /= (Board.scores_games * 10)  # TODO: change this

        self.new_scores = np.zeros((Board.SIZE ** 2 + 20, Board.SIZE, Board.SIZE), dtype=int)
        self.new_scores_games = 0
        self.board = self.build_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        self.turn = 1
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == 7:
                    self.fields.add((j, i))

    def build_board(self):
        board = np.full((self.SIZE, self.SIZE), 7, dtype='int8')
        board[3][3] = 0
        board[4][4] = 0
        board[3][4] = 1
        board[4][3] = 1
        return board

    def reset(self):
        self.board = self.build_board()
        self.fields = set()
        self.move_list = []
        self.history = []
        self.turn = 1
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if self.board[i][j] == 7:
                    self.fields.add((j, i))

    def update_stats(self, res):
        if res == 0:
            return
        if res < 0:
            winner = 0
            loser = 1
        else:
            winner = 1
            loser = 0
        for turn, sit in enumerate(self.history):
            for i in range(self.SIZE):
                for j in range(self.SIZE):
                    if sit[i][j] == winner:
                        self.new_scores[turn][i][j] += 1
                    elif sit[i][j] == loser:
                        self.new_scores[turn][i][j] -= 1
        self.new_scores_games += 1

    def save(self):
        game_data = {
            "scores": self.new_scores.tolist(),
            "scores_games": self.new_scores_games,
        }
        with open("game_data.json", "w") as data:
            data.write(json.dumps(game_data, indent=2))

    def draw(self, player):
        text = 'Player 0: #' if player == 0 else 'Player 1: o'
        print(text)
        for i in range(self.SIZE):
            res = []
            for j in range(self.SIZE):
                b = self.board[i][j]
                if b == 7:
                    res.append('.')
                elif b == 0:
                    res.append('#')
                else:
                    res.append('o')
            print(''.join(res))
        print()

    def moves(self, player):
        res = []
        for (x, y) in self.fields:
            if any(self.can_beat(x, y, direction, player) for direction in Board.dirs):
                res.append((x, y))
        if not res:
            return [None]
        return res

    def can_beat(self, x, y, d, player):
        dx, dy = d
        x += dx
        y += dy
        cnt = 0
        while self.get(x, y) == 1 - player:
            x += dx
            y += dy
            cnt += 1
        return cnt > 0 and self.get(x, y) == player

    def get(self, x, y):
        if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
            return self.board[y][x]
        return None

    def light_get(self, board, x, y):
        if 0 <= x < self.SIZE and 0 <= y < self.SIZE:
            return board[y][x]
        return None

    def do_move(self, move, player, his=False):
        self.turn += 1
        if his:
            self.history.append(copy.deepcopy(self.board))
        self.move_list.append(move)

        if move is None:
            return
        x, y = move
        x0, y0 = move
        self.board[y][x] = player
        self.fields -= set([move])
        for dx, dy in self.dirs:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.get(x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.get(x, y) == player:
                for (nx, ny) in to_beat:
                    self.board[ny][nx] = player

    def light_move(self, board, move, player, turn):
        new_board = copy.deepcopy(board)
        balance = 0

        if move is None:
            return new_board, 0

        x, y = move
        x0, y0 = move
        new_board[y][x] = player
        balance += Board.scores[turn][y][x]

        for dx, dy in self.dirs:
            x, y = x0, y0
            to_beat = []
            x += dx
            y += dy
            while self.light_get(new_board, x, y) == 1 - player:
                to_beat.append((x, y))
                x += dx
                y += dy
            if self.light_get(new_board, x, y) == player:
                for (nx, ny) in to_beat:
                    new_board[ny][nx] = player
                    balance += Board.scores[turn][ny][nx]
        if player:
            balance *= -1
        return new_board, balance

    def result(self):
        res = 0
        points = self.SIZE * self.SIZE
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                b = self.board[y][x]
                if b == 0:
                    res += 1
        if res > 32:
            text = 'Player 0 (#) won!; ' + str(res) + ' : ' + str(points - res)
        elif res < 32:
            text = 'Player 1 (o) won!; ' + str(points - res) + ' : ' + str(res)
        else:
            text = 'Draw! ; 32:32'
        return text

    def quick_result(self):
        res = 0
        for y in range(self.SIZE):
            for x in range(self.SIZE):
                b = self.board[y][x]
                if b == 0:
                    res -= 1
                elif b == 1:
                    res += 1
        return res

    def terminal(self):
        if not self.fields:
            return True
        if len(self.move_list) < 2:
            return False
        return self.move_list[-1] == self.move_list[-2] is None

    def random_move(self, player):
        ms = self.moves(player)
        if ms:
            return random.choice(ms)
        return None

    def archives_boost(self, board, turn):  # This is no longer used
        # return 0  # TODO: make this switchable
        boost = 0
        for i in range(self.SIZE):
            for j in range(self.SIZE):
                if board[i][j] == 0:
                    boost += Board.scores[turn][i][j]
                if board[i][j] == 1:
                    boost -= Board.scores[turn][i][j]
        return boost

    def corners_boost(self, board):
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]
        player_0 = 0
        player_1 = 0
        for i, j in corners:
            if board[i][j] == 0:
                player_0 += 1

            elif board[i][j] == 1:
                player_1 += 1
        boost = 0
        if player_0 + player_1 != 0:
            boost = (player_0 - player_1) / math.sqrt(player_0 + player_1)
        return boost

    def safe_fields(selfs, board):
        boost = 0
        if board[0][0] == 0:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d < 7:
                d += 1
                f += 1
                if flag_d and board[0][d] == 0:
                    boost += 1
                else:
                    flag_d = False
                if flag_f and board[f][0] == 0:
                    boost += 1
                else:
                    flag_f = False

        elif board[0][0] == 1:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d < 7:
                d += 1
                f += 1
                if flag_d and board[0][d] == 1:
                    boost -= 1
                else:
                    flag_d = False
                if flag_f and board[f][0] == 1:
                    boost -= 1
                else:
                    flag_f = False

        if board[0][7] == 0:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d < 7:
                d += 1
                f -= 1
                if flag_d and board[d][7] == 0:
                    boost += 1
                else:
                    flag_d = False
                if flag_f and board[0][7 + f] == 0:
                    boost += 1
                else:
                    flag_f = False

        elif board[0][7] == 1:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d < 7:
                d += 1
                f -= 1
                if flag_d and board[d][7] == 1:
                    boost -= 1
                else:
                    flag_d = False
                if flag_f and board[0][7 + f] == 1:
                    boost -= 1
                else:
                    flag_f = False

        if board[7][0] == 0:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d < 7:
                d += 1
                f -= 1
                if flag_d and board[7][d] == 0:
                    boost += 1
                else:
                    flag_d = False
                if flag_f and board[7 + f][0] == 0:
                    boost += 1
                else:
                    flag_f = False

        elif board[7][0] == 1:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d < 7:
                d += 1
                f -= 1
                if flag_d and board[7][d] == 1:
                    boost -= 1
                else:
                    flag_d = False
                if flag_f and board[7 + f][0] == 1:
                    boost -= 1
                else:
                    flag_f = False

        if board[7][7] == 0:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d > 0:
                d -= 1
                f -= 1
                if flag_d and board[7][d] == 0:
                    boost += 1
                else:
                    flag_d = False
                if flag_f and board[f][7] == 0:
                    boost += 1
                else:
                    flag_f = False

        elif board[7][7] == 1:
            d = 0
            f = 0
            flag_d = True
            flag_f = True
            while (flag_d or flag_f) and d > 0:
                d -= 1
                f -= 1
                if flag_d and board[7][d] == 1:
                    boost -= 1
                else:
                    flag_d = False
                if flag_f and board[f][7] == 1:
                    boost -= 1
                else:
                    flag_f = False
        return boost

    def close_boost(self, board):
        close = {(0, 0): [(0, 1), (1, 0), (1, 1)],  # top left
                 (0, 7): [(0, 6), (1, 7), (1, 6)],  # top right
                 (7, 0): [(6, 0), (7, 1), (6, 1)],  # bot left
                 (7, 7): [(6, 7), (7, 6), (6, 6)]}  # bot right
        player_0 = 0
        player_1 = 0
        for i, j in close:
            if board[i][j] == 7:
                for x, y in close[(i, j)]:
                    if board[x][y] == 0:
                        player_0 += 1
                    if board[x][y] == 1:
                        player_1 += 1
        penalty = 0
        if player_0 + player_1 != 0:
            penalty = (player_0 - player_1) / (player_0 + player_1)
        return -penalty

    def boost(self, board, turn, archives=True):
        boost = self.HEU_CORN * self.corners_boost(board) + \
                self.HEU_CLO * self.close_boost(board) + \
                self.HEU_EDGE * self.safe_fields(board)
        return boost

    def best_move(self, player, turn):
        # Poor min-max without min, just max
        fitness = []
        all_moves = self.moves(player)

        for move in all_moves:
            new_board, balance = self.light_move(self.board, move, player, turn)
            total_boost = self.boost(new_board, turn, archives=False)
            fitness.append(total_boost + balance)

        res = all_moves[fitness.index(max(fitness))]
        return res
    """
    def alpha_beta(self, player, turn):
        # Mini-max with alpha-beta and sorting
        depth = 2
        awesomest = None
        minval, maxval = np.inf, -np.inf
        for m in self.moves(player):  # TODO: Sorting
            board, balance = self.light_move(self.board, m, player, turn)
            boost = self.boost(board) + balance
            # Pruning will be considered at least on grandson's level
            if player == 0:
                boost += self.min_value(board, 1 - player, depth - 1, -np.inf, np.inf, turn + 1)
                if boost > maxval:
                    maxval = boost
                    awesomest = m
            else:
                boost += self.max_value(board, 1 - player, depth - 1, -np.inf, np.inf, turn + 1)
                if boost < minval:
                    minval = boost
                    awesomest = m
        return awesomest

    def max_value(self, board, player, depth, alpha, beta, turn):
        if self.terminal() or depth == 0:
            return self.boost(board)
        value = -np.inf
        moves = self.moves(player)
        if moves and None not in moves:
            moves.sort(key=lambda pair: Board.scores[turn][pair[0]][pair[1]])
        for move in moves:  # TODO: Sorting
            b, balance = self.light_move(board, move, player, turn)
            value = max(value, self.min_value(b, 1 - player, depth - 1, alpha, beta, turn + 1) + balance)
            if value >= beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, board, player, depth, alpha, beta, turn):
        if self.terminal() or depth == 0:
            return self.boost(board)
        value = np.inf
        moves = self.moves(player)
        if moves and None not in moves:
            moves.sort(key=lambda pair: - Board.scores[turn][pair[0]][pair[1]])
        for move in moves:  # TODO: Sorting
            b, balance = self.light_move(board, move, player, turn)
            value = min(value, self.max_value(b, 1 - player, depth - 1, alpha, beta, turn + 1) + balance)
            if value <= alpha:
                return value
            beta = min(beta, value)
        return value
    """
    def launch_mini_max(self, player, turn):
        depth = 2

        def mini_max(board, depth, player, alpha, beta, turn):
            if self.terminal() or depth == 0:
                return self.boost(board, turn)

            if player == 0:
                best_val = np.NINF
                moves = self.moves(player)
                if moves and None not in moves:
                    moves.sort(key=lambda pair: - Board.scores[turn][pair[0]][pair[1]])
                for move in moves:
                    child_board, balance = self.light_move(board, move, player, turn + 1)
                    value = mini_max(child_board, depth - 1, 1 - player, alpha, beta, turn + 1)
                    best_val = max(best_val, value + balance)
                    alpha = max(alpha, best_val)
                    if beta <= alpha:
                        break
                return best_val

            else:
                best_val = np.inf
                moves = self.moves(player)
                if moves and None not in moves:
                    moves.sort(key=lambda pair: Board.scores[turn][pair[0]][pair[1]])
                for move in moves:
                    child_board, balance = self.light_move(board, move, player, turn + 1)
                    value = mini_max(child_board, depth - 1, 1 - player, alpha, beta, turn + 1)
                    best_val = min(best_val, value + balance)
                    beta = min(alpha, best_val)
                    if beta <= alpha:
                        break
                return best_val

        def choose_move(player, turn, depth):
            chosen = None
            minval, maxval = np.inf, np.NINF
            for m in self.moves(player):
                new_board, balance = self.light_move(self.board, m, player, turn)
                boost = self.boost(new_board, turn + 1) + balance

                if player == 0:
                    boost += mini_max(new_board, 1 - player, depth - 1, np.NINF, np.inf, turn + 1)
                    if boost > maxval:
                        maxval = boost
                        chosen = m
                else:
                    boost += mini_max(new_board, 1 - player, depth - 1, np.NINF, np.inf, turn + 1)
                    if boost < minval:
                        minval = boost
                        chosen = m
            return chosen

        return choose_move(player, turn, depth)


def game(runs):
    start_time = time.time()
    p1 = 0
    p2 = 0
    tie = 0
    B = Board()
    for run in range(1, runs + 1):
        B.reset()
        player = 1 if random.random() < 0.5 else 0
        turn = 0
        while True:
            turn += 1
            # print('turn:', turn)
            # B.draw(player)
            if player == 0:
                # m = B.best_move(player, turn)  # TODO: Make this switchable
                m = B.launch_mini_max(player, turn)
            else:
                m = B.random_move(player)
            B.do_move(m, player)
            player = 1 - player
            if B.terminal():
                break
        result = B.quick_result()
        # print(B.result())
        if result < 0:
            p1 += 1
        elif result > 0:
            p2 += 1
        else:
            tie += 1

    print('RESULT: ', p1, ':', tie, ':', p2)
    print("--- %s seconds ---" % (time.time() - start_time))


def gather_info(runs):
    B = Board()
    player = 1 if random.random() < 0.5 else 0
    for k in range(runs):
        B.reset()
        while True:
            m = B.random_move(player)
            B.do_move(m, player, his=True)
            player = 1 - player
            if B.terminal():
                break
        B.update_stats(B.quick_result())
    if runs:
        B.save()


def pretty_read():
    mini_b = Board()
    print("Played:", mini_b.scores_games, "games!")
    for turn, vals in enumerate(mini_b.scores):
        print("Turn", turn, "scores:")
        arr = np.array(vals, dtype=int)
        print(arr)


game(1000)
# pretty_read()
