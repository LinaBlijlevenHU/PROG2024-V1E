"""
Demonstratie van een aantal methoden uit de random-library.
"""
import random

# Namen van de studenten
studenten = ["Max", "Ticho", "Vasco", "Camil", "Jian", "Ashraf", "Howick", "Skip"]

# Maak een random leerteam (selecteer uit studenten, selecteer 4 van de studenten)
leerteam1 = random.sample(studenten, 4)
print(leerteam1)

# Shuffle de studenten (deze functie past de lijst zelf aan)
random.shuffle(studenten)
print(studenten)

# Knip in de lijst om twee teams te maken
# We doen dit door middel van indexering.
leerteam1 = studenten[0:4]      # Student op index 0-3
leerteam2 = studenten[4:8]      # Student op index 4-7

print(leerteam1)
print(leerteam2)

# Kies een willekeurige student uit als klassenvoorzitter.
# random.choice neemt hiervoor een lijst aan en maakt één enkele keuze.
print(f"{random.choice(studenten)} wordt de klassenvoorzitter!")
