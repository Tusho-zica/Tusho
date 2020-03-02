#while_soma

sequencia = int(input("Digite o número da sequência de valores que serão somados: "))
#soma começa com o elemento neutro
soma = 0

#para que o programa entre no loop, o valor de while não pode ser 0
valor = 1

#iniciei o contador com 1 (estou usando contador <= sequencia)
contador = 1

while contador <= sequencia:
    valor = float(input("Digite um valor a ser somado: "))
    soma += valor
    contador += 1

print("a soma dos valores digitados é: ", soma)
