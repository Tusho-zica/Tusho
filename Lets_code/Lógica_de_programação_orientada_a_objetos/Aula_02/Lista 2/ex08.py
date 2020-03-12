# 8. Vamos fazer um programa para verificar quem é o assassino de um
# crime. Para descobrir o assassino, a polícia faz um pequeno
# questionário com 5 perguntas onde a resposta só pode ser sim ou não:
# a. Mora perto da vítima?
# b. Já trabalhou com a vítima?
# c. Telefonou para a vítima?
# d. Esteve no local do crime?
# e. Devia para a vítima?

ponto = 0

print('Responda apenas "s" ou "n"')

casa = input("Mora perto da vítima?\n")
if casa == "s":
    ponto += 1

trabalho = input("Já trabalhou com a vítima?\n")
if trabalho == "s":
    ponto += 1

telefone = input("Telefonou para a vítima?\n")
if telefone == "s":
    ponto += 1

local = input("Esteve no local do crime?\n")
if local == "s":
    ponto += 1

divida = input("Devia para a vítima?\n")
if divida == "s":
    ponto += 1

# Cada resposta sim dá um ponto para o suspeito. A polícia considera
# que os suspeitos com 5 pontos são os assassinos, com 4 a 3 pontos são
# cúmplices e 2 pontos são apenas suspeitos, necessitando outras
# investigações. Valores abaixo de 1 são liberados.

if ponto <= 1:
    print("Você está liberado.")
elif ponto == 2:
    print("Você está liberado por enquanto, mas não saia da cidade!")
elif ponto == 3 or ponto == 4:
    print("Você está preso por ser cúmplice do crime!")
elif ponto == 5:
    print("Você está preso Assasino! Tudo o que falar pode e será usado contra você no tribunal")