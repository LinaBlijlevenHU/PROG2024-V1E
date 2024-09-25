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
    :param file_path:   Filename (use Path.cwd() if necessary)
    :return:            dict, or None if the file doesn't exist or can't be read
    """
    # Using pathlib we can check
    path = Path(file_path)

    if not path.exists():
        print(f"File '{file_path}' does not exist. Please check the file path.")
        return None

    if not path.is_file():
        print(f"'{file_path}' is not a valid file. Please check the file path.")
        return None

    with path.open('r') as file:
        data = json.load(file)
        return data


# Laad de pokemons in uit een file
pokemeneren = load_pokemon_data("pokemon.json")["pokemon"]

# Standaard kunnen we dit gewoon uitprinten met Python.
print(pokemeneren)

# Met de JSON dumps-functie kunnen we ook printen met wat meer indentatie, voor meer leesbaarheid.
print(json.dumps(pokemeneren, indent=2))
