"""
read_pokemon.py

Leer werken met dictionaries en JSON met Pokémon-data.
"""

# De JSON-library bevat prettige tools om met JavaScript Object Notation
# te werken. Dit format gebruiken we inmiddels in alle programmeertalen.
import json

from pathlib import Path


def load_pokemon_data(file_path):
    """
    Load the data from the JSON file.
    :param file_path:   Filename (use os.cwd() if necessary)
    :return:            dict, or None if the file doesn't exist or can't be read
    """
    # Met pathlib kunnen we wat handige functionaliteiten rondom bestanden gebruiken
    path = Path(file_path)

    # Zoals bijvoorbeeld een methode om te checken of de betreffende folder bestaat
    if not path.exists():
        print(f"File '{file_path}' does not exist. Please check the file path.")
        return None

    # Of om te checken of de file zelf bestaat voordat we deze uit gaan lezen.
    if not path.is_file():
        print(f"'{file_path}' is not a valid file. Please check the file path.")
        return None

    # Open de JSON file met json.load
    with path.open('r') as file:
        data = json.load(file)
        return data


# Laad de pokemons in uit een file
pokemeneren = load_pokemon_data("pokemon.json")["pokemon"]

# Standaard kunnen we dit gewoon uitprinten met Python.
#print(pokemeneren)
# Met de JSON dumps-functie kunnen we ook printen met wat meer indentatie, voor meer leesbaarheid.
#print(json.dumps(pokemeneren, indent=3))

# Per type gaan we een lijst maken van de Pokémon met dit type.
pokemon_by_type = {}

# Loop over de (binnenste) lijst met pokemon
for pokemon in pokemeneren:
    name = pokemon["name"]
    # Dit heet type, maar kunnen ook meerdere types zijn
    types = pokemon["type"]

    # Sommige Pokémon hebben twee types
    for ptype in types:
        # Hebben we dit type eerder gezien?
        if ptype in pokemon_by_type:
            # We hebben dit type vaker gezien, dus de huidige pokemon gaat ook in de lijst
            pokemon_by_type[ptype].append(name)
        # Eerste keer dat we het type zien
        else:
            # We zien dit type voor het eerst
            pokemon_by_type[ptype] = [name]





