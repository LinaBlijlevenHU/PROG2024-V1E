"""
for_loop_list_voorbeeld.py

Voorbeelden voor het combineren van for-loops met lijsten.
"""

'1. Een string opbouwen met een for-loop'
# Lijst met verschillende letters uit het alfabet.
lijst = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

# Een lege string gedraagt zich als een lege lijst. Als
# we hier karakters aan toevoegen, kunnen we dus in delen
# een stuk tekst opbouwen.
alphabet = ""

# We gaan de letters aan elkaar plakken. Hiervoor
# moeten we elk karakter in de lijst langs.
for e in lijst:
    # Plak elk karakter aan de string die we tot nu hebben opgebouwd.
    alphabet = alphabet + e

print(f"Het alfabet is: {alphabet}")

# Dit is een simpel voorbeeld, dit specifieke geval kan namelijk makkelijker:
alphabet = "".join(lijst)
print(f"Het alfabet is: {alphabet}")

'2. Het totaal van een lijst berekenen met een for-loop.'
# Lijstje met getallen
getallen = [5, 4, 7, 8, 34, 5, 0, 90]
# Als we willen opsommen beginnen we met tellen vanaf 0.
som = 0

# We gaan elk getal in de lijst langs
for getal in getallen:
    # som = (huidige) som + getal, kunnen we ook als som += getal schrijven. :)
    som += getal

print(f"De som van de lijst is: {som}")

# Ook dit is een simpel voorbeeld en kan natuurlijk makkelijker:
# sum(lijst)