from turtle import*


tracer(0, 1)

pix = 5


def pixel(a, b, c):
    pu()
    goto(-200 + a * pix, 200 - b * pix)
    pd()
    color((c[0] / 255, c[1] / 255, c[2] / 255))
    begin_fill()
    for i in range(4):
        fd(pix)
        rt(90)
    end_fill()
    pu()


inf = []

for x in open('zadanko.txt'):
    inf.append(x.strip())
for i in range(len(inf)):
    a = inf[i].strip()
    print(a)
    inf[i] = a


print(inf)
update()
xd = input()
