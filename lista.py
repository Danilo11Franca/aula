bola = []

from doctest import testfile
from operator import truediv
import random

x = random.randint (1,60)

testlist = [1,60]    


if x in bola :
    print("x esta na lista")

else    :
    print("nao esta na lista") 
    bola = bola + [x]

    while len (bola) < 6 : 

        x = random.rendint (1,60)

    print(x)

    testlist = [1 , 60]

    if x in bola :
        print("x esta na lista")

    else :
        print("nao esta na lista ")
        bola = bola + [x]
        print(bola)



    #print(bola)