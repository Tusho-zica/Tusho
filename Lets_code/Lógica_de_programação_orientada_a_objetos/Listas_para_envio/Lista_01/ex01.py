# Faça um programa que leia o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário.

salario_atual = float(input("Digite o salário mensal atual: "))
reajuste = float(input("Digite o valor (em %) de reajuste do salário: ")) / 100
novo_salario = salario_atual + (salario_atual * reajuste)

print(f"O novo salário é de: {novo_salario}!")