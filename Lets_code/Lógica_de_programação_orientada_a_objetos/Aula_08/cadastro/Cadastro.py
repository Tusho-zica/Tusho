class Cadastro:
    def __init__(self):
        self.clientes = []

    def adicionar(self, cliente):
        self.clientes.append(cliente)

    def buscar_cliente(self, email):
        for pos, cliente in enumerate(self.clientes):
            if cliente.email == email:
                return pos
        return None

    def remover(self, email):
        pos = self.buscar_cliente(email)
        if pos is not None:
            del self.clientes[pos]
            return True
        return False
    
    def alterar(self, email, cliente):
        if self.remover(email):
            self.adicionar(cliente)

    def imprimir(self):
        for cliente in self.clientes:
            print(cliente)
