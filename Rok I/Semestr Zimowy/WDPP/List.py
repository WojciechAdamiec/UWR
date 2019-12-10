from wdi import*


class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None


def add(lista, nval):
    while lista.next is not None:
        lista = lista.next
    lista.next = ListItem(nval)


def wypisz(lista):
    while lista is not None:
        print(lista.val)
        lista = lista.next


def delete(lista):
    while lista.next.next is not None:
        lista = lista.next
    lista.next = None

"""
lis = ListItem(3)
for i in range(10):
    add(lis, i)
wypisz(lis)
"""


usu = ListItem(0)
for i in range(1, 10):
    add(usu, i)
delete(usu)
wypisz(usu)
