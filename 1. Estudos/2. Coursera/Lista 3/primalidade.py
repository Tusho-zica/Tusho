#Escreva um programa que receba um número inteiro positivo
#na entrada e verifique se é primo. Se o número for primo,
#imprima "primo". Caso contrário, imprima "não primo".

num = int(input("Digite um número inteiro: "))

#0 e 1 não são primos.
#2, 3, 5, 7, 11, 13, 17, 19, 21...

if num > 1: 
   for i in range(2, num): 
       if (num % i) == 0: 
           print("não primo")
           break
   else: 
       print("primo") 
else: 
   print("não primo") 