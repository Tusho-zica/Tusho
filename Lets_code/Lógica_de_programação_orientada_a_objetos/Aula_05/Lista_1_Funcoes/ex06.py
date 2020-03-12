# 6. Faça uma função que recebe um número e retorna True se ele é par
# ou False, se ele é ímpar.

def par(num):
    if num % 2 == 0:
        return print(True)
    else:
        return print(False)


num = par(int(input("Digite um número. Se for Par o resultado será True!\n")))