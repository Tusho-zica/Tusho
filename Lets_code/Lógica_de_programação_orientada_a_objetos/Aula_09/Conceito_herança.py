class Ponto2D:
    def __init__(self):
        self.x = 0
        self.y = 0
    
    def imprimir(self):
        print(self.x, self.y)

class Ponto3D(Ponto2D):
    def __init__(self):
        self.z = 0

    #Estamos sobrescrevendo a função da classe pai na classe filha.
    def imprimir(self):
        print(self.x, self.y, self.z)

ponto = Ponto2D()

ponto.x = 1
ponto.y = 2
ponto.imprimir()

ponto2 = Ponto3D()
ponto2.x = 1
ponto2.y = 2
ponto2.z = 3
ponto2.imprimir()
