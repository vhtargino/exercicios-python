# 8. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

altura1 = float(input("Qual a sua altura? Digite apenas números: "))
peso_ideal = (72.2*altura1) - 58

print(f"Se sua altura é {altura1}m, seu peso ideal é {peso_ideal:.1f}")
