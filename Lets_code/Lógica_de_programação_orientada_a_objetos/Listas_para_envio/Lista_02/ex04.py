# Programa que leia do teclado uma lista de 6 elementos e inverta 
# esta lista (sem usar funções prontas da linguagem).

num0 = int(input("Digite o primeiro número da lista: "))
num1 = int(input("Digite o segundo número da lista: "))
num2 = int(input("Digite o terceiro número da lista: "))
num3 = int(input("Digite o quarto número da lista: "))
num4 = int(input("Digite o quinto número da lista: "))
num5 = int(input("Digite o sexto número da lista: "))

lista = [num0, num1, num2, num3, num4, num5]

print(lista)

lista = lista[::-1]

print (lista)

