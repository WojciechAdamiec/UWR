from wdi import*

a = Array(101)
for i in range(100):
    a[i] = i + 0.5
a[100] = 16


x = a[100]
lewy = 0
prawy = 99
while lewy < prawy:
    k = (lewy + prawy) // 2
    if a[k] < x:
        lewy = k + 1 #Tutej musi być + 1, bo zaokrąglenie wynikające z dzielenia całkowitego może niczego nie zmienic
    else:
        prawy = k - 1
print(lewy, prawy)





