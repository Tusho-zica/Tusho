# 11. Faça uma função que receba duas listas e retorne o produto item a
# item dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a
# função deve retornar [1x3, 4x5, 3x1] = [3, 20, 3].

def multiplica_lista(lista1, lista2):
    lista3 = [None] * len(lista1)
    #lista3 = []

    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            lista3[i] = (lista1[i] * lista2[i])
            #lista3.append(lista1[i] * lista2[i])
    return lista3

listaa = [1, 2, 3, 5, 6, 8, 10]
listab = [4, 5, 6, 90, 10, 11, 5]
print(multiplica_lista(listaa, listab))
