"""
maanden_dictionary.py

Voorbeeld V1H
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

# Of andersom: trucje om keys en values om te draaien
maand_naar_number = dict(zip(number_naar_maand.values(), number_naar_maand.keys()))
print(maand_naar_number)

print(f"De maanden van het jaar zijn {number_naar_maand.values()}")
print(f"De maandnummers zijn {number_naar_maand.keys()}")

maand = input("Which month is it?").lower()

# Lelijke manier :(
if maand == "january":
    print(f"Het is de 1ste maand van het jaar.")
elif maand == "february":
    print(f"Het is de 2nd maand van het jaar.")
elif maand == "march":
    print(f"Het is de 3rd maand van het jaar.")
elif maand == "april":
    print(f"Het is de 4th maand van het jaar.")
elif maand == "may":
    print(f"Het is de 5th maand van het jaar.")
elif maand == "june":
    print(f"Het is de 6th maand van het jaar.")
elif maand == "july":
    print(f"Het is de 7th maand van het jaar.")
elif maand == "august":
    print(f"Het is de 8th maand van het jaar.")
elif maand == "september":
    print(f"Het is de 9th maand van het jaar.")
elif maand == "october":
    print(f"Het is de 10th maand van het jaar.")
elif maand == "november":
    print(f"Het is de 11th maand van het jaar.")
elif maand == "december":
    print(f"Het is de 12th maand van het jaar.")
else:
    print(f"Dat is geen geldige maand.")

# Sigma manier
# Vergeet de capitalize niet, als het ook zo geschreven is in je dict
getal = maand_naar_number[maand.capitalize()]
print(f"{maand.capitalize()} is de {getal} de maand van het jaar.")