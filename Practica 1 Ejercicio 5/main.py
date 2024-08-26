from ColaSecuencial import ColaSecu
from ColaEncadenada import ColaEnca
import random
#tiempo-> minutos 
#almacenar tiempos en la cola
#iterar con el tiempo
#el tiempo promedio es 5 es lo que tarda en atender->verificar si esta disponible zz(0 a 5 o 5 a 0)
#parra el ultimo ejercicio retornar la cantidad para evaluar cual es la cola mas corta

"""""whike i<120
        a=random(0,1)
        0<=a<=1/frecuencia de llegada(5min)
        c.insertar(i)
        x=c.suprimir()
        tiempo=i-x
"""


if __name__ =="__main__":
    pila = ColaEnca()
    import numpy as np
    cajas=np.ndarray(3)
    cajas[0]=0
    cajas[1]=0
    cajas[2]=0
    caj1=0
    caj2=0
    caj3=0

    tiempo=int(input("Tiempo total"))
    tiempo=tiempo*60
    a=random(0,1)
    i=0
    tiempo=0
    while i<120:
        0<=a<=(1/5)
        pila.insertar(i)
        if caj1==0:
            x=pila.suprimir()
            caj1+=1
        elif caj1<=5:
            caj1+=1
        if caj1!=0 and caj2==0:
            x=pila.suprimir()
            caj2+=1
        else:
            caj2+=1
        if caj2!=0 and caj1!=0 and caj3==0:
            x=pila.suprimir()
            caj3+=1
        else:
            caj3+=1

        if caj1==5:
            caj1=0
        if caj2==5:
            caja2=0
        if caj3==5:
            caj3=0 
        tiempo=i-x
        i+=1






    
    #ColaSecuencial = ColaSecu()

    numero1 = 10
    numero2 = 20
    numero3 = 30
    numero4 = 40

    pila = ColaEnca()
    #pila.suprimir()

    pila.insertar(numero1)
    pila.insertar(numero2)
    pila.insertar(numero3)
    pila.insertar(numero4)

    pila.recorrer()
    pila.suprimir()
    pila.recorrer()