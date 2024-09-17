# Functiedefinitie
def kwadraat(getal):
    res = getal ** 2 + 10
    return res

# 1x aanroepen
gtal = 2
# Functie-aanroep: activatie van de functie
gtal2 = kwadraat(gtal)

print(f"Het kwadraat van {gtal} + 10 = {gtal2}")

getallen = [1, 2, 3, 4, 5]

# 1x voor elk element in een lijst
for g in getallen:
    ans = kwadraat(g)
    print(f"Het kwadraat van {g} + 10 = {ans}")