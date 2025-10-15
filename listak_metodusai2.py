honapok = ['január', 'február','március', 'április', 'május', 'június']
#honapok = [1,3,5,2]

sorted_honapok = sorted(honapok)
print(honapok)
print(sorted_honapok)

reversed_honapok = sorted(honapok,reverse=True)
print(reversed_honapok)

#adott elem első leőfordulásának indexe
print(honapok.index('március'))

print("április"in honapok)