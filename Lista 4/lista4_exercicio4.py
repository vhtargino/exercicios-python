# 4. Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos
# com mais de 13 anos possuem altura inferior à média de altura desses alunos.

import random

alunostotal = {}
alturas = []

for n in range(30):
    idade = random.randint(5, 19)
    altura = (round(random.uniform(1.14, 1.82),2))
    alturas.append(altura)
    alunostotal[f'Aluno {n+1}'] = [idade, altura]

alturamedia = sum(alturas)/30
contador = 0
alunosabaixodamedia = []

print("Abaixo está a relação de alunos, suas respectivas idades e alturas:")
for k, v in alunostotal.items():
    print(k + ": " + str(v[0]) + " anos, " + str(v[1]) + "m")

for k, v in alunostotal.items():
    if v[0] > 13 and v[1] < alturamedia:
        contador += 1
        alunosabaixodamedia.append(k)

print(f"""
A estatura média dos alunos é {alturamedia:.2f}m.
{contador} alunos com mais de 13 anos estão abaixo da estatura média.""")

print("""
Os alunos que estão abaixo da estatura média são:""")
for i in alunosabaixodamedia:
    print(i)
