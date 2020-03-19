# Prepare um algoritmo para perguntar o nome, o sexo e a idade de 40 pessoas e informar:

# a média de idades
# a média de idades dos homens
# o total de mulheres

lista_nome = []
lista_sexo = []
lista_idade_geral = []
lista_idade_mulheres = []
lista_idade_homens = []

count = 0

while count < 40:
    nome = input("Digite o nome: ")
    lista_nome.append(nome)
    sexo = input("Digite o sexo (M/F): ")
    sexo = sexo.upper()
    lista_sexo.append(sexo)

    if sexo == 'F':
        idade_mulheres = int(input("Digite a idade: "))
        lista_idade_mulheres.append(idade_mulheres)
        lista_idade_geral.append(idade_mulheres)
    else:
        idade_homens = int(input("Digite a idade: "))
        lista_idade_homens.append(idade_homens)
        lista_idade_geral.append(idade_homens)
    count += 1

# print(lista_nome)
# print(lista_sexo)
# print(lista_idade_geral)
# print(lista_idade_mulheres)
# print(lista_idade_homens)

# a média de idades

soma = 0

for item in lista_idade_geral:
    soma += item
    media_idade = soma/len(lista_idade_geral)

# a média de idades dos homens

soma_h = 0

for item_h in lista_idade_homens:
    soma_h += item_h
    media_idade_homens = soma_h/len(lista_idade_homens)

# o total de mulheres

count = 0

for item_h in lista_idade_mulheres:
    count +=1
    total_mulheres = count

print(f"A média geral das idades é de: {media_idade}")
print(f"A média das idades dos participantes homens é de: {media_idade_homens}")
print(f"O total de participantes mulheres é de: {total_mulheres}")


