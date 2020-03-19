# Elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes categorias:

# infantil A = 5-7 anos;
# infantil B = 8-10 anos;
# juvenil A = 11-13 anos;
# juvenil B = 14-17 anos;
# adulto = maiores de 18 anos


idade = int(input("Digite a idade do nadador para saber sua classe: "))

if idade >= 5 and idade <= 7:
    print("Classe Infantil A")
elif idade >= 8 and idade <= 10:
    print("Classe Infantil B")
elif idade >= 11 and idade <= 13:
    print("Classe Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Classe Juvenil B")
elif idade >= 18:
    print("Classe Adulto")
else:
    print("Idade inválida")  