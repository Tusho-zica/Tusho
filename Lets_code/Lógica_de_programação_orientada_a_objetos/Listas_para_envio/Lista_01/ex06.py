# Prepare um algoritmo para realizar o cálculo do preço de um serviço de Consultoria. 
# Seu algoritmo deverá perguntar os seguintes dados e informar o valor total do serviço:
# Tipo de Serviço (Projeto ou Auditoria)
# N.o dias trabalhados
# N.o de viagens realizadas 
# 
# Você deve usar a seguinte tabela para calcular o valor dos serviços:
# Tipo de serviço	Dia de trabalho	        Cada viagem
# Projeto				200,00			    500,00
# Auditoria			    100,00			    1500,00

servico = input("Digite o tipo de serviço prestado (Projeto ou Auditoria): ")
servico = servico.title()
dias_trabalhados = int(input("Digite o número de dias trabalhados: "))
viagens = int(input("Digite o número de viagens realizadas: "))
preco_servico = 0

if servico == 'Projeto':
    preco_servico = (dias_trabalhados * 200) + (viagens * 500)
    print(f"O preço do serviço prestado é de: {preco_servico}")
elif servico == 'Auditoria':
    preco_servico = (dias_trabalhados * 100) + (viagens * 1500)
    print(f"O preço do serviço prestado é de: {preco_servico}")
else:
    print("O tipo de servico informado é inválido.")
