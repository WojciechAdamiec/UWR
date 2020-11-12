slowa = []

for x in open('caryca.txt'):
    y = x.split()
    for e in y:
        if e != "":
            slowa.append(e)
slowa2 = []
for i in range(len(slowa)):
    a = list(slowa[i])
    for w in a:
        if w in [".", ",", "!", '"', "'", "?"]:
            a.remove(w)
    slowa2.append(''.join(a))
long = 0
for e in slowa2:
    l = len(e)
    if l > long:
        long = l
lista3 = []
for e in slowa2:
    if len(e) == long:
        lista3.append(e)
lista3.sort()
for e in lista3:
    print(e)

