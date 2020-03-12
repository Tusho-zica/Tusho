# 1. Escreva um algoritmo que solicite uma quantidade de presenças e 3 notas 
# para o usuário. Ao final, ele deve mostrar na tela quantas faltas ele teve 
# (base 30 aulas), quanto essas faltas representam do total em %, a média das 
# notas e se ele passou ou não, sendo que, para passar, ele precisa de média > 6 
# e menos de 20% de faltas. *

# Setando a variável presenca, solicitando dados ao usuário já com conversão de tipo para int
presenca = int(input("Digite a quantidade de presenças que o aluno teve no período: "))

# Setando as variaveis nota(x), solicitando dados ao usuário já com conversão de tipo para float
nota1 = float(input("Digite a primeira nota do aluno no período: "))
nota2 = float(input("Digite a segunda nota do aluno no período: "))
nota3 = float(input("Digite a terceira nota do aluno no período: "))

# variável faltas é a diminuição do total de aulas pelo valor de presença informado pelo usuário.
faltas = (30 - presenca)

# quanto essas faltas representam do total em %
percentual = (faltas/30) * 100

# Calculando a média das notas do aluno.
media_notas = (nota1 + nota2 + nota3) / 3

# Criação da condição para verificar se o aluno passou de ano.
# Se o aluno teve média acima de 6 e percentual de faltas não maior que 20%:
if media_notas > 6 and percentual <= 20:
    print(f"O aluno teve {faltas} faltas")
    print(f"As faltas representam {percentual}% do total de presença")
    print(f"A média do aluno no ano é: {media_notas}")
    print("Parabéns. O aluno passou de ano!")
# Se não:
else:
    print(f"O aluno teve {faltas} faltas")
    print(f"As faltas representam {percentual}% do total de presença")
    print(f"A média do aluno no ano é: {media_notas}")
    print("Infelizmente o aluno não passou de ano.")


