#Distancia entre dois pontos

import math

x1 = float(input("informe a primeira coordenada x:"))
y1 = float(input("informe a primeira coordenada y:"))
x2 = float(input("informe a segunda coordenada x:"))
y2 = float(input("informe a segunda coordenada y:"))

#d(x, y) = sqrt(((x1 - x2) **2) + ((y1 - y2) **2))

distancia = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2) **2))

##print(distancia)

if(distancia >= 10):
    print("longe")
else:
    print("perto")