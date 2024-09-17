"""
variabelen_omwisselen.py

Soms moeten we de waarde van twee elementen kunnen verwisselen.
Bijvoorbeeld binnen een lijst (in algoritmes die sorteren!).

We hebben in Python twee manieren om dit aan te pakken.
"""
a = 5
b = 3

print(a, b)

# Methode 1: taalongevoelig
# Twee variabelen wisselen. Vergelijk het met het omwisselen van de inhoud
# van twee glazen: rood en blauw. Dit zou ook niet kunnen zonder extra glas!
# Het extra glas in dit scenario is de variabele temp(orary).
temp = b    # We gebruiken temp als een tijdelijke opslag voor b
b = a       # Nu kunnen we b overschrijven met de waarde van a
a = temp    # De waarde van b is al overschreven met a, dus we gebruiken de 'backup' van b

print(a, b)

# Methode 2: dit kan niet in elke programmeertaal,
# maar wel in Python :)
# Twee variabelen wisselen
a, b = b, a

print(a, b)