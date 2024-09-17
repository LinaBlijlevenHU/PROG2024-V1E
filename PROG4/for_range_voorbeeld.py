"""
for_range_voorbeeld.py

Het voorbeeld dat Joris heeft uitgewerkt voor de klas uit de slides van PROG3.
"""

# Print de volgende getallen: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
for i in range(0, 11, 1):
    print(i)

# MAAR, als je een stapgrootte hebt van 1, dan kan je die weglaten.
# En als je begint vanaf 0, kun je die ook weglaten :)

# range(0, 5, 1)        # 0, 1, 2, 3, 4
# range(0, 5)           # 0, 1, 2, 3, 4
# range(5)              # 0, 1, 2, 3, 4

# Andere ranges:
# range(0, 9, 2)        # 0, 2, 4, 6, 8
# range(1, 10, 2)       # 1, 3, 5, 7, 9
# range(20, 80, 10)     # 20, 30, 40, 50, 60, 70
