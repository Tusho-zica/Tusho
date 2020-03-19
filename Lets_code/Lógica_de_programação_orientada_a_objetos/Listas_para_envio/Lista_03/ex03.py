# Faça uma função chamada inverte_numero que retorne o reverso de um número 
# inteiro informado. Por exemplo: 127 -> 721.

def inverte_numero(numero):
    numero = str(numero)
    return numero[::-1]


print(inverte_numero(123456789))