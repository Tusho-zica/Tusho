# 8. Faça um programa que peça para o usuário digitar a idade, o salário
# e o sexo de uma pessoa até que as entradas digitadas sejam válidas.
# a. Idade: entre 0 e 150;
# b. Salário: maior que 0;
# c. Sexo: M, F ou Outro.

idade = int(input("Digite a sua idade:\n"))
count1 = 1
count2 = 1
count3 = 1

while count1 > 0:
    if idade < 0 or idade > 150:
        idade = int(input("Idade digitada está inválida. Digite novamente a sua idade: \n"))
    else:
        print(f"Sua idade é: {idade} \n")
        break

salario = float(input("Digite o seu salario:\n"))
while count2 > 0:
    if salario < 0:
        salario = int(input("Salário digitado está inválido. Digite novamente o seu salário: \n"))
    else:
        print(f"Seu salario é: {salario}\n")
        break


sexo = input('Sexo: "M", "F"" ou OUTROS"? \n')
sexo = sexo.upper()

while count3 > 0: 
    if sexo == "M" or sexo == "F" or sexo == "OUTROS":
        print(f"Sexo: {sexo}\n")
        break
    else:
        sexo = input("Sexo digitado está inválido. Digite novamente o seu sexo: \n")
