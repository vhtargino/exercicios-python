# 9. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
# - Para homens: (72.7*h) - 58
# - Para mulheres: (62.1*h) - 44.7

altura2 = float(input("Qual a sua altura? Digite apenas números: "))
peso_masc = (72.2*altura2) - 58
peso_fem = (62.1*altura2) - 44.7

print(f"\nO peso ideal para homens com {altura2}m é {peso_masc:.1f}")
print(f"O peso ideal para mulheres com {altura2}m é {peso_fem:.1f}")
