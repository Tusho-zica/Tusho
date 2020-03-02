# 13. Faça uma função que recebe uma lista de números e retorna a soma
# dos elementos dessa lista.

def soma_elemento(lista):
    soma = 0

    for i in lista:
        soma += i
    return soma

lista = [1, 2, 3, 4, 5]
print(soma_elemento(lista))