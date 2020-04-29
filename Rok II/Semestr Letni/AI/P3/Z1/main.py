import numpy as np
import itertools


class Nonogram:

    def __init__(self, rows, cols, row_desc, col_desc):
        self.r = rows                # Number of rows
        self.c = cols                # Number of cols
        self.row_desc = row_desc     # Rows description
        self.col_desc = col_desc     # Cols description

        self.data = np.zeros((rows, cols), dtype=np.int8)

        # We set initial Domains
        self.rowDomain = [self.get_domain(row, self.c) for row in self.row_desc]
        self.colDomain = [self.get_domain(col, self.r) for col in self.col_desc]

        self.isTransposed = False

    def __str__(self):
        return '\n'.join([''.join(["#" if v == 1 else "." for v in row])
                          for row in (self.data if not self.isTransposed else self.data.T)])

    def info(self):
        print('==============================')
        print()
        print(self)
        print()
        print('==============================')

    def transpose(self):
        self.r, self.c = self.c, self.r
        self.rowDomain, self.colDomain = self.colDomain, self.rowDomain
        self.data = self.data.transpose()
        self.isTransposed = not self.isTransposed

    def get_domain(self, row_desc, row_len):

        # This function returns domain (set) for a row (with desc and len)
        row_desc = list(row_desc)

        # Simple case when only one number defines a row
        if len(row_desc) == 1:
            zeros = row_len - row_desc[0]
            return {tuple([0]*i + [1]*row_desc[0] + [0]*(zeros-i))
                    for i in range(zeros + 1)}

        limit = row_len - row_desc[-1]
        ans = []

        # We take all combinations (starting positions of series)
        # If they satisfy all rules we add them to domain
        for comb in itertools.combinations(range(limit + 1), len(row_desc)):
            not_overlapping = True
            for c in range(len(comb) - 1):
                if comb[c] + row_desc[c] >= comb[c+1]:
                    not_overlapping = False
                    break
            if not_overlapping:
                t = [0] * row_len
                for i, c in enumerate(comb):
                    for j in range(c, c + row_desc[i]):
                        t[j] = 1
                ans.append(t)

        return {tuple(a) for a in ans}

    def intersect_domain(self, dom, pixel=1):
        # Function deduces which pixels has to be on or off
        value = 1 if pixel else 0
        anti_value = 0 if value else 1

        dom = list(dom)  # It is a set, so we need conversion
        size = len(dom[0])

        intersect = [anti_value] * size
        for pos in range(size):
            flag = True
            for each in dom:
                if each[pos] != value:
                    flag = False
                    break
            if flag:
                intersect[pos] = value
        return intersect

    def is_ok(self):
        # Returns True if Nonogram is already done
        for i, row in enumerate(self.data):
            if tuple(row) not in self.rowDomain[i]:
                return False

        for j, col in enumerate(self.data.T):
            if tuple(col) not in self.colDomain[j]:
                return False
        return True

    def constrain_domain(self, pixels, pixel):
        # We eliminate elements of Domains which don't satisfy already set pixels
        for i, j in pixels:
            to_remove = []
            for col in self.colDomain[j]:
                if col[i] == pixel:
                    to_remove.append(col)
            for rm in to_remove:
                self.colDomain[j] -= {rm}

    def work(self):

        while not self.is_ok():
            self.info()
            pixels_on = set()
            pixels_off = set()

            for i, row in enumerate(self.rowDomain):

                # We deduce which pixels must be on
                for j, r in enumerate(self.intersect_domain(row, pixel=1)):
                    if r == 1:
                        self.data[i][j] = 1
                        pixels_on.add((i, j))

                # We deduce which pixels must be off
                for j, r in enumerate(self.intersect_domain(row, pixel=0)):
                    if r == 0:
                        self.data[i][j] = 0
                        pixels_off.add((i, j))

            # We constrain domains based on already set up pixels
            self.constrain_domain(pixels_on, pixel=0)
            self.constrain_domain(pixels_off, pixel=1)

            # We do transposition to work on columns (rows)
            self.transpose()


def init(file):
    lines = []
    with open(file) as f:
        for line in f:
            lines.append(list(map(int, line.strip('\n').split())))
    r, c = lines[0][0], lines[0][1]

    return Nonogram(r, c, row_desc=lines[1:r+1], col_desc=lines[r+1:])


if __name__ == '__main__':

    file_input = 'zad_input.txt'
    file_output = 'zad_output.txt'

    image = init(file_input)

    image.work()
    print(image)

    paint = open(file_output, "w")
    print(image, file=paint)
