#DO-WHILE - n existe no python... como ficaria? \/

count = 0
while True:
    print(count, "TESTE")
    count += 1
    if count > 10:
        break

#While normal
count = 0
while count >= 10:
    print(count, "TESTE")
    count += 1

#NÃO UTILIZAR == quando for fazer testes de while e / ou usar FLOAT.
#Somente conseguimos fazer uma expessão bool com WHILE. For não da pra usar!

