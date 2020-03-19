# Faça uma função que receba uma lista de inteiros, e retorne True caso a 
# sequência 1, 2, 3 apareça na lista em algum lugar, caso contrário, 
# retorne False. Chame essa função de has_123.

# Método alternativo (talvez muito ineficiente...) de se pensar/fazer para resolver o problema! haha

import random

def has_123(lista):
    string = [str(item) for item in lista]
    convert = "".join(string)
    numero_base = int(convert)    
    
    _123 = False

    contador = len(convert)

    unidade = 0
    dezena = 0
    centena = 0
    while contador != 0 or _123 == False:
        unidade = numero_base % 10
        dezena = (numero_base // 10) % 10
        centena = (numero_base // 100) % 10
        numero_base = numero_base // 10
        if centena == 1 and dezena == 2 and unidade == 3:
            _123 = True
        contador -= 1
    if centena == 1 and dezena == 2 and unidade == 3:    
        return True
    else:
        return False

# lista = [random.randint(0,3) for item in range(10)]
lista = [2, 0, 3, 1, 2, 3, 1, 3, 2, 1]

print(lista)
print(has_123(lista))
