#modelo simples

num0 = input("Digite o primeiro número da lista: ")
num1 = input("Digite o primeiro número da lista: ")
num2 = input("Digite o primeiro número da lista: ")
num3 = input("Digite o primeiro número da lista: ")
num4 = input("Digite o primeiro número da lista: ")

lista = [num0, num1, num2, num3, num4]
lista_float = []

for item in lista:
    lista_float.append(float(item))

print(lista)
print(lista_float)

#modelo mother fohcka! (comprehension)

list_float = [float(item) for item in lista]
print (list_float)

#SINTAXE: Variavel = [função (item) for item in "destino"]

#método mothafohcka com filtro

list_float_filter = [float(item) for item in lista if float(item) >= 10]
print (list_float_filter)

#Preferir usar compreensão a funcional.
