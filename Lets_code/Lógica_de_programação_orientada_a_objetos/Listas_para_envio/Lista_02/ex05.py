# Nome na vertical em escada. Crie um programa que peça uma string para o usuário 
# e imprima de forma a mostrar o nome em formato de escada.

# F
# FU
# FUL
# FULA
# FULAN
# FULANO

nome = input("Digite seu nome aqui: ")
count = 0

while count <= len(nome):
    print (nome[0:count])
    count += 1