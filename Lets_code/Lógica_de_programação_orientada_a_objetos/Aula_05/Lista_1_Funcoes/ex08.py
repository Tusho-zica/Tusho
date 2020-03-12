# 8. Faça uma função que recebe um número n de entrada, sorteia n
# números aleatórios entre 0 e 100 e retorna a média deles.

import random

def sorteio(num):
    num = int(input("Digite o número de bolas que deseja sortear: "))
    sorteado = random.sample(range(100), num)

    print (sorteado)

    soma = 0
    media = 0

    for item in sorteado:
        soma += item
        media = soma/len(sorteado)
    
    return media

teste = 0
print (sorteio(teste))