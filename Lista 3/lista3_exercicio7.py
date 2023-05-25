# 7. Faça um cadastro de usuários com nome, idade e email,
# utilizando apenas o que você aprendeu até agora.

usuarios = {}

while True:
    nome = input("Digite seu nome: ").title()
    while True:
        idade = input("Digite sua idade: ")
        if not idade.isnumeric():
            print("Você precisa digitar um número.")
            continue
        else:
            break
    email = input("Digite seu email: ")
    usuarios[f'{nome}'] = [idade, email]

    cadastrarnovamente = input("Gostaria de cadastrar mais um usuário? (S/N): ").upper()

    while cadastrarnovamente != "S" and cadastrarnovamente != "N":
        print("Escolha S ou N.")
        cadastrarnovamente = input("Gostaria de cadastrar mais um usuário? (S/N): ").upper()

    if cadastrarnovamente == "S":
        continue
    else:
        break

print(usuarios)
