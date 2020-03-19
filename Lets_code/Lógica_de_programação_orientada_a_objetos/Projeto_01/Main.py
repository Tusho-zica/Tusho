from classe_contato import Contato
from funcoes import comparar_numero, checar_email, ordenar_lista, formatar_para_csv
from programa_de_cadastro import GeradorArquivo, file_folder, file_name

class Programa:
    def __init__(self):
        self.contatos = []
        # file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        # lines = file_reader.readlines()
        # file_reader.close()
        # lines = [line.strip() for line in lines]
        # self.contatos = [line.split(';') for line in lines]

    def buscar_contato(self, nome):    

        file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        busca_contatos = [line.split(';') for line in lines]

        #condição usando filter e lambda
        #Vide: https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
        condicao = filter(lambda x: x[0] == nome, busca_contatos)
        filtro = list(condicao)

        resultado_busca = []
        for pos, item in enumerate(busca_contatos):
            if item in filtro:
                resultado_busca.append(item)
                print(resultado_busca, pos)
        return pos

    def remover_contato(self, nome):
        file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        remove_contatos = [line.split(';') for line in lines]

        #condição usando filter e lambda
        #Vide: https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
        condicao = filter(lambda x: x[0] != nome, remove_contatos)
        resultado = list(condicao)
        # print(resultado)

        contato_format = []
        for i in range(len(resultado)):
            contato_format.append(ordenar_lista(resultado[i]))

        file_writer = open(file_folder + file_name, 'w', encoding='utf-8')
        data = [formatar_para_csv(contato) for contato in contato_format]
        file_writer.writelines(data)
        file_writer.close()


    def adicionar_contato(self):
        contato = []
        nome = input('Digite o nome: ')
        nome = nome.title()
        telefone = input('Digite o telefone: ')
        email = input('Digite o email: ')
        contato.append(Contato(nome, telefone, email))
        
        file_writer = open(file_folder + file_name, 'a', encoding='utf-8')
        data = [formatar_para_csv(contato) for contato in contato]
        file_writer.writelines(data)
        file_writer.close()
    
    def imprimir_contato(self):
        file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        imprime_contatos = [line.split(';') for line in lines]
        print(imprime_contatos)

    def main(self):

        terminar = False

        while not terminar:
            comando = input('Digite "b" para buscar um contato, "i" para inserir, "r" para remover, "p" para visualizar a lista armazenada e "s" para sair:\n')
            comando = comando.lower()

            if comando == 'b': 
                nome = input('Digite o nome do contato que deseja buscar: ')
                nome = nome.title()
                self.buscar_contato(nome)
            elif comando == 'i': self.adicionar_contato()
            elif comando == 'r': 
                nome = input('Digite o nome do contato que deseja remover: ')
                nome = nome.title()
                self.remover_contato(nome)
            elif comando == 'p': self.imprimir_contato()
            elif comando == 's': terminar = True
            else: print('comando inválido')

GeradorArquivo()
# Programa().imprimir_contato()
# Programa().adicionar_contato()
# Programa().imprimir_contato()
Programa().main()