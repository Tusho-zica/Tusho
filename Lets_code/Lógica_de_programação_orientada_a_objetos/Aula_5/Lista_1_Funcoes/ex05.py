# 5. Faça uma função que recebe um nome e um horário e imprime “Bom
# dia, [nome]”, caso seja antes de 12h, “Boa Tarde, [nome]”, caso seja
# entre 12h e 18h e “Boa noite, [nome]” se for após às 18h.

from datetime import datetime
agora = datetime.now()
# print (agora)
# print(agora.hour)

def saudacoes(nome):
    if 0 < agora.hour < 12:
        return print(f"Bom dia, {nome}!")
    elif 12 < agora.hour < 18:
        return print(f"Boa tarde, {nome}!")
    else:
        return print(f"Boa noite, {nome}!")

nome = saudacoes(input("Digite aqui o seu nome:\n"))