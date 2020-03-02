# 11. Faça um Programa que peça as 4 notas bimestrais e mostre a média
# aritmética delas, usando listas.

num0 = input("Digite a primeira nota: ")
num1 = input("Digite a segunda nota: ")
num2 = input("Digite a terceira nota: ")
num3 = input("Digite a quarta nota: ")

lista = [num0, num1, num2, num3]

lista_notas = [float(item) for item in lista]
for item in range(len(lista_notas)):
    media = [((lista_notas[0] + lista_notas[1] + lista_notas[2] + lista_notas[3]) / 4)]

print (lista_notas)

#RESPOSTA:
print(media)

