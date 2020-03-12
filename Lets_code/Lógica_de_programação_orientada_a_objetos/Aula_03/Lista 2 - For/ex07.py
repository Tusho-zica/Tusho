# 7. Faça um programa que, dadas duas listas de mesmo tamanho, crie
# uma nova lista com cada elemento igual a soma dos elementos da
# lista 1 com os da lista 2, na mesma posição.
# Exemplo: dadas lista1 = [1, 4, 5] e lista2 = [2, 2, 3], então lista3 = [1+2, 4+2,
# 5+3] = [3, 6, 8]

lista1 = [1, 4, 5]
lista2 = [2, 2, 3]

#lista_soma = [3, 6, 8]

lista3 = [None, None, None]

if len(lista1) == len(lista2):
    for i in range(len(lista1)):
        lista3[i] = lista1[i] + lista2[i]

print(lista1)
print(lista2)
print(lista3)
