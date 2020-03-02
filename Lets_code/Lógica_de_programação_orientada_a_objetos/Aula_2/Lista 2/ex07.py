# 7. Faça um programa que mostre uma questão de múltipla escolha com
# 5 opções (letras a, b, c, d, e e). Sabendo a resposta certa, o programa
# deve receber a opção do usuário e informar a letra que o usuário
# marcou e se a resposta está certa ou errada.

print("digite apenas a letra como resposta...")
resposta = input("Em que ano o Brasil foi penta campeão?\n a 1998\n b 2006\n c 1994\n d 2002\n e 1990\n\n")

if resposta == "d":
    print("RESPOSTA CERTA")
else:
    print("ERROOOOOOOOU, ta pegando fogo, bicho!")

