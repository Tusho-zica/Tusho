#14. Faça um programa que peça um valor monetário e diminua-o em 15%.
#Seu programa deve imprimir a mensagem “O novo valor é R$[valor]”.

valor = float(input("Indique um valor em reais: "))
percentual = valor * 0.15
montante = valor - percentual

print(montante)

#ou valor /= 1.15