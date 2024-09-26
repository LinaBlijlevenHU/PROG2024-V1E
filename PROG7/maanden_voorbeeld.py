"""
maanden_voorbeeld.py

V1E maanden voorbeeld
"""

number_naar_maand = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

# items(), values() en keys()
print(number_naar_maand.items())

for (nummer, maand) in number_naar_maand.items():
    print(f"{maand} is de {nummer}de maand van het jaar.")

print(f"De maanden van het jaar zijn: {number_naar_maand.values()}")
print(f"De nummers van de maanden van het jaar zijn: {number_naar_maand.keys()}")

# Wissel de positie van keys en values, zodat we nu nummers kunnen opzoeken op basis van maanden
maand_naar_number = dict(zip(number_naar_maand.values(), number_naar_maand.keys()))

