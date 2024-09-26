"""
wordcount_oefening.py

Oefenen met het tellen van woorden in een string
"""

txt = "Implement function wordcount() that takes as input a text—as a string—\
        and prints the frequency of "\
        "each word in the text; assume there is no punctuation in the text"

# Implement function wordcount() that takes as input a text—as a
# string— and prints the frequency of each word in the text; assume
# there is no punctuation in the text

def wordcount(txt):
    # Split de tekst naar woorden
    woorden = txt.split()

    # Houd per woord bij hoe vaak het voorkomt
    freq = {}

    # Tel alle woorden
    for woord in woorden:
        # Al gezien
        if woord in freq:
            freq[woord] += 1
        # Eerste keer zien
        else:
            freq[woord] = 1

    return freq

print(wordcount(txt))