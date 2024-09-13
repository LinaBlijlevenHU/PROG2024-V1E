# Met strings

lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
alphabet = ""

for e in lijst:
    alphabet = alphabet + e

print(f"Het alfabet is: {alphabet}")

# Met getallen

getallen = [5, 4, 7, 8, 34, 5, 0, 90]
som = 0

for getal in getallen:
    # som = som + getal
    som += getal

print(f"De som van de lijst is: {som}")