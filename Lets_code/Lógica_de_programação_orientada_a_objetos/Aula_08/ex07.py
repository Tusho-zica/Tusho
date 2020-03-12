# 7. Crie uma classe Televisor cujos atributos são:
# a. fabricante;
# b. modelo;
# c. canal atual
# d. lista de canais; e
# e. volume.
# Faça métodos para aumentar/diminuir volume, trocar o canal e
# sintonizar um novo canal, que adiciona um novo canal à lista de canais
# (somente se esse canal não estiver nessa lista). No atributo lista de
# canais, devem estar armazenados todos os canais já sintonizados
# dessa TV.
# Obs.: O volume não pode ser menor que zero e maior que cem; só se
# pode trocar para um canal que já esteja na lista de canais.


class Televisor:
    def __init__(self, fabricante, modelo, canal_atual, lista_canais, volume):
        self.fabricante = fabricante
        self.modelo = modelo
        self.canal_atual = canal_atual
        self.lista_canais = lista_canais
        self.volume = volume
        # print(self.fabricante, self.modelo, self.canal_atual, self.lista_canais, self.volume)

    def __str__(self):
        return f'{self.fabricante}, {self.modelo}, {self.canal_atual}, {self.lista_canais}, {self.volume}'

    def mudar_volume(self):
        print("vamos mudar o volume...")
        novo_volume = int(input("Digite o volume da televisão: "))

        if novo_volume < 0 or novo_volume > 100:
            print("Volume não pode ser menor que 0 ou maior que 100")
            # print(self.volume)
        else:
            self.volume = novo_volume
            print(f"Volume agora é: {self.volume}")
    
    def get_volume(self):
        return self.volume  

    def novo_canal(self):
        novo_canal = int(input("Digite o canal que deseja adicionar a lista: "))
        for canal in self.lista_canais:
            if novo_canal == canal:
                print("canal já exixtente.")
                break
        else:
            self.lista_canais.append(novo_canal)
            print("canal adicionado a lista de canais.")
        # print(novo_canal, self.lista_canais)

    def trocar_canal(self):
        print(f'Canais disponíveis: {self.lista_canais}')
        troca_canal = int(input("Digite o canal que deseja assistir: "))
        for canal in self.lista_canais:
            # print(canal, troca_canal)
            if troca_canal == canal:
                self.canal_atual = troca_canal
                print(f"O canal atual é: {self.canal_atual}")
                break
        else:
            print("Canal inválido")
            

                

# tv_std = Televisor("Philco", "Tubão", 5, [1,2,3,4,5], 10)
# print(tv_std)
# tv_std.mudar_volume()
# tv_std.novo_canal()
# print(tv_std.lista_canais)
# tv_std.trocar_canal()




# lista_canais = [1, 2, 3, 4, 5]
# canal_atual = 5
# canal = int(input("digite o canal que deseja assistir: "))
# # Televisor.novo_canal(canal)
# Televisor.trocar_canal(canal)