# While infinito
while True:
    print("Loop infinito")
    break


#Conceito de flag
terminar = False
count = 0

while not terminar:
    print('teste')
    count += 1
    if count > 10: terminar = True