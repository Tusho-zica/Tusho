#5. Faça um programa que peça as 4 notas bimestrais de um aluno e
#mostre a média aritmética delas.

nota1 = float(input("Digite a primeira nota bimestral do aluno: "))
nota2 = float(input("Digite a segunda nota bimestral do aluno: "))
nota3 = float(input("Digite a terceira nota bimestral do aluno: "))
nota4 = float(input("Digite a quarta nota bimestral do aluno: "))

media = ((nota1 + nota2 + nota3 + nota4) / 4)

print(f"A média do aluno é: {media}")