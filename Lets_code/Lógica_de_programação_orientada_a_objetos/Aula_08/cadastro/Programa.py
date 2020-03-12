from Cliente import Cliente
from Cadastro import Cadastro

class Programa:
    def __init__(self):
        self.cadastro = Cadastro()

    def alterar(self):
        emailAtual = input('Digite o email atual para alterar o cliente: ')
        
        nome = input('Digite o novo nome para o cliente: ')
        idade = input('Digite a nova idade: ')
        email = input('Digite o novo email: ')
        cliente = Cliente(nome, idade, email)

        self.cadastro.alterar(emailAtual, cliente)

    def adicionar(self):
        nome = input('Digite o nome: ')
        idade = input('Digite a idade: ')
        email = input('Digite o email: ')
        cliente = Cliente(nome, idade, email)
        
        self.cadastro.adicionar(cliente)
    
    def imprimir(self):
        self.cadastro.imprimir()

    def main(self):

        terminar = False

        while not terminar:
            comando = input('Digite "i" para inserir, "a" para alterar, "p" para imprimir e "s" para sair:\n')
            comando = comando.lower()

            if comando == 'i': self.adicionar()
            elif comando == 'a': self.alterar()
            elif comando == 'p': self.imprimir()
            elif comando == 's': terminar = True
            else: print('comando inválido')

Programa().main()