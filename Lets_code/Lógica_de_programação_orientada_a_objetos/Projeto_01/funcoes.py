from classe_contato import Contato

def comparar_numero(string):
    numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    status = False
    for i in range(len(numeros)):
        if numeros[i] in string:
            status = True
    return status

def checar_email(string):
    arroba = '@'
    status = False
    if arroba in string:
        status = True
    return status

def ordenar_lista(lista):
    email = None
    tel = None
    nome = None
    for i in range(len(lista)):
        if checar_email(lista[i]):
            email = lista[i]
            # print(f'email = {email}')
        elif comparar_numero(lista[i]):
            tel = lista[i]
            # print(f'tel = {tel}')
        else:
            nome = lista[i]
            # print(f'nome = {nome}')
    return Contato(nome,tel,email)

def formatar_para_csv(contato: Contato):
    return f'{contato.nome};{contato.tel};{contato.email}\n'
