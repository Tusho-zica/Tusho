# 1. Faça um programa que peça para o usuário digitar o nome e a idade
# de um aluno e o número de provas que esse aluno fez. Depois, o
# programa deve pedir para o usuário digitar as notas de cada prova do
# aluno. Ao final o programa deve imprimir uma lista contendo:
# a. Nome do aluno na posição 0
# b. Idade do aluno na posição 1
# c. Uma lista com todas as notas na posição 2
# d. A média do aluno na posição 3
# e. True ou False, caso a média seja maior que 5 ou não, na posição 4
# Dica: Use o que você fez nos exercícios anteriores para criar esse
# programa.

nome = input("Digite seu nome\n")
idade = int(input("Quantos anos você tem?\n"))
num_provas = int(input("Quantas provas você fez?\n"))
notas = []
contador = 0

while contador != num_provas:
    notas.append(float(input("Digite a nota da prova\n")))
    contador += 1

lista = notas[:]
soma = 0
media = 0

for item in lista:
    soma += item
    media = soma/len(lista)

passou = 0

if media >= 5:
    passou =True
else: 
    passou = False

# print(media)
# print(contador)
# print(notas)

lista_completa = [nome, idade, notas, media, passou]
print(lista_completa)
