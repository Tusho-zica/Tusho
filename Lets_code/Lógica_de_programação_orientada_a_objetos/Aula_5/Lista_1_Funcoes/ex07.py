# 7. Faça uma função que sorteia 10 números aleatórios entre 0 e 100 e
# retorna o maior entre eles.

import random

def maior_100(num):
    num = random.sample(range(100), 10)
    print(num)
    return max(num)

teste = 0
print (maior_100(teste))