# Implemente um programa que lê três valores e três pesos. calcule e mostre a média ponderada

n1 = float(input("Digite a primeira nota: "))
p1 = float(input("Digite o peso da primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
p2 = float(input("Digite o peso da segunda nota: :"))
n3 = float(input("Digite a terceira nota: "))
p3 = float(input("Digite o peso da terceira nota: :"))

media_ponderada = ((n1 * p1) + (n2 * p2) + (n3 * p3)) / (p1 + p2 + p3)

print(media_ponderada)