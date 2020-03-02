# 8. Faça um programa que dadas duas listas de mesmo tamanho,
# imprima o produto escalar entre elas.
# OBS: produto escalar é a soma do resultado da multiplicação entre
# o número na posição i da lista1 pelo número na posição i da lista2,
# com i variando de 0 ao tamanho da lista.

lista1 = [2, 2, 2]
lista2 = [2, 3, 4]
lista3 = [None, None, None]
count = 0
soma_produto = 0

if len(lista1) == len(lista2):
    for i in range(len(lista1)):
        lista3[i] = lista1[i] * lista2[i]
    while count < len(lista3):
        soma_produto += lista3[count]
        count += 1

print(lista3)
print(soma_produto)
