# 7. Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. Após,
# calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). Também
# testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo',
# senão escrever a mensagem 'Saldo Negativo'.

conta = input("Digite o número da conta: ")[:4]
saldo = float(input("Qual o seu saldo? "))
debito = float(input("Quanto você deve? "))
credito = 1000 # Estabeleci um valor de crédito fixo para o exercício.
saldo_atual = saldo - debito + credito

print(f"""Número da conta: {conta}
Saldo: R${saldo}
Débitos: R${debito}
Crédito: R${credito}
Saldo atual: R${saldo_atual}""")

if saldo_atual < 0:
    print("Saldo negativo")
else:
    print("Saldo positivo")
