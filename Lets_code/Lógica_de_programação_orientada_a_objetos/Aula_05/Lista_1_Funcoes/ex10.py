# 10. Faça uma função que recebe duas listas e retorna a soma item a item
# dessas listas.
# Exemplo: Se a função receber as listas [1,4,3] e [3,5,1], então a
# função deve retornar [1+3, 4+5, 3+1] = [4, 9, 4].


def soma_lista(lista1, lista2):
    lista3 = [None] * len(lista1)

    if len(lista1) == len(lista2):
        for i in range(len(lista1)):
            lista3[i] = lista1[i] + lista2[i]
    return lista3

listaa = [1, 2, 3, 5, 6, 8, 10]
listab = [4, 5, 6, 90, 10, 11, 5]
print(soma_lista(listaa, listab))