class Cadastro:
    def __init__(self):
        self.contatos = []

    def adicionar(self, contato):
        self.contatos.append(contato)

    def buscar_contato(self, nome):
        for pos, contato in enumerate(self.contatos):
            if contato.nome == nome:
                return pos
            return None

    def remover(self, email):
        pos = self.buscar_contato(email)
        if pos is not None:
            del self.contatos[pos]  # remoção em lista
            return True
        return False

    def alterar(self, email, contato):
        if self.remover(email):
            self.adicionar(email)

    def imprimir(self):
        for contato in self.contatos:
            print(contato)