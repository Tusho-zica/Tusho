#Para um numero de 0 até 10 passo 1 faça:

#Na linguagem C ---> for (int i = 0; i < 10; i++)
#                        (DE;       ATÉ;    Passo)

#Exemplo:

lista = [1, 2, 3, 4]

for item in lista:
    print(item)
print("___________")

lista2 = range(10)

for _ in lista2:
    print(_)
print("___________")

#Quando a variavel não for utilizada em nenhum outro lugar do código, pelas boa práticas, usar sempre o "_" no lugar do "item"

lista3 = range(0, 10, 2)

for i in lista3:
    print(i)
print("___________")

lista4 = [11, 25, 63, 74, 95, 62, 71]

for i, v in enumerate(lista4):
    print(i, v)
print("___________")

#Primeiro a posição do valor na lista, depois o valor dessa posição


#melhor forma de verificar todos os dados de uma lista.

for i in range(len(lista)):
    print(i, lista[i])
