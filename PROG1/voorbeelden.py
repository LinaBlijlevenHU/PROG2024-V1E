"""
voorbeelden.py
"""

# Print "Hello World"
print("Hello world")

# Operatoren:
# +: plus
# -: min
# /: gedeeld door
# *: keer
# //: gedeeld door en naar beneden afronden (floor division)
# %: modulo
# **: tot de macht (bijv. 2**3 is 2^3)
# wortel: tot de macht 1/2

print("\n5 gedeeld door 2 is:")
print(5 / 2)

print("\n5 // 2 is:")
print(5 // 2)

print("\n5 % 2 is:")
print(5 % 2)

print("\nDe absolute waarde van -2 is:")
print(abs(-2))

print("\n\n")
# Variabelen in snake_case
leeftijd = 19
heeft_rijbewijs = True

# AND
print("Mag deze persoon rijden?")
print(leeftijd >= 18 and heeft_rijbewijs)

# Variabelen kun je aanpassen
leeftijd = 17

# AND
print("Mag deze persoon rijden?")
print(leeftijd >= 18 and heeft_rijbewijs)

# Variabelen
lina_age = 29
lisa_age = lina_age - 2

# Strings and string functions
tekst = "Welkom bij V1H!"
naam = "Pietje"

print("\nStaat V1H in de tekst?")
# Substring
print("V1H" in tekst)

# Printen met string concatenation (+je)
print("\nHallo " + naam)
# Printen met een f-string
print(f"\nHallo {naam}")

