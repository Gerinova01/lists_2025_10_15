honapok = ['január', 'február','március', 'április']

#lista típusa
print(type(honapok))

#lista hossza: len()
print(len(honapok))

print(honapok[0])
print(honapok[1])
print(honapok[2])
print(honapok[3])

#hátulról első elem
print(f"Utolsó elem ea listában.{honapok[-1]}")

#csak 1-2 es elem
print(honapok[1:3])

#Az elejétől a a 2-es indexel bezárólag
print(honapok[:3])
#2-ől a végéig
print(honapok[2:])

#join() a lista elemeit egy stringé
print('; '.join(honapok))

#lista bejárása for range ciklussal
for i in range(len(honapok)):
    print(honapok[i])

#lista bejárása for - items
print("\nHonapok\n")
for honap in honapok:
    print(honap)