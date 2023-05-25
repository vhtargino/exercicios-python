# 2. Use um dicionário para armazenar os números favoritos de algumas pessoas. Escolha cinco colegas, e
# pergunte quais seus números favoritos. Use seus nomes para serem as chaves de cada número
# favorito. Ao final, exiba o nome de cada pessoa e seu número favorito.

colegasdicio = {}

for i in range(5):
    numero = int(input(f"Digite o número favorito da {i + 1}ª pessoa: "))
    colegasdicio[f"Colega {i + 1}"] = numero

print(colegasdicio)
