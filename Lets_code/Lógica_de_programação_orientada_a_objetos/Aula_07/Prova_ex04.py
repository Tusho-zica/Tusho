# 4. Faça uma lista randômica de 10 valores, usando list comprehension 
# e randint. Verifique se o valor 10 está presente na lista. 
# Imprima a lista e a primeira posição do valor 10, se houver. 
# (Observe que pode haver duplicação do 10)

import random

#Criação da lista com random e list comprehension.
lista = [random.randint(0,10) for item in range(10)]
print (lista)

#Verificação do numero 10 na primeira posição da lista.
for i, item in enumerate(lista):
    if item == 10:
        print(i, item)
        break
else:
    print("não existe")

