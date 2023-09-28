# 6. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em
# graus Fahrenheit.

graus_celsius = float(input("Qual a temperatura atual em Celsius? Digite apenas números: "))
conversao_farenheit = graus_celsius * 1.8 + 32
print(f"{graus_celsius}°C é o mesmo que {conversao_farenheit:.1f}°F")
