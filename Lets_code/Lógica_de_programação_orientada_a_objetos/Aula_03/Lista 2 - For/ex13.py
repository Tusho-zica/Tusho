# 13. Faça um programa que sorteia 10 números entre 0 e 100 e conte
# quantos números sorteados são maiores que 50.

import random

sorteio = random.sample(range(100), 10)

print(sorteio)
print("__________________________\n")

over50 = [item for item in sorteio if item >= 50]
print(over50)
print("__________________________\n")

#RESPOSTA:
print(len(over50))


#OOOOU

sorteio2 = [random.randint(0,100) for item in range(10)]

over50_2 = [item for item in sorteio2 if item >= 50]
print(over50_2)
print("__________________________\n")

#RESPOSTA:
print(len(over50))