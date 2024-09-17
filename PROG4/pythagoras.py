"""
pythagoras.py

Voorbeeld van de pythagoras-functie, die twee argumenten gebruikt.
Uiteraard kunnen functies nog veel meer argumenten accepteren:
we proberen alleen onze functies ook niet té ingewikkeld te maken.
Het liefst krijgt elke functie maar één verantwoordelijkheid.
"""
import math

def pythagoras(a, b):
    """ Neem twee zijden van een driehoek aan en bereken de lengte van de lange zijde. """
    c = math.sqrt(a ** 2 + b ** 2)
    return c


# Aanroepen
print(pythagoras(3, 4))

'Extra verdieping'
def pythagoras_met_type_hinting(a: float, b: float) -> float:
    """
    Functies met type-hinting zien er bijvoorbeeld zo uit.
    """
    return pythagoras(a, b)


# Extra
print(pythagoras_met_type_hinting(3, 4))
