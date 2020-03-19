class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email
        
    def __str__(self):
        return f'{self.nome} {self.idade} {self.email}'

    def imprime_cliente(self):
        print(f' Nome: {self.nome}\n Idade: {self.idade}\n E-mail: {self.email}\n')
    