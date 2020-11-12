def function(n, m):
    dic = {}
    dic2 = {}
    for e in n:
        if e is not ' ':
            if e in dic:
                dic[e] = dic[e] + 1
            else:
                dic[e] = 1
    for e in m:
        if e is not ' ':
            if e in dic2:
                dic2[e] = dic2[e] + 1
            else:
                dic2[e] = 1
    for d in dic:
        if d not in dic2 or dic[d] > dic2[d]:
            return "Nie"
    return "Tak"


print(function('wilkor alfa', 'wilkor alfa'))
print(function('wilkor alfa', 'wilkor'))
print(function('wilkor alfa', 'wilkor alfa cos jeszcze'))
print(function('wilkor alfa', 'alfa wilkor'))






