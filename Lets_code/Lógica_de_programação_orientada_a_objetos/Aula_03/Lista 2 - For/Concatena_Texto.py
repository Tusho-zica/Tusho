texto =''

while True:
    comando = input('Digite "i" para adicionar e "d" para remover.\n')
    if comando == "i":
        letra = input("Digite uma letra: ")
        texto += letra
    elif comando == "d":
        texto = texto [:-1]
    elif comando == '':
        break
    else:
        print("comando inválido")
print(texto)
