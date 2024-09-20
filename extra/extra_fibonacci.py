"""
extra_fibonacci.py

Extra voorbeeld met de reeks van Fibonacci (niet in de les behandeld).
Dit scriptje demonstreert nogmaals hoe functies werken en hoe we informatie
kunnen doorgeven met behulp van het return-keyword.

Tip: run dit scriptje met de debug-tool (klik daarvoor op het insect naast de run-knop)
"""

# Eerst moeten we weten wat de reeks van Fibonacci is:
# In deze reeks tellen we steeds de vorige twee getallen bij elkaar op, om de volgende te krijgen.
# Daarom begint deze reeks ook alvast met twee getallen: 0 en 1.
fib = [0, 1]

# Hoeveel getallen we in de reeks gaan berekenen.
aantal = 10


# Functie om het volgende getal te kunnen berekenen.
def fibonacci(previous, previouser):
    """
    Functie om een getal van Fibonacci te berekenen op basis van de vorige twee getallen.
    Dit is natuurlijk een simpele functie, maar je kan hier nog veel meer doen!
    """
    # We tellen eerst de getallen bij elkaar op
    new_number = previous + previouser
    # Dan geven we het resultaat terug:
    return new_number


# Nu kunnen we elk getal gaan berekenen. Het eerste getal is 0, het tweede getal is 1.
# Wij kijken dus vanaf getal 3.
for i in range(2, aantal):
    # Met negatieve indexen kunnen we de vorige twee getallen uit de lijst selecteren.
    # Als we dus steeds onze nieuwe getallen toevoegen, gaat dit altijd goed! :)
    vorig_getal = fib[-1]
    voriger_getal = fib[-2]

    # We kunnen nu het nieuwe getal berekenen. Eigenlijk is dat best simpel,
    # maar we gaan er toch een functie voor gebruiken om te oefenen.
    # !!! Belangrijk: we slaan de waarde uit de functie op in een variabele.
    # Als we dit niet doen, komt er None in de lijst te staan!
    nieuw_getal = fibonacci(vorig_getal, voriger_getal)

    # Nu kunnen we het nieuwe getal toevoegen aan de lijst.
    # De volgende iteratie (keer dat we door de loop heen gaan) zal deze
    # de vorige twee getallen opnieuw correct herkennen.
    fib.append(nieuw_getal)

print(f"De reeks van Fibonacci met {aantal} getallen is {fib}")