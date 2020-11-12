slowa = []
pom = []


for x in open('zadanie.txt'):
    slowa.append(x.strip())
for i in range(len(slowa)):
    if slowa[i] != "":
        pom.append(slowa[i])
for i in range(len(pom)):
    pom[i] = pom[i].capitalize()
    pom[i] = str(pom[i]) + str(".")


print(slowa)
print(pom)
