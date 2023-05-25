# 6. Seja criativo ao desenvolver este programa.
    # a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.
    # b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.
    # c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos convites. Imprima o nome das pessoas que não poderão comparecer.
    # d. Modifique sua lista, substitua os desistentes por novos convidados.
    # e. Exiba um novo convite para cada pessoa que continua presente em sua lista.

from time import sleep

convidados = ["Elon Musk", "Steve Jobs", "Phil Spencer", "Guido van Rossum", "Tim Berners-Lee"]

for c in convidados:
    print(f'Olá, {c.upper()}! Você está convidado a comparecer ao grande evento de lançamento do livro "Programando com Python", de Wuldson Franco, no dia 02/07!\nTe esperamos no Auditório Master da Uniesp - Centro Universitário, às 20h!\n')
    sleep(1)

print(f"\033[0;031mInfelizmente, {convidados[1]} não poderá comparecer.\033[0;0m\n")
sleep(1)
naopodecomparecer = []
naopodecomparecer.append(convidados[1])
convidados.pop(1)

convidados.insert(1, "Gottfrid Svartholm")

for c in convidados:
    print(f'Olá, {c.upper()}! Você está convidado a comparecer ao grande evento de lançamento do livro "Programando com Python", de Wuldson Franco, no dia 02/07!\nTe esperamos no Auditório Master da Uniesp - Centro Universitário, às 20h!\n')
    sleep(1)
