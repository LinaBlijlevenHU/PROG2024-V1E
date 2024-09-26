"""
dict_voorbeeld_count.py

Voorbeeld V1H

1. Telt alle cijfers die een student heeft gehaald
2. Telt hoe vaak elk woord voorkomt in het Bee Movie script.
"""

import json
import re

# Cijfers van een student
cijfers = [8, 5, 3, 6, 9, 6, 8, 3, 8, 7, 5, 9, 7]

def frequency_counter(lst):
    """
    Tel alle frequenties binnen een gegeven lijst en
    geef een dictionary met frequenties terug

    Tip:
        probeer dit korter met dict.get() of dict.count()

    :param:     Lijst om in te tellen
    :return:    Dictionary met frequenties
    """
    # Maak alvast een lege dictionary aan
    freq = {}

    for cijfer in lst:
        # Hebben we dit cijfer eerder gezien?
        if cijfer in freq.keys():
            # Pak de huidige waarde en tel daar 1 bij op.
            freq[cijfer] += 1
        # Eerste keer dat we het cijfer zien
        else:
            # Met deze keer erbij hebben het cijfer nu 1x gezien.
            freq[cijfer] = 1

    return freq


# We kunnen nu inzicht krijgen in de cijfers van een student met behulp van deze functie.
print(frequency_counter(cijfers))

"""
Beemovie (Extra)

Maar dit is herbruikbaar: deze functie kunnen we ook gebruiken om het script van de Bee Movie 
mee te analyzeren.
"""

# Open het volledige script van de Bee Movie
with open("beemovie.txt") as file:
    # Lees alles
    text = file.read()

    # Verwijder symbolen
    text = re.sub('[(){}<>?!.,*/-]', '', text)

    # Split op woorden
    words = text.split()

    # Ales naar lowercase (dit is list comprehension)
    words = [word.lower() for word in words]


# Tel hoe vaak elk woord voorkomt in de bee movie.
word_counts = frequency_counter(words)
print(word_counts)
print(f"Het woord 'bee' komt {word_counts["bee"]}x voor.")

# De sorted-functie kan ons helpen om te sorteren op de values (item[1] geeft dit aan)
sorted_dict = dict(sorted(word_counts.items(), key=lambda item: item[1], reverse=True))
print(json.dumps(sorted_dict, indent=4))
