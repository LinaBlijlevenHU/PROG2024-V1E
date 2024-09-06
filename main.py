"""
main.py

Welkom in main.py! Dit is een voorbeeld van hoe Python-code eruit ziet.
Wat je nu leest heet een docblock: deze staat bovenaan de code en vertelt je
er meer over.

Script uitvoeren:
- Je kunt hiervoor op 'run' klikken binnen je editor
- Je kunt dit ook doen met de shortcut Shift+F10!
- Je kunt het script uitvoeren in debug mode met het beestje naast de 'run' knop.
"""


def print_hi(name):
    """
    Dit is een functie! Hier leren we meer over in PROG4 (tijdens Nano).
    Dit is de functiedefinitie: hier bepalen we wat de functie doet.

    :param name:    De naam waar we hallo tegen zeggen!
    """
    # Boven deze regel staat een break point: dat betekent dat als we de debug-mode gebruiken,
    # we even het programma kunnen pauzeren op dit punt. Dat kan heel handig zijn om te zien wat er precies
    # in de applicatie gebeurt.
    # Je herkent het breakpoint aan een rood bolletje en een rode regel. CTRL+F8 zet een breakpoint aan of uit,
    # maar je kan ook op het regelnummer klikken.
    print(f'Hi {name}!')


def is_over_18(age):
    """
    Deze functie bepaalt of je boven de 18 bent!
    :param age:     Leeftijd
    :return:        True/False (een boolean)
    """
    return age > 18


# Als we alleen de bovenstaande functie zouden willen 'lenen' in een andere file,
# zou het vervelend zijn als we alle code in dit bestand uitvoeren.
# De onderstaande regel code zorgt dat we alleen hallo printen als we deze code runnen,
# en niet als we uit dit bestand importeren.
if __name__ == '__main__':

    # Dit is de functieaanroep. Hier nemen we de functie in gebruik.
    print_hi('studenten')
