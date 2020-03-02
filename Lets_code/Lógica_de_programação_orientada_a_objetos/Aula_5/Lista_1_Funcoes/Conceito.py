import math
def raiz_quadrada(valor):
    return math.sqrt(valor)



def input_int(texto):
    num = int(input(texto))
    return num

num = float(input("Digite um número"))

#sem usar a função
resultado2 = num ** 0.5
#usando a função
resultado = raiz_quadrada(num)

print(resultado2)
print(resultado)

#sem usar a função
num1 = input("Digite um texto")
#usando a função
num2 = input_int("Digite um texto")

print([num1, num2])