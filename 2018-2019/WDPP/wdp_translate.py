from collections import defaultdict as dd
import random


pol_ang = dd(list)

for x in open('pol_ang.txt'):
    x = x[:-1]
    wiersz = x.split('=')
    if len(wiersz) != 2:
        continue
    pol, ang = wiersz
    pol_ang[pol].append(ang)
    
def tlumacz(L):
    wynik = []
    for w in L:
        if w in pol_ang:
            wynik.append(random.choice(pol_ang[w]))
        else:
            wynik.append('?' + w)
    return wynik
    
        
for wiersz in open('tekst.txt'):
    wiersz = wiersz.split()
    print (' '.join(tlumacz(wiersz)))
    
    
