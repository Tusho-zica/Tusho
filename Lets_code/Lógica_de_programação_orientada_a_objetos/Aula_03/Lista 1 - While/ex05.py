# 5. Faça um programa que recebe um número inteiro do usuário e
# imprime na tela a quantidade de divisores desse número e quais são
# eles.

num = int(input("Digite um número: "))

count = 1

while count <= num:
    if num % count == 0:
        print(count)
    count += 1