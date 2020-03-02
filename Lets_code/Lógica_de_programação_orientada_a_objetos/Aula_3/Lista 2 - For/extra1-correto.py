import random

lista1 = random.sample(range(20), 10)
lista2 = random.sample(range(20), 10)

print(lista1)
print(lista2)

result = []
for i, num in enumerate(lista1):
    partial_result = []
    for j, num2 in enumerate(lista1):
        if num == num2 and i != j:
            partial_result.append(j)
    result.append((num, partial_result))

print(result)