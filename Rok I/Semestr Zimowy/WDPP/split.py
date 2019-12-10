def splitter(n):
    L = list(n)
    i = 0
    s = ""
    a = True
    X = []
    while i < len(L):
        if L[i] == " ":
            p = True
        else:
            p = False
            s = str(s) + str(L[i])
        if (not a) and p:
            X.append(s)
            s = ""
        a = p
        i = i + 1
    return X


print(splitter("   jabłko   owoc drzewo liscie   "))
"[[1]*20] * 20"