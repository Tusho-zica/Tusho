#while_produto

sequencia = int(input("Digite o número da sequência de valores que serão multiplicados: "))

#produto começa com o elemento neutro
produto = 1

#para que o programa entre no loop, o valor de while não pode ser 0
valor = 1

#iniciei o contador com 0 (estou usando contador < sequencia)
contador = 0

while contador < sequencia:
    valor = float(input("Digite um valor a ser multiplicado: "))
    produto *= valor
    contador += 1

print("o produto dos valores digitados é: ", produto)