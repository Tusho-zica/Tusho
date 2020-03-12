# 2. Faça um programa como o do item anterior, porém que imprima a
# média sem considerar a maior e menor nota do aluno (nesse caso o
# número de provas precisa ser obrigatoriamente maior que dois).
# Dica: crie uma cópia com a lista de todas as notas antes de fazer a
# média.

nome = input("Digite seu nome\n")
idade = int(input("Quantos anos você tem?\n"))
num_provas = int(input("Quantas provas você fez? Mínimo 2\n"))
notas = []
contador = 0

if num_provas < 2:
    print("fodeu chóvem. Não da pra seguir assim.")

while contador != num_provas:
    notas.append(float(input("Digite a nota da prova\n")))
    contador += 1

lista = notas[:]

print(lista)
lista.sort()
lista.pop()
lista.pop(0)
soma = 0
media = 0

for item in lista:
    soma += item
    media = soma/len(lista)

passou = 0

if media >= 5:
    passou =True
else: 
    passou = False

# print(media)
# print(contador)
# print(notas)

lista_completa = [nome, idade, lista, media, passou]
print(lista_completa)