#11. Faça um programa que peça 2 números inteiros e um número real,
# calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo.
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.

int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
real = float(input("Digite um número real: "))

resp1 = (int1 * 2) * (int2 / 2)
resp2 = (int1 * 3) + real
resp3 = (real ** 3)

print("o produto do dobro do primeiro com metade do segundo é:\n", resp1)
print("a soma do triplo do primeiro com o terceiro é: \n", resp2)
print("o terceiro elevado ao cubo é:\n", resp3)

