honapok = ['január', 'február','március', 'április', 'május', 'június']
honapok.append('július')
print(honapok)

#eleme eltávolítása listából
honapok.pop()
print(f"Utolsó hónap tőrőlése után a lista:\n {honapok}")
torolt_honap = honapok.pop
print(f"Utlsó hónap: {torolt_honap}")
print(honapok)

#torlés adott index alapján
torolt_honap =honapok.pop(0)
print(torolt_honap)

print(honapok.remove("február"))
print(honapok)

#adott index helyére beszúrja a megadott állam
honapok.insert(0,'február')
print(honapok)

#lista ürítése
honapok.clear()
print(honapok)