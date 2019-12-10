slownik1 = {}
slownik2 = {}
alf = 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'
for i in range(len(alf)):
    slownik1[i] = alf[i]
for i in range(len(alf)):
    slownik2[alf[i]] = i


def szyfr(slowo, klucz):
    wynik = []
    for e in slowo:
        wynik.append(slownik2[e])
    for i in range(len(wynik)):
        wynik[i] = (wynik[i] + klucz) % 31
    return slowo, klucz, ''.join([slownik1[x] for x in wynik])



