"""
if_elif_portfoliopunten.py

Een oefening waarbij we met een combinatie van verschillende statements
if, elif en else inzetten.
"""

# De informatie die we nodig hebben:
# 95 perfect
# >=76 boven niveau
# >=61 op niveau
# <61 onder niveau

# Dit programma houdt natuurlijk geen rekening met andere vereisten.
# Je zou kunnen proberen dit programma voor jezelf uit te breiden, dan kun
# je het als checklist gebruiken!

# Eerst mag de student een aantal punten invoeren. Vergeet niet de input om
# te zetten naar een integer!
punten = int(input("Hoeveel punten heb je nu behaald voor het semester? "))

# Aantal punten afhandelen:
# Let op: we hebben niet gekeken of er daadwerkelijk een getal is ingevoerd door de
# gebruiker, dus dit zal helaas errors geven als ze i.p.v. getallen tekst invoeren.
#
# Verdieping: https://automatetheboringstuff.com/2e/chapter8/ (inputvalidatie)
if punten < 61:                                 # 0 - 61 (en stiekem ook negatieve getallen)
    print("Helaas zit je niet op niveau.")
elif punten < 76:                               # 61 - 75 (alles onder de 61 is al afgehandeld)
    print("Je zit op niveau en krijgt een voldoende.")
elif punten < 95:                               # 76 - 94 (alles onder de 76 is al afgehandeld)
    print("Je zit boven niveau en krijgt een 8.")
else:                                           # Alles > 95
    print("Je hebt het vrijwel perfect gedaan en krijgt een handdruk en een sticker.")