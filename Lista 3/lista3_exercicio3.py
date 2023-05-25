# 3. Armazene os nomes de alguns de seus amigos em uma lista chamada amigos. Exiba o nome de cada
# pessoa acessando cada elemento da lista um de cada vez.

from time import sleep

amigos = ["leo", "maísa", "rafaela", "renata", "carol", "leticia"]

for a in amigos:
    print(a.title())
    sleep(0.5)
