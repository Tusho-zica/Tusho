# 6. Escreva um programa que peça a nota de 3 provas de um aluno e
# verifique se ele passou ou não de ano.
# Obs.: O aluno irá passar de ano se sua média for maior que 6.

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
nota3 = float(input("Digite a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    print("O aluno passou de ano!")
else:
    print("Não foi dessa vez meu chapa!")