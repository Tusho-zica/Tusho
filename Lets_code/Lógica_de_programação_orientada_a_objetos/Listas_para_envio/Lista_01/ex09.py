# Faça um programa que escreva todos os números múltiplos de 7 entre 1 e N, sendo N um valor introduzido pelo utilizador. Por exemplos: 7, 14, 21, 28, 35.

repetidor = int(input("Digite o número de multiplos de 7 que deseja visualizar: "))

count = 1
lista = []
while count <= repetidor:
    multiplo = 7 * count
    lista.append(multiplo)
    #método 1
    # print(multiplo)
    count += 1

#método 2
print(lista)
