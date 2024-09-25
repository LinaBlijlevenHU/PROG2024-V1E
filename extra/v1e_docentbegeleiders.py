import random

names = [
    "Sem", "Silo", "Tyler", "Max", "Ashraf", "Jian", "Merlijn",
    "Howick", "Camil", "Walid", "Seyf", "Enrico", "Mert", "Jelte",
    "Baha", "Tristan", "Ticho", "Vasco", "Soulaimane", "Valentijn",
    "Skip", "Jason", "Lucas", "Merijn", "Emil", "Daan", "Victor"
]

x = len(names) // 3
random.shuffle(names)

print(f"Matthias krijgt {names[:x]}")
print(f"Lina krijgt {names[x:2*x]}")
print(f"Jeroen krijgt {names[2*x:]}")


