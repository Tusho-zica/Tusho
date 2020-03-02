#fizzbuzz parcial parte3

numero_entrada = int(input("digite um número inteiro: "))

if (numero_entrada % 3 == 0 and numero_entrada % 5 == 0):
    print("FizzBuzz")
else:
    print(numero_entrada)