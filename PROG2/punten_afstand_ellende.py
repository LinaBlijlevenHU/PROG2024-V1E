"""
punten_afstand_ellende.py

Uitwerking van een oefening (d) uit de slides: het berekenen of gegeven coördinaten binnen een cirkel liggen,
met behulp van de stelling van Pythagoras.
"""
import math

# We hebben een punt op de grafiek. We willen gaan bepalen of deze binnen een
# gegeven cirkel valt.
point = (5, 5)

# De radius van de gegeven cirkel. Het midden van deze cirkel bevindt zich op (0, 0).
radius = 7

# We tekenen een denkbeeldige driehoek: we weten de lengte van de rechte zijden (5 en 5).
# Hiermee bepalen we de afstand tot het middenpunt (de lange zijde van de denkbeeldige driehoek).
# Hiervoor passen we de stelling van Pythagoras toe: A^2 + B^2 = C^2
point_distance = math.sqrt(point[0]**2 + point[1]**2)

# Als de lange zijde korter is dan de radius ligt het punt binnen de cirkel.
print(point_distance < radius)
