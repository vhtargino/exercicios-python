# 4. Faça um programa que receba um número e que calcule e mostre a tabuada desse número.

num = int(input("Escolha um número: "))

for contagem in range(1,11):
    print(f"{num} x {contagem} = {num*contagem}")
