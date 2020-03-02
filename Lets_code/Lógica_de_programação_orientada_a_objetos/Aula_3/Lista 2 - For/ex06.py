# Agora usando o método max() faça um programa que imprima os três
# maiores números de uma lista.
# Dica: Use o método próprio de listas .remove().

lista = [1, 2002, 20, 40, 5]
listanew = [None, None, None]

for i in lista:
    maxlista = max(lista)
    listanew.insert(0, maxlista)
    listanew.pop()
    lista.remove(maxlista)

print(lista)
print(listanew)