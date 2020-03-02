#números ímpares

#Receba um número inteiro positivo na entrada e imprima os nn primeiros números ímpares naturais. 


n = int(input("Digite o valor de n: "))

count = 0
aux = 0

while (count < n * 2):
    aux += 1 
    if aux % 2 != 0:
        print (aux)
    count += 1
    