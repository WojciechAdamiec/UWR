data = []
for x in open('zad4_input.txt'):
    data.append(x.strip().split(' '))


def opt_dist(array, D):
    length = len(array)
    start = 0
    end = D - 1
    best = 0
    ones = 0
    for i in range(length - D + 1):
        aux = 0
        for j in range(start, end + 1):
            if (array[j] == '1'):
                aux += 1
        if aux > best:
            best = aux
        start += 1
        end += 1
    for element in array:
        if element == '1':
            ones += 1
    return D - 2 * best + ones


f = open('zad4_output.txt', 'w+')
for dat in data:
    f.write(str(opt_dist(list(dat[0]), int(dat[1]))) + '\n')
