# 5. Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior
# deles.

num1 = float(input("Digite um número: "))
num2 = float(input("Agora digite um número diferente: "))

if num1 > num2:
    print(f"{num1} é maior que {num2}")
else:
    print(f"{num2} é maior que {num1}")
