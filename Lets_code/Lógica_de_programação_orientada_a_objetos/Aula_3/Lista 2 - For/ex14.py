# 14. Faça um programa que sorteie 10 números entre 0 e 100 e imprima:

import random

lista = random.sample(range(100), 10)
print(lista)
print("__________________________\n")

# a. o maior número sorteado;
print(max(lista))
print("__________________________\n")

# b. o menor número sorteado;
print(min(lista))
print("__________________________\n")

# c. a média dos números sorteados;
lista2 = lista[:]
soma = 0
media = 0

for item in lista2:
    soma += item
    media = soma/len(lista2)

print(media)
print("__________________________\n")

# # d. a soma dos números sorteados.
lista3 = lista[:]
soma2 = 0

for item in lista3:
    soma2 += item
    
print(soma2)
print("__________________________\n")