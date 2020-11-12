from copy import copy

L = []
for x in open('slowa.txt', encoding="utf8"):
    L.append(x.strip())
X = []
for e in L:
    value = True
    for l in ['aąbcćdeęfghijklłmnoóprsśtuwxyzźż']:
        if l in e:
            a = copy(e)
            a.remove(l)
            if l in a:
                value = False
                break
    if value:
        X.append(e)
print(X)

