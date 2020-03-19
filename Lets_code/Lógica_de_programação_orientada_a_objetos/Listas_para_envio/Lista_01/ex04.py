# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: 
# F - Feminino, M - Masculino, Sexo Inválido. 
# Obs: O programa deve funcionar para letras maiúsculas e minúsculas.

sexo = input("Digite o sexo para verificação (F/M):\n")
sexo = sexo.upper()

if sexo == 'F':
    print("F - Feminino")
elif sexo == 'M':
    print("M - Masculino")
else:
    print("Sexo Inválido.")