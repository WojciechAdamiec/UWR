litery = {}

for i in ['A', 'E', 'I', 'N', 'O', 'R', 'S', 'W', 'Z']:
    litery[i] = 1
for i in ['C', 'D', 'K', 'L', 'M', 'P', 'T', 'Y']:
    litery[i] = 2
for i in ['B', 'G', 'H', 'J', 'Ł', 'U']:
    litery[i] = 3
for i in ['Ą', 'Ę', 'F', 'Ó', 'Ś', 'Ż']:
    litery[i] = 5
litery['Ć'] = 6
litery['Ń'] = 7
litery['Ź'] = 9

slowa = []
for x in open('caryca.txt'):
    y = x.strip()
    c = y.split(' ')
    for d in c:
        slowa.append(d)


for i in range(len(slowa)):
    if len(slowa[i]) > 0 and slowa[i][-1] in [".", ';', '"', '!', ',', ':']:
        slowa[i] = slowa[i][:-1]

max = 0
wynik = ''


def value(e):
    val = 0
    S = list(e.upper())
    for s in S:
        if s in litery:
            val = val + litery[s]
        else:
            return 0
    return val


for e in slowa:
    if len(e) == 7:
        x = value(e)
        if x > max:
            max = x
            wynik = e

print(max, wynik)


