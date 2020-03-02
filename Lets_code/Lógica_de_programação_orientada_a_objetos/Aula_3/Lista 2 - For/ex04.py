# 4. Faça um programa que olhe todos os itens de uma lista e diga
# quantos deles são pares.

numero_lista = int(input("Digite um número: "))

lista = range(numero_lista)
count = 0

for num in lista:
    if num % 2 == 0:
        count += 1

print(f"O número possui {count} pares")