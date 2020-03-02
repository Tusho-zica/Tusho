# 2. Peça ao usuário para digitar um número n e some todos os números
# de 1 a n.

n = int(input("Digite um número: "))

i = 0
soma = 0

while i <= n:
    i += 1
    soma = n + i

print(soma)