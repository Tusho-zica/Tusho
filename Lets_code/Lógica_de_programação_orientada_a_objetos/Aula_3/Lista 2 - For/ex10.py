# 10. Pegue a lista gerada no exercício anterior e transforme cada um dos
# itens dessa lista em um float.
# OBS: Não é para alterar o programa anterior, mas sim a lista gerada
# por ele.

num0 = input("Digite o primeiro número da lista: ")
num1 = input("Digite o primeiro número da lista: ")
num2 = input("Digite o primeiro número da lista: ")
num3 = input("Digite o primeiro número da lista: ")
num4 = input("Digite o primeiro número da lista: ")

lista = [num0, num1, num2, num3, num4]
lista_float = []

for item in lista:
    lista_float.append(float(item))

print(lista_float)