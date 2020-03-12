

# file = open()

# file.close()


# abrir arquivo sem a necessidade de usar o close no final
# with open() as file:
    # './teste.csv'
    # '../teste.csv'
    # './teste/teste.csv'
    # O r retira a necessidade de colocar scapes (\) para poder utilizar caracteres especiais.
    # r"C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Aula_10\teste.txt.py"


fileHandler = open(r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Aula_10\Manipulação_de_arquivos\teste.txt', 'r', encoding = 'utf-8')
content = fileHandler.read()
#Padronização dos arquivos de windows para linux.
#a quebra de linha do windows é representada por \r\n
#a quebra no linux é somente \n.
content.replace('\r\n', '\n')
print(content.split('\n'))
fileHandler.close()


#OOOOOOOOU...

fileHandler2 = open(r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Aula_10\Manipulação_de_arquivos\teste.txt', 'r', encoding = 'utf-8')
content2 = fileHandler2.readlines()
print([line.strip() for line in content2])
fileHandler2.close()



# OUTRA MANEIRA:

fileHandler3 = open(r'C:\Users\tusho\Desktop\Python\Lets_code\Lógica_de_programação_orientada_a_objetos\Aula_10\Manipulação_de_arquivos\teste.txt', 'r', encoding = 'utf-8')
for line in fileHandler3:
    print([line.strip() for line in fileHandler3])
fileHandler3.close()