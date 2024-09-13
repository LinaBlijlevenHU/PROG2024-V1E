# 95 perfect
# >=76 boven niveau
# >=61 op niveau
# <61 onder niveau

punten = int(input("Hoeveel punten heb je nu behaald voor het semester?"))

# 0 - 61 (en stiekem ook negatieve getallen)
if punten < 61:
    print("Helaas zit je niet op niveau.")
# 61 - 75
elif punten < 76:
    print("Je zit op niveau en krijgt een voldoende.")
# 76 - 94
elif punten < 95:
    print("Je zit boven niveau en krijgt een 8.")
# Alles > 95
else:
    print("Je hebt het vrijwel perfect gedaan en krijgt een handdruk en een sticker.")