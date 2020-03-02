# Peça ao usuário para digitar um número e imprima o fatorial de n.
import math

n = int(input("digite o valor de n: "))

fatorial = 0

if n == 0:
    print("1")
else:
    fatorial = math.factorial(n)
    print(fatorial)