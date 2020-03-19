# Faça um algoritmo para simular uma situação simples de depósito, retirada e consulta em um banco. 
# O algoritmo inicialmente deverá mostrar um menu com as seguintes opções:

# Depósito
# Retirada
# Saldo
# Sair do algoritmo
# Se a escolha do usuário for depósito ou retirada, o algoritmo deverá pedir o valor da operação 
# e atualizar automaticamente o valor existente na conta. O algoritmo deverá ser utilizado até que 
# o usuário escolha a opção sair do algoritmo.

from ex11_cliente import Cliente

class ContaCorrente:
    def __init__(self, cliente, saldoInicial):
        self.cliente = Cliente(nome, idade, email)
        self.saldoInicial = saldo

    def deposito(self):
        deposito = float(input("Digite o valor que deseja depositar: "))

        self.saldoInicial += deposito
        print(f"Depósito realizado com sucesso. Seu novo saldo é de: {self.saldoInicial}")      

    def saque(self):
        saque = float(input("Digite o valor que deseja sacar: "))    

        if saque > self.saldoInicial:
            print(f"Você não tem saldo suficiente para realizar esta transação. Seu saldo é de: {self.saldoInicial}")
        else:
            self.saldoInicial -= saque
            print(f"Saque realizado com sucesso. Seu novo saldo é de: {self.saldoInicial}")

    def transferencia(self):      
        transferencia = float(input("Digite o valor que deseja transferir: "))

        if transferencia > self.saldoInicial:
            print(f"Você não tem saldo suficiente para realizar esta transação. Seu saldo é de: {self.saldoInicial}")
        else:
            self.saldoInicial -= transferencia
            print(f"Transferência realizada com sucesso. Seu novo saldo é de: {self.saldoInicial}")

    def __str__(self):
        return f'{self.saldoInicial}'

    def saldo_final(self):
        print(self.saldoInicial)


nome = input('Digite o nome: ')
idade = input('Digite a idade: ')
email = input('Digite o email: ')
cliente = Cliente(nome, idade, email)
cliente.imprime_cliente()
saldo = float(input("Digite o saldo inicial da conta: "))


