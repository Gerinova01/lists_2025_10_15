'''
2. Feladat
A program generáljon 10 darab véletlenszámot [1;3] intervallumon, ezeket tárolja egy listában, a lista tartalmát írja ki a képernyőre! A felhasználónak legyen lehetősége megadni egy számot [1;3] intervallumon, és a program törölje ennek a számnak valamennyi előfordulását a listából, majd írja ki a módosított listát a képernyőre!
'''

import random as r

szam = []

for i in range (1,11):
    random = r.randint(1,3)
    szam.append(random)

valasz = int(input("Adj meg egy számot 1 és 3 között! "))

while valasz in szam:
    szam.remove(valasz)

print(szam)