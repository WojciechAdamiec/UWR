print("Python Zaawansowany: Lista 1; Zadanie 6")
print()


def tabliczka(x1, x2, y1, y2):
    hor = [i for i in range(y1, y2 + 1)]
    ver = [i for i in range(x1, x2 + 1)]
    max = x2 * y2
    space = len(str(max))
    print(space * " ", end=" ")
    for v in ver:
        outcome = (space - len(str(v))) * " " + str(v)
        print(outcome, end=" ")
    print()
    for h in hor:
        outcome = (space - len(str(h))) * " " + str(h)
        print(outcome, end=" ")
        for v in ver:
            outcome = h * v
            outcome = (space - len(str(outcome))) * " " + str(outcome)
            print(outcome, end=" ")
        print()

    print()


tabliczka(3, 6, 2, 8)
print()
print()
tabliczka(10, 14, 17, 22)
