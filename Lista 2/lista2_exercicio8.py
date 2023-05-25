# 8. Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em
# estoque e quantidade mínima em estoque de um produto. Calcular e escrever a
# quantidade média ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a quantidade média, escrever a
# mensagem 'Não efetuar compra', senão escrever a mensagem 'Efetuar compra'.

estoque = int(input("Digite a quantidade de itens atualmente em estoque: "))
quantidade_maxima = 50
quantidade_minima = 5
quantidade_media = (quantidade_maxima + quantidade_minima)/2

if estoque >= quantidade_media:
    print("Não efetuar compra")
else:
    print("Efetuar compra")
