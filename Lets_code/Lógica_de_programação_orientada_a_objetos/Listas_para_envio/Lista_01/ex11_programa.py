from ex11_cliente import Cliente
from ex11_Conta_Corrente import ContaCorrente

class Programa:
    
    def __init__(self):
        self.contaCorrente = ContaCorrente(Cliente,0)

    def main(self):

        terminar = False

        while not terminar:
            comando = input('Digite "1" para verificar o saldo atual da conta, "2" para depositar, "3" para sacar, "4" para transferir e "0" para sair:\n')
            comando = int(comando)

            if comando == 1: self.contaCorrente.saldo_final()
            elif comando == 2: self.contaCorrente.deposito()
            elif comando == 3: self.contaCorrente.saque()
            elif comando == 4: self.contaCorrente.transferencia()
            elif comando == 0: terminar = True
            else: print('comando inválido')

Programa().main()