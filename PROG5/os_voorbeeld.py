import os

output_path = "/output/"
fname = "producten.txt"

# Current Working Directory
print(f"CWD: {os.getcwd()}")
# Output directory
print(f"Output directory: {os.getcwd() + output_path}")

# Volledige pad voor de file
fpath = os.getcwd() + output_path + fname
print(fpath)

# Open het bestand met de producten en print de inhoud
with open(fpath, encoding='UTF-8') as my_file:
    # read(): Bestand als 1 string
    content = my_file.read()
    print(type(content))

with open(fpath, encoding='UTF-8') as my_file:
    # readlines(): Bestand als list inlezen
    lines = my_file.readlines()
    print(type(lines))
    print(lines)

# File is gesloten nu we de code vervolgen
productnamen = []
productprijzen = []

# Voor elk product
for line in lines:
    # Trek de productnaam los (twee delen: product dan de prijs, dus index 0)
    productnaam = line.strip().split(' - ')[0]
    productprijs = line.strip().split(' - ')[1]
    productnamen.append(productnaam)
    productprijzen.append(productprijs)

print(productnamen)
print(productprijzen)
