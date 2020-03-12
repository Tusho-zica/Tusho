# 5. Faça uma função que recebe uma matriz e um vetor. Verifique 
# se é possível fazer a multiplicação dessa matriz por esse vetor 
# (quantidade de itens no vetor deve ser a mesma das colunas da matriz) 
# e retorne uma tupla contendo True ou False e o 
# tamanho do vetor resultante (quantidade de linhas da matriz). *


def analise_matriz(matriz, vetor):
    tamanho_vetor = len(vetor)

    linha_matriz = len(matriz)
    colunas_matriz = len(matriz[0])

    possivel_multiplicar = tamanho_vetor == colunas_matriz

    if possivel_multiplicar == True:
        return(possivel_multiplicar, linha_matriz)
    else:
        return(None)

matriz = [[1,2,3], [4,5,6]]
vetor = [7,8,9]
print(analise_matriz(matriz, vetor))