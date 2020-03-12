import random


# List comprehensive para criar uma lista com 10 números randomicos
lista = [random.randint(0,20) for item in range(10)]

#enumerate gera um tupla como resultado. neste caso, estou 
# pegando a posição (i) e o valor (item) na lista.
for i, item in enumerate(lista):
    print(i, item)




