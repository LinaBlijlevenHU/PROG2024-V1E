"""
logic_operators.py

De logische operatoren in Python: and, or en not.
Je kunt deze gebruiken om bijvoorbeeld meerdere condities aan elkaar te koppelen.
"""

# AND
print(f"True and True: {True and True}")        # True
print(f"True and False: {True and False}")      # False
print(f"False and True: {False and True}")      # False
print(f"False and False: {False and False}\n")  # False

# Langere AND-combinaties: we kunnen zoveel achter elkaar
# koppelen als we willen. We lezen van links naar rechts.
# Één false in deze reeks is genoeg om het resultaat ook False te maken.
print(f"True and True and True and True and False: {True and True and True and True and False}")  # False

# Hier weten we zelfs na de eerste vergelijking (False and True)
# al dat we kunnen stoppen.
# Verdieping: https://www.geeksforgeeks.org/short-circuiting-techniques-python/
print(f"False and True and True and True and True: {False and True and True and True and True}\n")  # False

# OR
print(f"True or True: {True or True}")          # True
print(f"True or False: {True or False}")        # True
print(f"False or True: {False or True}")        # True
print(f"False or False: {False or False}\n")    # False

# Langere OR-combinaties: we kunnen zoveel achter elkaar
# koppelen als we willen. We lezen van links naar rechts.
# Één True in deze reeks is genoeg om het resultaat ook True te maken.
print(f"True or True or True or True or False: {True or True or True or True or False}")  # True

# NOT
print(f"not True: {not True}")                              # False
print(f"not False: {not False}")                            # True
print(f"not not not False: {not not not False}")            # True
print(f"not not not not False: {not not not not False}")    # False

# Tip: denk aan de wiskunde en negatieve getallen.
# 'not' kun je als het minnetje zien: als er twee keer 'not' staat kunnen we deze
# tegen elkaar wegstrepen.
