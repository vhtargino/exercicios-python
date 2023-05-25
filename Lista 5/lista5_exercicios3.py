# 3. Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por
# exemplo: 127 -> 721.

def reverso(num):
    num = str(num)
    novonum = int(num[::-1])
    num = int(num)
    print(f"O contrário de {num} é {novonum}.")


numero = int(input("Digite um número: "))

reverso(numero)
