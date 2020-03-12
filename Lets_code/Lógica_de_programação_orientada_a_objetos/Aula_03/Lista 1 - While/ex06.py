# 6. Faça um programa, usando loops, que peça para um usuário digitar
# um número e que só finaliza quando o usuário digitar 0. Ao final
# imprima a soma de todos os números digitados.

print("Digite uma sequência de valores que finaliza o loop quando informado o valor 0")
#soma começa com o elemento neutro
soma = 0

#para que o programa entre no loop, o valor de while não pode ser 0
valor = 1

while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma += valor

print("a soma dos valores digitados é: ", soma)