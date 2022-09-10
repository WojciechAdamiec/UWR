class Formula:

    def evaluate(self, var):
        pass

    def __str__(self):
        pass


class TConst(Formula):

    def evaluate(self, var):
        return True

    def __str__(self):
        return 'T'


class FConst(Formula):

    def evaluate(self, var):
        return False

    def __str__(self):
        return 'F'


class Neg(Formula):

    def __init__(self, content):
        self.content = content

    def evaluate(self, var):
        return not self.content.evaluate(var)

    def __str__(self):
        return '~' + str(self.content)


class Var(Formula):

    def __init__(self, name):
        self.name = name

    def evaluate(self, var):
        for pair in var:
            if pair[0] == self.name:
                return pair[1]
        print("Error, no such variable in environment")
        return False

    def __str__(self):
        return self.name


class Con(Formula):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, var):
        return self.left.evaluate(var) and self.right.evaluate(var)

    def __str__(self):
        return '(' + str(self.left) + '^' + str(self.right) + ')'


class Dis(Formula):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, var):
        return self.left.evaluate(var) or self.right.evaluate(var)

    def __str__(self):
        return '(' + str(self.left) + 'v' + str(self.right) + ')'


class Imp(Formula):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, var):
        return (not self.left.evaluate(var)) or self.right.evaluate(var)

    def __str__(self):
        return '(' + str(self.left) + '->' + str(self.right) + ')'


class Bic(Formula):

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def evaluate(self, var):
        a = self.left.evaluate(var)
        b = self.right.evaluate(var)
        return (a and b) or (not a) and (not b)

    def __str__(self):
        return '(' + str(self.left) + '<->' + str(self.right) + ')'
