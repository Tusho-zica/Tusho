# Faça uma função que recebe um dia da semana identificado como 0=Dom, 1=Seg, 2=Ter, ... 6=Sáb, 
# e um booleano indicando se estamos ou não em férias, retorne uma string na forma "7:00" 
# indicando a hora em que o alarme deve tocar. Em dias de semana, o alarme deve tocar às "7:00" 
# e nos fins de semana, o alarme deve tocar às "10:00". A menos que estejamos de férias, nesse 
# caso, em dias de semana, o alarme deve tocar às "10:00" e em fins de semana a resposta do 
# alarme deve ser "off". Chame essa função de set_alarm.

def set_alarm(dia_semana, ferias):
    if ferias == True and dia_semana > 0 and dia_semana < 6:
        return '10:00'
    elif ferias == True and dia_semana == 0 or dia_semana == 6:
        return 'OFF'
    elif ferias == False and dia_semana > 0 and dia_semana < 6:
        return '7:00'
    elif ferias == False and dia_semana == 0 or dia_semana == 6:
        return '10:00'
    else:
        return 'input inválido'

print(set_alarm(10,False))