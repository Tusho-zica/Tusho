# Lista telefonica
class Contato:
    def __init__(self, nome, ra, email):
        self.nome = nome
        self.ra = ra
        self.email = email

    # def __str__(self):
    #     return f'{self.nome}\n {self.ra}\n {self.email}'

    def imprime(self):
        print(self.nome, self.ra, self. email)

contatos = [
    Contato('Lucas', 123456, 'teste@teste.com'),
    Contato('teste', 987987, 'lucas@teste.com')
]

contatos[0].imprime()




