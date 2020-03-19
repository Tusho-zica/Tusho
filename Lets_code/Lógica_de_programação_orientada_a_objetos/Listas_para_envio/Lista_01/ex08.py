# Prepare um algoritmo para perguntar 10 números e informar a soma total destes números.

total = 0
count = 0
while count < 10:
    numeros = int(input("Digite um número que deseja somar: "))
    total += numeros
    count += 1

print(f"A soma dos números digitados é: {total}")