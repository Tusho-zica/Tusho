from classe_contato import Contato
from funcoes import comparar_numero, checar_email, ordenar_lista, formatar_para_csv
file_folder = r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Projeto_01'

class Cadastro:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

        file_writer = open(file_folder + r'\contatos_organizados.csv', 'a', encoding='utf-8')
        data = [formatar_para_csv(contato) for contato in contato]
        file_writer.writelines(data)
        file_writer.close()

    def buscar_contato(self, nome):
        for pos, contato in enumerate(self.contatos):
            if contato.nome == nome:
                return pos
            return None

    def remover(self, nome):
        pos = self.buscar_contato(nome)
        if pos is not None:
            del self.contatos[pos]  # remoção em lista
            return True
        return False

    def alterar(self, email, contato):
        if self.remover(email):
            self.adicionar(email)

    def imprimir(self):
        file_reader = open(file_folder + r'\contatos_organizados.csv', 'r', encoding='utf-8')
        lines = file_reader.readlines()
        file_reader.close()
        lines = [line.strip() for line in lines]
        content = [line.split(';') for line in lines]
        print(content)