# Crie uma classe Bola cujos atributos são cor e raio. Crie um método
# que imprime a cor da bola. Crie um método para calcular a área dessa
# bola. Crie um método para calcular o volume da bola. Crie um objeto
# dessa classe e calcule a área e o volume, imprimindo ambos em
# seguida.
# Obs.: Área da esfera = 4*3.14*r*r/3; Volume da esfera = 4*3.14*r*r*r

class Bola:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
    
    def imprimir_cor_bola(self):
        print(self.cor)

    def area_bola(self):
        self.area = (4 * 3.14 * self.raio * self.raio) / 3
    
    def volume_bola(self):
        self.volume = (4 * 3.14 * self.raio * self.raio * self.raio)

    # def __str__(self):
    #     return f'Bola({self.cor}\n {self.area}\n {self.volume})'

    def imprime_bola(self):
        print(self.area, self.volume)

cor = "vermelho"
raio = 5
bola = Bola(cor, raio)
bola.cor = cor
bola.area_bola()
bola.volume_bola()
bola.imprimir_cor_bola()
bola.imprime_bola()


# __________________________________________________________________________________

class Bola2:
    def __init__(self, cor, raio):
        self.cor2 = cor
        self.raio2 = raio
    
    def imprimir_cor_bola2(self):
        return self.cor2

    def area_bola2(self):
        return 4 * 3.14 * self.raio2 * self.raio2 / 3
    
    def volume_bola2(self):
        return 4 * 3.14 * self.raio2 * self.raio2 * self.raio2

bola2 = Bola2("Verde", 10)
print(bola2.imprimir_cor_bola2(), bola2.area_bola2(), bola2.volume_bola2())