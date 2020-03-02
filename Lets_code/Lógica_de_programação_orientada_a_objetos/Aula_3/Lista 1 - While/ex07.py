# 7. Faça um programa que sorteia um número N e peça para o usuário
# adivinhar o número sorteado. A cada resposta errada, o seu programa
# deve imprimir um aviso dizendo que a resposta está errada e pedir
# novamente uma resposta ao usuário.

import random

# random.randint(a, b)¶
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).

num_random = random.randint(1, 10)
print(num_random)

errou = 0
num = int(input("Digite um número: "))

while num != num_random:
    num = int(input("você não está com os poderes afiados, tente novamente! \n"))
    if num == num_random:
        print("Você é ZICA brother!")
        break



