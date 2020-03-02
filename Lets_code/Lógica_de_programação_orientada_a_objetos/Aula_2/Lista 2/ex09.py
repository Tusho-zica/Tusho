# Um produto vai sofrer aumento de acordo com a Tabela 1 abaixo. Faça
# um programa que peça para o usuário digitar o valor do produto de
# acordo com o preço antigo e escreva uma das mensagens da Tabela
# 2, de acordo com o preço reajustado:
# 
# Preço Antigo Percentual de   Aumento

# Até R$ 50                     5%
# Entre R$ 50 e R$100           10%
# Entre R$100 e R$150           13%
# Acima de R$150                15%

valor = float(input("digite o valor do produto:\n"))

valor_ajustado = 0

if valor <= 50:
    valor_ajustado = valor + (valor * 0.05)
elif valor > 50 and valor <= 100:
    valor_ajustado = valor + (valor * 0.10)
elif valor > 100 and valor <= 150:
    valor_ajustado = valor + (valor * 0.13)
elif valor > 150:
    valor_ajustado = valor + (valor * 0.15)

# Preço Novo                    Mensagem
# Até R$80                      Barato
# Entre R$ 80 e R$115           Razoável
# Entre R$ 115 e R$150          Normal
# Entre R$ 150 e R$170          Caro
# Acima de R$170                Muito Caro

if valor_ajustado <= 80:
    print(valor_ajustado)
    print("Barato")
elif valor_ajustado > 80 and valor_ajustado <= 115:
    print(valor_ajustado)
    print("Razoável")
elif valor_ajustado > 115 and valor_ajustado <= 150:
    print(valor_ajustado)
    print("Normal")
elif valor_ajustado > 150 and valor_ajustado <= 170:
    print(valor_ajustado)
    print("Caro")
elif valor_ajustado > 170:
    print(valor_ajustado)
    print("MuitoCaro")


