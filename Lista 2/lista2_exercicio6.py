# 6. Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em
# ordem crescente.

num1 = float(input("Digite um número: "))
num2 = float(input("Agora digite um número diferente: "))

if num1 < num2:
    print(f"{num1}, {num2}")
else:
    print(f"{num2}, {num1}")
