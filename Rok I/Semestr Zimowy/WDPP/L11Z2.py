def ppn(s):
    S = {}
    i = 1
    for e in s:
        if e in S:
            pass
        else:
            S[e] = i
            i = i + 1
    A = []
    for e in s:
        A.append(str(S[e]))
    return '-'.join(A)


print(ppn('tata'))
print(ppn('mama'))
print(ppn('wojtek'))