"""
while_loops.py

Voorbeeld van inputvalidatie.
"""

age = -1

# We gebruiken de while loop, omdat we nog niet weten wanneer we een correct antwoord krijgen.
while age == -1:
    # Vraag de leeftijd van de gebruiker op (als STRING)
    ans = input("Wat is je leeftijd? ")

    # Kunnen we veilig converteren naar een getal?
    if ans.isnumeric():
        ans = int(ans)
    else:
        print("Gebruik alleen getallen!")

        # Stop hier met de uitvoering binnen deze loop
        # en vraag het de gebruiker nog een keer.
        continue

    # Voer een check uit om te kijken of de leeftijd ook logisch is.
    if ans >= 0 and ans <= 120:
        # We passen age pas aan als we zeker weten dat deze numeriek
        # én logisch is.
        age = ans
    else:
        print("Dat is geen geldige leeftijd, pannekoek")