#Exercício Adicional 3 - Lista 1

dezena = int(input("Digite um número inteiro: "))

if dezena < 10:
    print("O dígito das dezenas é", 0)
elif dezena >= 10:
    print("O dígito das dezenas é", int(((dezena / 10) % 10) // 1))