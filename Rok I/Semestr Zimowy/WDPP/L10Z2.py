from L10Z1 import*


L = []
for x in open('test.txt', encoding="utf8"):
    L.append(x.strip())


result = []
for i in range(len(L)):
    A = []
    for j in range(1, 30):
        A.append(szyfr(L[i], j))
    for e in A:
        if e[2] in L[i:]:
            result.append((e[0], e[2]))
print(result)


#Problem z polskimi znakami w win10
#Problem ze złożonością dla dużych plików
