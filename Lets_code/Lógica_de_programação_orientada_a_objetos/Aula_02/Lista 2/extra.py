# Solicitar ao usuário 2 datas e imprimir a maior ou se são iguais

data1_dia = int(input("digite o dia da primeira data: "))
data1_mes = int(input("digite o mês da primeira data: "))
data1_ano = int(input("digite o ano da primeira data: "))

data2_dia = int(input("digite o dia da primeira data: "))
data2_mes = int(input("digite o mês da primeira data: "))
data2_ano = int(input("digite o ano da primeira data: "))

if data2_ano == data1_ano and data1_mes == data2_mes and data1_dia == data2_dia:
    print("As duas datas são iguais.")
else:
    if data2_ano > data1_ano:
        print("A segunda data é maior que a primeira!")
    elif data2_ano < data1_ano:
        print("A primeira data é maior que a segunda!")
    else:
        if data2_mes > data1_mes:
            print("A segunda data é maior que a primeira!")
        elif data2_mes < data1_mes:
            print("A primeira data é maior que a segunda!")
        else:
            if data2_dia > data1_dia:
                print("A segunda data é maior que a primeira!")
            elif data2_dia < data1_dia:
                print("A primeira data é maior que a segunda!")