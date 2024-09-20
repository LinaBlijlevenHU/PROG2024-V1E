def is_ja(antwoord):
    """ Geeft True/False terug voor het antwoord op een ja/nee vraag """
    return antwoord in ["ja", "jup", "j", "yes", "y"]

def spelletje():
    naam = input("Wat is je naam? ")
    ans = input(f"{naam.capitalize()}, ben je klaar om te spelen? Ja/Nee\n")

    if is_ja(ans.lower()):
        print("We zijn klaar om te spelen.")
    else:
        print("Ja dan niet.")


spelletje()
