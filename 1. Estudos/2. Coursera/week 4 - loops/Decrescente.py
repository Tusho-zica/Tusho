#indicador de passagem
#sequencia decrescente


decrescente = True
primeiro_numero = int(input("Digite o primeiro número da sequência: "))

contador = 1

while contador != 0 and decrescente:
    contador = int(input("Digite o próximo número da sequência: "))
    if contador > primeiro_numero:
        decrescente = False
    primeiro_numero = contador

if decrescente == True:
    print("A sequência está em ordem decrescente")
else:
    print("A sequencia não está em ordem decrescente")


