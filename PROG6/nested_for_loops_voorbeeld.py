"""
nested_for_loops_voorbeeld.py
"""

table = [[3, 5, 7, 9], [0, 2, 1, 6], [3, 8, 3, 1]]
row = table[0]  # Selecteer eerste element [3, 5, 7, 9]
print(row[3])  # Selecteert uit [3, 5, 7, 9] index 3 (dus de 9)

print(table[0][3])


def sum2D(t):
    """Sums the values in a 2D list"""
    som = 0

    for row in t:
        for item in row:
           som += item
    return som

def print2D(t):
    'prints values in 2D list t as a 2D table'

    # Loop over de rijen
    for row in t:
        # Loop over alle items in één rij
        for item in row:
            # Print the items met spaties ertussen
            print(item, end=' ')
        # Begin weer op een nieuwe regel
        print()


print2D(table)
print(f"De som van alle elementen in de 2D lijst is: {sum2D(table)}")
