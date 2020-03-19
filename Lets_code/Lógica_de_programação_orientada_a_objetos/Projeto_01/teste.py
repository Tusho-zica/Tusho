file_folder = r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Projeto_01'

# def buscar_contato(self, nome):
#     file_reader = open(file_folder + r'\contatos_organizados.csv', 'r', encoding='utf-8')
#     lines = file_reader.readlines()
#     file_reader.close()
#     lines = [line.strip() for line in lines]
#     content = [line.split(';') for line in lines]
#     print(content)

#     lista_busca = []
#     for i in range (len(content)):
#         for j in range (i):
#             if nome in content[i][j]:
#                 lista_busca.append((i, j))
#     return lista_busca


# teste = buscar_contato('Alisha', 'teste')
# print (teste)

#  , ['Simona', '4195032484', 'simona@morasca.com'], , ['Leota', '4087523500', 'leota@hotmail.com'], ['Sage', '6054142147', 'sage_wieser@cox.net'], ['Kris', '4106558723', 'kris@gmail.com'], ['Minna', '2158741229', 'minna_amigon@yahoo.com'], ['Abel', '6313353414', 'amaclead@gmail.com'], ['Kiley', '3104985651', 'kiley.caldarera@aol.com'], ['Graciela', '4407808425', 'gruta@cox.net'], ['Cammy', '9565376195', 'calbares@gmail.com'], ['Mattie', '6022774385', 'mattie@aol.com'], ['Meaghan', '9313139635', 'meaghan@hotmail.com'], ['Gladys', '4146619598', 'gladys.rim@rim.org'], ['Yuki', '3132887937', 'yuki_whobrey@aol.com'], ['fFletcher', '8158282147', 'letcher.flosi@yahoo.com'], ['Bette', '6105453615', 'bette_nicka@cox.net'], ['Veronika', '4085401785', 'vinouye@aol.com'], ['Willard', '9723039197', 'willard@hotmail.com'], ['Maryann', '5189667987', 'mroyster@royster.com'], ['Alisha', '7326583154', 'alisha@slusarski.com']]


lista = [['Nome', 'Telefone', 'e-mail'], ['James', '1146218927', 'jbutt@gmail.com'], ['Josephine', '8102929388', 'josephine_darakjy@darakjy.org'], ['Art', '8566368749', 'art@venere.org'], ['Mitsue', '7735736914', 'mitsue_tollner@yahoo.com']]
nome = input('Digite o nome do contato que deseja buscar: ')
nome = nome.title()
# #Conjunto de dados
# # data = [['julian', '0', '5'], ['ana', '10', '4']]
# finder = 'julian'

#Faz o filtro da lista atraves da condição especificada
condicao = filter(lambda x: x[0] == nome, lista)
#Converte o filtro para uma lista comum
filters = list(condicao)

result = []
#Percorre cada item da lista enumerando
for index, item in enumerate(lista):
    if item in filters:
        result.append(item)

print(result)