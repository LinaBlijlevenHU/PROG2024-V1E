"""
if_indentatie_voorbeeld.py

Dit voorbeeld laat zien hoe een if-statement werkt en hoe indentatie (spaties & tabs)
hier invloed op heeft.
"""

# Vraag de gebruiker om een temperatuur en zet deze om naar een getal.
temp = int(input("Wat is de temperatuur in F?"))

# Check of het erg warm is buiten!
if temp > 86:
    print("Het is warm! Drink extra water.")

# Staat dit ingesprongen? Dan hoort het bij het if-block. Zo niet, dan wordt deze regel code altijd uitgevoerd.
print("Fijne dag verder!")
