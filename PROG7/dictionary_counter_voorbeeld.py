"""
dictionary_counter_voorbeeld.py

Count the occurrences within a list using a frequency count function (re-usable function yaaay)
"""
import random

random.seed("V1E")

# 1. Lijst opbouwen met loop
lijst = []

for _ in range(20):
    g = random.randint(65, 95)
    lijst.append(g)
#print(lijst)

# 2. List comprehension
portfoliopunten = [random.randint(0, 95) for _ in range(20)]
print(portfoliopunten)

def frequenties(lijst):
    """
    Tel de frequencies binnen een lijst.
    """
    # Tellen met een dictionary
    punten_freq = {}

    for element in lijst:
        # Hebben we dit puntenaantal eerder gezien
        if element in punten_freq:
            # Verhoog de teller voor dit aantal
            punten_freq[element] += 1
        # Dit puntenaantal hebben we niet eerder gezien
        else:
            # Maak een nieuwe key aan (1x gezien)
            punten_freq[element] = 1

    return punten_freq

print(frequenties(['a', 'b', 'c', 'd', 'a', 'c', 'b']))

portfolio_freq = frequenties(portfoliopunten)
print(portfolio_freq)

# Met deze regel kunnen we een dictionary sorteren
# Sorteer op values (eerst alles wat 2x voorkomt)
sorted_dict = dict(sorted(portfolio_freq.items(), key=lambda item: item[1], reverse=True))
print(sorted_dict)

# Sorteer op keys (hoogste label eerst)
sorted_dict2 = dict(sorted(portfolio_freq.items(), key=lambda item: item[0], reverse=True))
print(sorted_dict2)
