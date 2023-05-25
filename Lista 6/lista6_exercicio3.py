# 3. Acrescente mais texto a esse arquivo criado anteriormente. Print todo o novo texto criado.

arquivo = open("arquivo.txt", "a") # "a" de append para adicionar mais conteúdo
arquivo.write(" Escrevendo algo mais no arquivo.")

arquivo = open("arquivo.txt", "r")
print(f"O arquivo agora possui {len(arquivo.read())} caracteres.")
