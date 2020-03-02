# sorteia duas listas.
# crie uma lista com a interseção dos items das duas

# para sortear você deve usar o random.sample()

# Veja a documentação!

import random

lista1 = random.sample(range(20), 10)
lista2 = random.sample(range(20), 10)

print(lista1)
print(lista2)

result = []
for num in lista1:
    partial_result = []
    for i, num2 in enumerate(lista1):
        if num == num2:
            partial_result.append(i)
    result.append((num, partial_result))

print(result)


lista3 =[random.randint(0,100) for x in range(10)]
pares = [x for i, x in enumerate(lista3) if i % 2 ==0]

print(lista3)
print(pares)