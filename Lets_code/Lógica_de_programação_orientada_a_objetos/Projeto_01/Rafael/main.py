from classe_contato import Contato
from funcoes import comparar_numero, checar_email, ordenar_lista, formatar_para_csv
from classe_gerador_arquivo import GeradorArquivo, file_folder, file_name
import csv

class Programa:
    def __init__(self):
        self.contatos = []
        file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        self.contatos = [line.split(';') for line in lines]

    def buscar_contato(self, nome):

        file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        self.contatos = [line.split(';') for line in lines]

        # condição usando filter e lambda
        #Vide: https://pythonhelp.wordpress.com/2012/05/13/map-reduce-filter-e-lambda/
        condicao = filter(lambda x: x[0] == nome, self.contatos)
        filtro = list(condicao)

        resultado_busca = []
        for pos, item in enumerate(self.contatos):
            if item in filtro:
                resultado_busca.append(item)
                print(resultado_busca, pos)
        return pos

    def remover_contato(self, nome):
        file_reader = open(file_folder + file_name, 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        self.contatos = [line.split(';') for line in lines]

        identificador = 0

        file_writer = open(file_folder + file_name, 'w', encoding='utf-8')
        file_writer.write('Nome;Telefone;e-mail\n')
        for i in range(len(self.contatos)):
            self.contatos[i] = ordenar_lista(self.contatos[i])
        contato_alterado = [formatar_para_csv(contato) for contato in self.contatos]
        if nome == self.contatos[i]:
            identificador = 1
        if identificador != 1:
            file_writer.writelines(contato_alterado)

        # pos = self.buscar_contato(nome)
        # # print(f'selfcontatos antes: {self.contatos}')
        # if pos is not None:
        #     del self.contatos[pos]
        #     # atualizar o csv
        #     contato_alterado = [formatar_para_csv(contato) for contato in self.contatos]
        #     file_writer.writelines(contato_alterado)
        #     file_writer.close()
        #     # print(self.contatos)
        #     return True
        # # print(f'selfcontatos depois: {self.contatos}')
        # return False

        
        # with open(file_folder + file_name, "r") as file:
        #     contatos = csv.reader(file, delimiter=';')
        #     data = list(contatos)
        # with open(file_folder + file_name, "w") as file:
        #     file_writer = csv.writer(file, delimiter=';')
        #     ident = None
        #     for linha in data:
        #         linha = nome_contato, telefone, email
        #         if nome == nome_contato:
        #             ident = identificador
        #         if identificador != ident:
        #             file_writer.writerow(linha)


    def adicionar_contato(self):
        contato = []
        nome = input('Digite o nome: ')
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
        self.contatos = [line.split(';') for line in lines]
        print(f'{self.contatos}')

    def main(self):

        terminar = False

        while not terminar:
            comando = input(
                'Digite "b" para buscar um contato, "i" para inserir, "r" para remover, "p" para visualizar a lista armazenada e "s" para sair:\n')
            comando = comando.lower()

            if comando == 'b':
                nome = input('Digite o nome do contato que deseja buscar: ')
                nome = nome.title()
                self.buscar_contato(nome)
            elif comando == 'i':
                self.adicionar_contato()
            elif comando == 'r':
                nome = input('Digite o nome do contato que deseja remover: ')
                nome = nome.title()
                self.remover_contato(nome)
            elif comando == 'p':
                self.imprimir_contato()
            elif comando == 's':
                terminar = True
            else:
                print('comando inválido')


GeradorArquivo()
# Programa().imprimir_contato()
# Programa().adicionar_contato()
# Programa().imprimir_contato()
Programa().main()
