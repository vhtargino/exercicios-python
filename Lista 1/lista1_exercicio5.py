# 5. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre
# a temperatura em graus Celsius.
# C = 5 * ((F-32) / 9).

graus_farenheit = float(
    input("Qual a temperatura atual em Farenheit? Digite apenas números: "))
conversao_celsius = 5 * ((graus_farenheit - 32) / 9)
print(f"{graus_farenheit:.1f}°F é o mesmo que {conversao_celsius:.1f}°C")
