'''
1.1 Feladat
A program tároljon egy listában színeket.
Kérjen be a felhasználótól egy színt, és állapítsa meg,
hogy a megadott szín már szerepel-e az adott listában.
A vizsgálat eredményéről tájékoztassa a program a felhasználót,
 és írja ki egymás mellé vesszővel elválasztva a lista által tartalmazott színeket!

'''

szinek = ['zöld', 'kék', 'piros', 'sárga']
valasz = input("Válassz egy színt: ")

if valasz in szinek:
    print("Ez a szín benne van a listában")
    print(szinek)
else:
    print("Ez a szín nincs benne a listában")
    print(szinek)
