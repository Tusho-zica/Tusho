# 9. Faça uma função que recebe uma lista de palavras e retorna uma lista
# contendo as mesmas palavras da lista anterior, porém escritas em
# caixa alta.

def Upper(texto):
    texto = texto.upper()
    return texto

def Lower(texto):
    texto = texto.lower()
    return texto

teste = "este é um texto em letras minusculas"
teste2 = "ESTE É UM TEXTO EM LETRAS MAIUSCULAS"
print(Upper(teste))
print(Lower(teste2))