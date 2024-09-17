"""
kwadraat_functie.py

Voorbeeld van functies met behulp van een sommetje.
"""


# Functiedefinitie: hier geven we aan wat de functie moet doen. De eerste regel
# heet ook wel een 'functie signature'.
# Verdieping: https://dagster.io/blog/python-type-hinting (om functies gebruiksvriendelijker te maken)
def kwadraat(getal):
    """
    Eigenlijk doet deze functie het getal in het kwadraat plus 10.

    :param getal:   Het getal om te kwadrateren en 10 bij op te tellen
    :return:        Resultaat van de som
    """
    res = getal ** 2 + 10

    # Return zorgt ervoor dat het resultaat in de code hieronder
    # weer in een variabele wordt opgeslagen. Als je het
    # resultaat hier alleen print, heeft de code hieronder geen toegang meer!
    return res

# Getal om mee te testen
gtal = 2

# Functie-aanroep: hier wordt de functie in gebruik genomen
# met de gewenste parameters. We roepen de naam van de functie aan
# en geven er in de juiste volgorde onze eigen getallen aan mee.
# Daarnaast moeten we een nieuwe variabele aanmaken om het getal in
# op te slaan, zodat we het daarna kunnen printen.
gtal2 = kwadraat(gtal)

# Wat gebeurt er als je "return res" hierboven vervangt door "print(res)"?
print(f"Het kwadraat van {gtal} + 10 = {gtal2}")

# Nu gaan we de functie nog een aantal keren gebruiken, dit
# keer doen we dat ook met een loop!
getallen = [1, 2, 3, 4, 5]

# We gaan de functie gebruiken voor elk getal in de lijst.
# Zo kunnen we meerdere berekeningen afhandelen met weinig code
# en werkt ons programma voor elke hoeveelheid getallen die we
# willen gebruiken.
for g in getallen:
    # Roep de functie aan met het huidige getal uit de lijst
    ans = kwadraat(g)
    print(f"Het kwadraat van {g} + 10 = {ans}")