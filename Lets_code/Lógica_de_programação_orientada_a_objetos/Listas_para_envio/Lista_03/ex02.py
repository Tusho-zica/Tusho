# Faça uma função chamada toPM_AM que converta da notação de 24 horas para a notação de 12 horas. 
# Por exemplo, o programa deve converter 14:25 em 2:25 PM ou 7:00 em 7:00 AM. A entrada é dada em 
# dois inteiros (horas e minutos). Inclua um loop que permita que o usuário repita esse cálculo 
# para novos valores de entrada todas as vezes que desejar.

def toPM_AM(horas, minutos):
    if horas <= 12:
        hora_ampm = horas
    else:
        hora_ampm = (horas - 12)

    if hora_24 <= 12:
        am_pm = 'AM'
    else:
        am_pm = 'PM'
    
    return f'{hora_ampm}:{minutos} {am_pm}'
     
time = False
while not time:

    hora_24 = int(input("Digite a hora que deseja converter ou digite '0' para sair: "))

    if hora_24 == 0:
        break

    minutos = int(input("Digite os minutos: "))

    print(toPM_AM(hora_24,minutos))