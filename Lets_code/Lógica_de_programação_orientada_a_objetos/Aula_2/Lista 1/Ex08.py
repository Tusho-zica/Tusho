#Faça um programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês e depois, calcule e mostre o
#total do seu salário no referido mês.


valor_hora = float(input("Quanto você ganha por hora?\n"))
horas_trabalhadas = int(input("Quantas horas voce trabalha no mês?\n"))

salario = valor_hora * horas_trabalhadas

print("O total do salário mensal é de:", salario)