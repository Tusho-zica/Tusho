# 3. Solicite ao usuário 3 valores inteiros a,b,c. Crie uma função 
# que calcula o delta de baskara (b^2 - 4 . a . c). Utilize essa 
# função para verificar se o número tem duas raízes reais (delta > 0), 
# uma raiz real (delta = 0) ou nenhuma raiz real (delta < 0). 
# Se o número tiver raízes reais, calcule e imprima-as na tela (-b ± √∆) / 2.a. 
# Para a raiz quadrada: importe math e use math.sqrt( x ). *

import math

# Solicitando as variáveis ao usuário e já realizando a conversão para o tipo int
a = int(input("digite o valor de a:"))
b = int(input("digite o valor de b:"))
c = int(input("digite o valor de c:"))

#teste
#raiz1 = (-b + math.sqrt(delta)) / (a * 2)
#raiz2 = (-b - math.sqrt(delta)) / (a * 2)

#print("O valor de delta é: \n", delta)

# definindo a função chamada func_delta que irá receber os valores de a, b e c digitados pelo usuário
def func_delta(a,b,c):
    # Calculando delta
    delta = (b ** 2 - (4 * a * c))
    
    # Condição inicial: A variável A não pode ser 0.
    if a == 0 and b == 0 and c == 0:
        print("O valor de 'a' não podem ser zerado!")
    # Se a variavel não for 0, siga adiante.
    else:
        # Condições delta:
        #se delta < 0 = essa equação não possui raíz real
        #se delta == 0 = a raíz dessa equação é: 
        #se delta > 0 = as raízes dessa equação são: 
        if (delta == 0):
            raiz1 = (-b + math.sqrt(delta)) / (a * 2)
            return(f"A raíz da equação é: {raiz1}")
        else:
            if delta < 0:
                return("Essa equação não possui raíz real.")
            else:
                raiz1 = (-b + math.sqrt(delta)) / (a * 2)
                raiz2 = (-b - math.sqrt(delta)) / (a * 2)
                return(f"As raízes dessa equação são: {raiz1}, e {raiz2}")
    
# teste da função
print(func_delta(a,b,c))


