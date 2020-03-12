#9. Faça um programa que peça a temperatura em graus Fahrenheit (F),
#transforme e mostre a temperatura em graus Celsius (°C).
#°C = (5 * (F-32) / 9)
#Obs: Tente também fazer um programa que faça o inverso: peça a
#temperatura em graus Celsius e a transforme em graus Fahrenheit.

fahrenheit = float(input("Digite a temperatura em fahreneit que deseja converter:\n"))
celsius = float(input("Digite a temperatura em celsius que deseja converter:\n"))

conv_celsius = ((5 * (fahrenheit - 32) / 9))
conv_fahrenheit = ((celsius * 9 / 5) + 32)

print(f"A temperatura em Farehneit é:{conv_fahrenheit}")
print(f"A temperatura em Celsius é:{conv_celsius}")
