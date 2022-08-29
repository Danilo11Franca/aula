#rafael lindo 
import random

lista =[]

while len(lista) < 6:
    x = random.randint(1, 60)

    if x in lista:
        print("x está na lista")
    else:
        lista.append(x)
            #lista = lista + [x]

lista.sort()
print(lista)
    