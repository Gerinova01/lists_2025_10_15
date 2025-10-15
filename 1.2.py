'''
1.3 Feladat
Egészítsük ki az előbbi programot úgy, hogy a kiértékelést követően a felhasználó által megadott szín kerüljön felvételre a listába, és csak ezután történjen meg a lista tartalmának kiírása!
'''

szinek = ['zöld', 'kék', 'piros', 'sárga']
valasz = input("Válassz egy színt: ")

if valasz in szinek:
    print(szinek.index())
    print(szinek)
else:
    print("Ez a szín nincs benne a listában")
    print(szinek)