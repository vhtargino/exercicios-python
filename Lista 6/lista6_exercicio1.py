# 1. Crie um arquivo em .txt, escreva uma frase nesse arquivo e posteriormente print essa frase.

arquivo = open("arquivo.txt", "w")
arquivo.write("Escrevendo no arquivo!")

arquivo = open("arquivo.txt", "r")
print(arquivo.read())
