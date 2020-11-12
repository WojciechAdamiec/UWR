from math import pi
#kwadrat = "kwadrat", (x1, y1), (x2, y2)
#kolo = "kolo", (x1, y1), r
#trojkat = "trojkat", (x1, y1), (x2, y2), (x3, y3)


def utworz():
    figura = []
    print('Podaj rodzaj figury: ')
    a = str(input())
    figura.append(a)
    if figura[0] == 'kwadrat':
        print('Podaj współrzędne dowolnego wierzchołka: ')
        print('x: ', end='')
        x = float(input())
        print('y: ', end='')
        y = float(input())
        figura.append((x, y))
        print('Podaj współrzędne naprzeciwległego wierzchołka: ')
        print('x: ', end='')
        x = float(input())
        print('y: ', end='')
        y = float(input())
        figura.append((x, y))
    elif figura[0] == 'kolo':
        print('Podaj współrzędne środka: ')
        print('x: ', end='')
        x = float(input())
        print('y: ', end='')
        y = float(input())
        figura.append((x, y))
        print('Podaj długość promienia: ')
        print('r: ', end='')
        r = float(input())
        if r <= 0:
            print('Niedozwolony promień: ')
            return 'Error'
        figura.append(r)
    elif figura[0] == 'trojkat':
        print('Podaj współrzędne pierwszego wierzchołka: ')
        print('x: ', end='')
        x = float(input())
        print('y: ', end='')
        y = float(input())
        figura.append((x, y))
        print('Podaj współrzędne drugiego wierzchołka: ')
        print('x: ', end='')
        x = float(input())
        print('y: ', end='')
        y = float(input())
        figura.append((x, y))
        print('Podaj współrzędne trzeciego wierzchołka: ')
        print('x: ', end='')
        x = float(input())
        print('y: ', end='')
        y = float(input())
        figura.append((x, y))
    else:
        print('Nie ma takiej figury')
        return 'figura type error'
    return figura


def pole(figura):
    if figura[0] == 'kwadrat':
        return (figura[2][0] - figura[1][0])**2
    if figura[0] == 'kolo':
        return pi * ((figura[2])**2)
    if figura[0] == 'trojkat':
        return 0.5 * abs((figura[2][0] - figura[1][0])*(figura[3][1] - figura[1][1]) - (figura[2][1] - figura[1][1])*(figura[3][0] - figura[1][0]))
    return 0


def przesun(figura, x, y):
    if figura[0] == 'kwadrat':
        figura[1] = figura[1][0] + x, figura[1][1] + y
        figura[2] = figura[2][0] + x, figura[2][1] + y
    if figura[0] == 'trojkat':
        figura[1] = figura[1][0] + x, figura[1][1] + y
        figura[2] = figura[2][0] + x, figura[2][1] + y
        figura[3] = figura[3][0] + x, figura[3][1] + y
    if figura[0] == 'kolo':
        figura[1] = figura[1][0] + x, figura[1][1] + y


def sumapol(lista):
    wynik = 0
    for e in lista:
        wynik = wynik + pole(e)
    return wynik
