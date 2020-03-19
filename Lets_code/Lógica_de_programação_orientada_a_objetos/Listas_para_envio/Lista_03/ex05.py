# Faça uma função que receba uma string e retorne uma versão "invertido à esquerda de 2" 
# onde os dois primeiros caracteres são movidos para o final. O tamanho da string será 
# ao menos 2. Chame essa função de left_2.

# Ex: left_2('Hello') -> 'lloHe'


def left_2(str):
    a = str[2::]
    b = str[:2:]
    return a + b


print(left_2('Hello'))