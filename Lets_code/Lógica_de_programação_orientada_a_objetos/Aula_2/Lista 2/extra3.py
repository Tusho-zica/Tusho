# 3. Um hospital quer fazer o diagnóstico de gripe ou dengue a partir de
# um questionário de sintomas, tendo as perguntas abaixo, faça um
# programa que faça o diagnóstico deste hospital:
# a. Sente dor no corpo?
# b. Você tem febre?
# c. Você tem tosse?
# d. Está com congestão nasal?
# e. Tem manchas pelo corpo?
# Para o diagnóstico ele tem a seguinte tabela:



a = 0
b = 0
c = 0
d = 0
e = 0

print('Responda apenas "s" ou "n"')

dor = input("Sente dor no corpo?\n").lower()
if dor == "s":
    a += 1

febre = input("Você tem febre?\n").lower()
if febre == "s":
    b += 1

tosse = input("Você tem tosse?\n").lower()
if tosse == "s":
    c += 1

congestao = input("Está com congestão nasal?\n").lower()
if congestao == "s":
    d += 1

manchas = input("Tem manchas pelo corpo?\n").lower()
if manchas == "s":
    e += 1


# A    B      C    D      E       Resultado
# Sim  Sim    Não  Não    Sim     Dengue
# Sim  Sim    Sim  Sim    Não     Gripe
# Não  Sim    Sim  Sim    Não     Gripe
# Sim  Sim    Sim  Sim    Não     Gripe
# Sim  Não    Não  Não    Não     Sem Doenças
# Não  Não    Não  Não    Não     Sem Doenças


if a == 1 and b == 1 and c == 0 and d == 0 and e == 1:
    print("Parabéns! Você está oficialmente dengoso!")
elif (a == 1 or a == 0) and b == 1 and c == 1 and d == 1 and e == 0:
    print("Poxa, você só está gripado. Volte quando estiver pior!")
elif (a == 1 or a == 0) and b == 0 and c == 0 and d == 0 and e == 0:
    print("SAIA JÁ DAQUI SEU SADIO DO CARALHO!")
else:
    print("Não sei o que você tem, mas parece mimimi.")