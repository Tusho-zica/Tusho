# 12. Faça uma função que recebe um número x e uma lista numérica e
# retorna uma lista cujos elementos são os itens da lista de entrada
# multiplicado por x.
# Exemplo: se a função receber o número 5 e a lista [3,5,1], então a
# função deve retornar [5x3, 5x5, 5x1] = [15, 25, 5].

def multiplica_fator(fator, lista):
    lista2 = [None] * len(lista)

    for i in range(len(lista)):
            lista2[i] = lista[i] * fator
    return lista2

listaa = [1, 2, 3, 5, 6, 7, 8]
fator = int(input("Digite um fator: "))
print(multiplica_fator(fator, listaa))