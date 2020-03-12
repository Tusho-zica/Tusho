# Crie uma classe lampada com um atributo aceso (bool)
# Esse atributo deve ser encapsulado e aterado apenas pelos metodos ascender e apagar.
# E um método __str__ que mostre o estado atual.

class Lampada:
    def __init__(self):
        self.__aceso = True

    def acender(self):
        self.__aceso = True
        
    def apagar(self):
        self.__aceso = False
    
    def __str__(self):
        if self.__aceso == True:
            return "Aceso"
        else:
            return "Apagado"

# Crie uma classe interruptor que tem uma lista encapsulada de lampadas.
# Ele deve ter um metodo adicionar que recebe uma lampada e adiciona-a na lista
# Ele deve ter um metodo apagar que apaga todas as lampadas
# E um metodo acender que acente todas as lampadas.

class Interruptor:
    def __init__(self):
        self.__lampadas = []
    
    def incluir_lampadas(self, lampada):
        self.__lampadas.append(lampada)
        # tamanho = len(self.__lampadas)
        # print(f'lampada adicionada. O novo número de lampadas é: {tamanho}')

    def apagar_lampadas(self):
        for lampada in self.__lampadas:
            lampada.apagar()
            print(lampada) 
            # return lampada
        
    def acender_lampadas(self):
        for lampada in self.__lampadas:
            lampada.acender()
            print(lampada)
            # return lampada
    
    def __str__(self):
        for _ in self.__lampadas:
            return "\t".join([str(lampada) for lampada in self.__lampadas])


l1 = Lampada()
l2 = Lampada()
l3 = Lampada()
Interrup = Interruptor()

Interrup.incluir_lampadas(l1)
Interrup.incluir_lampadas(l2)
Interrup.incluir_lampadas(l3)

Interrup.acender_lampadas()
print(Interrup)
Interrup.apagar_lampadas()
print(Interrup)

