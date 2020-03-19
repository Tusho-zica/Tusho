from classe_contato import Contato
from funcoes import comparar_numero, checar_email, ordenar_lista, formatar_para_csv
file_folder = r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Projeto_01'
file_name = r'\contatos_organizados_3.csv'


class GeradorArquivo:
    def __init__(self):

        # Extração
        # abre o stream
        file_reader = open(file_folder + r'\contatos.csv',
                           'r', encoding='utf-8')
        # lê as linhas do arquivo e armazena na variável
        lines = file_reader.readlines()
        # fecha o stream
        file_reader.close()

        # Transformação
        # já com o stream fechado, manipula os dados:
        lines = [line.strip() for line in lines]
        lines = [line.strip(';') for line in lines]
        content = [line.split(';') for line in lines]

        contato_format = []
        for i in range(len(content)):
            contato_format.append(ordenar_lista(content[i]))
        # print(f'ordenada = {contato_format}')

        file_writer = open(
            file_folder + r'\contatos_organizados_3.csv', 'w', encoding='utf-8')
        file_writer.write('Nome;Telefone;e-mail\n')
        data = [formatar_para_csv(contato) for contato in contato_format]
        file_writer.writelines(data)
        file_writer.close()
