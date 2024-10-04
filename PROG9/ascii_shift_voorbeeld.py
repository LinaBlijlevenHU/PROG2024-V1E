SHIFT = 3

def shift_letter(char):
    # Letter omzetten naar een getal + shift de letter
    getal = ord(char) + SHIFT

    # Getal omzetten naar een letter
    return chr(getal)

def shift_sentence(txt):
    # Bouw de nieuwe tekst/zin
    new_sentence = ""

    # Voor elk karakter
    for char in txt:
        # Shift het karakter
        new_char = shift_letter(char)
        new_sentence += new_char

    return new_sentence


shifted = shift_sentence("abcde")
print(shifted)