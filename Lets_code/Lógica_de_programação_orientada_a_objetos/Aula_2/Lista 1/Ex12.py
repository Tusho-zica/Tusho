#12. Faça um programa que peça o peso e altura de uma pessoa e calcule
#seu IMC (Índice de Massa Corporal).
#Obs: IMC = Peso/Altura2


peso = float(input("Digite o seu peso:\n"))
altura = float(input("Digite a sua altura:\n"))

imc = peso/ (altura ** 2)

print(f"Seu IMC é de:{imc}")