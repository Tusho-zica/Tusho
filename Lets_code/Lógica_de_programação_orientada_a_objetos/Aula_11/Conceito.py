'''

Tratamendo de erros

'''
# ZeroDivisionError
# x = 9 / 0
# print (x)

# IndexError
# lista = [1,2,3]
# print(lista[8])

# TypeError
# print('a' + 1)

# try:
#     print('a' + 1)
# except:
#     print('error')

# def div(a,b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print('Divisão por zero')
#         return None

# div(10, 0)

lista_problemas = []

with open(r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Aula_11\teste.csv', 'r', encoding='utf-8') as file:
    count = 0
    for line in file:
        count += 1
        data = line.strip().split(',')
        try:
            print(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
        except:
            lista_problemas.append(f"problema na linha {count}")

print(lista_problemas)
