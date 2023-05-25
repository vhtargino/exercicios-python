# 1. Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros
# formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que
# é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto
# sobre vendas.

def somaImposto(taxaImposto, custo):
    custo = custo + (custo * (taxaImposto/100))
    print(f"O preço do produto + imposto sobre vendas é R${custo}")


taxa = float(input("Digite a taxa de imposto (%): "))
valor = float(input("Digite o valor do produto (R$): "))

somaImposto(taxa, valor)
