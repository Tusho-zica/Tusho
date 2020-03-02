#indicar se o número possui dois digitos adjacentes iguais


numero_base = input("Digite um número qualquer: ")

adjacente = False

contador = len(numero_base)
numero_base = int(numero_base)

unidade = 0
dezena = 0
if contador == 1:
    print("não")
else:
    while contador != 0 and adjacente == False:
        unidade = numero_base % 10
        dezena = (numero_base // 10 ) % 10
        numero_base = numero_base // 10
        if dezena == unidade:
            adjacente = True
        contador -= 1     
    if unidade == dezena:
        print("sim")
    else:
        print("não")