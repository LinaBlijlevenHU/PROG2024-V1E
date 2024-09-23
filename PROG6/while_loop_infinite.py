"""
while_loop_infinite.py

Liever gebruiken we geen 'while True', aangezien dit kan leiden tot een infinite loop.
Over het algemeen is het veiliger om de for-loop te gebruiken.
"""
som = 1

while True:
   som += 1
   print(f"We printen nu voor de {som}de keer")