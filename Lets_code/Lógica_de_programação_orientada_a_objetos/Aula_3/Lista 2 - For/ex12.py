# 12. Sorteie uma lista de 10 números e imprima:

import random

sorteio = random.sample(range(100), 10)
print(sorteio)
print("__________________________\n")

# a. uma lista com os 4 primeiros números;
print(sorteio[:4])
print("__________________________\n")

# # b. uma lista com os 5 últimos números;
print(sorteio[5:])
print("__________________________\n")

# # c. uma lista contendo apenas os elementos das posições pares;
print(sorteio[::2])
print("__________________________\n")

# d. uma lista contendo apenas os elementos das posições ímpares;
print(sorteio[1::2])
print("__________________________\n")

# e. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
sorteio2 = sorteio[:]
sorteio2.reverse()

print(sorteio2)
print("__________________________\n")

# f. uma lista inversa dos 5 primeiros números;
sorteio3 = sorteio[:]
sorteio3 [5:] = []

sorteio3.reverse()

#print(sorteio)
print(sorteio3)
print("__________________________\n")

# g. uma lista inversa dos 5 últimos números.
sorteio4 = sorteio[:]
sorteio4 [:5] = []

sorteio4.reverse()

print(sorteio4)
print("__________________________\n")