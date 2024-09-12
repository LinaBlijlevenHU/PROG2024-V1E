"""
Demonstratie van de random library
"""
import random

# Als we een seed instellen, zullen we altijd hetzelfde aantal ogen rollen in dezelfde volgorde.
random.seed(67890)

# Rol twee dobbelstenen!
dobbelsteen1 = random.randrange(1, 7)
dobbelsteen2 = random.randrange(1, 7)

# We kunnen ook het resultaat van twee dobbelstenen printen met één print statement als een kleine shortcut.
print(dobbelsteen1, dobbelsteen2)
