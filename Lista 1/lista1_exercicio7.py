# 7. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# - o produto do dobro do primeiro com metade do segundo .
# - a soma do triplo do primeiro com o terceiro.
# - o terceiro elevado ao cubo.

num_int1 = int(input("Digite um número inteiro: "))
num_int2 = int(input("Digite outro número inteiro: "))
num_real1 = float(input("Digite um número real: "))
resultado1 = (num_int1 * 2) * (num_int2 / 2)
resultado2 = (num_int1 * 3) + (num_real1)
resultado3 = num_real1**3

print(f"\nO produto do dobro de {num_int1} com a metade de {num_int2} é {resultado1}")
print(f"A soma do triplo de {num_int1} com {num_real1} é {resultado2}")
print(f"{num_real1} elevado ao cubo é {resultado3:.2f}")
