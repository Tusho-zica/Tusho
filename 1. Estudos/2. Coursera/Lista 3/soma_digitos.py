#soma de número informado

#quero receber um número qualquer e realizar a soma entre os números digitados

#Exemplo:
#Usuário digita 123456
#O sistema realizará a soma 1 + 2 + 3 + 4 + 5 + 6
#Resultado = 21

numero = input("Digite um número inteiro: ")

soma = 0
contador = len(numero)
numero = int(numero)
while contador != 0:
    mod = numero % 10
    soma += mod
    numero = numero // 10
    contador -= 1

print(soma)