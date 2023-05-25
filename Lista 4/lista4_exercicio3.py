# 3. Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de
# cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

import random
import math # Para poder somar floats com o método fsum()

notas1 = []
notas2 = []
notas3 = []
notas4 = []
notas5 = []
notas6 = []
notas7 = []
notas8 = []
notas9 = []
notas10 = []

for num in range(4):
    notas1.append(round(random.uniform(0, 10),1)) # Gerando notas aleatórias para cada aluno, a fim de evitar muitos inputs
    notas2.append(round(random.uniform(0, 10),1))
    notas3.append(round(random.uniform(0, 10),1))
    notas4.append(round(random.uniform(0, 10),1))
    notas5.append(round(random.uniform(0, 10),1))
    notas6.append(round(random.uniform(0, 10),1))
    notas7.append(round(random.uniform(0, 10),1))
    notas8.append(round(random.uniform(0, 10),1))
    notas9.append(round(random.uniform(0, 10),1))
    notas10.append(round(random.uniform(0, 10),1))

media1 = math.fsum(notas1)/4
media2 = math.fsum(notas2)/4
media3 = math.fsum(notas3)/4
media4 = math.fsum(notas4)/4
media5 = math.fsum(notas5)/4
media6 = math.fsum(notas6)/4
media7 = math.fsum(notas7)/4
media8 = math.fsum(notas8)/4
media9 = math.fsum(notas9)/4
media10 = math.fsum(notas10)/4

alunos = {"Aluno 1" : float(media1),
          "Aluno 2" : float(media2), 
          "Aluno 3" : float(media3), 
          "Aluno 4" : float(media4), 
          "Aluno 5" : float(media5), 
          "Aluno 6" : float(media6), 
          "Aluno 7" : float(media7), 
          "Aluno 8" : float(media8), 
          "Aluno 9" : float(media9), 
          "Aluno 10" : float(media10)}

aprovados = 0 # Total de aprovados; valor vai subindo na medida que a média dá maior ou igual a 7

for k, v in alunos.items():
    if v >=7:
        print(f"A média de {k} foi {v:.1f}. {k} foi \033[0;032maprovado por média.\033[0;0m")
        aprovados += 1
    else:
        print(f"A média de {k} foi {v:.1f}. {k} foi \033[0;031mreprovado por média.\033[0;0m")

if aprovados == 0:
    print("\nNenhum aluno foi aprovado.")
elif aprovados == 1:
    print(f"\nApenas {aprovados} aluno foi aprovado.")
else:
    print(f"\n{aprovados} alunos foram aprovados.")
