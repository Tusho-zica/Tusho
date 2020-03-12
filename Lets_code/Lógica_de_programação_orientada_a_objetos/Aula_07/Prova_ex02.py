# 2. Escreva um algoritmo que solicite duas datas ao usuário em três partes: 
# dia, mês, ano. Ao final, informe qual das datas é maior, ou se ambas são iguais

# Solicitando a primeira data ao usuário e já realizando a conversão para o tipo int
data1_dia = int(input("digite o dia da primeira data: "))
data1_mes = int(input("digite o mês da primeira data: "))
data1_ano = int(input("digite o ano da primeira data: "))

# Solicitando a segunda data ao usuário e já realizando a conversão para o tipo int
data2_dia = int(input("digite o dia da primeira data: "))
data2_mes = int(input("digite o mês da primeira data: "))
data2_ano = int(input("digite o ano da primeira data: "))

# Primeira condição: Verificar se as datas são iguais.
if data2_ano == data1_ano and data1_mes == data2_mes and data1_dia == data2_dia:
    print("As duas datas são iguais.")
# Se as datas não são iguais, uma será necessariamente maior que a outra. Logo,
# Se não:
else:
    # Se o ano da data 2 for maior que a data 1, a segunda data já é maior.
    if data2_ano > data1_ano:
        print("A segunda data é maior que a primeira!")
    # Se o ano da data 1 for maior que a data 2, a primeira data já é maior.
    elif data2_ano < data1_ano:
        print("A primeira data é maior que a segunda!")
    # Se não houver resposta até aqui, sabemos que os anos são idênticos. Vamos agora verificar o mês digitado. Logo,
    # Se não:
    else:
        # Se o mês da data 2 for maior que o da data 1, a segunda data já é maior.
        if data2_mes > data1_mes:
            print("A segunda data é maior que a primeira!")
        # Se o mês da data 1 for maior que o da data 2, a primeira data já é maior.
        elif data2_mes < data1_mes:
            print("A primeira data é maior que a segunda!")
        # Se não houver resposta até aqui, sabemos que os meses e os anos são idênticos. Vamos agora verificar o dia digitado. Logo,
        # Se não:
        else:
            # Se o dia da data 2 for maior que o da data 1, a segunda data já é maior.
            if data2_dia > data1_dia:
                print("A segunda data é maior que a primeira!")
            # Se o dia da data 1 for maior que o da data 2, a primeira data já é maior.
            elif data2_dia < data1_dia:
                print("A primeira data é maior que a segunda!")