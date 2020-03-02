# 1. Faça um programa que peça ao usuário um número e imprima todos
# os números de um até o número dado.
# Exemplo: digite: 5, imprime: 1 2 3 4 5

num = int(input("Digite um número: "))

i = 0

while i <= num:
    print(i)
    i += 1
