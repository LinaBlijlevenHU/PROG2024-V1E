import math


def pythagoras(a, b):
    """ Neem twee zijden van een driehoek aan en bereken de lengte van de lange zijde. """
    c = math.sqrt(a**2 + b**2)
    return c


print(pythagoras(3, 4))