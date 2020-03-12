def teste (a, *args, **kargs):
    print(a, args, kargs)
    return

teste(10, "teste", 30, testechave = 20)


# *args = argumentos opcionais (tupla)
# **kargs = Dicionário opcional {Dicionário}
# Sempre precisamos de pelo menos um parametro obrigatório e N opcionais.