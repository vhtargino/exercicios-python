# 5. Utilizando a lista do exercício anterior, exiba uma saudação ("Olá como vai você"), personalizado
# com o nome de cada amigo. A saudação deve ser a mesma, alterando apenas o nome do amigo.

from time import sleep

amigos = ["leo", "maísa", "rafaela", "renata", "carol", "leticia"]

for a in amigos:
    print(f"Olá, como vai você, {a.title()}?")
    sleep(0.5)
