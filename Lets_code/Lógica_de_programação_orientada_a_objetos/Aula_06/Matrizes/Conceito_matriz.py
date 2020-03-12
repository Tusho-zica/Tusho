# Matriz em python é basicamente uma lista de listas.
# Cada lista é uma linha
# O número de elementos dessas listas são o número de colunas da Matriz


matriz = [
    ["n1","n2","n3"],
    [1,2,3],
    [4,5,6]
]

print(matriz)
print("_____________________")

#Não quero o cabeçalho no meu print. Estou gerando somente do 1 pra frente.

for linha in matriz[1:]:
    print(linha)
print("_____________________")

#Quero trazer o cabeçalho. Estou gerando completo.

for linha in matriz:
    for coluna in linha:
        print(coluna)
    print("_____________________")

#Endereçamento linha e coluna.
print(matriz[1][1])
print("_____________________")


#Nature of code - Dan Shiffman


# Quando vamos trabalhar com soma, multiplicação, etc entre matrizes, sempre utilizar o enumerate.

for i, linha in matriz:
    for j, coluna in linha:
        print(coluna)
