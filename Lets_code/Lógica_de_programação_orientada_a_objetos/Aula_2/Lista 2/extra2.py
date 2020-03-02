# 2. Faça o mesmo programa do exercício anterior, porém com 4
# números.

num1 = int(input("digite o primeiro número: "))
num2 = int(input("digite o segundo número: "))
num3 = int(input("digite o terceiro número: "))
num4 = int(input("digite o quarto fucking número: "))

if num1 > num2 and num1 > num3 and num1 > num4:
    print(num1)
elif num2 > num1 and num2 > num3 and num2 > num4:
    print(num2)
elif num3 > num2 and num3 > num1 and num3 > num4:
    print(num3)
elif num4 > num2 and num4 > num1 and num4 > num3:
    print(num4)
else:
    print("possui números repetidos.")