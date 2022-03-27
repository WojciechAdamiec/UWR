L = []
X = []
Wynik = []

for x in open('slowa.txt', encoding="utf8"):
    L.append(x.strip())

for y in open('oim.txt', encoding="utf8"):
    for z in (y.strip()).split():
        X.append(z)

A = []
for y in [3, 4, 5, 6, 7, 8, 9, 10]:
    for i in range(len(X) - y):
        A = []
        for x in range(y):
            A.append(X[i + x])
        slowo = []
        for e in A:
            slowo.append(e[0].lower())
        w = ''.join(slowo)
        if w in L:
            print(w, ' '.join(A))
