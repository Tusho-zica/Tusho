# Faça um programa que imprima o maior número de uma lista, sem usar max().

import random

lista = random.sample(range(100), 10)
print(lista)

lista.sort()

print(lista[len(lista) - 1])
