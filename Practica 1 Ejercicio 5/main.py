from ColaSecuencial import ColaSecu
from ColaEncadenada import ColaEnca
from menu import menu
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


    import numpy as np

    cajas=np.ndarray(3)
    cajas[0]=0
    cajas[1]=0
    cajas[2]=0
    
    caj1=0
    caj2=0
    caj3=0

    tiempo=int(input("Ingrese tiempo total-> "))
    tiempo=tiempo*60
    llegada=5
    #a=random.random()

    i=0
    temp=0
    cont=0
    total=0
    x=0
    while i<tiempo:
        a=random.random()
        #print(a)

        if 0<=a<=(1/llegada):
            Cola.insertar(i)
            if caj1==0:
                x=Cola.suprimir()
                temp=i-x
                cont+=1
                caj1+=1
            elif caj1!=0 and caj2==0:
                x=Cola.suprimir()
                temp=i-x

                cont+=1
                caj2+=1
            elif caj2!=0 and caj1!=0 and caj3==0:
                x=Cola.suprimir()
                temp=i-x
                cont+=1
                caj3+=1


        if caj1==5:
            caj1=0
        elif caj1<5:
            caj1+=1
        if caj2==5:
            caj2=0
        elif caj2<5:
            caj2+=1
        if caj3==5:
            caj3=0 
        elif caj3<5:
            caj3+=1
        #Tiempo actual - tiempo en el que ingreso
        total=total+temp
            
        i+=1
    print("Tiempo total de espera ",total,"min")
    print("Trabajos realizados ",cont)
    print("Tiempo promedio ",round(total/cont,2))
    print("Trabajos pendientes",Cola.getCant())
"""





if __name__ =="__main__":
    
    Cola = ColaEnca()
    unmenu=menu()
    print("Bienvenido\n")
    op=input("Ingrese la opcion que desea\n 1-Simulacion de impresoras\n 2-Simulacion cajeros\n 0-Salir\n")
    while op!='0':
        unmenu.opcion(op,Cola)
        op=input("Ingrese la opcion que desea\n 1-Simulacion de impresoras\n 2-Simulacion cajeros\n 0-Salir\n")








