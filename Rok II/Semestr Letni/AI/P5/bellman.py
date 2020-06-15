tasks_names = ['1', '2', '3', '6', '8', '9', '10', '11']


def bellman(number):
    global start, Olds, Values
    WIN = 100
    FAIL = -100
    GAMMA = 0.99
    COST = 0
    task_file = 'task' + number + '.txt'
    single_speeds = [-3, -2, -1, 0, 1, 2, 3]
    actions = [(0, 0), (1, 0), (0, 1), (1, 1), (-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)]
    speeds = set()
    for speed1 in single_speeds:
        for speed2 in single_speeds:
            speeds.add((speed1, speed2))
    tiles = set()
    oils = set()
    ends = set()
    states = set()
    start = None
    Values = {}
    Olds = {}
    Guide = {}
    data = []
    for line in open(task_file):
        data.append(line.strip())
    SIZE_Y, SIZE_X = len(data), len(data[0])

    def info():
        print('||||||||')
        print()
        for y in data:
            for x in y:
                print(x, end='')
            print()
        print()
        print('||||||||')

    def init():
        global start
        for y in range(SIZE_Y):
            for x in range(SIZE_X):
                if data[y][x] != '.' and data[y][x] != 'e':
                    tiles.add((x, y))
                if data[y][x] == 'o':
                    oils.add((x, y))
                if data[y][x] == 's':
                    start = x, y
                if data[y][x] == 'e':
                    ends.add((x, y))

        for tile in tiles:
            t_x, t_y = tile
            for speed in speeds:
                s_x, s_y = speed
                states.add((t_x, t_y, s_x, s_y))

        for state in states:
            Olds[state] = 0
            Values[state] = 0
            Guide[state] = (0, 0)

    def move(state, action):
        x, y, vx, vy = state
        if (x, y) not in oils:
            dvx, dvy = action
            vx += dvx
            vy += dvy
            if vx > 3: vx = 3
            if vy > 3: vy = 3
            if vx < -3: vx = -3
            if vy < -3: vy = -3
            x += vx
            y += vy
            new_state = x, y, vx, vy
            return {new_state: 1}
        events = {}
        for act in actions:
            x, y, vx, vy = state
            dvx, dvy = action
            oil_x, oil_y = act
            vx += oil_x
            vy += oil_y
            vx += dvx
            vy += dvy
            if vx > 3: vx = 3
            if vy > 3: vy = 3
            if vx < -3: vx = -3
            if vy < -3: vy = -3
            x += vx
            y += vy
            new_state = x, y, vx, vy
            if new_state in events:
                events[new_state] += 1/9
            else:
                events[new_state] = 1/9
        return events

    def find_value(state):
        if state in Olds:
            return Olds[state]
        x, y, vx, vy = state
        if (x, y) in ends:
            return WIN
        return FAIL

    def update():
        global Olds
        for state in states:
            decisions = []
            for action in actions:
                dic = move(state, action)
                fit = 0
                for var in dic:
                    fit += dic[var] * (COST + GAMMA * find_value(var))
                decisions.append((fit, action, dic))
            best_fit, best_action, best_dic = (max(decisions, key=lambda three: three[0]))
            Guide[state] = best_action
            Values[state] = best_fit
        Olds = Values

    def iterate(N):
        for i in range(N):
            update()
        file_output = 'policy_for_task' + number + '.txt'
        paint = open(file_output, "w")
        for state in states:
            x, y, vx, vy = state
            dvx, dvy = Guide[state]
            print(x, y, vx, vy, '    ', dvx, dvy, file=paint)

    info()
    init()
    iterate(100)


for task in tasks_names:
    bellman(task)
