# 3. As maçãs custam 1,30 cada, se forem compradas menos de uma dúzia, e 1,00 se
# forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs
# compradas, calcule e escreva o custo total da compra.

compra_macas = int(input("Quantas maçãs vocês deseja comprar? Digite apenas números: "))

if compra_macas < 12:
    maca = 1.3
    print(f"O valor total de {compra_macas} maçãs é R${compra_macas*maca:.2f}")
else:
    maca = 1
    print(f"O valor total de {compra_macas} maçãs é R${compra_macas*maca:.2f}")
