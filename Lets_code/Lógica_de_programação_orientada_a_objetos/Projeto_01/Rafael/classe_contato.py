class Contato:
    def __init__(self, nome, tel, email):
        self.nome = str(nome)
        self.tel = str(tel)
        self.email = str(email)

    def __str__(self):
        return f'{self.nome}, {self.tel}, {self.email}'