#Função para equação de segundo grau

import math

a = float(input("digite o valor de a:"))
b = float(input("digite o valor de b:"))
c = float(input("digite o valor de c:"))

delta = (b ** 2 - (4 * a * c))

#raiz1 = (-b + math.sqrt(delta)) / (a * 2)
#raiz2 = (-b - math.sqrt(delta)) / (a * 2)

#print("O valor de delta é: \n", delta)

#print("O valor de x é: \n", x)


#se delta < 0 = essa equação não possui raíz real
#se delta == 0 = a raíz dessa equação é: 
#se delta > 0 = as raízes dessa equação são: 


if (delta == 0):
    raiz1 = (-b + math.sqrt(delta)) / (a * 2)
    print("a raiz desta equação é", raiz1)
else:
    if delta < 0:
        print("esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (a * 2)
        raiz2 = (-b - math.sqrt(delta)) / (a * 2)
        if (raiz1 > raiz2):
            print("as raízes da equação são", raiz2, "e", raiz1)
        else:
            print("as raízes da equação são", raiz1, "e", raiz2)


