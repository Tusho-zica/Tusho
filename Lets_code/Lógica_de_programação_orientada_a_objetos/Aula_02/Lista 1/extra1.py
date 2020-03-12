# Peça para o usuário digitar uma velocidade inicial (em m/s), uma
# posição inicial (em m) e um instante de tempo (em s) e imprima a
# posição de um projétil nesse instante de tempo.
# Dica: use a fórmula matemática:
# 𝑦(𝑡) = 𝑦(0) + 𝑣(0) ∙ 𝑡 + (𝑔 ∙ 𝑡^2)/2
# Onde, g é a aceleração da gravidade (-10m/s²), y(t) é a posição
# final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o
# instante de tempo.

vel0 = int(input("digite a velocidade inicial (em m/s): "))
pos0 = int(input("digite a posição inicial (em m): "))
tem0 = int(input("digite um instante de tempo (em s): "))
g = (-10 * pos0) / (tem0 ** 2)
pos1 = 0

pos1 = pos0 + (vel0 * tem0) + ((g * tem0 **2) / 2)

print(f"A posição do projétil nesse instante de tempo é: {pos1}")