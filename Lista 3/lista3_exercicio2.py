# 2. Faça um programa que mostre as tabuadas dos números de 1 a 10.

for num1 in range(1, 11):
    print('') # Para dar um espaço entre cada tabuada
    for num2 in range(1, 11):
        print (f'{num1} x {num2} = {num1 * num2}')
