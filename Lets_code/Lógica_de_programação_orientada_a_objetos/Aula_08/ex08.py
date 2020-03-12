# Crie uma classe ControleRemoto cujo atributo é televisão (isso é,
# recebe um objeto da classe do exercício 7). Crie métodos para
# aumentar/diminuir volume, trocar o canal e sintonizar um novo canal,
# que adiciona um novo canal à lista de canais (somente se esse canal
# não estiver nessa lista).

from ex07 import Televisor

class ControleRemoto():
    def __init__(self, canal):
        self.canal = canal
        # print(self.televisor)

    def __str__(self):
        return f'{self.televisor}'
    
    def aumentar_volume(self):
        print(Televisor.get_volume())



tv_std = Televisor("Philco", "Tubão", 5, [1,2,3,4,5], 10)
controle_std = ControleRemoto(tv_std)
controle_std.aumentar_volume()