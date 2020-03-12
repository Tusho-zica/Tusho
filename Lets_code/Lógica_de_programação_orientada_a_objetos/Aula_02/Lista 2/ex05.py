import math

count = 0
soma = 1
term = 1
fatorial = math.factorial(count)

while count < 1000:
    term /= 2
    soma += term
    count += 1

print(soma)