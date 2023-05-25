# 1. Use um dicionário para armazenar informações sobre uma pessoa que você conheça. Armazene seu
# primeiro nome, o sobrenome, a idade e a cidade em que ela vive. Você deverá ter chaves como
# primeiro_nome, sobrenome, idade, e cidade. Por fim, mostre cada informação armazenada em seu
# dicionário.

pessoa = ('José', 'Xavier', '85', 'João Pessoa')
pessoadicio = dict(primeiro_nome = pessoa[0], sobrenome = pessoa[1], idade = pessoa[2], cidade = pessoa[3])

print(pessoadicio)
