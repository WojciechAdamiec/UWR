dic = set()

for x in open('dic.txt', encoding='UTF-8'):
    dic.add(x.strip())

lines = []

for x in open('zad2_input.txt', encoding='UTF-8'):
    lines.append(x.strip())

def divide(string):
    decay = {'':''}
    value = {'': 0}

    def rec(small):
        counter = 0
        word = ''
        length = len(small)
        while counter < length:
            word = word + small[counter]
            if word in dic:
                rest = small[counter + 1:]
                if rest in decay:
                    current = value[rest] + len(word)**2
                    if small not in decay or value[small] < current:
                        decay[small] = word + ' ' + decay[rest]
                        value[small] = current
                else:
                    rec(rest)
                    if rest in decay:
                        current = value[rest] + len(word)**2
                        if small not in decay or value[small] < current:
                            decay[small] = word + ' ' + decay[rest]
                            value[small] = current
            counter = counter + 1
    rec(string)
    return decay[string]


output = open('zad2_output.txt', 'r+', encoding='UTF-8')
for line in lines:
    new_line = divide(line)
    print(new_line)
    output.write(new_line + '\n')
output.close()
