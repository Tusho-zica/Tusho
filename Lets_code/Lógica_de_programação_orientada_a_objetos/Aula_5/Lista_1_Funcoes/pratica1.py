# Faça uma função que imprime hello na tela
# Faça uma função para cada operação matemática (+, -, /, *)
# Faça uma função que recebe uma lista e retorna a média

def hello(texto):
    print("Hello!")
    return

hello(hello)

def soma(x, y):
    return x + y

print(soma(10, 20))

def subtracao(x, y):
    return x - y

print(subtracao(10,20))

def divisao(x, y):
    return x / y

print(divisao(10,20))

def multiplicacao(x, y):
    return x * y

print(multiplicacao(10,20))

def media(lista):
    return sum(lista) / len(lista)

lista1 = [10, 20, 50]
print(media(lista1))

# Faça uma função que recebe uma lista e uma outra função que aplique a função 
# recebida por parametro em cada item da lista retorne uma nova lista com novos valores.

def map_manual(lista, f):
    return [f(x) for x in lista]

lista_1 = [10, 20, 30]
lista_2 = map_manual(lista1, lambda x : x * 2)
print(lista_2)