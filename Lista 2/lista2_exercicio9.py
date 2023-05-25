# 9. Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
# tabela abaixo:
# Média de Aproveitamento Conceito
# Entre 9.0 e 10.0 A
# Entre 7.5 e 9.0 B
# Entre 6.0 e 7.5 C
# Entre 4.0 e 6.0 D
# Entre 4.0 e zero E
# O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a
# mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o
# conceito for D ou E.

nota3 = float(input("Digite a primeira nota: "))
nota4 = float(input("Digite a segunda nota: "))
media2 = (nota3 + nota4)/2

if media2 >= 9:
    media_aproveitamento_conceito = "A"
elif media2 >= 7.5 and media2 < 9:
    media_aproveitamento_conceito = "B"
elif media2 >= 6 and media2 < 7.5:
    media_aproveitamento_conceito = "C"
elif media2 >= 4 and media2 < 6:
    media_aproveitamento_conceito = "D"
else:
    media_aproveitamento_conceito = "E"

if media_aproveitamento_conceito in ["A", "B", "C"]:
    aprovacao = "APROVADO"
else:
    aprovacao = "REPROVADO"

print(f"""Nota 1: {nota3}
Nota 2: {nota4}
Média: {media2}
Média de Aproveitamento Conceito: {media_aproveitamento_conceito}
{aprovacao}""")
