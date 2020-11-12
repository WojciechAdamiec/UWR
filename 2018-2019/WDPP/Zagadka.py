slowa = []
poskladane = []


for x in open('slowa2.txt'):
    for e in x.split():
        slowa.append(e)


def pobierz(tekst):
    L = {}
    for e in tekst:
        if e in L:
            L[e] = L[e] + 1
        else:
            L[e] = 1
    return L


def doable(first, second):
    for e in first:
        if second[e] is


print(pobierz("adampokuta"))
