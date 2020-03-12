# 1. Faça um programa que leia 3 números e informe o maior deles.

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
elif num3 > num2 and num3 > num1:
    print(num3)
else:
    print("possui números repetidos.")