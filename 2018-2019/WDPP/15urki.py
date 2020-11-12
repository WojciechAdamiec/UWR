def fractal(n):
    if n == 0:
        return 1
    else:
        return n * fractal(n - 1)


def fractal2(n):
    def fractal_iter(n, acc):
        if n == 0:
            return acc
        else:
            return fractal_iter(n - 1, acc * n)
    return fractal_iter(n, 1)


print(fractal2(5))
