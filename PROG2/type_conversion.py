"""
Werken met verschillende datatypes
"""

# We gebruiken de input-functie om een leeftijd op te vragen.
# Deze zetten we om naar een integer, zodat we eventueel kunnen rekenen/vergelijken.
ans = int(input("Wat is je leeftijd?\n"))

# We kunnen altijd het type van onze variabelen checken met de type()-functie.
print(type(ans))

# F-string: Impliciet casten
# Als je print met een f-string hoef je niet eerst alle variabelen terug om te zetten naar strings.
print(f"Je leeftijd is {ans}")

# Standaard print: Expliciet casten
# Als we printen met de plus-operator moeten we eerst casten naar string.
print("Je leeftijd is " + str(ans))