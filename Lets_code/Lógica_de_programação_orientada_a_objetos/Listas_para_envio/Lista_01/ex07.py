# Prepare um algoritmo para informar o total gasto em uma lavanderia. O algoritmo inicialmente deverá perguntar o total de camisas, 
# o total de calças e o total de meias e informar o total gasto, levando em conta a seguinte tabela de preços:

# Camisas : 5.00
# Calças : 10.00
# Meias : 2.00
# Depois de informar o total gasto, o algoritmo deverá perguntar ao usuário se o mesmo deseja fazer um novo cálculo de gasto, 
# caso a resposta seja positiva, o algoritmo deverá retornar ao seu início, caso contrário deverá ser finalizado.

loop = True

while loop is not False:
    camisas = int(input("Qual o total de camisas que deseja lavar? "))
    calcas = int(input("Qual o total de calças que deseja lavar? "))
    meias = int(input("Qual o total de meias que deseja lavar? "))

    valor_total = float((camisas * 5) + (calcas * 10) + (meias * 2))

    novo_calculo = input(f'O valor total é de: {valor_total}.\nDeseja fazer um novo cálculo? (S/N)\n')
    novo_calculo = novo_calculo.upper()
    
    if novo_calculo == 'S':
        loop = True
    else:
        loop = False