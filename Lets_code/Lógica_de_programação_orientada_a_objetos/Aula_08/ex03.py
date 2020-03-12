# Crie uma classe Cliente cujos atributos são nome, idade e e-mail.
# Construa um método que imprima as informações tal como abaixo:
# Nome: Fulano de Tal
# Idade: 40
# E-mail: fulano@mail.com

class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def __str__(self):
        return f'{self.nome} {self.idade} {self.email}'

    def imprime_cliente(self):
        print(f' Nome: {self.nome}\n Idade: {self.idade}\n E-mail: {self.email}\n')
    
nome = 'Fulano de Tal'
idade = 40
email = 'fulano@mail.com'
cliente = Cliente(nome, idade, email)

cliente.imprime_cliente()