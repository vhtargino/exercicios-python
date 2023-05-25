# 2. Com o arquivo criado anteriormente, conte quantos caracteres possui esse arquivo.

arquivo = open("arquivo.txt", "r")
print(f"O arquivo possui {len(arquivo.read())} caracteres.")
