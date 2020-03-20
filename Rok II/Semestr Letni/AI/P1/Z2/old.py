dic = set()

for x in open('dic.txt', encoding='UTF-8'):
    dic.add(x.strip())

lines = []

for x in open('zad2-input.txt', encoding='UTF-8'):
    lines.append(x.strip())

def divide(string):
    length = len(string)
    counter = 0
    magnitude = 0
    words = []
    word = ''
    best = ''
    power = 0
        
    while word != string:
        # print('Cycle!', words,'word: ', word, 'magnitude: ', magnitude, 'counter: ', counter)
        while counter < length:
            # print('Inner!', words,'word: ', word, 'magnitude: ', magnitude, 'counter: ', counter)
            word = word + string[counter]
            if word in dic:
                words.append(word)
                magnitude = magnitude + len(word)
                word = ''
            counter = counter + 1
        if word == '':
            # print('WYNIK: ', words)
            pontential = 0
            for element in words:
                pontential = pontential + len(element) ** 2
            if pontential > power:
                power = pontential
                best = ' '.join(words)
        
        if word != string:
            last = words.pop(len(words) - 1)
            diff = len(last)
            counter = magnitude
            magnitude = magnitude - diff
            # print(word)
            word = last
        
    return best


output = open('zad2-output.txt', 'r+', encoding='UTF-8')
for line in lines:
    new_line = divide(line)
    print(new_line)
    output.write(new_line + '\n')
output.close()
