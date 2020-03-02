# 14. Faça uma função que recebe uma lista de números e retorna a média
# aritmética dos elementos dessa lista.

def media_elemento(lista):
    soma = 0
    media = 0

    for i in lista:
        soma += i
    media = soma / len(lista)
    return media

lista = [1, 2, 3, 4, 5]
print(media_elemento(lista))